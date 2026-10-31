#!/usr/bin/env python3
"""Resolve FOCUS semantic references in assembled Markdown, producing plain Markdown.

This is the build-time counterpart of focus_semantic.py. It runs on the output
of markdown-pp (spec.semantic.md) and writes spec.md, so everything downstream
(pymarkdownlnt, Pandoc, wkhtmltopdf, the link tests, the published spec.md
artifact) sees ordinary Markdown in today's conventions.

Input requirements:

* File boundaries are marked by the lines markdown-pp's Include module emits:
  "<!-- focus:begin <path> -->" and "<!-- focus:end <path> -->". Paths are
  relative to the specification directory. The marker lines are removed.

Dataset scope: a file's dataset comes from its location (a column file, or any
file under datasets/<dataset>/) or, for other files, from "dataset:" in its
front matter. Unqualified column references in a file with a dataset resolve
in that dataset only. A file without one may leave a column unqualified only
when a single dataset defines it.

Metadata scope works the same way with collections: an unqualified metadata
reference resolves in the collection that holds the file's own definition, or
at the top level in any other file (e.g., [DatasetInstanceId](#meta) in
metadata/recency/ means the Recency field).

Rendering rules (the same as focus_semantic.py):

* The first reference to an entity in each source file becomes a link; later
  references render without one. A hand-written link to an entity's anchor also
  counts as its first mention, so mixed files never link an entity twice.
* References inside Content Constraints tables always link, except glossary
  terms.
* A hand-written link in any other table does not count as a first mention (the
  approach proposed for entity catalog tables in #2514 and #2765), so the
  Columns table in dataset.md does not turn the links in the requirements below
  it into repeats.
* In glossary.md, each entry is its own scope: the first reference in each
  entry links, because the Editorial Guidelines count first mentions per entry
  there.
* References to the entity a file defines never link. A JSON object defined in
  its column's file is a separate entity and links normally.
* Glossary terms render in italics; other entities render as plain text.
* Allowed values render as written, without a link.

Diagnostics go to stderr as "<source file>:<line>: <LEVEL> <code> <message>".
Errors (unknown entities, invalid values, ambiguous columns) make the exit
status non-zero unless --no-strict is given.

Usage:
    resolve_semantic.py --registry registry.json spec.semantic.md -o spec.md
"""

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_registry import split_front_matter  # noqa: E402
from focus_semantic import TYPES, Registry  # noqa: E402

MARKER = re.compile(r"^<!-- focus:(begin|end) (\S+) -->$")
TOC_ANCHOR = re.compile(r'^<a class="toc-anchor" name="[^"]*">&nbsp;</a>$')
SEMANTIC_LINK = re.compile(r"\[([^\]\n]+)\]\(#(" + "|".join(TYPES) + r")(?::([^)\s]*))?\)")
ANY_FRAGMENT_LINK = re.compile(r"\]\(#([^)\s]+)\)")
CODE_SPAN = re.compile(r"(`+[^`]*`+)")
HEADING = re.compile(r"^(#+)\s+(?:\d+(?:\.\d+)*\.\s+)?(.*?)\s*$")
HAND_LINK_TARGET = re.compile(r"\]\([^)]*\)")
HTML_TAG = re.compile(r"<[^>]+>")
BULLET = re.compile(r"^\s*[*-]\s")
WORDS = re.compile(r"[\w'-]+")
# A term at the start of a line, list item, table cell or sentence may be capitalized
SENTENCE_START = re.compile(r"(^\s*([*|>]\s*)*|[.:!?|]\s+)(\*\*)?$")
# Kinds whose tag text is an entity name (an ID or a Display Name), so its case is checked
NAMED = ("col", "ds", "attr", "omc", "obj", "schema", "meta")


def word_case(word):
    """U for an acronym (a trailing plural s is ignored, e.g., SKUs), T for a capital, l otherwise."""
    bare = re.sub(r"(?<=[A-Z])'?s$", "", word)
    if len(bare) > 1 and bare.isupper():
        return "U"
    return "T" if word[:1].isupper() else "l"


