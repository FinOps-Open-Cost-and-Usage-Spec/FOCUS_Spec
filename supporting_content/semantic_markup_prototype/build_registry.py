#!/usr/bin/env python3
"""Build the FOCUS entity registry from the specification source files.

The registry is the single source of truth for every entity that semantic
references can point to: columns, column values, datasets, attributes,
operating model conditions, JSON objects and their schemas, metadata fields,
and glossary terms. Nothing in it is written by hand. Each entry is derived
from the file that defines the entity.

Each entry records:

* type: col, val, ds, attr, omc, obj, schema, meta, or term
* id: the canonical identifier (ColumnId, attribute ID, glossary key, ...)
* display: the Display Name or glossary term as written in its heading
* aliases: other names that resolve to the entity (from front matter)
* anchor: the anchor the assembled spec uses (same algorithm as markdown-pp)
* source: the defining file, relative to the specification directory
* dataset (col, val, obj), column (val, obj), collection (meta): the scope the
  entity is defined in; a meta entry's collection is the Metadata ID of the
  collection that contains it, or absent at the top level

Definitions are recognized by structure, not markup: a column is a file under
datasets/<dataset>/columns/ with "## Column ID" and "## Display Name" sections,
a JSON object is a "### Object ID" (or "### Value ID") and "### Object Display
Name" pair in a column file, a schema is a level-3 heading in
schemas/schemas.mdpp, a metadata field is a file under metadata/ with
"## Metadata ID" and "## Metadata Name" sections, and so on. That structure is the contract, so this script also checks it
(REG codes below) and reports any definition it cannot read reliably.

The source files are expected to contain mistakes, and finding them is a goal.
A finding means two places that should agree do not (an ID and a file name, a
heading and a name section, the specification and the Requirements Model). It
does not say which one is wrong; messages name both sides and leave that to a
person.

Optional YAML front matter on a defining file holds what the structure cannot:

    ---
    aliases: [invoice issuer name]
    ---

In glossary.md, aliases are keyed by glossary key:

    ---
    aliases:
      covered-charge: [covered]
    ---

Any file outside datasets/ may name the dataset its unqualified column
references resolve to (files under datasets/ take it from their location):

    ---
    dataset: CostAndUsage
    ---

Definition checks:

* REG001 error  column file has no Column ID or no Display Name section
* REG002 warn   column file H1 differs from its Display Name
* REG003 warn   Column ID is not PascalCase
* REG004 error  Allowed Values table has no "Value" column or column headed with the Display Name
* REG005 warn   the same allowed value is listed twice for one column
* REG006 warn   glossary key does not match its term (e.g., key "covered-charge" for "Covered Charge")
* REG007 warn   Content Constraints "Dataset" row does not name the column's own dataset
* REG008 error  an alias or name is shared by two entities of the same type
* REG009 info   an alias or name is shared by entities of different types (references must state the type)
* REG010 error  malformed glossary anchor (the term would be silently dropped)
* REG011 warn   unknown front matter key, or an alias for an unknown glossary key
* REG012 warn   a file under datasets/ declares a dataset in front matter
* REG013 error  an ID section without its name section, or the reverse; or an attribute,
                operating model condition, or dataset file with neither (its ID falls back to its H1)
* REG014 warn   a dataset, attribute, operating model condition, or metadata file's H1, or an
                object's level-2 heading, differs from its name
* REG016 warn   a file or folder that defines an entity is not named after its ID in lowercase,
                per the Repository Naming Conventions (e.g., numericformat.md for NumericFormat)
* REG017 warn   the specification and the Requirements Model disagree: an entity with no rule
                file, a rule file with no entity, or a different ID or name (see below)

Requirements Model cross-check (REG017). The rule files under
requirements_model/releases/latest/model_rules/ are named after the entity they
cover, like the specification files: attributes/<id>.json,
conditions/<id>.json, and datasets/<dataset>/<id>.json, columns/<id>.json, and
objects/<id>.json. Each rule records the EntityId and EntityName it applies to.
Neither side is treated as correct. Every column, dataset, attribute, operating
model condition, and JSON object is expected to have a rule file, every rule file
to match an entity, and the ID and name in the rules to match the
specification's; any difference is reported for a person to resolve on either
side. Metadata fields and schemas
have no rule files, so they are not checked. A rule file whose rules all have
Status "Removed" is history for a removed entity and is expected to have no
entity. This is one possible answer to how
the registry relates to the Requirements Model (#2406); the build does not
fail on it.

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
FRONT_MATTER_KEYS = {"aliases", "dataset"}


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


def section_body(text, heading, level=2):
    """Return the text under a heading, up to the next heading of the same or a higher level."""
    hashes = "#" * level
    # A trailing comment such as <!--SkipTOC--> is not part of the heading
    match = re.search(rf"^{hashes} {re.escape(heading)}\s*(?:<!--.*?-->)?\s*\n(.*?)(?=^#{{1,{level}}} |\Z)",
                      text, re.M | re.S)
    return match.group(1).strip() if match else None


def id_and_name(text, id_heading, name_heading, source, diag, level=2):
    """Return (id, name) for a definition, None when the file has neither section."""
    ident = section_body(text, id_heading, level)
    name = section_body(text, name_heading, level)
    if ident is None and name is None:
        return None
    if not ident or not name:
        diag.report("ERROR", "REG013", source, f'has "{id_heading}" or "{name_heading}" but not both')
        return None
    return ident, name


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


def check_name(path, ident, source, diag):
    """REG016: an entity's file (or folder) is named after its ID in lowercase."""
    name = path.name if path.is_dir() else path.stem
    if name != ident.lower():
        convention = ident.lower() + ("" if path.is_dir() else path.suffix)
        kind = "folder" if path.is_dir() else "file"
        diag.report("WARN", "REG016", source, f'{kind} name "{path.name}" and ID {ident} disagree '
                    f'(the naming convention pairs {ident} with "{convention}")')


