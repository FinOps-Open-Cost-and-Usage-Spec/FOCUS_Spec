#!/usr/bin/env python3
"""Rewrite specification source files to use semantic references.

It edits files in place, records each converted kind as "mechanical" in the
file's "semantic:" front matter (a kind already "reviewed" keeps that status),
and prints what it could not decide, which is left for a person:

* Hand-written links to an entity's anchor become semantic references, in the
  shortest form that resolves to the same entity:
  [*charge*](#glossary:charge) -> [charge](#term)
* Dataset-qualified column references lose a qualifier the file's dataset makes
  unnecessary: [BilledCost](#col:CostAndUsage.BilledCost) -> [BilledCost](#col)
* Italic phrases that name a glossary term become term references:
  *charges* -> [charges](#term)
* Display Names written as plain words become references when they name one
  entity unambiguously: at least two words, written exactly as the registry
  has them, outside quotes, headings, and code, and not also a glossary term.
  The file's own entity is tagged even when its name is one word.
  Billed Cost -> [Billed Cost](#col)
* A file with no dataset of its own gets a default from the columns it already
  references: when every hard-coded column link, and every ColumnId that only
  one dataset defines, points into a single dataset, the file gets
  "dataset: <Dataset>" in its front matter and shared ColumnIds resolve there.
* A quoted value right after a column reference becomes a value reference when
  the value is one of that column's allowed values:
  [ChargeCategory](#col) is "Tax" -> is ["Tax"](#val:ChargeCategory)
* ColumnIds, dataset IDs, attribute IDs, operating model condition IDs, JSON
  object and schema IDs, and multi-word metadata IDs written as plain words
  become references, including the file's own entity:
  BilledCost -> [BilledCost](#col), CostAndUsage -> [CostAndUsage](#ds)
* In a column file, quoted allowed values of that column become value
  references: "Correction" -> ["Correction"](#val:ChargeClass)

Left alone, and reported as NEEDS-REVIEW where relevant:

* Headings, code spans and blocks, raw HTML lines, existing link text, and the
  ID and name sections that define the entity (Column ID, Display Name, ...).
* Tables outside Content Constraints. Only Content Constraints tables link every
  row today; other tables (example data, catalogs of entities) are left as they
  are, and the count of such rows that hold references is reported.
* Display Names that are also a glossary term, that several entities share, or
  that are one word (other than the file's own entity), because plain prose may
  or may not mean the entity.
* ColumnIds that exist in several datasets when no single dataset can be
  inferred for the file.
* ColumnIds that are not in the file's dataset; they need a qualifier.

With --check it changes nothing. For each file, it reruns the conversion for the
kinds the file lists as "mechanical" and reports each line the converter would
change (FOCUS021), so a reference added later in the old style is caught. The
build runs it on every source file.

Usage:
    tag_sources.py --registry semantic-registry.json [--spec-dir DIR] [--kinds col,term,...] FILE...
    tag_sources.py --registry semantic-registry.json [--spec-dir DIR] --check FILE...
"""

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_registry import split_front_matter  # noqa: E402
from registry import TYPES, Registry  # noqa: E402
from resolve_semantic import conversion_status  # noqa: E402

LINK = re.compile(r"\[([^\]\n]+)\]\(([^)\s]+)\)")
CODE_SPAN = re.compile(r"(`+[^`]*`+)")
ITALIC = re.compile(r"(?<![*\w])\*(?![\s*])([^*\n]+?)(?<![\s*])\*(?![*\w])")
QUOTED = re.compile(r'(?<![\[\w])"([^"\n]+)"(?!\]\()')
DEFINITION_SECTIONS = {"Column ID", "Display Name", "Attribute ID", "Attribute Name",
                       "Operating Model Condition ID", "Dataset ID", "Metadata ID", "Metadata Name",
                       "Object ID", "Object Display Name", "Value ID", "Value Display Name"}


