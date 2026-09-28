"""Validate SQL code blocks in the specification documentation.

Runs as part of the spec build (see the Makefile). Every ```sql fenced code
block in a searched directory must:

* contain syntactically valid SQL, and
* reference only columns of the tables they read (or query-local names such
  as aliases, CTEs, and table aliases).

A table is named by its dataset's Dataset ID (e.g. ``CostAndUsage``, read
from each ``datasets/*/dataset.md``; ``focus_data_table`` also names Cost and
Usage), and a column read from it must be one of that dataset's Column IDs.
Qualifiers resolve through table aliases, CTEs, and derived tables. An
unqualified column in a query that joins several tables must be a column of
at least one of them.

The ``?`` character is permitted as a bind placeholder for tunable query
values; sqlglot parses it natively, so no preprocessing is required.
Custom columns (``x_`` prefix) are allowed, per the FOCUS custom column rules.

To validate SQL blocks in additional sections, add the directory name to
``SQL_SEARCH_DIRS`` below.
"""

import re
from pathlib import Path

import pytest
import sqlglot
from sqlglot import exp
from sqlglot.errors import OptimizeError, ParseError
from sqlglot.optimizer.scope import Scope, ScopeType, traverse_scope
from sqlglot.tokens import Tokenizer, TokenType

SPEC_DIR = Path(__file__).resolve().parent.parent
DATASETS_DIR = SPEC_DIR / "datasets"

# Directories (relative to the specification/ root) searched for ```sql blocks.
# Append more section names here to extend coverage over time.
SQL_SEARCH_DIRS = [
    SPEC_DIR / "datasets",
    SPEC_DIR / "supported_features",
]


def _collect_dataset_columns():
    """Return {Dataset ID: set of Column IDs} for every FOCUS dataset.

    Each dataset directory holds a ``dataset.md`` whose ``## Dataset ID``
    section names the dataset (e.g. ``CostAndUsage``), and one ``.md`` file per
    column under ``columns/`` whose ``## Column ID`` section holds the
    PascalCase identifier (e.g. ``BilledCost``). Lower-cased for
    case-insensitive matching, since SQL identifiers are case-insensitive.
    """
    dataset_id_re = re.compile(
        r"^##\s*Dataset ID\b[^\n]*\n+\s*([A-Za-z0-9_]+)", re.MULTILINE
    )
    column_id_re = re.compile(
        r"^##\s*Column ID\s*\n+\s*([A-Za-z0-9_]+)", re.MULTILINE
    )
    datasets = {}
    for dataset_file in sorted(DATASETS_DIR.glob("*/dataset.md")):
        match = dataset_id_re.search(dataset_file.read_text(encoding="utf-8"))
        if not match:
            continue
        ids = set()
        for column_file in dataset_file.parent.glob("columns/*.md"):
            column_match = column_id_re.search(
                column_file.read_text(encoding="utf-8")
            )
            if column_match:
                ids.add(column_match.group(1).lower())
        datasets[match.group(1).lower()] = ids
    return datasets


DATASET_COLUMNS = _collect_dataset_columns()

# Table names that stand for a FOCUS dataset without being its Dataset ID.
# Supported feature queries written before FOCUS defined more than one dataset
# read the Cost and Usage dataset as ``focus_data_table``.
_TABLE_NAME_ALIASES = {"focus_data_table": "costandusage"}

# Query scopes whose unqualified columns can also resolve against an enclosing
# query: correlated subqueries, the arguments of UNNEST, and the branches of a
# UNION (which resolve wherever the UNION itself does).
_CORRELATED_SCOPE_TYPES = {ScopeType.SUBQUERY, ScopeType.UDTF, ScopeType.UNION}

# Match fenced ```sql blocks whose fences sit at the start of a line, capturing
# the block body. Non-greedy so each block stops at its own closing fence.
_SQL_BLOCK_RE = re.compile(
    r"^```sql[^\n]*\n(.*?)^```", re.MULTILINE | re.DOTALL | re.IGNORECASE
)


