#!/usr/bin/env python3
"""Pandoc filter that resolves FOCUS semantic references and lints their use.

Semantic references are ordinary Markdown links whose target names an entity
type (and optionally an ID) instead of a location:

    [ResourceType](#col)                 column, ID taken from the link text
    [resource type](#col:ResourceType)   column, explicit ID, any display text
    [BilledCost](#col:InvoiceDetail.BilledCost)   column in a specific dataset
    ["Usage"](#val:ChargeCategory)       allowed value of a column
    [Cost and Usage](#ds)                dataset
    [NumericFormat](#attr)               attribute
    [Includes Tags](#omc)                operating model condition
    [ContractAppliedObject](#obj)        JSON object (or value) a column defines
    [ContractAppliedObjectSchema](#schema)   JSON schema
    [FocusVersion](#meta)                metadata field or collection
    [DatasetInstanceId](#meta:Recency.DatasetInstanceId)   metadata field in a specific collection
    [charges](#term)                     glossary term (plurals resolve)
    [covered](#term:covered-charge)      glossary term, explicit key

Rendering rules:

* The first reference to an entity in each source file becomes a link. Later
  references render without a link.
* References inside tables always link, except glossary terms (Content
  Constraints and similar tables are lookup aids, so each cell stands alone).
* References to the entity the current file defines never link.
* Glossary terms render in italics. Other entities render as plain text.

File boundaries come from `<!-- focus:file <path> -->` markers (markdown-pp
would emit one per !INCLUDE), or from the `focus-file` metadata value.

Metadata options (pass with -M):

* focus-registry=PATH       registry JSON from build_registry.py (default: build/registry.json)
* focus-file=PATH           source path for single-file runs
* focus-link-mode=anchor    link to assembled-spec anchors (default)
* focus-link-mode=source    link to the defining .md file (GitHub-style previews)
* focus-annotate=true       wrap references in <span class="focus-col" ...> for CSS
* focus-lint-terms=true     also report plain (non-italic) text matching glossary terms
* focus-strict=true         exit non-zero when any error is reported

Diagnostics go to stderr as: <file> § <section>: <LEVEL> <code> <message>
"""

import json
import os
import re
import sys
from pathlib import Path

import panflute as pf

HERE = Path(__file__).resolve().parent
TYPES = ("col", "val", "ds", "attr", "omc", "obj", "schema", "meta", "term")
MARKER = re.compile(r"<!--\s*focus:file\s+(\S+)\s*-->")


def slug(text):
    return re.sub(r"\s+", "-", text.strip().lower())


def singular_forms(key):
    """Candidate singular keys for a slugged glossary phrase."""
    head, _, last = key.rpartition("-")
    prefix = f"{head}-" if head else ""
    forms = []
    if last.endswith("ies"):
        forms.append(prefix + last[:-3] + "y")
    if last.endswith("es"):
        forms.append(prefix + last[:-2])
    if last.endswith("s"):
        forms.append(prefix + last[:-1])
    return forms


def words_to_inlines(text):
    out = []
    for i, word in enumerate(text.split(" ")):
        if i:
            out.append(pf.Space())
        if word:
            out.append(pf.Str(word))
    return out


def inside(elem, *types):
    parent = elem.parent
    while parent is not None:
        if isinstance(parent, types):
            return True
        parent = parent.parent
    return False