class Tagger:
    def __init__(self, registry, path, declared=None, kinds=None):
        self.registry = registry
        self.kinds = set(kinds or TYPES)
        self.path = path
        cols = registry.by_type["col"]
        self.home_col = next((e for e in cols if e["source"] == path), None)
        self.dataset = self.home_col["dataset"] if self.home_col else next(
            (e["id"] for e in registry.by_type["ds"] if Path(e["source"]).parent in Path(path).parents), declared)
        self.collection = registry.collection_of(path)
        # PascalCase IDs that may appear as plain words: columns, attributes, conditions,
        # JSON objects and schemas, and metadata IDs with more than one word
        # (one-word IDs such as Schema or Deprecated are also ordinary words)
        self.id_kind = {e["id"]: e["type"] for t in ("attr", "omc", "obj", "schema") for e in registry.by_type[t]}
        self.id_kind.update({e["id"]: "meta" for e in registry.by_type["meta"]
                             if re.search(r"[a-z0-9][A-Z]", e["id"])})
        self.id_kind.update({i: "col" for i in registry.col_ids})
        self.id_kind.update({e["id"]: "ds" for e in registry.by_type["ds"]})
        ids = sorted(self.id_kind, key=len, reverse=True)
        datasets = "|".join(sorted((e["id"] for e in registry.by_type["ds"]), key=len, reverse=True))
        # An optional dataset qualifier, e.g. CostAndUsage.BilledCost, is kept as written.
        # The head of a property path (ContractAppliedObject.Elements) is left alone.
        self.id_word = re.compile(r"(?<![\w\[#.`/])((?:(?:" + datasets + r")\.)?(?:" + "|".join(ids) + r"))(?![\w\]`(]|\.\w)")
        self.home_values = ({e["value"] for e in registry.by_type["val"]
                             if e["column"] == self.home_col["id"] and e["dataset"] == self.dataset}
                            if self.home_col else set())
        self.col_datasets = {}
        for e in registry.by_type["col"]:
            self.col_datasets.setdefault(e["id"], set()).add(e["dataset"])
        self.inferred = None
        self.used_default = False
        self.html_links = 0
        self.table_rows_skipped = 0
        self.home = self.home_col or next(
            (e for t in ("attr", "omc", "obj", "schema", "meta", "ds") for e in registry.by_type[t]
             if e["source"] == path), None)
        self.name_reason = {}
        self.name_re = self.build_names()
        self.changes = 0
        self.lineno = 0
        self.review = []

    def build_names(self):
        """Display Names that may be tagged in prose, and why the others may not."""
        names = {}
        for t in ("col", "attr", "omc", "ds", "obj", "schema", "meta"):
            for e in self.registry.by_type[t]:
                names.setdefault(e["display"], []).append(e)
        usable = []
        for name, entities in names.items():
            is_home = any(e is self.home for e in entities)
            if " " not in name and not is_home:
                continue
            ids = {(e["type"], e["id"]) for e in entities}
            if self.registry.find("term", None, name, None)[0] is not None:
                self.name_reason[name] = "also a glossary term"
            elif len(ids) > 1:
                self.name_reason[name] = "names several entities"
            elif entities[0]["type"] == "meta" and not self.path.startswith("metadata/"):
                self.name_reason[name] = "metadata name outside the metadata section (may mean a role or an ordinary phrase)"
            else:
                usable.append(name)
        # Skipped phrases stay in the pattern so a shorter name inside one is not tagged by mistake
        phrases = sorted([*usable, *self.name_reason], key=len, reverse=True)
        if not phrases:
            return None
        return re.compile(r"(?<![\w/#-])(" + "|".join(re.escape(n) for n in phrases) + r")(?![\w-])")

    def infer_dataset(self, text):
        """Pick the one dataset a file with none of its own is about, when its columns agree.

        Evidence is every column the file references that only one dataset can mean, in any
        form (hard-coded link, tag, plain ColumnId, plain Display Name). Reading tags as well
        as links keeps the decision the same after the file is converted.
        """
        if self.dataset or not self.ok("col"):
            return
        evidence = set()
        body = re.sub(r"```.*?```", "", text, flags=re.S)
        for target in re.findall(r"\]\(#(datamodel\.[^)\s]+)\)", body):
            entity = self.registry.anchors.get(target)
            if entity and entity["type"] == "col":
                evidence.add(entity["dataset"])
        for name, ident in re.findall(r"\[([^\]\n]+)\]\(#col(?::([^)\s]*))?\)", body):
            entity, _ = self.registry.find("col", ident or None, name, None)
            if entity:
                evidence.add(entity["dataset"])
        plain = CODE_SPAN.sub("", re.sub(r"\[[^\]\n]*\]\([^)]*\)", "", body))
        for word in self.id_word.findall(plain):
            datasets = self.col_datasets.get(word.rpartition(".")[2])
            if datasets and len(datasets) == 1:
                evidence |= datasets
        if self.name_re is not None:
            for m in self.name_re.finditer(plain):
                entity, _ = self.registry.find("col", None, m.group(1), None)
                if entity:
                    evidence.add(entity["dataset"])
        if len(evidence) == 1:
            self.inferred = self.dataset = next(iter(evidence))

    def ok(self, kind):
        """True when this run converts references of this kind."""
        return kind in self.kinds

    def note(self, lineno, message):
        self.review.append(f"{self.path}:{lineno}: NEEDS-REVIEW {message}")

    def reference(self, kind, entity, text):
        """Shortest semantic link for an entity, given the visible text."""
        found, _ = self.registry.find(kind, None, text, self.dataset, self.collection)
        if found is entity:
            if kind == "col" and len(self.col_datasets.get(entity["id"], ())) > 1:
                self.used_default = True
            return f"[{text}](#{kind})"
        ident = entity["id"]
        if kind in ("col", "meta"):
            qualified, _ = self.registry.find(kind, ident, text, self.dataset, self.collection)
            if qualified is not entity:
                ident = f'{entity.get("dataset") or entity.get("collection") or ""}.{ident}'
        return f"[{text}](#{kind}:{ident})"

    def convert_link(self, match):
        text, target = match.group(1), match.group(2)
        if not target.startswith("#"):
            return match.group(0)
        if target.startswith("#col:"):
            if not self.ok("col"):
                return match.group(0)
            # Drop a dataset qualifier the file's dataset makes unnecessary, unless the
            # visible text is qualified too (e.g., to contrast two datasets)
            if "." in text:
                return match.group(0)
            entity, _ = self.registry.find("col", target[5:], text, self.dataset)
            shorter = self.reference("col", entity, text) if entity else match.group(0)
            if shorter != match.group(0):
                self.changes += 1
            return shorter
        entity = self.registry.anchors.get(target[1:])
        if entity is None or not self.ok(entity["type"]):
            return match.group(0)
        raw = text.strip()
        # Strip emphasis only when it wraps the whole text; a stray * (e.g., "Allocated*") is text
        emphasized = len(raw) > 2 and raw[0] == raw[-1] and raw[0] in "*_" and raw[1] != raw[0]
        plain = raw[1:-1].strip() if emphasized else raw
        if emphasized and entity["type"] != "term" and plain[:1].islower():
            # A lowercase italic phrase linking to a non-term (e.g., *data generator*) is used like a
            # glossary term; tagging it as the entity would drop the italics
            self.note(self.lineno, f'italic link "{plain}" points to {entity["type"]} {entity["id"]}, not a glossary term; left as written')
            return match.group(0)
        self.changes += 1
        if entity["type"] == "col" and plain == f'{entity["dataset"]}.{entity["id"]}':
            return f"[{plain}](#col:{plain})"  # the text names the dataset, so the reference does too
        if entity["type"] in ("col", "attr", "omc", "obj", "schema", "meta", "ds") and "." not in plain:
            named, _ = self.registry.find(entity["type"], None, plain, self.dataset, self.collection)
            if named is not None and named["id"] != entity["id"]:
                self.note(self.lineno, f'link text "{plain}" names {named["id"]}, but the link points to {entity["id"]}')
        return self.reference(entity["type"], entity, plain)

    def convert_italic(self, match):
        phrase = match.group(1)
        entity, _ = self.registry.find("term", None, phrase, None)
        if entity is None or not self.ok("term"):
            return match.group(0)
        self.changes += 1
        return self.reference("term", entity, phrase)

    def convert_id(self, match, lineno):
        word = match.group(1)
        qualifier, _, bare = word.rpartition(".")
        kind = self.id_kind[bare]
        if not self.ok(kind):
            return word
        if qualifier and kind != "col":
            return word
        entity, error = self.registry.find(kind, word, bare, self.dataset, self.collection)
        if entity is None and kind == "col" and "is not in the" in (error or ""):
            # The column lives in exactly one other dataset: qualify it, which keeps the reference exact
            entity, _ = self.registry.find(kind, word, bare, None)
            if entity is not None:
                self.changes += 1
                return self.reference(kind, entity, word)
        if entity is None:
            self.note(lineno, f"{word}: {error}")
            return word
        self.changes += 1
        if qualifier:
            return f"[{word}](#col:{word})"
        return self.reference(kind, entity, word)

    def convert_value(self, match):
        value = match.group(1)
        if value not in self.home_values or not self.ok("val"):
            return match.group(0)
        self.changes += 1
        return f'["{value}"](#val:{self.home_col["id"]})'

    def convert_text(self, text, lineno):
        """Convert plain text that holds no links or code."""
        self.lineno = lineno
        text = ITALIC.sub(self.convert_italic, text)
        # Each step produces links; the next only touches what is still outside links
        text = self.map_plain(text, lambda c: self.tag_names(c, lineno))
        return self.map_plain(text, lambda c: self.tag_ids_and_values(c, lineno))

    @staticmethod
    def map_plain(text, fn):
        pieces = LINK.split(text)
        out = []
        for i in range(0, len(pieces), 3):
            out.append(fn(pieces[i]))
            if i + 2 < len(pieces):
                out.append(f"[{pieces[i + 1]}]({pieces[i + 2]})")
        return "".join(out)

    def tag_names(self, chunk, lineno):
        if self.name_re is None:
            return chunk

        def replace(m):
            phrase = m.group(1)
            if chunk[:m.start()].count('"') % 2:
                return phrase  # inside a quoted value
            if phrase in self.name_reason:
                self.note(lineno, f'plain display name "{phrase}"; {self.name_reason[phrase]}')
                return phrase
            entity, error = None, None
            for kind in ("col", "attr", "omc", "ds", "obj", "schema", "meta"):
                if any(e["display"] == phrase for e in self.registry.by_type[kind]):
                    entity, error = self.registry.find(kind, None, phrase, self.dataset, self.collection)
                    break
            if entity is None:
                self.note(lineno, f'plain display name "{phrase}"; {error}')
                return phrase
            if not self.ok(kind):
                return phrase
            self.changes += 1
            return self.reference(kind, entity, phrase)
        return self.name_re.sub(replace, chunk)

    def tag_ids_and_values(self, chunk, lineno):
        chunk = self.id_word.sub(lambda m: self.convert_id(m, lineno), chunk)
        if self.home_values:
            chunk = QUOTED.sub(self.convert_value, chunk)
        return chunk

    def convert_line(self, line, lineno):
        if line.lstrip().startswith("|"):
            # Convert cell by cell and keep each cell's width, so table columns stay aligned
            cells = line.split("|")
            for i, cell in enumerate(cells[1:-1], 1):
                new = self.convert_segment(cell, lineno)
                cells[i] = new.ljust(len(cell)) if len(new) < len(cell) else new
            return "|".join(cells)
        return self.convert_segment(line, lineno)

    def convert_segment(self, line, lineno):
        parts = CODE_SPAN.split(line)
        for i in range(0, len(parts), 2):
            segments = []
            last = 0
            for m in LINK.finditer(parts[i]):
                segments.append(self.convert_text(parts[i][last:m.start()], lineno))
                segments.append(self.convert_link(m))
                last = m.end()
            segments.append(self.convert_text(parts[i][last:], lineno))
            parts[i] = self.tag_column_values("".join(segments))
        return "".join(parts)

    COLUMN_VALUE = re.compile(r'(\[[^\]]+\]\(#col(?::([^)\s]+))?\)(?:\s+column)?\s+'
                              r'(?:is not|is|MUST NOT be|MUST be|equals|!=|=)\s+)"([^"\n]+)"(?!\]\()')

    def tag_column_values(self, text):
        """A quoted value right after a column reference, when it is one of that column's values."""
        if not self.ok("val"):
            return text
        def replace(m):
            ident = m.group(2) or re.match(r"\[([^\]]+)\]", m.group(1)).group(1)
            entity, _ = self.registry.find("col", ident if m.group(2) else None, ident, self.dataset)
            if entity is None:
                return m.group(0)
            value = m.group(3)
            if not any(e["column"] == entity["id"] and e["dataset"] == entity["dataset"] and e["value"] == value
                       for e in self.registry.by_type["val"]):
                return m.group(0)
            self.changes += 1
            return f'{m.group(1)}["{value}"](#val:{entity["dataset"]}.{entity["id"]})'
        return self.COLUMN_VALUE.sub(replace, text)

    def report_display_names(self, line, lineno):
        text = LINK.sub("", CODE_SPAN.sub("", line))
        for phrase in sorted(self.name_reason, key=len, reverse=True):
            if re.search(rf"(?<![\w-]){re.escape(phrase)}(?![\w-])", text):
                self.note(lineno, f'plain display name "{phrase}"; {self.name_reason[phrase]}')
                text = text.replace(phrase, "")

    def run(self, text):
        self.infer_dataset(text)
        out = []
        in_code = in_front_matter = False
        section = None
        for lineno, line in enumerate(text.splitlines(keepends=True), 1):
            body = line.rstrip("\n")
            if lineno == 1 and body == "---":
                in_front_matter = True
            elif in_front_matter:
                in_front_matter = body != "---"
            elif body.lstrip().startswith("```"):
                in_code = not in_code
            elif not in_code and body.startswith("#"):
                # A trailing comment such as <!--SkipTOC--> is not part of the section name
                section = re.sub(r"\s*<!--.*?-->", "", body.lstrip("#")).strip()
            elif not in_code and body.lstrip().startswith("<"):
                self.html_links += body.count("](#")  # raw HTML is left alone
            elif not in_code and body.lstrip().startswith("|") and section != "Content Constraints":
                if "](#" in body or re.search(r"(?<![*\w])\*[^*\s][^*]*\*(?![*\w])", body):
                    self.table_rows_skipped += 1
            elif not in_code and section not in DEFINITION_SECTIONS and body.strip():
                new = self.convert_line(body, lineno)
                line = new + line[len(body):]
            out.append(line)
        return "".join(out)