def term_case_agrees(text, display, at_start):
    """True when a glossary term is written lowercase (acronyms kept), as in the glossary,
    or lowercase with a capital first letter at the start of a sentence."""
    words, names = WORDS.findall(text), WORDS.findall(display)
    # Different wording (an explicit key, or "accrual basis" for Accrual-Based Accounting)
    # has no case to compare; plurals and possessives still compare word by word
    if len(words) != len(names) or any(not w.lower().startswith(n.lower()[:max(1, len(n) - 2)])
                                       for w, n in zip(words, names)):
        return True
    shape = [word_case(w) for w in words]
    prose = ["U" if word_case(n) == "U" else "l" for n in names]
    if shape in (prose, [word_case(n) for n in names]):
        return True
    return at_start and shape == ["T" if i == 0 and c == "l" else c for i, c in enumerate(prose)]


class Frame:
    """Per-source-file state."""

    def __init__(self, path, registry, spec_dir):
        self.path = path
        self.line = 0
        self.seen = set()
        self.declared = None
        self.collection = registry.collection_of(path)
        self.dataset = next((e["dataset"] for e in registry.by_type["col"] if e["source"] == path), None)
        if self.dataset is None:
            self.dataset = next((e["id"] for e in registry.by_type["ds"]
                                 if Path(e["source"]).parent in Path(path).parents), None)
        source = spec_dir / path
        if source.suffix == ".md" and source.exists():
            text = source.read_text(encoding="utf-8")
            front, body = split_front_matter(text)
            # Include drops the front matter and the blank lines after it; count them
            # so reported line numbers match the source file
            if front:
                stripped = text[:len(text) - len(body.lstrip("\n"))]
                self.line = stripped.count("\n")
            if self.dataset is None:
                self.declared = front.get("dataset") or None
                self.dataset = self.declared


