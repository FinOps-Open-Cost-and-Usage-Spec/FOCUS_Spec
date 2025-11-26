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
      2) The numeric segment from ModelRuleId (e.g., '...-003-...')
      3) A '-123-' pattern found in MustSatisfy text
      4) "?" as a fallback (sorted last)
  - EntityType source priority:
      1) Rule's 'EntityType' field (if present)
      2) Infer from ModelRuleId: '-D-' => 'Dataset', '-C-' => 'Column'
      3) 'Other'

Usage:
  python output_normative_text_from_model.py /path/to/model-1.2.json --filename /path/to/out.md
  python output_normative_text_from_model.py /path/to/model-1.2.json --reference "BilledCost"
  python output_normative_text_from_model.py --reference "BilledCost" --exclude-rmids

Defaults (if no args):
  input:  ./build/model-1.2.json
  output: console (unless --filename specified)
"""

import sys
import json
import re
import argparse
from pathlib import Path
from collections import defaultdict, OrderedDict


def infer_entity_type(model_key: str, explicit: str | None) -> str:
    if explicit and isinstance(explicit, str) and explicit.strip():
        return explicit.strip()
    if isinstance(model_key, str):
        if re.search(r'-D-', model_key):
            return "Dataset"
        if re.search(r'-C-', model_key):
            return "Column"
    return "Other"


def extract_entity_from_ids(model_key: str, explicit_eid: str | None, must_text: str | None):
    """
    Return (display_eid, num).
    Prefer explicit_eid; else derive from ModelRuleId; else from MustSatisfy; else ('?', big).
    """
    if explicit_eid and isinstance(explicit_eid, str) and explicit_eid.strip():
        s = explicit_eid.strip()
        m = re.search(r'(\d+)', s)
        return s, (int(m.group(1)) if m else 10**12)

    if isinstance(model_key, str):
        m = re.search(r'-(\d+)(?:-|$)', model_key)
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
    rules = spec.get("ModelRules", {}) or {}
    by_ref = defaultdict(list)  # ref -> list of dicts with eid, num, etype, must

    for model_key, model in rules.items():
        # Skip deprecated entities
        status = model.get("Status", "").strip()
        if status == "Deprecated":
            continue
            
        ref = model.get("Reference")
        vc = model.get("ValidationCriteria") or {}
        must = vc.get("MustSatisfy")
        if not (isinstance(ref, str) and ref.strip() and isinstance(must, str) and must.strip()):
            continue

        eid, num = extract_entity_from_ids(model_key, model.get("EntityId"), must)
        etype = infer_entity_type(model_key, model.get("EntityType"))
        order = model.get("Order")  # Extract Order field
        by_ref[ref.strip()].append({"ruleid": model_key, "eid": eid, "num": num, "etype": etype, "must": must.strip(), "order": order})

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

    def sort_key(it):
        # If Order field exists and is a number, use it as primary sort key
        if it.get("order") is not None and isinstance(it["order"], (int, float)):
            return (it["order"], group_priority(it), it["num"], it["eid"].lower())
        # Otherwise use the original sorting logic
        return (float('inf'), group_priority(it), it["num"], it["eid"].lower())

    ordered = OrderedDict()
    for ref, items in sorted(deduped.items(), key=lambda kv: kv[0].lower()):
        items_sorted = sorted(items, key=sort_key)
        ordered[ref] = items_sorted
    return ordered


def build_markdown(grouped, exclude_rmids=False):
    lines = []
    for ref, items in grouped.items():
        lines.append(f"# {ref}")
        lines.append("")
        for it in items:
            if exclude_rmids:
                lines.append(f'{it["must"]}')
            else:
                lines.append(f'{it["ruleid"]} – {it["must"]}')
        lines.append("")
    return ("\n".join(lines)).rstrip() + "\n"


def main(in_path: Path, out_path: Path | None = None, exclude_rmids: bool = False, reference_filter: str | None = None) -> None:
    spec = json.loads(in_path.read_text(encoding="utf-8"))
    grouped = collect(spec)
    
    # Filter by reference if specified
    if reference_filter:
        filtered_grouped = OrderedDict()
        for ref, items in grouped.items():
            if ref.lower() == reference_filter.lower():
                filtered_grouped[ref] = items
        grouped = filtered_grouped
    
    md = build_markdown(grouped, exclude_rmids=exclude_rmids)
    
    if out_path:
        out_path.write_text(md, encoding="utf-8")
    else:
        print(md, end="")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate a Markdown summary grouped by Reference, listing 'EntityId – MustSatisfy' lines."
    )
    parser.add_argument("input", nargs="?", default="build/model-1.2.json", 
                       help="Path to input JSON file (default: build/model-1.2.json)")
    parser.add_argument("--exclude-rmids", "--no-rmids", action="store_true",
                       help="Exclude Rule Model IDs from the output (only show MustSatisfy text)")
    parser.add_argument("--filename", type=str, help="Save output to specified filename instead of printing to console")
    parser.add_argument("--reference", type=str, help="Only display the normative text for the specified reference entity")
    
    args = parser.parse_args()
    
    in_path = Path(args.input)

    out_path = None
    if args.filename:
        out_path = Path(args.filename)

    
    main(in_path, out_path, exclude_rmids=args.exclude_rmids, reference_filter=args.reference)
