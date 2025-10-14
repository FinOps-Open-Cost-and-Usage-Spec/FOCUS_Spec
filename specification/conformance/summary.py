#!/usr/bin/env python3
"""
Generate a Markdown summary grouped by Reference, listing "EntityId – MustSatisfy" lines.

Ordering per Reference:
  1) The -000- entry first
  2) Then EntityType: Dataset items, ordered by numeric ID
  3) Then everything else (e.g., Column), ordered by numeric ID

Other behavior:
  - References are sorted alphabetically (case-insensitive)
  - Deduplicates by (EntityId, EntityType) within each Reference (keeps first seen)
  - EntityId source priority:
      1) Rule's 'EntityId' field (if present)
      2) The numeric segment from ConformanceRuleId (e.g., '...-003-...')
      3) A '-123-' pattern found in MustSatisfy text
      4) "?" as a fallback (sorted last)
  - EntityType source priority:
      1) Rule's 'EntityType' field (if present)
      2) Infer from ConformanceRuleId: '-D-' => 'Dataset', '-C-' => 'Column'
      3) 'Other'

Usage:
  python build_reference_entity_musts_ordered.py /path/to/cr-1.2.json /path/to/out.md

Defaults (if no args):
  input:  ./cr-1.2.json
  output: ./conformance_reference_entity_musts_ordered.md
"""

import sys
import json
import re
from pathlib import Path
from collections import defaultdict, OrderedDict


def infer_entity_type(cr_key: str, explicit: str | None) -> str:
    if explicit and isinstance(explicit, str) and explicit.strip():
        return explicit.strip()
    if isinstance(cr_key, str):
        if re.search(r'-D-', cr_key):
            return "Dataset"
        if re.search(r'-C-', cr_key):
            return "Column"
    return "Other"


def extract_entity_from_ids(cr_key: str, explicit_eid: str | None, must_text: str | None):
    """
    Return (display_eid, num).
    Prefer explicit_eid; else derive from ConformanceRuleId; else from MustSatisfy; else ('?', big).
    """
    if explicit_eid and isinstance(explicit_eid, str) and explicit_eid.strip():
        s = explicit_eid.strip()
        m = re.search(r'(\d+)', s)
        return s, (int(m.group(1)) if m else 10**12)

    if isinstance(cr_key, str):
        m = re.search(r'-(\d+)(?:-|$)', cr_key)
        if m:
            num = int(m.group(1))
            return f"-{m.group(1)}-", num

    if isinstance(must_text, str):
        m = re.search(r'-(\d+)(?:-|$)', must_text)
        if m:
            num = int(m.group(1))
            return f"-{m.group(1)}-", num

    return "?", 10**12


def collect(spec: dict):
    rules = spec.get("ConformanceRules", {}) or {}
    by_ref = defaultdict(list)  # ref -> list of dicts with eid, num, etype, must

    for cr_key, cr in rules.items():
        ref = cr.get("Reference")
        vc = cr.get("ValidationCriteria") or {}
        must = vc.get("MustSatisfy")
        if not (isinstance(ref, str) and ref.strip() and isinstance(must, str) and must.strip()):
            continue

        eid, num = extract_entity_from_ids(cr_key, cr.get("EntityId"), must)
        etype = infer_entity_type(cr_key, cr.get("EntityType"))
        by_ref[ref.strip()].append({"crid": cr_key, "eid": eid, "num": num, "etype": etype, "must": must.strip()})

    # Deduplicate by (eid, etype) within a reference (keep first occurrence)
    deduped = {}
    for ref, items in by_ref.items():
        seen = set()
        out = []
        for it in items:
            key = (it["eid"], it["etype"])
            if key in seen:
                continue
            seen.add(key)
            out.append(it)
        deduped[ref] = out

    # Order within each reference
    def group_priority(it):
        if it["eid"] == "-000-" or it["num"] == 0:
            return 0
        return 1 if it["etype"] == "Dataset" else 2

    ordered = OrderedDict()
    for ref, items in sorted(deduped.items(), key=lambda kv: kv[0].lower()):
        items_sorted = sorted(items, key=lambda it: (group_priority(it), it["num"], it["eid"].lower()))
        ordered[ref] = items_sorted
    return ordered


def build_markdown(grouped):
    lines = []
    for ref, items in grouped.items():
        lines.append(f"# {ref}")
        lines.append("")
        for it in items:
            lines.append(f'{it["crid"]} – {it["must"]}')
        lines.append("")
    return ("\n".join(lines)).rstrip() + "\n"


def main(in_path: Path, out_path: Path) -> None:
    spec = json.loads(in_path.read_text(encoding="utf-8"))
    grouped = collect(spec)
    print(grouped)
    md = build_markdown(grouped)
    out_path.write_text(md, encoding="utf-8")


if __name__ == "__main__":
    in_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("build/cr-1.2.json")
    out_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("conformance_reference_entity_musts_ordered.md")
    main(in_path, out_path)
