#!/usr/bin/env python3
"""Rewrite specification source files to use semantic references.

This is the mechanical part of a migration (step 2). It edits files in place
and prints what it could not decide, which is left for a person:

* Hand-written links to an entity's anchor become semantic references, in the
  shortest form that resolves to the same entity:
  [*charge*](#glossary:charge) -> [charge](#term)
* Dataset-qualified column references lose a qualifier the file's dataset makes
  unnecessary: [BilledCost](#col:CostAndUsage.BilledCost) -> [BilledCost](#col)
* Italic phrases that name a glossary term become term references:
  *charges* -> [charges](#term)
* ColumnIds, attribute IDs, and operating model condition IDs written as plain
  words become references, including the file's own entity:
  BilledCost -> [BilledCost](#col)
* In a column file, quoted allowed values of that column become value
  references: "Correction" -> ["Correction"](#val:ChargeClass)

Left alone, and reported as NEEDS-REVIEW where relevant:

* Headings, code spans and blocks, existing link text, and the ID and name
  sections that define the entity (Column ID, Display Name, and so on).
* Display Names written as plain words (e.g., "Billed Cost" in prose), because
  plain prose may or may not mean the entity.
* ColumnIds that exist in several datasets when the file has no dataset, from
  its location or from "dataset:" in its front matter.
* ColumnIds that are not in the file's dataset; they need a qualifier.

Usage:
    tag_sources.py --registry semantic-registry.json [--spec-dir DIR] FILE...
"""

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_registry import split_front_matter  # noqa: E402
from focus_semantic import Registry  # noqa: E402

LINK = re.compile(r"\[([^\]\n]+)\]\(([^)\s]+)\)")
CODE_SPAN = re.compile(r"(`+[^`]*`+)")
ITALIC = re.compile(r"(?<![*\w])\*(?![\s*])([^*\n]+?)(?<![\s*])\*(?![*\w])")
QUOTED = re.compile(r'(?<![\[\w])"([^"\n]+)"(?!\]\()')
DEFINITION_SECTIONS = {"Column ID", "Display Name", "Attribute ID", "Attribute Name",
                       "Operating Model Condition ID", "Dataset ID"}


class Tagger:
    def __init__(self, registry, path, declared=None):
        self.registry = registry
        self.path = path
        cols = registry.by_type["col"]
        self.home_col = next((e for e in cols if e["source"] == path), None)
        self.dataset = self.home_col["dataset"] if self.home_col else next(
            (e["id"] for e in registry.by_type["ds"] if Path(e["source"]).parent in Path(path).parents), declared)
        # PascalCase IDs that may appear as plain words: columns, attributes, conditions
        self.id_kind = {e["id"]: e["type"] for t in ("attr", "omc") for e in registry.by_type[t]}
        self.id_kind.update({i: "col" for i in registry.col_ids})
        ids = sorted(self.id_kind, key=len, reverse=True)
        datasets = "|".join(sorted((e["id"] for e in registry.by_type["ds"]), key=len, reverse=True))
        # An optional dataset qualifier, e.g. CostAndUsage.BilledCost, is kept as written
        self.id_word = re.compile(r"(?<![\w\[#.`/])((?:(?:" + datasets + r")\.)?(?:" + "|".join(ids) + r"))(?![\w\]`(])")
        self.home_values = ({e["value"] for e in registry.by_type["val"]
                             if e["column"] == self.home_col["id"] and e["dataset"] == self.dataset}
                            if self.home_col else set())
        self.changes = 0
        self.review = []

    def note(self, lineno, message):
        self.review.append(f"{self.path}:{lineno}: NEEDS-REVIEW {message}")

    def reference(self, kind, entity, text):
        """Shortest semantic link for an entity, given the visible text."""
        found, _ = self.registry.find(kind, None, text, self.dataset)
        if found is entity:
            return f"[{text}](#{kind})"
        ident = entity["id"]
        if kind == "col":
            qualified, _ = self.registry.find(kind, ident, text, self.dataset)
            if qualified is not entity:
                ident = f'{entity["dataset"]}.{ident}'
        return f"[{text}](#{kind}:{ident})"

    def convert_link(self, match):
        text, target = match.group(1), match.group(2)
        if not target.startswith("#"):
            return match.group(0)
        if target.startswith("#col:"):
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
        if entity is None:
            return match.group(0)
        self.changes += 1
        plain = text.strip().strip("*_").strip()
        return self.reference(entity["type"], entity, plain)

    def convert_italic(self, match):
        phrase = match.group(1)
        entity, _ = self.registry.find("term", None, phrase, None)
        if entity is None:
            return match.group(0)
        self.changes += 1
        return self.reference("term", entity, phrase)

    def convert_id(self, match, lineno):
        word = match.group(1)
        qualifier, _, bare = word.rpartition(".")
        kind = self.id_kind[bare]
        if qualifier and kind != "col":
            return word
        entity, error = self.registry.find(kind, word, bare, self.dataset)
        if entity is None:
            self.note(lineno, f"{word}: {error}")
            return word
        self.changes += 1
        if qualifier:
            return f"[{word}](#col:{word})"
        return self.reference(kind, entity, word)

    def convert_value(self, match):
        value = match.group(1)
        if value not in self.home_values:
            return match.group(0)
        self.changes += 1
        return f'["{value}"](#val:{self.home_col["id"]})'

    def convert_text(self, text, lineno):
        """Convert plain text that holds no links or code."""
        text = ITALIC.sub(self.convert_italic, text)
        # Italic conversion produced links; only touch what is still outside links
        pieces = LINK.split(text)
        out = []
        for i in range(0, len(pieces), 3):
            chunk = self.id_word.sub(lambda m: self.convert_id(m, lineno), pieces[i])
            if self.home_values:
                chunk = QUOTED.sub(self.convert_value, chunk)
            out.append(chunk)
            if i + 2 < len(pieces):
                out.append(f"[{pieces[i + 1]}]({pieces[i + 2]})")
        return "".join(out)

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
            parts[i] = "".join(segments)
        return "".join(parts)

    def report_display_names(self, line, lineno):
        text = LINK.sub("", CODE_SPAN.sub("", line))
        for phrase in self.registry.display_phrases:
            if re.search(rf"(?<![\w-]){re.escape(phrase)}(?![\w-])", text):
                self.note(lineno, f'plain display name "{phrase}"; tag it if it means the entity')
                text = text.replace(phrase, "")

    def run(self, text):
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
                section = body.lstrip("#").strip()
            elif not in_code and section not in DEFINITION_SECTIONS and body.strip():
                new = self.convert_line(body, lineno)
                self.report_display_names(new, lineno)
                line = new + line[len(body):]
            out.append(line)
        return "".join(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--registry", type=Path, required=True)
    parser.add_argument("--spec-dir", type=Path, default=Path("."))
    args = parser.parse_args()

    registry = Registry(json.loads(args.registry.read_text(encoding="utf-8")))
    spec_dir = args.spec_dir.resolve()
    for file in args.files:
        rel = str(file.resolve().relative_to(spec_dir))
        original = file.read_text(encoding="utf-8")
        front, _ = split_front_matter(original)
        tagger = Tagger(registry, rel, front.get("dataset") or None)
        converted = tagger.run(original)
        if converted != original:
            file.write_text(converted, encoding="utf-8")
        print(f"{rel}: {tagger.changes} reference(s) tagged, {len(tagger.review)} to review")
        for item in tagger.review:
            print(f"  {item}")


if __name__ == "__main__":
    main()