def set_front_matter(text, dataset=None, semantic=None):
    """Return text with "dataset:" and "semantic:" set in its front matter, keeping other keys."""
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    lines = match.group(1).splitlines() if match else []
    body = text[match.end():] if match else "\n" + text
    kept, skipping = [], False
    for line in lines:
        key = line.partition(":")[0].strip()
        if not line.startswith((" ", "\t")):
            skipping = (key == "semantic" and semantic is not None) or (key == "dataset" and dataset is not None)
        if not skipping:
            kept.append(line)
    if dataset is not None:
        kept.append(f"dataset: {dataset}")
    if semantic:
        kept.append("semantic:")
        kept.extend(f"  {kind}: {semantic[kind]}" for kind in TYPES if kind in semantic)
    return "---\n" + "\n".join(kept) + "\n---\n" + body if kept else body.lstrip("\n")


def convert(registry, rel, original, kinds):
    """Convert one file; return (tagger, converted text without front matter changes)."""
    front, _ = split_front_matter(original)
    tagger = Tagger(registry, rel, front.get("dataset") or None, kinds)
    return tagger, tagger.run(original)


def check(registry, rel, original):
    """Report what rerunning the converter would change for the kinds a file lists as mechanical."""
    front, _ = split_front_matter(original)
    status, _ = conversion_status(front)
    kinds = [k for k, v in status.items() if v == "mechanical"]
    if not kinds:
        return 0
    tagger, converted = convert(registry, rel, original, kinds)
    problems = 0
    if tagger.inferred and tagger.used_default and "dataset" not in front:
        print(f"{rel}:1: ERROR FOCUS021 the converter would add \"dataset: {tagger.inferred}\"", file=sys.stderr)
        problems += 1
    for lineno, (old, new) in enumerate(zip(original.splitlines(), converted.splitlines()), 1):
        if old != new:
            print(f"{rel}:{lineno}: ERROR FOCUS021 {', '.join(kinds)} listed as mechanical, but the converter "
                  f"would write: {new.strip()}", file=sys.stderr)
            problems += 1
    return problems


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--registry", type=Path, required=True)
    parser.add_argument("--spec-dir", type=Path, default=Path("."))
    parser.add_argument("--kinds", default=",".join(TYPES),
                        help=f"comma-separated tag kinds to convert (default: all: {','.join(TYPES)})")
    parser.add_argument("--check", action="store_true",
                        help="change nothing; fail when rerunning the converter would change a file "
                             "for a kind it lists as mechanical")
    args = parser.parse_args()

    kinds = [k.strip() for k in args.kinds.split(",") if k.strip()]
    unknown = [k for k in kinds if k not in TYPES]
    if unknown:
        parser.error(f"unknown kind(s) {', '.join(unknown)}; kinds: {', '.join(TYPES)}")
    registry = Registry(json.loads(args.registry.read_text(encoding="utf-8")))
    spec_dir = args.spec_dir.resolve()
    problems = 0
    for file in args.files:
        rel = str(file.resolve().relative_to(spec_dir))
        original = file.read_text(encoding="utf-8")
        if args.check:
            problems += check(registry, rel, original)
            continue
        front, _ = split_front_matter(original)
        tagger, converted = convert(registry, rel, original, kinds)
        dataset = None
        if tagger.inferred and tagger.used_default and "dataset" not in front:
            dataset = tagger.inferred
            print(f"{rel}: dataset: {tagger.inferred} inferred")
        status, _ = conversion_status(front)
        status.update({k: "mechanical" for k in kinds if status.get(k) != "reviewed"})
        converted = set_front_matter(converted, dataset=dataset, semantic=status)
        if converted != original:
            file.write_text(converted, encoding="utf-8")
        skipped = f", {tagger.table_rows_skipped} table row(s) left as is" if tagger.table_rows_skipped else ""
        print(f"{rel}: {tagger.changes} reference(s) tagged, {len(tagger.review)} to review{skipped}")
        for item in tagger.review:
            print(f"  {item}")
    if args.check:
        print(f"Conversion status: {problems} problem(s)", file=sys.stderr)
        if problems:
            sys.exit(1)


if __name__ == "__main__":
    main()
