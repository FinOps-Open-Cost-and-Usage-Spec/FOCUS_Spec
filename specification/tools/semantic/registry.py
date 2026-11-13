"""Entity registry lookups shared by the FOCUS semantic tag tools.

A semantic tag is an ordinary Markdown link whose target names an entity kind
(and optionally an ID) instead of a location:

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

The registry itself is built by build_registry.py. This module only reads it.
"""

import re

TYPES = ("col", "val", "ds", "attr", "omc", "obj", "schema", "meta", "term")


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
