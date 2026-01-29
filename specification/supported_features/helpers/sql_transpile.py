#!/usr/bin/env python3
import argparse
import glob
import re
import sys
from typing import Optional, List, Tuple

import sqlglot
from sqlglot.errors import ParseError

# Prefer the engines you most commonly use by ordering them first
CANDIDATE_DIALECTS: List[str] = [
    "bigquery", "trino", "presto", "duckdb", "mysql", "postgres",
    "snowflake", "tsql", "spark", "hive", "redshift", "sqlite", "oracle", None
]

# Matches fenced code blocks like:
# ```sql
# ...code...
# ```
# and also allows a dialect hint after `sql`, e.g.:
# ```sql trino
# ```sql:bigquery
FENCE_RE = re.compile(
    r"```sql(?:[ \t]+([\w:-]+))?[ \t]*\n(.*?)\n```",
    re.IGNORECASE | re.DOTALL
)

def parse_fenced_sql(md_text: str) -> List[Tuple[int, Optional[str], str]]:
    """
    Return a list of (block_index, hint, sql_text) for each fenced ```sql block.
    'hint' is an optional dialect hint following 'sql' in the fence.
    """
    blocks = []
    for i, m in enumerate(FENCE_RE.finditer(md_text), start=1):
        raw_hint = m.group(1) or ""
        # Normalize hint: accept "trino", "sql:trino", "sql-trino", "trino:xyz"
        hint = raw_hint.strip().lower()
        hint = hint.replace("sql:", "").replace("sql-", "")
        hint = hint.split(":")[0] if ":" in hint else hint  # keep left-most token if colon-separated
        hint = hint or None
        sql_text = m.group(2).strip()
        blocks.append((i, hint, sql_text))
    return blocks

def detect_dialect(sql: str) -> Optional[str]:
    """Heuristically detect a dialect by attempting to parse with common dialects."""
    successes = []
    for d in CANDIDATE_DIALECTS:
        try:
            sqlglot.parse(sql, read=d)
            successes.append(d)
        except ParseError:
            continue
    return successes[0] if successes else None

def transpile_sql(sql: str, read: Optional[str], write: str) -> str:
    if write is not None and write.lower() == "ansi":
        write = None  # SQLGlot uses None for ANSI
    if read is not None and read.lower() == "ansi":
        read = None
    parts = sqlglot.transpile(
        sql,
        read=read,     # None => let SQLGlot assume ANSI-ish
        write=write,
        pretty=True,
    )
    return ";\n".join(p.strip() for p in parts if p.strip())

def main():
    ap = argparse.ArgumentParser(
        description="Find ```sql blocks in Markdown, detect dialect, and transpile with SQLGlot."
    )
    ap.add_argument("files", nargs='+', help="Markdown files or glob patterns (e.g., 'docs/*.md' or file1.md file2.md)")
    ap.add_argument("--to", default="ansi", help="Target dialect (default: ansi)")
    ap.add_argument("--prefer", action="append", default=[],
                    help="Prefer this dialect in detection (can be given multiple times).")
    ap.add_argument("--list", action="store_true",
                    help="Only list sql blocks found, do not transpile.")
    args = ap.parse_args()

    # If user provided preferred dialects, move them to the front of the candidate list
    if args.prefer:
        preferred = [d.lower() for d in args.prefer]
        uniq = []
        for d in preferred + CANDIDATE_DIALECTS:
            if d not in uniq:
                uniq.append(d)
        CANDIDATE_DIALECTS[:] = uniq

    # Collect all files from patterns and individual files
    all_files = []
    for pattern_or_file in args.files:
        matched = glob.glob(pattern_or_file)
        if matched:
            all_files.extend(matched)
        else:
            # If no glob match, treat as individual file
            all_files.append(pattern_or_file)
    
    files = sorted(set(all_files))  # Remove duplicates and sort
    if not files:
        print("No files found.", file=sys.stderr)
        sys.exit(1)

    for path in files:
        with open(path, "r", encoding="utf-8") as f:
            md_text = f.read()

        blocks = parse_fenced_sql(md_text)

        print(f"=== {path} ===")
        if not blocks:
            print("(no ```sql code blocks found)\n")
            continue

        for idx, hint, sql in blocks:
            print(f"[block #{idx}]")
            if args.list:
                print(f"  hint: {hint or '(none)'}")
                print(f"  first line: {sql.splitlines()[0] if sql.splitlines() else ''}")
                continue
            if hint not in CANDIDATE_DIALECTS:
                hint = None  # ignore unrecognized hints
            read = hint or detect_dialect(sql)
            
            detected_label = read or "ansi (fallback)"
            try:
                out = transpile_sql(sql, read=read, write=args.to)
                print(f"Detected: {detected_label} -> {args.to}")
                print(out)
            except ParseError as e:
                print(f"Detected: {detected_label} -> {args.to}")
                print(f"ERROR: {e}", file=sys.stderr)
            print()  # spacing between blocks

        print()  # spacing between files

if __name__ == "__main__":
    main()
