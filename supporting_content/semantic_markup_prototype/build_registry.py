#!/usr/bin/env python3
"""Build the FOCUS entity registry from the specification source files.

The registry is the single source of truth for every entity that semantic
references can point to: columns, column values, datasets, attributes,
operating model conditions, and glossary terms. Nothing in it is written
by hand. Each entry is derived from the file that defines the entity.

Each entry records:

* type: col, val, ds, attr, omc, or term
* id: the canonical identifier (ColumnId, attribute ID, glossary key, ...)
* display: the Display Name or glossary term as written in its heading
* aliases: other names that resolve to the entity (from front matter)
* anchor: the anchor the assembled spec uses (same algorithm as markdown-pp)
* source: the defining file, relative to the specification directory

Definitions are recognized by structure, not markup: a column is a file under
datasets/<dataset>/columns/ with "## Column ID" and "## Display Name" sections,
and so on. That structure is the contract, so this script also checks it
(REG codes below) and reports any definition it cannot read reliably.

Optional YAML front matter on a defining file holds what the structure cannot:

    ---
    aliases: [invoice issuer name]
    ---

In glossary.md, aliases are keyed by glossary key:

    ---
    aliases:
      covered-charge: [covered]
    ---

Definition checks:

* REG001 error  column file has no Column ID or no Display Name section
* REG002 warn   column file H1 differs from its Display Name
* REG003 warn   Column ID is not PascalCase, or does not match the file name
* REG004 error  Allowed Values table has no "Value" column or column headed with the Display Name
* REG005 warn   the same allowed value is listed twice for one column
* REG006 warn   glossary key does not match its term (e.g., key "covered-charge" for "Covered Charge")
* REG007 warn   Content Constraints "Dataset" row does not name the column's own dataset
* REG008 error  an alias or name is shared by two entities of the same type
* REG009 info   an alias or name is shared by entities of different types (references must state the type)
* REG010 error  malformed glossary anchor (the term would be silently dropped)
* REG011 warn   unknown front matter key, or an alias for an unknown glossary key

Usage:
    ./build_registry.py [--spec-dir DIR] [--overlay DIR] [--out registry.json] [--strict]

--overlay DIR reads a file from DIR instead of the spec when DIR holds a file at
the same relative path. The prototype uses it to try front matter without
editing specification/.
"""

import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_SPEC_DIR = HERE.parent.parent / "specification"
FRONT_MATTER_KEYS = {"aliases"}


class Diagnostics:
    def __init__(self):
        self.counts = {"ERROR": 0, "WARN": 0, "INFO": 0}

    def report(self, level, code, source, message):
        self.counts[level] += 1
        print(f"{source}: {level} {code} {message}", file=sys.stderr)


class Source:
    """Reads spec files, preferring an overlay copy when one exists."""

    def __init__(self, spec_dir, overlay=None):
        self.spec_dir = spec_dir
        self.overlay = overlay

    def rel(self, path):
        return str(path.relative_to(self.spec_dir))

    def read(self, path):
        if self.overlay:
            candidate = self.overlay / path.relative_to(self.spec_dir)
            if candidate.exists():
                return candidate.read_text(encoding="utf-8")
        return path.read_text(encoding="utf-8")


def split_front_matter(text):
    """Return (front matter dict, body). Supports the small YAML subset used here:
    "key: value", "key: [a, b]", and one level of "  key: [a, b]" under a key."""
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not match:
        return {}, text
    data, current = {}, None
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        nested = line.startswith((" ", "\t"))
        key, _, value = line.strip().partition(":")
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            value = [v.strip().strip("'\"") for v in value[1:-1].split(",") if v.strip()]
        if nested and current is not None:
            data[current][key.strip()] = value
        elif value == "":
            current = key.strip()
            data[current] = {}
        else:
            current = None
            data[key.strip()] = value
    return data, text[match.end():]


def anchor_part(title):
    """Mirror MarkdownPP TableOfContents anchor cleaning for one heading."""
    return re.sub(r"([\s,-,\(,\)]+)", "", title).lower()


def pascal_id(title):
    """Derive an ID from a heading, e.g. "Numeric Format" -> "NumericFormat"."""
    return "".join(w[:1].upper() + w[1:] for w in re.split(r"[\s/-]+", title) if w)


def h1(text, source):
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError(f"No level-1 heading in {source}")