def _collect_sql_blocks():
    """Return (id, sql) pairs for every ```sql block in the searched dirs."""
    blocks = []
    md_files = sorted(
        {md for directory in SQL_SEARCH_DIRS for md in directory.rglob("*.md")}
    )
    for md_file in md_files:
        text = md_file.read_text(encoding="utf-8")
        rel = md_file.relative_to(SPEC_DIR)
        for match in _SQL_BLOCK_RE.finditer(text):
            line = text[: match.start()].count("\n") + 1
            blocks.append((f"{rel}:{line}", match.group(1).strip()))
    return blocks


SQL_BLOCKS = _collect_sql_blocks()

# Token types that legally terminate a comma-separated expression list. A comma
# sitting immediately before one of these (or before the end of a statement) is
# a dangling trailing comma. sqlglot parses trailing commas without complaint,
# since some dialects (e.g. BigQuery, DuckDB) permit them, so they are caught
# here explicitly.
_TRAILING_COMMA_TERMINATORS = {
    TokenType.R_PAREN,
    TokenType.SEMICOLON,
    TokenType.FROM,
    TokenType.WHERE,
    TokenType.GROUP_BY,
    TokenType.ORDER_BY,
    TokenType.HAVING,
    TokenType.LIMIT,
    TokenType.OFFSET,
    TokenType.WINDOW,
    TokenType.QUALIFY,
    TokenType.FETCH,
    TokenType.UNION,
    TokenType.EXCEPT,
    TokenType.INTERSECT,
}


def _trailing_comma(sql):
    """Return the 1-based line of the first dangling trailing comma, or None.

    A trailing comma is a ``,`` immediately followed by a list-terminating token
    (e.g. ``FROM``, ``)``, ``GROUP BY``) or by the end of a statement.
    """
    tokens = Tokenizer().tokenize(sql)
    for current, following in zip(tokens, tokens[1:]):
        if current.token_type is TokenType.COMMA and (
            following.token_type in _TRAILING_COMMA_TERMINATORS
        ):
            return current.line
    if tokens and tokens[-1].token_type is TokenType.COMMA:
        return tokens[-1].line
    return None

# Parametrize over discovered blocks; fall back to a single clean skip when the
# datasets docs contain no SQL blocks yet.
_PARAMS = [pytest.param(sql, id=block_id) for block_id, sql in SQL_BLOCKS] or [
    pytest.param(None, id="no-sql-blocks-found")
]


@pytest.mark.parametrize("sql", _PARAMS)
def test_sql_block_is_valid(sql):
    """Each ```sql block parses as valid SQL (``?`` placeholders allowed)."""
    if sql is None:
        pytest.skip("no ```sql blocks found in the searched directories")

    error = None
    statements = None
    try:
        # A block may hold multiple statements; parse() validates them all.
        statements = sqlglot.parse(sql)
    except ParseError as exc:
        error = str(exc).splitlines()[0]

    if error is None and (not statements or any(s is None for s in statements)):
        error = "SQL did not parse into any statement"

    if error is None:
        comma_line = _trailing_comma(sql)
        if comma_line is not None:
            error = f"dangling trailing comma (line {comma_line} of block)"

    if error is not None:
        pytest.fail(f"Invalid SQL in block:\n{sql}\n\n{error}", pytrace=False)


