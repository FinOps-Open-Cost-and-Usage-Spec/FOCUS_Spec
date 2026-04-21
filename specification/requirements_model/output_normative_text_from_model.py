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
    python output_normative_text_from_model.py --reference "BilledCost"
    python output_normative_text_from_model.py --reference "BilledCost" --include-rmids
  python output_normative_text_from_model.py --reference "BilledCost" --include-order

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


def load_spec_file(in_path: Path) -> dict:
    """Load and parse the model JSON with user-friendly error messages."""
    try:
        raw = in_path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise RuntimeError(
            "Input model file was not found: "
            f"{in_path}\n"
            "If you have not generated the model yet, run\n"
            "  ./build_json.py --build-only\n"
            "from specification/requirements_model/."
        ) from exc
    except PermissionError as exc:
        raise RuntimeError(f"Input model file is not readable: {in_path}") from exc
    except OSError as exc:
        raise RuntimeError(f"Unable to read input model file '{in_path}': {exc}") from exc

    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            "Input model file is not valid JSON: "
            f"{in_path}\n"
            f"JSON parse error at line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc


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
        ref = model.get("Reference")
        vc = model.get("ValidationCriteria") or {}
        must = vc.get("MustSatisfy")
        status = model.get("Status")
        
        # Skip rules with Status "Removed"
        if status == "Removed":
            continue
        
        if not (isinstance(ref, str) and ref.strip() and isinstance(must, str) and must.strip()):
            continue

        eid, num = extract_entity_from_ids(model_key, model.get("EntityId"), must)
        etype = infer_entity_type(model_key, model.get("EntityType"))
        order = model.get("Order")  # Extract Order field
        function = model.get("Function")  # Extract Function field
        dependencies = vc.get("Dependencies", [])  # Extract Dependencies
        dataset_id = model.get("DatasetId")  # Extract DatasetId field
        by_ref[ref.strip()].append({
            "ruleid": model_key, 
            "eid": eid, 
            "num": num, 
            "etype": etype, 
            "must": must.strip(), 
            "order": order,
            "function": function,
            "dependencies": dependencies,
            "dataset_id": dataset_id
        })

    # Deduplicate by rule ID within a reference (keep first occurrence)
    # Each rule ID should be unique, so this mainly handles any data issues
    deduped = {}
    for ref, items in by_ref.items():
        seen = set()
        out = []
        for it in items:
            key = it["ruleid"]  # Use rule ID as the unique key
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


def _dependency_allowed(parent_item: dict, dep_item: dict, follow_dependencies: bool) -> bool:
    """Return True when a dependency should be followed for output expansion."""
    parent_type = parent_item.get("etype")
    dep_type = dep_item.get("etype")

    # Column rules: only same EntityId + EntityType by default.
    if parent_type == "Column":
        if dep_type == "Column" and dep_item.get("eid") == parent_item.get("eid"):
            return True
        # Optional expansion to related object rules.
        if follow_dependencies and dep_type == "Object":
            return True
        return False

    # Dataset rules: same EntityType is sufficient by default.
    if parent_type == "Dataset":
        if dep_type == "Dataset":
            return True
        # Optional expansion to related attribute rules.
        if follow_dependencies and dep_type == "Attribute":
            return True
        return False

    return False