def entity_id(text, id_heading, name_heading, title, source, diag):
    """Return (id, name) from a definition's ID and name sections, checking the name against the H1.
    Without the sections, fall back to an ID derived from the H1 and report it."""
    found = id_and_name(text, id_heading, name_heading, source, diag)
    if found is None:
        diag.report("ERROR", "REG013", source, f'no "{id_heading}" section; ID derived from the H1')
        return pascal_id(title), title
    if found[1] != title:
        diag.report("WARN", "REG014", source, f'H1 "{title}" differs from {name_heading} "{found[1]}"')
    return found


def check_no_dataset(front, source, diag):
    if "dataset" in front:
        diag.report("WARN", "REG012", source, "files under datasets/ take their dataset from their location")


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
        ds_id, ds_name = entity_id(text, "Dataset ID", "Display Name", ds_title, src.rel(dataset_md), diag)
        check_no_dataset(front, src.rel(dataset_md), diag)
        check_name(dataset_md.parent, ds_id, src.rel(dataset_md), diag)
        add(type="ds", id=ds_id, display=ds_name, anchor=ds_anchor, source=src.rel(dataset_md),
            aliases=aliases_of(front, src.rel(dataset_md), diag))

        for col_md in sorted((dataset_md.parent / "columns").glob("*.md")):
            source = src.rel(col_md)
            front, text = split_front_matter(src.read(col_md))
            check_no_dataset(front, source, diag)
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
            else:
                check_name(col_md, col_id, source, diag)

            constraints = section_body(text, "Content Constraints")
            ds_row = next((r for r in table_rows(constraints or "") if r and r[0] == "Dataset"), None)
            if ds_row is None or link_text(ds_row[1]) != ds_title:
                found = link_text(ds_row[1]) if ds_row else "no Dataset row"
                diag.report("WARN", "REG007", source,
                            f'Content Constraints Dataset is "{found}", but the file is in the "{ds_title}" dataset folder')

            col_anchor = f"{ds_anchor}.{anchor_part(title)}"
            add(type="col", id=col_id, display=display, dataset=ds_id, anchor=col_anchor,
                source=source, aliases=aliases_of(front, source, diag))

            # A JSON column defines its object (or value) under a level-2 heading named by it
            for label in ("Object", "Value"):
                found = id_and_name(text, f"{label} ID", f"{label} Display Name", source, diag, level=3)
                if found is None:
                    continue
                obj_id, obj_name = found
                if not re.search(rf"^## {re.escape(obj_name)}\s*$", text, re.M):
                    diag.report("WARN", "REG014", source, f'no level-2 heading "{obj_name}" for {obj_id}')
                add(type="obj", id=obj_id, display=obj_name, dataset=ds_id, column=col_id,
                    anchor=f"{col_anchor}.{anchor_part(obj_name)}", source=source)

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

    # Attributes and operating model conditions: one entity per file, with ID and name sections
    for kind, folder, overview, id_heading, name_heading in (
        ("attr", "attributes", "attributes_overview.md", "Attribute ID", "Attribute Name"),
        ("omc", "operating_model_conditions", "operating_model_conditions_overview.md",
         "Operating Model Condition ID", "Display Name"),
    ):
        prefix = anchor_part(h1(src.read(spec_dir / folder / overview), overview))
        for md in sorted((spec_dir / folder).glob("*.md")):
            if md.name == overview:
                continue
            front, text = split_front_matter(src.read(md))
            title = h1(text, md)
            ident, name = entity_id(text, id_heading, name_heading, title, src.rel(md), diag)
            check_name(md, ident, src.rel(md), diag)
            add(type=kind, id=ident, display=name,
                anchor=f"{prefix}.{anchor_part(title)}", source=src.rel(md),
                aliases=aliases_of(front, src.rel(md), diag))

    # JSON schemas: level-3 headings in schemas/schemas.mdpp, grouped by dataset at level 2
    schemas_mdpp = spec_dir / "schemas" / "schemas.mdpp"
    text = src.read(schemas_mdpp)
    root = anchor_part(h1(text, schemas_mdpp))
    group = None
    for block in re.split(r"(?m)^(?=#{2,3} )", text):
        heading = block.splitlines()[0]
        if heading.startswith("## "):
            group = anchor_part(heading[3:].strip())
        elif heading.startswith("### "):
            title = heading[4:].strip()
            schema_id = pascal_id(title)
            include = re.search(r'^!INCLUDECODE "([^"]+)"', block, re.M)
            if include:
                check_name(spec_dir / include.group(1), schema_id, src.rel(schemas_mdpp), diag)
            add(type="schema", id=schema_id, display=title, anchor=f"{root}.{group}.{anchor_part(title)}",
                source=src.rel(schemas_mdpp))

    # Metadata: each folder under metadata/ is a collection whose *_overview.md
    # defines it; every other file with a Metadata ID defines a field in it
    def overview(folder):
        return next(iter(sorted(folder.glob("*_overview.md"))), None)

    def collection_anchor(folder):
        part = anchor_part(h1(src.read(overview(folder)), overview(folder)))
        return part if folder == spec_dir / "metadata" else f"{collection_anchor(folder.parent)}.{part}"

    def collection_id(folder):
        if folder == spec_dir / "metadata":
            return None
        found = id_and_name(split_front_matter(src.read(overview(folder)))[1], "Metadata ID", "Metadata Name",
                            src.rel(overview(folder)), Diagnostics())
        return found[0] if found else None

    for md in sorted((spec_dir / "metadata").rglob("*.md")):
        source = src.rel(md)
        front, text = split_front_matter(src.read(md))
        found = id_and_name(text, "Metadata ID", "Metadata Name", source, diag)
        if found is None:
            continue
        meta_id, name = found
        title = h1(text, md)
        if title != name:
            diag.report("WARN", "REG014", source, f'H1 "{title}" differs from Metadata Name "{name}"')
        if md == overview(md.parent):
            # A collection is defined by its folder; the overview file itself uses kebab-case
            check_name(md.parent, meta_id, source, diag)
            anchor, collection = collection_anchor(md.parent), collection_id(md.parent.parent)
        else:
            check_name(md, meta_id, source, diag)
            anchor, collection = f"{collection_anchor(md.parent)}.{anchor_part(title)}", collection_id(md.parent)
        entry = dict(type="meta", id=meta_id, display=name, anchor=anchor, source=source,
                     aliases=aliases_of(front, source, diag))
        if collection:
            entry["collection"] = collection
        add(**entry)

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
            diag.report("WARN", "REG006", "glossary.md", f'key "{key}" and term "{term}" disagree (the term gives "{expected}")')
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