def _local_names(tree):
    """Names defined within a statement that are not FOCUS columns.

    Covers output aliases, CTE names, table names and aliases (including
    derived-table column lists), UNNEST aliases, inline column definitions, and
    any qualifier used on a column reference. Lower-cased for matching.
    """
    names = set()
    for alias in tree.find_all(exp.Alias):
        if alias.alias:
            names.add(alias.alias.lower())
    for cte in tree.find_all(exp.CTE):
        if cte.alias:
            names.add(cte.alias.lower())
    for table_alias in tree.find_all(exp.TableAlias):
        if table_alias.name:
            names.add(table_alias.name.lower())
        for column in table_alias.args.get("columns") or []:
            if getattr(column, "name", None):
                names.add(column.name.lower())
    for table in tree.find_all(exp.Table):
        if table.name:
            names.add(table.name.lower())
        if table.alias:
            names.add(table.alias.lower())
    for unnest in tree.find_all(exp.Unnest):
        unnest_alias = unnest.args.get("alias")
        if unnest_alias is not None and getattr(unnest_alias, "name", None):
            names.add(unnest_alias.name.lower())
    for column_def in tree.find_all(exp.ColumnDef):
        if column_def.name:
            names.add(column_def.name.lower())
    for json_column_def in tree.find_all(exp.JSONColumnDef):
        if json_column_def.name:
            names.add(json_column_def.name.lower())
    for column in tree.find_all(exp.Column):
        if column.table:
            names.add(column.table.lower())
    return names


def _is_table_function(source):
    """Whether a FROM/JOIN source is UNNEST or a function such as JSON_TABLE.

    These sources expose only names the query declares itself (an alias, a
    column definition), which ``_local_names`` collects.
    """
    if isinstance(source, Scope):
        return source.scope_type is ScopeType.UDTF
    return not isinstance(source.this, exp.Identifier)


def _source_columns(source, dataset_columns):
    """Return the lower-cased column names a FROM/JOIN source exposes.

    A table exposes the Column IDs of the dataset it names. A CTE or derived
    table exposes its column list, else its projection, expanding ``*``
    through its own sources. Returns None when the names cannot be known: a
    table function, a table that is not a FOCUS dataset, or an unexpandable
    ``*``.
    """
    if _is_table_function(source):
        return None
    if isinstance(source, exp.Table):
        name = source.name.lower()
        return dataset_columns.get(_TABLE_NAME_ALIASES.get(name, name))
    query = source.expression
    container = query.parent
    table_alias = container.args.get("alias") if container is not None else None
    if isinstance(table_alias, exp.TableAlias) and table_alias.columns:
        return {column.name.lower() for column in table_alias.columns}
    names = set()
    for projection in query.selects:
        if not projection.is_star:
            if projection.alias_or_name:
                names.add(projection.alias_or_name.lower())
            continue
        if isinstance(query, exp.SetOperation):
            return None
        for _, inner in source.selected_sources.values():
            inner_names = _source_columns(inner, dataset_columns)
            if inner_names is None:
                return None
            names |= inner_names
    return names


def _source_label(name, source):
    """Name a source in failure messages: its table name, else its alias."""
    if isinstance(source, exp.Table) and source.name:
        return source.name
    return name


def _find_source(scope, qualifier):
    """Return the FROM/JOIN source a column qualifier names, or None.

    Searches the column's own query first, then enclosing queries, so a
    correlated subquery can name an outer table.
    """
    qualifier = qualifier.lower()
    while scope is not None:
        for name, (_, source) in scope.selected_sources.items():
            if name.lower() == qualifier:
                return source
        scope = scope.parent
    return None


def _visible_sources(scope):
    """Return (name, source) pairs an unqualified column can resolve against."""
    sources = []
    while scope is not None:
        sources.extend(
            (name, source) for name, (_, source) in scope.selected_sources.items()
        )
        if scope.scope_type not in _CORRELATED_SCOPE_TYPES:
            break
        scope = scope.parent
    return sources


def _match_cte_names(tree):
    """Spell each reference to a CTE the way the CTE declares its name.

    sqlglot matches CTE names case-sensitively, but SQL identifiers are
    case-insensitive: without this, ``WITH Totals AS (...) ... FROM totals``
    reads ``totals`` as a table.
    """
    declared = {cte.alias.lower(): cte.alias for cte in tree.find_all(exp.CTE)}
    for table in tree.find_all(exp.Table):
        name = declared.get(table.name.lower())
        if name and not table.db and isinstance(table.this, exp.Identifier):
            table.this.set("this", name)