class Registry:
    def __init__(self, entries):
        self.entries = entries
        self.by_type = {t: [e for e in entries if e["type"] == t] for t in TYPES}
        self.anchors = {e["anchor"]: e for e in entries if e["type"] != "val"}
        self.col_ids = {e["id"] for e in self.by_type["col"]}
        self.term_keys = {e["id"].lower(): e for e in self.by_type["term"]}
        self.display_phrases = sorted(
            {name for t in ("col", "attr", "omc", "obj", "schema", "meta") for e in self.by_type[t]
             for name in [e["display"], *e.get("aliases", [])] if " " in name},
            key=len, reverse=True)

    @staticmethod
    def names(e):
        return {e["display"].lower(), *(a.lower() for a in e.get("aliases", []))}

    def collection_of(self, path):
        """The metadata collection a file's own definition sits in (None at the top level)."""
        return next((e.get("collection") for e in self.by_type["meta"] if e["source"] == path), None)

    def find(self, kind, ident, text, dataset, collection=None):
        """Return (entity, error) for a reference."""
        if kind == "term":
            key = (ident or slug(text)).lower()
            for candidate in [key] + ([] if ident else singular_forms(key)):
                if candidate in self.term_keys:
                    return self.term_keys[candidate], None
            if not ident:
                for candidate in [text.lower()] + [k.replace("-", " ") for k in singular_forms(slug(text))]:
                    for e in self.by_type["term"]:
                        if candidate in self.names(e):
                            return e, None
            return None, f'unknown glossary term "{ident or text}"'

        if kind == "val":
            if not ident:
                return None, f'value reference "{text}" needs a column, e.g. (#val:ChargeCategory)'
            value = text.strip().strip('"')
            ds, _, col = ident.rpartition(".")
            matches = [e for e in self.by_type["val"]
                       if e["column"] == col and e["value"] == value and (not ds or e["dataset"] == ds)]
            if not matches:
                known = sorted({e["value"] for e in self.by_type["val"] if e["column"] == col})
                hint = f" (allowed: {', '.join(known)})" if known else " (column has no allowed values)"
                return None, f'"{value}" is not an allowed value of {col}{hint}'
            return self._pick(matches, dataset, f"{col} value"), None

        if kind == "meta":
            return self._find_meta(ident, text, collection)

        ds, _, ident_tail = (ident or "").rpartition(".") if kind == "col" else ("", "", ident)
        wanted = (ident_tail or re.sub(r"\s+", "", text)).lower()
        # An explicit ID decides the entity; the link text is then only what readers see
        matches = [e for e in self.by_type[kind]
                   if e["id"].lower() == wanted or (not ident_tail and text.lower() in self.names(e))]
        if ds:
            matches = [e for e in matches if e.get("dataset") == ds]
        elif kind == "col" and dataset and matches:
            # A file with a dataset (its location or its front matter) resolves unqualified
            # columns there only, so a column added to another dataset later cannot change it
            local = [e for e in matches if e.get("dataset") == dataset]
            if not local:
                other = matches[0]
                return None, (f'col "{other["id"]}" is not in the {dataset} dataset; '
                              f'qualify it, e.g. (#col:{other["dataset"]}.{other["id"]})')
            matches = local
        if not matches:
            return None, f'unknown {kind} "{ident or text}"'
        picked = self._pick(matches, dataset, f"{kind} {matches[0]['id']}")
        if picked is None:
            sets = ", ".join(sorted(e.get("dataset", "?") for e in matches))
            return None, (f'{kind} "{matches[0]["id"]}" exists in several datasets ({sets}); '
                          f'qualify it, e.g. (#col:{matches[0].get("dataset")}.{matches[0]["id"]})')
        return picked, None

    def _find_meta(self, ident, text, collection):
        """Metadata IDs repeat across collections (e.g., DatasetInstanceId). An unqualified
        reference resolves in the file's own collection, or at the top level outside one."""
        scope, _, ident_tail = (ident or "").rpartition(".")
        wanted = (ident_tail or re.sub(r"\s+", "", text)).lower()
        matches = [e for e in self.by_type["meta"]
                   if e["id"].lower() == wanted or (not ident_tail and text.lower() in self.names(e))]
        if scope:
            matches = [e for e in matches if e.get("collection") == scope]
        elif (ident or "").startswith("."):
            matches = [e for e in matches if not e.get("collection")]  # ".DataGenerator": top level
        if not matches:
            return None, f'unknown meta "{ident or text}"'
        if len(matches) == 1:
            return matches[0], None
        local = [e for e in matches if e.get("collection") == collection]
        if len(local) == 1:
            return local[0], None
        sets = ", ".join(sorted(e.get("collection", "top level") for e in matches))
        example = next(e for e in matches if e.get("collection"))
        return None, (f'meta "{matches[0]["id"]}" exists in several collections ({sets}); '
                      f'qualify it, e.g. (#meta:{example["collection"]}.{example["id"]})')

    @staticmethod
    def _pick(matches, dataset, _label):
        if len(matches) == 1:
            return matches[0]
        local = [e for e in matches if e.get("dataset") == dataset]
        return local[0] if len(local) == 1 else None


