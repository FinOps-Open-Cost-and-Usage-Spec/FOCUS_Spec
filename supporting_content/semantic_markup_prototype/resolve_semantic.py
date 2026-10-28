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

Rendering rules (the same as focus_semantic.py):

* The first reference to an entity in each source file becomes a link; later
  references render without one. A hand-written link to an entity's anchor also
  counts as its first mention, so mixed files never link an entity twice.
* References inside table rows always link, except glossary terms.
* References to the entity a file defines never link.
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
from focus_semantic import TYPES, Registry  # noqa: E402

MARKER = re.compile(r"^<!-- focus:(begin|end) (\S+) -->$")
SEMANTIC_LINK = re.compile(r"\[([^\]\n]+)\]\(#(" + "|".join(TYPES) + r")(?::([^)\s]*))?\)")
ANY_FRAGMENT_LINK = re.compile(r"\]\(#([^)\s]+)\)")
CODE_SPAN = re.compile(r"(`+[^`]*`+)")
HEADING = re.compile(r"^(#+)\s+(?:\d+(?:\.\d+)*\.\s+)?(.*?)\s*$")


class Frame:
    """Per-source-file state."""

    def __init__(self, path, registry):
        self.path = path
        self.line = 0
        self.seen = set()
        self.dataset = next((e["dataset"] for e in registry.by_type["col"] if e["source"] == path), None)
        if self.dataset is None:
            self.dataset = next((e["id"] for e in registry.by_type["ds"]
                                 if Path(e["source"]).parent in Path(path).parents), None)


class SemanticResolver:
    def __init__(self, registry, strict=True):
        self.registry = registry
        self.strict = strict
        self.stack = [Frame("spec.mdpp", registry)]
        self.sections = []
        self.in_code = False
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
        return entity["type"] != "term" and source == self.frame.path

    @staticmethod
    def key(entity):
        return (entity["type"], entity["id"], entity.get("dataset"))

    @property
    def in_requirements(self):
        return any(title == "Requirements" for _, title in self.sections)

    def resolve_link(self, match, in_table):
        text, kind, ident = match.group(1), match.group(2), match.group(3) or None
        plain = text.strip().strip("*_").strip()
        entity, error = self.registry.find(kind, ident, plain, self.frame.dataset)
        if error:
            self.report("ERROR", "FOCUS008" if kind == "val" else "FOCUS001", error)
            return plain
        self.resolved += 1
        qualified_id = f'{entity.get("dataset")}.{entity["id"]}'
        if kind == "col" and self.in_requirements and plain not in (entity["id"], qualified_id):
            self.report("WARN", "FOCUS003",
                        f'display text "{plain}" in Requirements; normative text uses {entity["id"]}')
        if kind == "val":
            return plain

        key = self.key(entity)
        link = not self.is_home(entity) and ((in_table and kind != "term") or key not in self.frame.seen)
        self.frame.seen.add(key)
        content = f"*{plain}*" if kind == "term" else plain
        return f"[{content}](#{entity['anchor']})" if link else content

    def note_legacy_links(self, segment):
        for target in ANY_FRAGMENT_LINK.findall(segment):
            entity = self.registry.anchors.get(target)
            if entity:
                self.frame.seen.add(self.key(entity))

    def transform(self, line):
        stripped = line.rstrip("\n")
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
        in_table = stripped.lstrip().startswith("|")
        parts = CODE_SPAN.split(stripped)
        for i in range(0, len(parts), 2):
            # Note hand-written links first so a semantic reference after them is not re-linked
            self.note_legacy_links(parts[i])
            parts[i] = SEMANTIC_LINK.sub(lambda m: self.resolve_link(m, in_table), parts[i])
        return "".join(parts) + ("\n" if line.endswith("\n") else "")

    def run(self, lines):
        out = []
        for line in lines:
            marker = MARKER.match(line.rstrip("\n"))
            if marker:
                if marker.group(1) == "begin":
                    self.stack.append(Frame(marker.group(2), self.registry))
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
    parser.add_argument("--no-strict", action="store_true")
    args = parser.parse_args()

    registry = Registry(json.loads(args.registry.read_text(encoding="utf-8")))
    resolver = SemanticResolver(registry, strict=not args.no_strict)
    lines = args.input.read_text(encoding="utf-8").splitlines(keepends=True)
    args.output.write_text("".join(resolver.run(lines)), encoding="utf-8")
    print(f"Semantic references: {resolver.resolved} resolved, {resolver.errors} error(s), "
          f"{resolver.warnings} warning(s)", file=sys.stderr)
    if resolver.errors and resolver.strict:
        sys.exit(1)


if __name__ == "__main__":
    main()