def section_body(text, heading):
    """Return the text under a level-2 heading, up to the next level-2 heading."""
    match = re.search(rf"^## {re.escape(heading)}\s*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    return match.group(1).strip() if match else None


def table_rows(body):
    return [[c.strip() for c in line.strip().strip("|").split("|")]
            for line in body.splitlines() if line.strip().startswith("|")]


def allowed_values(body, display):
    """Return the allowed values in an Allowed Values table, or None when the
    table has no column headed "Value" or headed with the column's Display Name."""
    rows = table_rows(body)
    if len(rows) < 3:
        return None
    header = rows[0]
    for name in ("Value", display):
        if name in header:
            index = header.index(name)
            return [row[index] for row in rows[2:] if len(row) > index and row[index]]
    return None


def link_text(cell):
    match = re.match(r"\[([^\]]+)\]", cell)
    return match.group(1) if match else cell


def aliases_of(front, source, diag):
    for key in front:
        if key not in FRONT_MATTER_KEYS:
            diag.report("WARN", "REG011", source, f'unknown front matter key "{key}"')
    aliases = front.get("aliases", [])
    return aliases if isinstance(aliases, list) else [aliases]


def collect(src, diag):
    spec_dir = src.spec_dir
    entities = []

    def add(**entry):
        entry.setdefault("aliases", [])
        entities.append(entry)

    # Datasets and their columns
    data_model = anchor_part(h1(src.read(spec_dir / "datasets" / "data_model.md"), "data_model.md"))
    for dataset_md in sorted((spec_dir / "datasets").glob("*/dataset.md")):
        front, text = split_front_matter(src.read(dataset_md))
        ds_title = h1(text, dataset_md)
        ds_anchor = f"{data_model}.{anchor_part(ds_title)}"
        ds_id = pascal_id(ds_title)
        add(type="ds", id=ds_id, display=ds_title, anchor=ds_anchor, source=src.rel(dataset_md),
            aliases=aliases_of(front, src.rel(dataset_md), diag))

        for col_md in sorted((dataset_md.parent / "columns").glob("*.md")):
            source = src.rel(col_md)
            front, text = split_front_matter(src.read(col_md))
            col_id = section_body(text, "Column ID")
            display = section_body(text, "Display Name")
            if not col_id or not display:
                diag.report("ERROR", "REG001", source, "no Column ID or Display Name section; column skipped")
                continue
            title = h1(text, col_md)
            if title != display:
                diag.report("WARN", "REG002", source, f'H1 "{title}" differs from Display Name "{display}"')
            if not re.fullmatch(r"[A-Z][A-Za-z0-9]*", col_id):
                diag.report("WARN", "REG003", source, f'Column ID "{col_id}" is not PascalCase')
            elif col_md.stem != col_id.lower():
                diag.report("WARN", "REG003", source, f'file name "{col_md.name}" does not match Column ID "{col_id}"')

            constraints = section_body(text, "Content Constraints")
            ds_row = next((r for r in table_rows(constraints or "") if r and r[0] == "Dataset"), None)
            if ds_row is None or link_text(ds_row[1]) != ds_title:
                found = link_text(ds_row[1]) if ds_row else "no Dataset row"
                diag.report("WARN", "REG007", source, f'Content Constraints Dataset is "{found}", expected "{ds_title}"')

            col_anchor = f"{ds_anchor}.{anchor_part(title)}"
            add(type="col", id=col_id, display=display, dataset=ds_id, anchor=col_anchor,
                source=source, aliases=aliases_of(front, source, diag))

            allowed = section_body(text, "Allowed Values")
            if allowed is None:
                continue
            values = allowed_values(allowed, display)
            if values is None:
                diag.report("ERROR", "REG004", source,
                            f'Allowed Values table has no "Value" or "{display}" column; values skipped')
                continue
            seen_values = set()
            for value in values:
                if value in seen_values:
                    diag.report("WARN", "REG005", source, f'allowed value "{value}" is listed twice')
                    continue
                seen_values.add(value)
                add(type="val", id=f"{col_id}.{value}", column=col_id, value=value, dataset=ds_id,
                    display=f'"{value}"', anchor=col_anchor, source=source)

    # Attributes and operating model conditions: one entity per file, named by its H1
    for kind, folder, overview in (
        ("attr", "attributes", "attributes_overview.md"),
        ("omc", "operating_model_conditions", "operating_model_conditions_overview.md"),
    ):
        prefix = anchor_part(h1(src.read(spec_dir / folder / overview), overview))
        for md in sorted((spec_dir / folder).glob("*.md")):
            if md.name == overview:
                continue
            front, text = split_front_matter(src.read(md))
            title = h1(text, md)
            add(type=kind, id=pascal_id(title), display=title,
                anchor=f"{prefix}.{anchor_part(title)}", source=src.rel(md),
                aliases=aliases_of(front, src.rel(md), diag))

    # Glossary terms: explicit <a name="glossary:key"><b>Term</b></a> anchors
    front, text = split_front_matter(src.read(spec_dir / "glossary.md"))
    for key in front:
        if key not in FRONT_MATTER_KEYS:
            diag.report("WARN", "REG011", "glossary.md", f'unknown front matter key "{key}"')
    glossary_aliases = front.get("aliases", {}) or {}
    pattern = re.compile(r'<a name="glossary:([^"]+)"><b>(.*?)</b></a>')
    keys = set()
    for lineno, line in enumerate(text.splitlines(), 1):
        if "glossary:" not in line or not line.lstrip().startswith("<a "):
            continue
        match = pattern.search(line)
        if not match:
            diag.report("ERROR", "REG010", "glossary.md", f"line {lineno}: malformed glossary anchor: {line.strip()}")
            continue
        key, term = match.groups()
        # A trailing acronym in parentheses, e.g. "Cloud Service Provider (CSP)", is not part of the key
        expected = re.sub(r"[^a-z0-9]+", "-", re.sub(r"\s*\([A-Z]+\)$", "", term).lower()).strip("-")
        if key.lower() != expected:
            diag.report("WARN", "REG006", "glossary.md", f'key "{key}" does not match term "{term}" (expected "{expected}")')
        keys.add(key)
        aliases = glossary_aliases.get(key, [])
        add(type="term", id=key, display=term, anchor=f"glossary:{key}",
            source=f"glossary.md#glossary:{key}", aliases=aliases if isinstance(aliases, list) else [aliases])
    for key in glossary_aliases:
        if key not in keys:
            diag.report("WARN", "REG011", "glossary.md", f'aliases given for unknown glossary key "{key}"')

    return entities


def check_names(entities, diag):
    """REG008/REG009: names (display and aliases) shared between entities."""
    names = {}
    for e in entities:
        if e["type"] == "val":
            continue
        for name in {e["display"].lower(), *(a.lower() for a in e["aliases"])}:
            names.setdefault(name, []).append(e)
    for name, owners in sorted(names.items()):
        # The same column defined in several datasets shares its name by design
        distinct = {(e["type"], e["id"]) for e in owners}
        if len(distinct) < 2:
            continue
        by_type = {}
        for e in owners:
            by_type.setdefault(e["type"], set()).add(e["id"])
        for kind, ids in by_type.items():
            if len(ids) > 1:
                diag.report("ERROR", "REG008", "registry",
                            f'"{name}" names several {kind} entities: {", ".join(sorted(ids))}')
        if len(by_type) > 1:
            parts = ", ".join(f"{k} {'/'.join(sorted(v))}" for k, v in sorted(by_type.items()))
            diag.report("INFO", "REG009", "registry", f'"{name}" is shared by {parts}; references must state the type')


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--spec-dir", type=Path, default=DEFAULT_SPEC_DIR)
    parser.add_argument("--overlay", type=Path)
    parser.add_argument("--out", type=Path, default=HERE / "build" / "registry.json")
    parser.add_argument("--strict", action="store_true", help="exit non-zero on any error")
    args = parser.parse_args()

    diag = Diagnostics()
    src = Source(args.spec_dir.resolve(), args.overlay.resolve() if args.overlay else None)
    entities = collect(src, diag)
    check_names(entities, diag)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(entities, indent=2) + "\n", encoding="utf-8")

    counts = {}
    for e in entities:
        counts[e["type"]] = counts.get(e["type"], 0) + 1
    summary = ", ".join(f"{n} {t}" for t, n in sorted(counts.items()))
    aliases = sum(len(e["aliases"]) for e in entities)
    print(f"Wrote {args.out} ({summary}; {aliases} aliases)")
    print(f"Definition checks: {diag.counts['ERROR']} error(s), {diag.counts['WARN']} warning(s), "
          f"{diag.counts['INFO']} info", file=sys.stderr)
    if args.strict and diag.counts["ERROR"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