def filter_reference_with_dependencies(
    grouped,
    reference_filter: str,
    dependency_scope: str = "transitive",
    follow_dependencies: bool = False,
):
    """
        Filter to the requested reference and optionally include dependency rules,
        even when dependency rules use a different `Reference` value.

        dependency_scope values:
                - "none": selected reference rules plus all allowed transitive dependencies
            - "immediate": include only direct dependencies of selected rules
            - "transitive": include all dependency levels (default)
    """
    if not reference_filter:
        return grouped

    # Find the display name exactly as present in input (case-insensitive match).
    matched_refs = [ref for ref in grouped.keys() if ref.lower() == reference_filter.lower()]
    if not matched_refs:
        return OrderedDict()

    selected_ref = matched_refs[0]

    # Build a rule lookup from all references.
    rule_lookup = {}
    for items in grouped.values():
        for item in items:
            rule_lookup.setdefault(item["ruleid"], item)

    # Seed traversal with rules directly under the selected reference.
    # When a reference has mixed entity types (for example, Column + Dataset),
    # prefer non-Dataset direct matches so dataset presence rules do not appear
    # as primary output for a column reference.
    selected_items = grouped[selected_ref]
    non_dataset_items = [item for item in selected_items if item.get("etype") != "Dataset"]
    seed_items = non_dataset_items if non_dataset_items else selected_items
    seed_rule_ids = [item["ruleid"] for item in seed_items]

    if dependency_scope not in {"none", "immediate", "transitive"}:
        raise ValueError(f"Unsupported dependency scope: {dependency_scope}")

    ordered_ids = []
    seen = set()
    seed_set = set(seed_rule_ids)

    def add_rule(rule_id: str):
        if rule_id in seen:
            return
        if rule_id not in rule_lookup:
            return
        seen.add(rule_id)
        ordered_ids.append(rule_id)

    def walk_transitive(rule_id: str):
        add_rule(rule_id)
        parent_item = rule_lookup.get(rule_id)
        if not parent_item:
            return
        for dep in parent_item.get("dependencies") or []:
            dep_item = rule_lookup.get(dep)
            if not dep_item:
                continue
            if not _dependency_allowed(parent_item, dep_item, follow_dependencies):
                continue
            walk_transitive(dep)

    for rid in seed_rule_ids:
        add_rule(rid)

        # For `none`, still expand dependency closure for allowed entity matches,
        # so composite sections render complete child requirement trees.
        if dependency_scope == "none":
            parent_item = rule_lookup.get(rid)
            if not parent_item:
                continue
            for dep in parent_item.get("dependencies") or []:
                dep_item = rule_lookup.get(dep)
                if not dep_item:
                    continue
                if not _dependency_allowed(parent_item, dep_item, follow_dependencies):
                    continue
                walk_transitive(dep)
            continue

        if dependency_scope == "immediate":
            parent_item = rule_lookup.get(rid)
            if not parent_item:
                continue
            for dep in parent_item.get("dependencies") or []:
                dep_item = rule_lookup.get(dep)
                if not dep_item:
                    continue
                if not _dependency_allowed(parent_item, dep_item, follow_dependencies):
                    continue
                if dep in seed_set and dep != rid:
                    continue
                add_rule(dep)

        elif dependency_scope == "transitive":
            parent_item = rule_lookup.get(rid)
            if not parent_item:
                continue
            for dep in parent_item.get("dependencies") or []:
                dep_item = rule_lookup.get(dep)
                if not dep_item:
                    continue
                if not _dependency_allowed(parent_item, dep_item, follow_dependencies):
                    continue
                if dep in seed_set and dep != rid:
                    continue
                walk_transitive(dep)

    selected_items = [rule_lookup[rid] for rid in ordered_ids]
    return OrderedDict({selected_ref: selected_items})


def build_markdown(grouped, include_rmids=False, include_order=False):
    # Build a global lookup so a reference section can render dependency trees
    # that span rules with other Reference values.
    global_rule_map = {}
    for ref_items in grouped.values():
        for item in ref_items:
            global_rule_map[item["ruleid"]] = item

    def render_sort_key(item):
        order = item.get("order")
        if isinstance(order, (int, float)):
            return (order, item["num"], item["eid"].lower())
        return (float("inf"), item["num"], item["eid"].lower())

    lines = []
    for ref, items in grouped.items():
        lines.append(f"# {ref}")
        lines.append("")

        # Treat Order -1 as hidden: include for model logic, but do not render.
        visible_items = [
            item for item in items
            if str(item.get("order")).strip() != "-1"
        ]

        # When a section includes dataset composite rules, render their full
        # dependency closure even if dependencies belong to other references.
        section_rule_map = {item["ruleid"]: item for item in visible_items}
        dependency_stack = [
            item["ruleid"]
            for item in visible_items
            if item.get("etype") == "Dataset" and item.get("function") == "Composite"
        ]
        while dependency_stack:
            parent_rule_id = dependency_stack.pop()
            parent_item = global_rule_map.get(parent_rule_id)
            if not parent_item:
                continue
            for dep_rule_id in parent_item.get("dependencies") or []:
                dep_item = global_rule_map.get(dep_rule_id)
                if not dep_item:
                    continue
                if str(dep_item.get("order")).strip() == "-1":
                    continue
                if dep_rule_id in section_rule_map:
                    continue
                section_rule_map[dep_rule_id] = dep_item
                dependency_stack.append(dep_rule_id)
        visible_items = sorted(section_rule_map.values(), key=render_sort_key)

        if not visible_items:
            lines.append("")
            continue
        
        # Build dependency tree to determine proper nesting
        def build_dependency_map(items):
            """Build a map of rule ID -> list of dependent rule IDs"""
            dependency_map = {}
            rule_map = {}  # rule_id -> item
            
            for item in items:
                rule_id = item["ruleid"]
                rule_map[rule_id] = item
                
                # If this is a composite rule, its dependencies are its children
                if item.get("function") == "Composite":
                    dependency_map[rule_id] = item.get("dependencies", [])
                else:
                    dependency_map[rule_id] = []
            
            return dependency_map, rule_map
        
        def get_rule_level(rule_id, dependency_map, rule_map, visited=None):
            """Recursively determine the nesting level of a rule"""
            if visited is None:
                visited = set()
            
            if rule_id in visited:
                return 0  # Avoid infinite recursion
            
            visited.add(rule_id)
            
            # Find ALL composite rules that contain this rule as a dependency
            parent_composites = []
            for parent_id, deps in dependency_map.items():
                if rule_id in deps:
                    parent_composites.append(parent_id)
            
            if parent_composites:
                # If multiple parents, choose the one that is itself a dependency (most specific)
                # This handles cases where a rule appears in both root and sub-composite dependencies
                specific_parent = None
                for parent_id in parent_composites:
                    # Check if this parent is itself a dependency of another composite
                    is_nested = any(parent_id in deps for other_id, deps in dependency_map.items() if other_id != parent_id)
                    if is_nested:
                        specific_parent = parent_id
                        break
                
                # If no nested parent found, use the first one (likely root)
                chosen_parent = specific_parent if specific_parent else parent_composites[0]
                parent_level = get_rule_level(chosen_parent, dependency_map, rule_map, visited.copy())
                return parent_level + 1
            
            # If not found as a dependency, it's a root-level rule
            # Check if this is the main composite rule for this Reference
            if rule_id in rule_map:
                rule = rule_map[rule_id]
                # The main composite is either Order 0 OR the composite that contains all other rules
                if rule.get("order") == 0:
                    return 0
                elif (rule.get("function") == "Composite" and 
                      rule.get("eid") == "-000-" and
                      not any(rule_id in deps for deps in dependency_map.values())):
                    # This composite is not a dependency of any other composite, so it's root
                    return 0
                
            return 1  # Default level for non-composite root rules
        
        dependency_map, rule_map = build_dependency_map(visible_items)
        
        # Generate output with proper indentation based on dependency structure
        for item in visible_items:
            rule_id = item["ruleid"]
            level = get_rule_level(rule_id, dependency_map, rule_map)
            indent = "  " * level
            
            # Build the line with optional order prefix
            order_prefix = f'{item.get("order", "")}\t' if include_order else ""
            
            if include_rmids:
                lines.append(f'{order_prefix}{indent}* {item["must"]} ({item["ruleid"]})')
            else:
                lines.append(f'{order_prefix}{indent}* {item["must"]}')
        lines.append("")
    return ("\n".join(lines)).rstrip() + "\n"


