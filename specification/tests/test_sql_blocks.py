"""Validate SQL code blocks in the specification documentation.

Runs as part of the spec build (see the Makefile). Every ```sql fenced code
block in a searched directory must:

* contain syntactically valid SQL, and
* reference only columns of the tables they read (or query-local names such
  as aliases, CTEs, and table aliases).

A table is named by its dataset's Dataset ID (e.g. ``CostAndUsage``, read
from each ``datasets/*/dataset.md``; ``focus_data_table`` also names Cost and
Usage), and a column read from it must be one of that dataset's Column IDs.
Qualifiers resolve through table aliases, CTEs, and derived tables. A
qualifier that names no source its query reads fails, unless it names a
column or an alias the statement declares (e.g. a PIVOT alias), which sqlglot
does not always map to a source. An unqualified column in a query that joins
several tables must be a column of at least one of them. An output alias
counts only in the query that defines it, and a CTE's column list only in a
query that reads the CTE.

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


def _output_aliases(tree):
    """Output aliases (``expression AS name``) defined within a statement.

    Kept apart from ``_local_names`` so that ``_enclosing_aliases`` can set
    aside an alias without also dropping a table alias, UNNEST alias, or
    JSON_TABLE column of the same name. These count only where the check
    falls back to every dataset; elsewhere a column sees the aliases of its
    own query (see ``_query_aliases``). Lower-cased for matching.
    """
    return {alias.alias.lower() for alias in tree.find_all(exp.Alias) if alias.alias}


def _query_aliases(query):
    """Output aliases a query defines in its own clauses.

    Covers the query's projection and PIVOT columns, not the aliases of a
    query nested inside it. An alias resolves only within the query that
    defines it (e.g. in its ORDER BY), not in a sibling CTE or an enclosing
    query. A UNION's aliases come from its first branch. Lower-cased for
    matching.
    """
    names = {
        projection.alias.lower()
        for projection in query.selects
        if isinstance(projection, exp.Alias) and projection.alias
    }
    for alias in query.find_all(exp.Alias):
        owner = alias.parent
        while owner is not None and not isinstance(owner, exp.Query):
            owner = owner.parent
        if owner is query and alias.alias:
            names.add(alias.alias.lower())
    return names


def _alias_names(tree):
    """Table aliases, column lists, and inline column definitions.

    A qualifier that names one of these but no source its query reads may be
    a PIVOT alias or a field of an UNNEST element, neither of which sqlglot
    maps to a source. CTE names are left out: a qualifier that names a CTE
    must name one its query reads. Lower-cased for matching.
    """
    names = set()
    for table_alias in tree.find_all(exp.TableAlias):
        if table_alias.name and not isinstance(table_alias.parent, exp.CTE):
            names.add(table_alias.name.lower())
        for column in table_alias.args.get("columns") or []:
            if getattr(column, "name", None):
                names.add(column.name.lower())
    for definition in tree.find_all(exp.ColumnDef, exp.JSONColumnDef):
        if definition.name:
            names.add(definition.name.lower())
    return names


def _local_names(tree, query_column_lists=True):
    """Names defined within a statement that are not FOCUS columns.

    Covers CTE names, table names and aliases (including derived-table column
    lists), UNNEST aliases, inline column definitions, and any qualifier used
    on a column reference. Output aliases are collected by
    ``_output_aliases``. With ``query_column_lists=False``, the column lists
    of CTEs, FROM-clause subqueries, and tables are left out: those names
    resolve only in a query that reads that source (see ``_source_columns``).
    Column lists on UNNEST, VALUES, and LATERAL stay. Lower-cased for
    matching.
    """
    names = set()
    for cte in tree.find_all(exp.CTE):
        if cte.alias:
            names.add(cte.alias.lower())
    for table_alias in tree.find_all(exp.TableAlias):
        if table_alias.name:
            names.add(table_alias.name.lower())
        if not query_column_lists and isinstance(
            table_alias.parent, (exp.CTE, exp.Subquery, exp.Table)
        ):
            continue
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
    """Whether a FROM/JOIN source is UNNEST, LATERAL, or a function such as JSON_TABLE.

    These sources expose only names the statement declares itself (an alias,
    a column definition), which ``_local_names`` and ``_output_aliases``
    collect.
    """
    if isinstance(source, Scope):
        return source.scope_type is ScopeType.UDTF
    return not isinstance(source.this, exp.Identifier)


def _source_columns(source, dataset_columns):
    """Return the lower-cased column names a FROM/JOIN source exposes.

    A table exposes the Column IDs of the dataset it names, plus the names in
    its column list. A CTE or derived table exposes its projection, expanding
    ``*`` through its own sources; a column list renames the projection by
    position, so columns past the list's end keep their names. Next to a
    ``*``, whose positions are unknown, the list's names are added to the
    projection's. Returns None when the names cannot be known: a table
    function, a table that is not a FOCUS dataset, or an unexpandable ``*``
    with no column list.
    """
    if _is_table_function(source):
        return None
    if isinstance(source, exp.Table):
        name = source.name.lower()
        columns = dataset_columns.get(_TABLE_NAME_ALIASES.get(name, name))
        table_alias = source.args.get("alias")
        if columns is not None and isinstance(table_alias, exp.TableAlias):
            # Column IDs carry no position, so the list's new names are added
            # rather than mapped onto the columns they rename.
            columns = columns | {column.name.lower() for column in table_alias.columns}
        return columns
    query = source.expression
    container = query.parent
    # The column list sits on the CTE or derived table, above a parenthesized
    # body or, for a recursive CTE read from inside itself, its first branch.
    while isinstance(container, (exp.SetOperation, exp.Subquery)):
        if container.args.get("alias"):
            break
        container = container.parent
    table_alias = container.args.get("alias") if container is not None else None
    renamed = []
    if isinstance(table_alias, exp.TableAlias):
        renamed = [column.name.lower() for column in table_alias.columns]
    projections = query.selects
    if not any(projection.is_star for projection in projections):
        projections = projections[len(renamed) :]
    names = set(renamed)
    for projection in projections:
        if not projection.is_star:
            if projection.alias_or_name:
                names.add(projection.alias_or_name.lower())
            continue
        if isinstance(query, exp.SetOperation):
            return set(renamed) if renamed else None
        # A qualified star (CU.*) expands only the source it names.
        qualifier = projection.table if isinstance(projection, exp.Column) else ""
        for inner_name, (_, inner) in source.selected_sources.items():
            if qualifier and inner_name.lower() != qualifier.lower():
                continue
            inner_names = _source_columns(inner, dataset_columns)
            if inner_names is None:
                return set(renamed) if renamed else None
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
    correlated subquery can name an outer table. The right side of a SEMI or
    ANTI join counts: sqlglot leaves it out of ``selected_sources``, but the
    join condition reads its columns.
    """
    qualifier = qualifier.lower()
    while scope is not None:
        for name, (_, source) in scope.selected_sources.items():
            if name.lower() == qualifier:
                return source
        for name, _ in scope.references:
            if name.lower() == qualifier and name in scope.sources:
                return scope.sources[name]
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


