"""Validate SQL code blocks in the specification documentation.

Runs as part of the spec build (see the Makefile). Every ```sql fenced code
block in a searched directory must:

* contain syntactically valid SQL, and
* reference only real FOCUS columns (or query-local names such as aliases,
  CTEs, and table aliases).

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
from sqlglot.errors import ParseError
from sqlglot.tokens import Tokenizer, TokenType

SPEC_DIR = Path(__file__).resolve().parent.parent
DATASETS_DIR = SPEC_DIR / "datasets"

# Directories (relative to the specification/ root) searched for ```sql blocks.
# Append more section names here to extend coverage over time.
SQL_SEARCH_DIRS = [
    SPEC_DIR / "datasets",
    SPEC_DIR / "supported_features",
]


def _collect_column_ids():
    """Return the set of FOCUS Column IDs, read from each column's ``.md`` file.

    Every column document has a ``## Column ID`` section holding the PascalCase
    identifier (e.g. ``BilledCost``). Lower-cased for case-insensitive matching,
    since SQL identifiers are case-insensitive.
    """
    column_id_re = re.compile(
        r"^##\s*Column ID\s*\n+\s*([A-Za-z0-9_]+)", re.MULTILINE
    )
    ids = set()
    for column_file in DATASETS_DIR.rglob("columns/*.md"):
        match = column_id_re.search(column_file.read_text(encoding="utf-8"))
        if match:
            ids.add(match.group(1).lower())
    return ids


COLUMN_IDS = _collect_column_ids()

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


@pytest.mark.parametrize("sql", _PARAMS)
def test_sql_block_references_known_columns(sql):
    """Each column reference is a FOCUS column, a local name, or an x_ column."""
    if sql is None:
        pytest.skip("no ```sql blocks found in the searched directories")

    try:
        statements = sqlglot.parse(sql)
    except ParseError:
        pytest.skip("block is not valid SQL (reported by test_sql_block_is_valid)")

    unknown = {}
    for tree in statements:
        if tree is None:
            continue
        local = _local_names(tree)
        for column in tree.find_all(exp.Column):
            name = column.name
            if not name or name.startswith("x_"):
                continue
            if name.lower() in COLUMN_IDS or name.lower() in local:
                continue
            unknown.setdefault(name, None)

    if unknown:
        names = ", ".join(sorted(unknown))
        pytest.fail(
            f"SQL references unknown column(s): {names}\n\n{sql}", pytrace=False
        )