RULE_TYPES = {"Column": "col", "Dataset": "ds", "Attribute": "attr", "Condition": "omc", "Object": "obj"}


def rule_path(e, by_dataset):
    """The rule file a registry entity should have, relative to model_rules/."""
    if e["type"] == "attr":
        return f'attributes/{e["id"].lower()}.json'
    if e["type"] == "omc":
        return f'conditions/{e["id"].lower()}.json'
    folder = Path(by_dataset[e["id"] if e["type"] == "ds" else e["dataset"]]["source"]).parent.name
    sub = {"ds": "", "col": "columns/", "obj": "objects/"}[e["type"]]
    return f'datasets/{folder}/{sub}{e["id"].lower()}.json'


def check_requirements_model(entities, spec_dir, release, diag):
    """REG017: compare the registry with the Requirements Model rule files."""
    rules_dir = spec_dir / "requirements_model" / "releases" / release / "model_rules"
    if not rules_dir.is_dir():
        diag.report("INFO", "REG017", "registry", f"no Requirements Model at {rules_dir}; cross-check skipped")
        return
    shown = f"requirements_model/releases/{release}/model_rules"
    by_dataset = {e["id"]: e for e in entities if e["type"] == "ds"}
    expected = {rule_path(e, by_dataset): e for e in entities if e["type"] in RULE_TYPES.values()}
    for path in sorted(rules_dir.rglob("*.json")):
        rel = path.relative_to(rules_dir).as_posix()
        rules = json.loads(path.read_text(encoding="utf-8")).values()
        # A dataset's rule file also covers each column's presence; its own entity is the one named like the file
        own = [r for r in rules if str(r.get("EntityId", "")).lower() == path.stem]
        # Rules for removed entities stay in the model as history, with Status "Removed"
        removed = bool(own) and all(r.get("Status") == "Removed" for r in own)
        entity = expected.pop(rel, None)
        if entity is None:
            if removed:
                continue
            kind = own[0].get("EntityType", "entity") if own else "entity"
            diag.report("WARN", "REG017", f"{shown}/{rel}", f"active rule file for {kind} "
                        f'"{own[0]["EntityId"] if own else path.stem}" matches no entity in the specification')
            continue
        if not own:
            diag.report("WARN", "REG017", f"{shown}/{rel}", f'no rule names {entity["id"]} as its EntityId')
            continue
        if removed:
            diag.report("WARN", "REG017", f"{shown}/{rel}",
                        f'every rule for {entity["id"]} has Status "Removed", but the specification defines it')
        rule_id = max({r["EntityId"] for r in own}, key=[r["EntityId"] for r in own].count)
        if rule_id != entity["id"]:
            diag.report("WARN", "REG017", f"{shown}/{rel}",
                        f'rule EntityId "{rule_id}" and specification ID "{entity["id"]}" ({entity["source"]}) disagree')
        names = {r.get("EntityName") for r in own if r.get("EntityName")}
        if names and entity["display"] not in names:
            diag.report("WARN", "REG017", f"{shown}/{rel}",
                        f'rule EntityName "{sorted(names)[0]}" and specification name "{entity["display"]}" '
                        f'({entity["source"]}) disagree')
    for rel, entity in sorted(expected.items()):
        diag.report("WARN", "REG017", entity["source"], f'{entity["id"]} matches no rule file ({shown}/{rel})')


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--spec-dir", type=Path, default=DEFAULT_SPEC_DIR)
    parser.add_argument("--overlay", type=Path)
    parser.add_argument("--out", type=Path, default=HERE / "build" / "registry.json")
    parser.add_argument("--strict", action="store_true", help="exit non-zero on any error")
    parser.add_argument("--rm-release", default="latest",
                        help="Requirements Model release to cross-check (default: latest; 'none' skips it)")
    args = parser.parse_args()

    diag = Diagnostics()
    src = Source(args.spec_dir.resolve(), args.overlay.resolve() if args.overlay else None)
    entities = collect(src, diag)
    check_names(entities, diag)
    if args.rm_release != "none":
        check_requirements_model(entities, src.spec_dir, args.rm_release, diag)

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