def _join_condition_sources(column, scope):
    """Return (name, source) for each SEMI or ANTI join whose ON holds ``column``.

    The right side of such a join is not a selected source, so the query's
    output cannot read it, but its own join condition can.
    """
    sources = []
    node = column
    while node is not scope.expression and node.parent is not None:
        parent = node.parent
        if (
            isinstance(parent, exp.Join)
            and parent.args.get("on") is node
            and parent.text("kind").upper() in ("SEMI", "ANTI")
        ):
            name = parent.this.alias_or_name
            if name in scope.sources:
                sources.append((name, scope.sources[name]))
        node = parent
    return sources


def _match_cte_names(tree):
    """Spell every CTE name, and each table reference to one, in lower case.

    sqlglot matches CTE names case-sensitively, but SQL identifiers are
    case-insensitive: without this, ``WITH Totals AS (...) ... FROM totals``
    reads ``totals`` as a table. Rewriting declarations and references alike
    keeps nested CTEs whose names differ only in case (``T`` and ``t``) bound
    to their own scope.
    """
    declared = set()
    for cte in tree.find_all(exp.CTE):
        alias = cte.args.get("alias")
        if alias is not None and isinstance(alias.this, exp.Identifier):
            alias.this.set("this", alias.name.lower())
            declared.add(alias.name)
    for table in tree.find_all(exp.Table):
        name = table.name.lower()
        if name in declared and not table.db and isinstance(table.this, exp.Identifier):
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