class SemanticResolver:
    def __init__(self, registry, strict=True, spec_dir=Path(".")):
        self.registry = registry
        self.strict = strict
        self.spec_dir = spec_dir
        self.stack = [Frame("spec.mdpp", registry, spec_dir)]
        self.sections = []
        self.in_code = False
        self.line_text = ""
        self.prefix = ""
        self.in_heading = False
        self.column_forms = set()
        # Single-word ColumnIds (e.g., Tags) are also ordinary words, so only compound IDs count
        ids = sorted({e["id"] for e in registry.by_type["col"] if re.search(r"[a-z][A-Z]", e["id"])},
                     key=len, reverse=True)
        self.column_id = re.compile(r"(?<![\w.\[/#-])(" + "|".join(ids) + r")(?![\w\]])") if ids else None
        self.errors = 0
        self.warnings = 0
        self.resolved = 0

    @property
    def frame(self):
        return self.stack[-1]

    def report(self, level, code, message):
        if level == "ERROR":
            self.errors += 1
        else:
            self.warnings += 1
        print(f"{self.frame.path}:{self.frame.line}: {level} {code} {message}", file=sys.stderr)

    def is_home(self, entity):
        source = entity["source"].split("#")[0]
        # A JSON object shares its column's file but is its own entity, so it links like any other
        return entity["type"] not in ("term", "obj") and source == self.frame.path

    @staticmethod
    def key(entity):
        return (entity["type"], entity["id"], entity.get("dataset"))

    @property
    def in_constraints(self):
        return any(title == "Content Constraints" for _, title in self.sections)

    @property
    def in_requirements(self):
        return any(title == "Requirements" for _, title in self.sections)

    def resolve_link(self, match, in_table):
        text, kind, ident = match.group(1), match.group(2), match.group(3) or None
        raw = text.strip()
        # Emphasis around the whole text is dropped; a stray * (e.g., "Allocated*") is text
        wrapped = len(raw) > 2 and raw[0] == raw[-1] and raw[0] in "*_" and raw[1] != raw[0]
        plain = raw[1:-1].strip() if wrapped else raw
        if wrapped:
            self.report("ERROR", "FOCUS016", f'emphasis inside the tag "{raw}"; the build sets the style, '
                                             f'so write [{plain}](#{kind}{":" + ident if ident else ""})')
        if self.in_heading:
            self.report("ERROR", "FOCUS017", f'tag "{match.group(0)}" in a heading; write the heading as plain text')
        entity, error = self.registry.find(kind, ident, plain, self.frame.dataset, self.frame.collection)
        if error:
            self.report("ERROR", "FOCUS008" if kind == "val" else "FOCUS001", error)
            return plain
        self.resolved += 1
        if ident and kind in ("col", "attr", "omc", "obj", "schema", "meta") and "." not in plain:
            named, _ = self.registry.find(kind, None, plain, self.frame.dataset, self.frame.collection)
            if named is not None and named["id"] != entity["id"]:
                self.report("WARN", "FOCUS011", f'link text "{plain}" names {named["id"]}, '
                                                f'but the reference is {entity["id"]}')
        scope = entity.get("dataset") or entity.get("collection")
        if (kind in ("col", "obj", "schema", "meta") and self.in_requirements
                and plain not in (entity["id"], f'{scope}.{entity["id"]}')):
            self.report("WARN", "FOCUS003",
                        f'display text "{plain}" in Requirements; normative text uses {entity["id"]}')
        if kind == "val":
            self.check_value(plain, entity)
            return plain
        self.check_case(kind, ident, plain, entity, scope, self.prefix + match.string[:match.start()])
        self.check_redundant(kind, ident, plain, entity, scope)
        if kind == "col" and self.in_requirements:
            self.column_forms.add("ID" if plain in (entity["id"], f"{scope}.{entity['id']}") else "Display Name")

        key = self.key(entity)
        every_row = in_table and kind != "term" and self.in_constraints
        link = not self.is_home(entity) and (every_row or key not in self.frame.seen)
        self.frame.seen.add(key)
        content = f"*{plain}*" if kind == "term" else plain
        return f"[{content}](#{entity['anchor']})" if link else content

    def check_value(self, plain, entity):
        if not (len(plain) >= 2 and plain[0] == plain[-1] == '"'):
            self.report("ERROR", "FOCUS014", f'value {plain} has no double quotes; '
                                             f'write ["{entity["value"]}"](#val:{entity["column"]})')
        column = entity["column"]
        if entity["source"] == self.frame.path:
            return  # the column's own file names it in every sentence by implication
        display = next((c["display"] for c in self.registry.by_type["col"]
                        if c["id"] == column and c.get("dataset") == entity.get("dataset")), column)
        # The value tag's own target names the column, so leave value targets out
        text = re.sub(r"\]\(#val:[^)]*\)", "]", self.line_text)
        if column not in text and display.lower() not in text.lower():
            self.report("WARN", "FOCUS015", f'value "{entity["value"]}" of {column}, '
                                            f'but the line does not name {column}')

    def check_case(self, kind, ident, plain, entity, scope, before):
        if kind == "term":
            if not term_case_agrees(plain, entity["display"], SENTENCE_START.search(before) is not None):
                self.report("WARN", "FOCUS013",
                            f'glossary term text "{plain}" and its glossary entry "{entity["display"]}" disagree '
                            f'in case; prose writes a term in lowercase, as in the glossary, or with a '
                            f'capital at the start of a sentence')
            return
        names = self.names(entity, scope)
        # An explicit ID records that other text was meant (e.g., [resource type](#col:ResourceType)),
        # and an operating model condition used as a condition is written as its lowercase phrase (#2765)
        if plain in names or ident or (kind == "omc" and plain == plain.lower()):
            return
        same = next((n for n in names if n.lower() == plain.lower()), None)
        if same is None and re.sub(r"\s+", "", plain).lower() == entity["id"].lower():
            same = entity["id"]
        if same is not None:
            self.report("WARN", "FOCUS012", f'tag text "{plain}" and the {kind} name "{same}" differ only '
                                            f'in case; match the case, or give the ID to keep this text')

    @staticmethod
    def names(entity, scope):
        names = [entity["display"], entity["id"], *entity.get("aliases", [])]
        return names + [f"{scope}.{entity['id']}"] if scope else names

    def check_redundant(self, kind, ident, plain, entity, scope):
        if not ident or kind not in NAMED:
            return
        if "." not in ident:
            if plain in self.names(entity, scope):
                self.report("ERROR", "FOCUS018", f'explicit ID {ident} is the one the text "{plain}" already '
                                                 f'gives; write [{plain}](#{kind})')
        elif kind == "col" and "." not in plain:
            dataset = ident.split(".")[0]
            shared = [c for c in self.registry.by_type["col"] if c["id"] == entity["id"]]
            if dataset == self.frame.dataset:
                self.report("ERROR", "FOCUS018", f"qualifier {dataset} is this file's dataset; "
                                                 f"write (#col:{entity['id']})")
            elif self.frame.dataset is None and len(shared) == 1:
                self.report("ERROR", "FOCUS018", f"qualifier {dataset} is the only dataset with "
                                                 f"{entity['id']}; write (#col:{entity['id']})")

    def check_untagged(self, segment):
        if self.column_id is None:
            return
        text = HTML_TAG.sub("", HAND_LINK_TARGET.sub("]", SEMANTIC_LINK.sub("", segment)))
        for word in self.column_id.findall(text):
            self.report("ERROR", "FOCUS004", f"untagged ColumnId {word}; write [{word}](#col)")

    def note_legacy_links(self, segment, in_table=False):
        if in_table and not self.in_constraints:
            return
        for target in ANY_FRAGMENT_LINK.findall(segment):
            entity = self.registry.anchors.get(target)
            if entity:
                self.frame.seen.add(self.key(entity))

    def transform(self, line):
        stripped = line.rstrip("\n")
        if self.frame.path == "glossary.md" and stripped.startswith('<a name="glossary:'):
            self.frame.seen.clear()
        if stripped.lstrip().startswith("```"):
            self.in_code = not self.in_code
            return line
        if self.in_code:
            return line
        heading = HEADING.match(stripped)
        if heading:
            level = len(heading.group(1))
            self.sections = [(lvl, t) for lvl, t in self.sections if lvl < level]
            self.sections.append((level, heading.group(2)))
        self.line_text = stripped
        self.in_heading = bool(heading)
        self.column_forms = set()
        in_table = stripped.lstrip().startswith("|")
        # Headings, tables, HTML and the ID and name sections that define an entity hold IDs as written
        innermost = self.sections[-1][1] if self.sections else ""
        prose = not (heading or in_table or stripped.lstrip().startswith("<")
                     or re.search(r"( ID| Name)$", innermost))
        parts = CODE_SPAN.split(stripped)
        for i in range(0, len(parts), 2):
            if prose:
                self.check_untagged(parts[i])
            # Note hand-written links first so a semantic reference after them is not re-linked
            self.note_legacy_links(parts[i], in_table)
            self.prefix = "".join(parts[:i])
            parts[i] = SEMANTIC_LINK.sub(lambda m: self.resolve_link(m, in_table), parts[i])
        if len(self.column_forms) == 2 and BULLET.match(stripped):
            self.report("ERROR", "FOCUS019", "requirement mixes ColumnIds and Display Names; "
                                             "normative text uses ColumnIds")
        return "".join(parts) + ("\n" if line.endswith("\n") else "")

    def run(self, lines):
        out = []
        skip_blank = False
        for line in lines:
            # markdown-pp adds an anchor line and a blank line before each heading;
            # they are not in the source file, so they do not advance its line count
            if TOC_ANCHOR.match(line.rstrip("\n")):
                out.append(line)
                skip_blank = True
                continue
            if skip_blank and not line.strip():
                out.append(line)
                skip_blank = False
                continue
            skip_blank = False
            marker = MARKER.match(line.rstrip("\n"))
            if marker:
                if marker.group(1) == "begin":
                    self.stack.append(Frame(marker.group(2), self.registry, self.spec_dir))
                    declared = self.frame.declared
                    line, self.frame.line = self.frame.line, 2  # report on the dataset: line
                    if declared and declared not in {e["id"] for e in self.registry.by_type["ds"]}:
                        self.report("ERROR", "FOCUS010", f'front matter names unknown dataset "{declared}"')
                    self.frame.line = line
                else:
                    self.stack.pop()
                    self.frame.line += 1  # the !INCLUDE line in the parent
                continue
            self.frame.line += 1
            out.append(self.transform(line))
        return out


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("input", type=Path)
    parser.add_argument("-o", "--output", type=Path, required=True)
    parser.add_argument("--registry", type=Path, required=True)
    parser.add_argument("--spec-dir", type=Path, default=Path("."),
                        help="directory the include paths are relative to (default: current directory)")
    parser.add_argument("--no-strict", action="store_true")
    args = parser.parse_args()

    registry = Registry(json.loads(args.registry.read_text(encoding="utf-8")))
    resolver = SemanticResolver(registry, strict=not args.no_strict, spec_dir=args.spec_dir)
    lines = args.input.read_text(encoding="utf-8").splitlines(keepends=True)
    args.output.write_text("".join(resolver.run(lines)), encoding="utf-8")
    print(f"Semantic references: {resolver.resolved} resolved, {resolver.errors} error(s), "
          f"{resolver.warnings} warning(s)", file=sys.stderr)
    if resolver.errors and resolver.strict:
        sys.exit(1)


if __name__ == "__main__":
    main()