def _enclosing_scope(column, scopes):
    """Return the innermost query scope containing ``column``, or None."""
    node = column.parent
    while node is not None:
        if id(node) in scopes:
            return scopes[id(node)]
        node = node.parent
    return None


def _enclosing_aliases(column):
    """Return the output aliases whose expression contains ``column``.

    An alias cannot name its own input (``SUM(x) AS x`` reads the source
    column ``x``), so these aliases do not vouch for the column.
    """
    names = set()
    node = column.parent
    while node is not None and not isinstance(node, exp.Select):
        if isinstance(node, exp.Alias) and node.alias:
            names.add(node.alias.lower())
        node = node.parent
    return names


def _column_problem(column, scope, dataset_columns, all_columns, local):
    """Return why ``column`` does not resolve, or None when it does.

    A qualified column must be a column of the source its qualifier names. An
    unqualified column must be a column of a source its query reads, or a
    query-local name. A column that cannot be traced to a dataset (outside a
    query, or read from UNNEST, a table function, or an unexpandable ``*``)
    only has to be a FOCUS column of some dataset or a query-local name.
    """
    name = column.name.lower()
    local = local - _enclosing_aliases(column)
    in_any_dataset = name in all_columns or name in local
    fallback = None if in_any_dataset else "not a FOCUS column"
    if scope is None:
        return fallback

    if column.table:
        source = _find_source(scope, column.table)
        if source is None or _is_table_function(source):
            return fallback
        names = _source_columns(source, dataset_columns)
        if names is not None:
            if name in names:
                return None
            return f"not a column of {_source_label(column.table, source)}"
        if isinstance(source, exp.Table):
            return f"no FOCUS dataset named {source.name}"
        return fallback

    known, labels, unknown_tables, opaque = set(), set(), set(), False
    for source_name, source in _visible_sources(scope):
        if _is_table_function(source):
            continue
        names = _source_columns(source, dataset_columns)
        if names is not None:
            known |= names
            labels.add(_source_label(source_name, source))
        elif isinstance(source, exp.Table):
            unknown_tables.add(source.name)
        else:
            opaque = True
    if name in known or name in local:
        return None
    if opaque or not (labels or unknown_tables):
        return fallback
    if unknown_tables:
        return f"no FOCUS dataset named {' or '.join(sorted(unknown_tables))}"
    return f"not a column of {' or '.join(sorted(labels))}"


def _unresolved_columns(sql, dataset_columns):
    """Return {column reference: reason} for references that do not resolve.

    ``dataset_columns`` maps each lower-cased Dataset ID to its lower-cased
    Column IDs (see ``_collect_dataset_columns``). Raises ``ParseError`` when
    the SQL does not parse.
    """
    all_columns = set().union(*dataset_columns.values())
    unresolved = {}
    for tree in sqlglot.parse(sql):
        if tree is None:
            continue
        local = _local_names(tree)
        _match_cte_names(tree)
        scopes = {id(scope.expression): scope for scope in traverse_scope(tree)}
        for column in tree.find_all(exp.Column):
            name = column.name
            if not name or name.startswith("x_") or column.is_star:
                continue
            scope = _enclosing_scope(column, scopes)
            try:
                problem = _column_problem(
                    column, scope, dataset_columns, all_columns, local
                )
            except OptimizeError:
                # sqlglot cannot map the query's sources (e.g. two unaliased
                # derived tables), so check against every dataset instead.
                problem = _column_problem(
                    column, None, dataset_columns, all_columns, local
                )
            if problem is not None:
                reference = f"{column.table}.{name}" if column.table else name
                unresolved.setdefault(reference, problem)
    return unresolved


@pytest.mark.parametrize("sql", _PARAMS)
def test_sql_block_references_known_columns(sql):
    """Each column reference is a column of the table it reads from."""
    if sql is None:
        pytest.skip("no ```sql blocks found in the searched directories")

    try:
        unresolved = _unresolved_columns(sql, DATASET_COLUMNS)
    except ParseError:
        pytest.skip("block is not valid SQL (reported by test_sql_block_is_valid)")

    if unresolved:
        details = "\n".join(
            f"* {reference}: {reason}"
            for reference, reason in sorted(unresolved.items())
        )
        pytest.fail(
            f"SQL references column(s) that do not resolve:\n{details}\n\n{sql}",
            pytrace=False,
        )