class Resolver:
    def __init__(self, doc):
        meta = lambda key, default=None: doc.get_metadata(key, default)  # noqa: E731
        registry_path = Path(meta("focus-registry", str(HERE / "build" / "registry.json")))
        self.registry = Registry(json.loads(registry_path.read_text(encoding="utf-8")))
        self.link_mode = meta("focus-link-mode", "anchor")
        self.annotate = str(meta("focus-annotate", "false")).lower() == "true"
        self.lint_terms = str(meta("focus-lint-terms", "false")).lower() == "true"
        self.strict = str(meta("focus-strict", "false")).lower() == "true"
        self.errors = 0
        self.warnings = 0
        self.set_file(meta("focus-file", "<stdin>"))

    # -- state ---------------------------------------------------------------

    def set_file(self, path):
        self.file = path
        self.seen = set()
        self.sections = []
        self.dataset = next((e["dataset"] for e in self.registry.by_type["col"]
                             if e["source"] == path), None)
        if self.dataset is None:
            self.dataset = next((e["id"] for e in self.registry.by_type["ds"]
                                 if Path(e["source"]).parent in Path(path).parents), None)

    def enter_header(self, header):
        self.sections = [(lvl, t) for lvl, t in self.sections if lvl < header.level]
        self.sections.append((header.level, pf.stringify(header)))

    @property
    def section(self):
        return self.sections[-1][1] if self.sections else "(top)"

    @property
    def in_requirements(self):
        return any(t == "Requirements" for _, t in self.sections)

    def report(self, level, code, message):
        if level == "ERROR":
            self.errors += 1
        elif level == "WARN":
            self.warnings += 1
        print(f"{self.file} § {self.section}: {level} {code} {message}", file=sys.stderr)

    def is_home(self, entity):
        source = entity["source"].split("#")[0]
        # A JSON object shares its column's file but is its own entity, so it links like any other
        return entity["type"] not in ("term", "obj") and source == self.file

    # -- lint pass (runs on the unresolved block) ------------------------------

    def lint(self, elem, doc):
        if inside(elem, pf.Header, pf.Code, pf.CodeBlock):
            return
        if isinstance(elem, pf.Link) and elem.url.startswith("#"):
            target = elem.url[1:]
            if target in self.registry.anchors:
                e = self.registry.anchors[target]
                text = pf.stringify(elem)
                short, _ = self.registry.find(e["type"], None, text, self.dataset)
                ref = e["type"] if short is e else f'{e["type"]}:{e["id"]}'
                self.report("WARN", "FOCUS007",
                            f'hard-coded link "{text}" -> #{target}; write [{text}](#{ref})')
        elif isinstance(elem, pf.Str) and not inside(elem, pf.Link):
            word = elem.text.strip(".,;:()\"'*")
            if word in self.registry.col_ids:
                home = any(e["id"] == word and self.is_home(e) for e in self.registry.by_type["col"])
                if not home:
                    self.report("WARN", "FOCUS004", f"untagged ColumnId {word}; write [{word}](#col)")
        elif isinstance(elem, pf.Emph) and not inside(elem, pf.Link):
            text = pf.stringify(elem)
            entity, _ = self.registry.find("term", None, text, None)
            if entity:
                self.report("WARN", "FOCUS005",
                            f'italic "{text}" matches glossary term {entity["id"]}; write [{text}](#term)')
        elif isinstance(elem, (pf.Para, pf.Plain)):
            self.lint_phrases(elem)

    def lint_phrases(self, block):
        """Find untagged display-name phrases in a paragraph's plain text."""
        parts = []

        def collect(e, _doc):
            if isinstance(e, (pf.Link, pf.Code, pf.Emph)):
                parts.append("\0")
            elif isinstance(e, pf.Str) and not inside(e, pf.Link, pf.Code, pf.Emph):
                parts.append(e.text)
            elif isinstance(e, (pf.Space, pf.SoftBreak)) and not inside(e, pf.Link, pf.Code, pf.Emph):
                parts.append(" ")

        block.walk(collect)
        text = "".join(parts)
        homes = {name for e in self.registry.entries if self.is_home(e)
                 for name in [e["display"], *e.get("aliases", [])]}
        for phrase in self.registry.display_phrases:
            if phrase in homes:
                continue
            for _ in re.finditer(rf"(?<![\w-]){re.escape(phrase)}(?![\w-])", text):
                self.report("WARN", "FOCUS006", f'untagged display name "{phrase}"; tag it or reword')
            text = text.replace(phrase, "\0")
        if self.lint_terms:
            for key, e in self.registry.term_keys.items():
                phrase = e["display"].lower()
                if re.search(rf"(?<![\w-]){re.escape(phrase)}s?(?![\w-])", text.lower()):
                    self.report("INFO", "FOCUS009", f'plain text matches glossary term "{phrase}"; '
                                f'tag it if the term is meant')

    # -- resolve pass ----------------------------------------------------------

    def resolve(self, elem, doc):
        if not isinstance(elem, pf.Link) or not elem.url.startswith("#"):
            return None
        kind, _, ident = elem.url[1:].partition(":")
        if kind not in TYPES:
            return None

        text = pf.stringify(elem)
        entity, error = self.registry.find(kind, ident or None, text, self.dataset)
        if error:
            self.report("ERROR", "FOCUS008" if kind == "val" else "FOCUS001", error)
            return pf.Span(*words_to_inlines(text), classes=["focus-error"])

        if kind == "col" and self.in_requirements and text != entity["id"]:
            self.report("WARN", "FOCUS003",
                        f'display text "{text}" in Requirements; normative text uses {entity["id"]}')

        key = (entity["type"], entity["id"], entity.get("dataset"))
        table_cell = kind != "term" and inside(elem, pf.Table)
        link = not self.is_home(entity) and (table_cell or key not in self.seen)
        if kind != "val":
            self.seen.add(key)

        content = words_to_inlines(text)
        if kind == "term":
            content = [pf.Emph(*content)]
        if link:
            content = [pf.Link(*content, url=self.url_for(entity))]
        if self.annotate:
            return pf.Span(*content, classes=[f"focus-{kind}", "focus-first" if link else "focus-repeat"],
                           attributes={"data-focus-id": entity["id"]})
        return content

    def url_for(self, entity):
        if self.link_mode == "source":
            path, _, fragment = entity["source"].partition("#")
            rel = os.path.relpath(path, os.path.dirname(self.file) or ".")
            return rel + (f"#{fragment}" if fragment else "")
        return "#" + entity["anchor"]

    # -- driver ------------------------------------------------------------------

    def run(self, doc):
        kept = []
        for block in doc.content:
            if isinstance(block, pf.RawBlock) and block.format == "html":
                match = MARKER.search(block.text)
                if match:
                    if self.annotate and kept:
                        kept.append(pf.RawBlock('<hr class="focus-file-break">'))
                    self.set_file(match.group(1))
                    continue
            if isinstance(block, pf.Header):
                self.enter_header(block)
            block.walk(self.lint)
            kept.append(block.walk(self.resolve))
        doc.content = kept
        print(f"{self.errors} error(s), {self.warnings} warning(s)", file=sys.stderr)


def main():
    doc = pf.load()
    resolver = Resolver(doc)
    resolver.run(doc)
    pf.dump(doc)
    if resolver.strict and resolver.errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