def main(
    in_path: Path,
    out_path: Path | None = None,
    include_rmids: bool = False,
    reference_filter: str | None = None,
    include_order: bool = False,
    dataset_filter: str = "CostAndUsage",
    attribute_filter: bool = False,
    reference_dependency_scope: str = "transitive",
    follow_dependencies: bool = False,
) -> None:
    spec = load_spec_file(in_path)
    grouped = collect(spec)
    
    # Filter by reference if specified. Include transitive dependencies of the
    # selected reference so nested rules are not dropped when they use another
    # Reference value.
    if reference_filter:
        grouped = filter_reference_with_dependencies(
            grouped,
            reference_filter,
            reference_dependency_scope,
            follow_dependencies,
        )
    
    # Filter by attribute if specified (disregards dataset filter)
    if attribute_filter:
        filtered_grouped = OrderedDict()
        for ref, items in grouped.items():
            filtered_items = [item for item in items if item.get("etype") == "Attribute"]
            if filtered_items:
                filtered_grouped[ref] = filtered_items
        grouped = filtered_grouped
    # Filter by dataset if not filtering by attribute
    elif dataset_filter:
        filtered_grouped = OrderedDict()
        for ref, items in grouped.items():
            filtered_items = [item for item in items 
                            if item.get("dataset_id") and item.get("dataset_id").lower() == dataset_filter.lower()]
            if filtered_items:
                filtered_grouped[ref] = filtered_items
        grouped = filtered_grouped
    
    md = build_markdown(grouped, include_rmids=include_rmids, include_order=include_order)
    
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
    parser.add_argument("--include-rmids", action="store_true",
                       help="Include Rule Model IDs in the output")
    parser.add_argument("--include-order", action="store_true",
                       help="Include Order field at the start of each line (tab-separated)")
    parser.add_argument("--filename", type=str, help="Save output to specified filename instead of printing to console")
    parser.add_argument("--reference", type=str, help="Only display the normative text for the specified reference entity")
    parser.add_argument("--reference-dependency-scope", choices=["none", "immediate", "transitive"], default="transitive",
                       help="When --reference is used, include dependency rules by scope (default: transitive)")
    parser.add_argument(
        "--follow-dependencies",
        action="store_true",
        help=(
            "When following dependencies via --reference, also traverse Dataset->Attribute "
            "and Column->Object dependencies."
        ),
    )
    parser.add_argument("--datasetid", "--dataset", type=str, default="CostAndUsage",
                       help="Filter entities by DatasetId (default: CostAndUsage)")
    parser.add_argument("--attribute", action="store_true",
                       help="Filter for Attribute entities only (disregards --datasetid)")
    
    args = parser.parse_args()
    
    in_path = Path(args.input)

    out_path = None
    if args.filename:
        out_path = Path(args.filename)

    
    try:
        main(
            in_path,
            out_path,
            include_rmids=args.include_rmids,
            reference_filter=args.reference,
            include_order=args.include_order,
            dataset_filter=args.datasetid,
            attribute_filter=args.attribute,
            reference_dependency_scope=args.reference_dependency_scope,
            follow_dependencies=args.follow_dependencies,
        )
    except RuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)