# Self-tests for the column check, run against a small fixed schema so they do
# not move when the spec's datasets change. Each case pairs a query with the
# column references the check must flag.
_SELF_TEST_DATASET_COLUMNS = {
    "costandusage": {
        "billedcost",
        "contractapplied",
        "invoiceid",
        "listunitprice",
        "skupriceid",
    },
    "invoicedetail": {"billedcost", "invoiceid"},
    "skuprice": {"contractid", "skupriceid", "unitprice"},
}

_SELF_TEST_CASES = [
    pytest.param(
        "SELECT ListUnitPrice FROM SkuPrice",
        {"ListUnitPrice"},
        id="unqualified-column-of-another-dataset",
    ),
    pytest.param(
        "SELECT SP.ListUnitPrice FROM SkuPrice SP",
        {"SP.ListUnitPrice"},
        id="qualifier-resolved-through-table-alias",
    ),
    pytest.param(
        "SELECT SP.ListUnitPrice FROM CostAndUsage CU "
        "JOIN SkuPrice SP ON CU.SkuPriceId = SP.SkuPriceId",
        {"SP.ListUnitPrice"},
        id="qualifier-checked-against-its-own-dataset-in-join",
    ),
    pytest.param(
        "SELECT ListUnitPrice, UnitPrice FROM CostAndUsage CU "
        "JOIN SkuPrice SP ON CU.SkuPriceId = SP.SkuPriceId",
        set(),
        id="unqualified-column-of-any-joined-dataset",
    ),
    pytest.param(
        "SELECT ListUnitPrice FROM focus_data_table",
        set(),
        id="focus-data-table-reads-cost-and-usage",
    ),
    pytest.param(
        "SELECT UnitPrice FROM focus_data_table",
        {"UnitPrice"},
        id="focus-data-table-is-only-cost-and-usage",
    ),
    pytest.param(
        "SELECT BilledCost FROM CostAndUsages",
        {"BilledCost"},
        id="table-that-is-not-a-dataset",
    ),
    pytest.param(
        "SELECT C.BilledCost FROM CostAndUsages C",
        {"C.BilledCost"},
        id="qualifier-names-a-table-that-is-not-a-dataset",
    ),
    pytest.param(
        "WITH T AS (SELECT SkuPriceId, SUM(BilledCost) AS Total "
        "FROM CostAndUsage GROUP BY SkuPriceId) "
        "SELECT T.SkuPriceId, Total FROM T ORDER BY Total",
        set(),
        id="cte-output-columns-and-aliases",
    ),
    pytest.param(
        "WITH A AS (SELECT ListUnitPrice FROM CostAndUsage) "
        "SELECT ListUnitPrice FROM SkuPrice",
        {"ListUnitPrice"},
        id="cte-not-joined-does-not-vouch",
    ),
    pytest.param(
        "WITH P (SkuPriceId, Quantity) AS (VALUES (?, ?)) "
        "SELECT P.Quantity * SP.UnitPrice AS Amount, P.ListUnitPrice "
        "FROM P JOIN SkuPrice SP ON SP.SkuPriceId = P.SkuPriceId",
        {"P.ListUnitPrice"},
        id="cte-column-list-defines-its-columns",
    ),
    pytest.param(
        "WITH U AS (SELECT * FROM CostAndUsage UNION ALL "
        "SELECT * FROM InvoiceDetail) SELECT UnitPrice, NotAColumn FROM U",
        {"NotAColumn"},
        id="unexpandable-star-falls-back-to-any-dataset",
    ),
    pytest.param(
        "WITH U AS (SELECT * FROM CostAndUsage UNION ALL "
        "SELECT * FROM InvoiceDetail) SELECT ContractApplied "
        "FROM U JOIN SkuPrice SP ON U.SkuPriceId = SP.SkuPriceId",
        set(),
        id="unexpandable-star-joined-to-a-dataset-falls-back",
    ),
    pytest.param(
        "WITH T AS (SELECT * FROM SkuPrice) SELECT T.ListUnitPrice FROM T",
        {"T.ListUnitPrice"},
        id="star-cte-exposes-its-dataset-columns",
    ),
    pytest.param(
        "SELECT ID.BilledCost FROM (SELECT InvoiceId FROM InvoiceDetail) ID",
        {"ID.BilledCost"},
        id="derived-table-exposes-only-its-projection",
    ),
    pytest.param(
        "SELECT SP.SkuPriceId FROM SkuPrice SP WHERE EXISTS "
        "(SELECT 1 FROM CostAndUsage CU "
        "WHERE CU.SkuPriceId = SP.SkuPriceId AND SP.ListUnitPrice > 0)",
        {"SP.ListUnitPrice"},
        id="correlated-qualifier-resolved-in-outer-query",
    ),
    pytest.param(
        "SELECT SP.SkuPriceId FROM SkuPrice SP WHERE EXISTS "
        "(SELECT 1 FROM CostAndUsage CU "
        "WHERE CU.SkuPriceId = SP.SkuPriceId AND UnitPrice > 0)",
        set(),
        id="correlated-unqualified-column-of-outer-query",
    ),
    pytest.param(
        "SELECT CU.x_Team, JSON_VALUE(CA, '$.ContractId') FROM CostAndUsage CU "
        "CROSS JOIN UNNEST(JSON_EXTRACT_ARRAY(CU.ContractApplied, '$.Elements'))"
        " AS CA",
        set(),
        id="unnest-alias-and-custom-column",
    ),
    pytest.param(
        "SELECT E.ContractId FROM CostAndUsage "
        "CROSS JOIN UNNEST(ContractApplied) AS E",
        set(),
        id="unnest-element-field",
    ),
    pytest.param(
        "SELECT JSON_VALUE(E, '$.Id') FROM SkuPrice CROSS JOIN "
        "UNNEST(JSON_EXTRACT_ARRAY(ContractApplied, '$.Elements')) AS E",
        {"ContractApplied"},
        id="unnest-argument-resolved-in-its-query",
    ),
    pytest.param(
        "SELECT SUM(ListUnitPrice) AS ListUnitPrice FROM SkuPrice",
        {"ListUnitPrice"},
        id="alias-does-not-vouch-for-its-own-input",
    ),
    pytest.param(
        "WITH Totals AS (SELECT InvoiceId FROM CostAndUsage) "
        "SELECT InvoiceId FROM totals",
        set(),
        id="cte-named-in-different-case",
    ),
    pytest.param(
        "SELECT BilledCost FROM (SELECT BilledCost FROM CostAndUsage) "
        "JOIN (SELECT InvoiceId FROM InvoiceDetail) ON TRUE",
        set(),
        id="unaliased-derived-tables",
    ),
    pytest.param(
        "SELECT SP.SkuPriceId FROM SkuPrice SP WHERE EXISTS "
        "(SELECT 1 FROM CostAndUsage CU WHERE CU.SkuPriceId = SP.SkuPriceId "
        "UNION ALL SELECT 1 FROM InvoiceDetail WHERE UnitPrice > 0)",
        set(),
        id="union-branch-resolves-in-outer-query",
    ),
    pytest.param(
        "SELECT CU.* FROM CostAndUsage CU",
        set(),
        id="qualified-star",
    ),
]


@pytest.mark.parametrize("sql, expected", _SELF_TEST_CASES)
def test_column_check_resolves_references_per_table(sql, expected):
    """The column check flags exactly the references that do not resolve."""
    assert set(_unresolved_columns(sql, _SELF_TEST_DATASET_COLUMNS)) == expected