def _column_problem(
    column, scope, dataset_columns, all_columns, local, statement_local, alias_names
):
    """Return why ``column`` does not resolve, or None when it does.

    A qualified column must be a column of the source its qualifier names, in
    its own query or one enclosing it. A qualifier that names no such source
    fails, unless it names a column or one of ``alias_names`` (field access,
    or a source sqlglot does not map); the column then falls back as below.
    An unqualified column must be a column of a source its query reads (in a
    SEMI or ANTI join's condition, that join's right side too), or a name in
    ``local``; in a query that reads a table function, any name in
    ``statement_local`` also counts. A column that cannot be traced to a
    dataset (outside a query, or read from UNNEST, a table function, or an
    unexpandable ``*``) only has to be a FOCUS column of some dataset or a
    name in ``statement_local``.
    """
    name = column.name.lower()
    in_any_dataset = name in all_columns or name in statement_local
    fallback = None if in_any_dataset else "not a FOCUS column"
    if scope is None:
        return fallback

    if column.table:
        source = _find_source(scope, column.table)
        if source is None:
            qualifier = column.table.lower()
            if qualifier in alias_names or qualifier in all_columns:
                return fallback
            return f"no table or alias named {column.table} in the query"
        if _is_table_function(source):
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
    sources = _visible_sources(scope) + _join_condition_sources(column, scope)
    for source_name, source in sources:
        if _is_table_function(source):
            # Names a table function exposes are not tracked per source, so a
            # query that reads one may use any name the statement defines.
            known |= statement_local
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
        declared = _local_names(tree)
        query_declared = _local_names(tree, query_column_lists=False)
        alias_names = _alias_names(tree)
        aliases = _output_aliases(tree)
        _match_cte_names(tree)
        scopes = {id(scope.expression): scope for scope in traverse_scope(tree)}
        for column in tree.find_all(exp.Column):
            name = column.name
            if not name or name.startswith("x_") or column.is_star:
                continue
            scope = _enclosing_scope(column, scopes)
            enclosing = _enclosing_aliases(column)
            statement_local = declared | (aliases - enclosing)
            local = statement_local
            if scope is not None:
                local = query_declared | (_query_aliases(scope.expression) - enclosing)
            try:
                problem = _column_problem(
                    column,
                    scope,
                    dataset_columns,
                    all_columns,
                    local,
                    statement_local,
                    alias_names,
                )
            except OptimizeError:
                # sqlglot cannot map the query's sources (e.g. two unaliased
                # derived tables), so check against every dataset and every
                # name the statement defines instead.
                problem = _column_problem(
                    column,
                    None,
                    dataset_columns,
                    all_columns,
                    local,
                    statement_local,
                    alias_names,
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
        "SELECT CU.BilledCost, SP.UnitPrice FROM CostAndUsage CU",
        {"SP.UnitPrice"},
        id="qualifier-names-no-source-in-the-query",
    ),
    pytest.param(
        "WITH T AS (SELECT UnitPrice FROM SkuPrice) "
        "SELECT T.UnitPrice FROM CostAndUsage",
        {"T.UnitPrice"},
        id="qualifier-names-a-cte-the-query-does-not-read",
    ),
    pytest.param(
        "SELECT CU.BilledCost FROM CostAndUsage CU LEFT SEMI JOIN InvoiceDetail I "
        "ON I.InvoiceId = CU.InvoiceId AND I.ListUnitPrice > 0",
        {"I.ListUnitPrice"},
        id="semi-join-right-side-resolves-to-its-dataset",
    ),
    pytest.param(
        "SELECT BilledCost FROM CostAndUsage CU LEFT SEMI JOIN SkuPrice SP "
        "ON CU.SkuPriceId = SP.SkuPriceId AND UnitPrice > 0",
        set(),
        id="semi-join-condition-reads-its-right-side",
    ),
    pytest.param(
        "SELECT BilledCost FROM CostAndUsage CU LEFT ANTI JOIN SkuPrice SP "
        "ON CU.SkuPriceId = SP.SkuPriceId AND UnitPrice > 0",
        set(),
        id="anti-join-condition-reads-its-right-side",
    ),
    pytest.param(
        "SELECT UnitPrice FROM CostAndUsage CU LEFT SEMI JOIN SkuPrice SP "
        "ON CU.SkuPriceId = SP.SkuPriceId",
        {"UnitPrice"},
        id="semi-join-right-side-hidden-outside-its-condition",
    ),
    pytest.param(
        "SELECT CU.Cost, CU.InvoiceId FROM CostAndUsage AS CU (Cost)",
        set(),
        id="table-column-list-adds-its-names",
    ),
    pytest.param(
        "SELECT InvoiceId, Cost FROM InvoiceDetail WHERE EXISTS "
        "(SELECT 1 FROM CostAndUsage AS CU (Cost))",
        {"Cost"},
        id="table-column-list-not-read-does-not-vouch",
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
        "WITH T AS (SELECT SUM(BilledCost) AS UnitPrice FROM CostAndUsage) "
        "SELECT InvoiceId, UnitPrice FROM InvoiceDetail",
        {"UnitPrice"},
        id="alias-in-cte-not-joined-does-not-vouch",
    ),
    pytest.param(
        "WITH T (UnitPrice) AS (SELECT BilledCost FROM CostAndUsage) "
        "SELECT InvoiceId, UnitPrice FROM InvoiceDetail",
        {"UnitPrice"},
        id="cte-column-list-not-joined-does-not-vouch",
    ),
    pytest.param(
        "WITH P (SkuPriceId, Quantity) AS (VALUES (?, ?)) "
        "SELECT P.Quantity * SP.UnitPrice AS Amount, P.ListUnitPrice "
        "FROM P JOIN SkuPrice SP ON SP.SkuPriceId = P.SkuPriceId",
        {"P.ListUnitPrice"},
        id="cte-column-list-defines-its-columns",
    ),
    pytest.param(
        "WITH T (Total) AS (SELECT SUM(BilledCost) FROM CostAndUsage) "
        "SELECT Total FROM T",
        set(),
        id="cte-column-list-resolves-where-the-cte-is-read",
    ),
    pytest.param(
        "WITH T (Cost) AS (SELECT BilledCost, InvoiceId FROM CostAndUsage) "
        "SELECT Cost, InvoiceId, T.BilledCost FROM T",
        {"T.BilledCost"},
        id="partial-cte-column-list-keeps-later-columns",
    ),
    pytest.param(
        "WITH RECURSIVE R (n) AS (SELECT 1 UNION ALL "
        "SELECT n + 1 FROM R WHERE n < 10) SELECT n FROM R",
        set(),
        id="recursive-cte-column-list",
    ),
    pytest.param(
        "WITH T (Total) AS ((SELECT SUM(BilledCost) FROM CostAndUsage)) "
        "SELECT Total FROM T",
        set(),
        id="parenthesized-cte-body-column-list",
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
        "WITH A AS (SELECT BilledCost AS Cost FROM CostAndUsage), "
        "B AS (SELECT BilledCost AS Cost FROM InvoiceDetail), "
        "U AS (SELECT * FROM A UNION ALL SELECT * FROM B) SELECT Cost FROM U",
        set(),
        id="unexpandable-star-falls-back-to-any-name-the-statement-defines",
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
        "SELECT InvoiceId, UnitPrice FROM InvoiceDetail WHERE EXISTS "
        "(SELECT 1 FROM (SELECT BilledCost FROM CostAndUsage) AS D (UnitPrice))",
        {"UnitPrice"},
        id="derived-table-column-list-not-read-does-not-vouch",
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
        "SELECT E.ContractId FROM CostAndUsage "
        "CROSS JOIN UNNEST(ContractApplied) AS T (E)",
        set(),
        id="unnest-element-field-through-column-alias",
    ),
    pytest.param(
        "SELECT ContractApplied.ContractId FROM CostAndUsage",
        set(),
        id="field-access-on-a-column-falls-back",
    ),
    pytest.param(
        "SELECT JSON_VALUE(E, '$.Id') FROM SkuPrice CROSS JOIN "
        "UNNEST(JSON_EXTRACT_ARRAY(ContractApplied, '$.Elements')) AS E",
        {"ContractApplied"},
        id="unnest-argument-resolved-in-its-query",
    ),
    pytest.param(
        "SELECT Total FROM CostAndUsage CU CROSS JOIN LATERAL "
        "(SELECT CU.BilledCost * 2 AS Total) AS L ORDER BY Total",
        set(),
        id="lateral-output-alias",
    ),
    pytest.param(
        "SELECT SUM(ListUnitPrice) AS ListUnitPrice FROM SkuPrice",
        {"ListUnitPrice"},
        id="alias-does-not-vouch-for-its-own-input",
    ),
    pytest.param(
        "SELECT SUM(BilledCost) AS Total FROM CostAndUsage ORDER BY Total",
        set(),
        id="alias-resolves-in-its-own-query",
    ),
    pytest.param(
        "SELECT InvoiceId FROM InvoiceDetail WHERE EXISTS "
        "(SELECT BilledCost AS Amount FROM CostAndUsage UNION ALL "
        "SELECT BilledCost FROM InvoiceDetail ORDER BY Amount)",
        set(),
        id="alias-resolves-in-union-order-by",
    ),
    pytest.param(
        "SELECT P.SkuPriceId, Compute FROM CostAndUsage PIVOT (SUM(BilledCost) "
        "FOR InvoiceId IN ('a' AS Compute, 'b' AS Storage)) AS P",
        set(),
        id="pivot-alias-and-output-names",
    ),
    pytest.param(
        "SELECT TRIM(E) AS E FROM CostAndUsage "
        "CROSS JOIN UNNEST(ContractApplied) AS E",
        set(),
        id="alias-repeats-an-unnest-alias",
    ),
    pytest.param(
        "SELECT JT.ContractName AS ContractName FROM CostAndUsage CU, "
        "JSON_TABLE(CU.ContractApplied, '$.Elements[*]' "
        "COLUMNS (ContractName VARCHAR(50) PATH '$.Name')) AS JT",
        set(),
        id="alias-repeats-a-json-table-column",
    ),
    pytest.param(
        "WITH Totals AS (SELECT InvoiceId FROM CostAndUsage) "
        "SELECT InvoiceId FROM totals",
        set(),
        id="cte-named-in-different-case",
    ),
    pytest.param(
        "WITH T AS (SELECT InvoiceId FROM CostAndUsage) SELECT InvoiceId "
        "FROM T WHERE EXISTS (WITH t AS (SELECT InvoiceId FROM InvoiceDetail) "
        "SELECT InvoiceId FROM t)",
        set(),
        id="nested-ctes-named-in-different-case",
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
    pytest.param(
        "WITH T AS (SELECT CU.* FROM CostAndUsage CU "
        "JOIN SkuPrice SP ON CU.SkuPriceId = SP.SkuPriceId) "
        "SELECT T.BilledCost, T.UnitPrice FROM T",
        {"T.UnitPrice"},
        id="qualified-star-cte-exposes-only-its-table",
    ),
]


@pytest.mark.parametrize("sql, expected", _SELF_TEST_CASES)
def test_column_check_resolves_references_per_table(sql, expected):
    """The column check flags exactly the references that do not resolve."""
    assert set(_unresolved_columns(sql, _SELF_TEST_DATASET_COLUMNS)) == expected
