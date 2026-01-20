# tests/test_c000_d_deps_presence_or_composite_reference.py
import re
import pytest


_C000_RE = re.compile(r"-C-000-")


def _iter_values_for_key(node, target_key):
    """Yield all string values for a given key (e.g., 'ModelRuleId') anywhere under node."""
    if node is None:
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if k == target_key and isinstance(v, str):
                yield v
            yield from _iter_values_for_key(v, target_key)
    elif isinstance(node, list):
        for item in node:
            yield from _iter_values_for_key(item, target_key)

def _collect_nested_d_rules(root_rule_id, rules, visited=None):
    """
    Depth-first collect all -D- ModelRuleIds reachable from a D rule via
    ValidationCriteria.Requirement/Condition trees (following ModelRuleId links).
    Includes ONLY rule IDs that exist in `rules` and contain '-D-'.
    """
    if visited is None:
        visited = set()
    stack = [root_rule_id]
    out = set()
    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        rule = rules.get(current) or {}
        vc = rule.get("ValidationCriteria") or {}
        for root_key in ("Requirement", "Condition"):
            root = vc.get(root_key)
            for ref in _iter_values_for_key(root, "ModelRuleId"):
                if isinstance(ref, str) and ref in rules and "-D-" in ref:
                    if ref not in out:
                        out.add(ref)
                        stack.append(ref)
    # remove the original root if it got added indirectly; caller handles root separately
    out.discard(root_rule_id)
    return out

@pytest.mark.dependency(name="c000_rules_d_deps_presence_or_composite_refs_match", scope="session")
def test_c000_rules_d_deps_presence_or_composite_refs_match(cr_json):
    rules = cr_json.get("ModelRules") or {}
    missing_any_d = []         # *-C-000-* with no -D- deps at all
    presence_mismatch = []     # mismatches for Presence D deps
    composite_mismatch = []    # mismatches for Composite D deps (self or nested)

    for col_id, col_rule in rules.items():
        # Only check Column "000" rules by ID pattern
        if not isinstance(col_id, str) or _C000_RE.search(col_id) is None:
            continue
        if (col_rule.get("EntityType") or "").strip() != "Column":
            continue

        vc = col_rule.get("ValidationCriteria") or {}
        deps = vc.get("Dependencies") or []
        deps = deps if isinstance(deps, list) else []
        # Valid -D- deps that exist as rules and are Dataset entity
        d_dep_ids = [
            d for d in deps
            if isinstance(d, str)
            and d in rules
            and (rules[d] or {}).get("EntityType") == "Dataset"
            and "-D-" in d
        ]

        if not d_dep_ids:
            missing_any_d.append(col_id)
            continue

        col_ref = col_rule.get("Reference")

        for d_id in d_dep_ids:
            d_rule = rules.get(d_id) or {}
            d_func = d_rule.get("Function")
            d_ref = d_rule.get("Reference")

            if d_func == "Presence":
                if d_ref != col_ref:
                    presence_mismatch.append((col_id, d_id, col_ref, d_ref))
                continue

            if d_func == "Composite":
                # Root D must match
                local_bad = []
                if d_ref != col_ref:
                    local_bad.append((d_id, d_ref))
                # All nested -D- rules reachable via Requirement/Condition must match too
                nested_d_ids = _collect_nested_d_rules(d_id, rules)
                for nd in nested_d_ids:
                    nd_ref = (rules.get(nd) or {}).get("Reference")
                    if nd_ref != col_ref:
                        local_bad.append((nd, nd_ref))
                if local_bad:
                    composite_mismatch.append((col_id, col_ref, d_id, local_bad))
                continue

            # If a -D- dep has some other Function, treat as mismatch (optional; or ignore)
            # composite_mismatch.append((col_id, col_ref, d_id, [(d_id, d_ref, f"unexpected Function={d_func!r}")]))

    assert not missing_any_d, (
        "Every *-C-000-* rule must declare at least one -D- dependency (Dataset entity):\n"
        + "\n".join(f"- {rid}" for rid in sorted(missing_any_d))
    )

    assert not presence_mismatch, (
        "For *-C-000-* rules, -D- dependencies with Function='Presence' must have matching Reference:\n"
        + "\n".join(
            f"- Column {cid}: D dep {did} -> Column.Ref='{c_ref}' vs D.Ref='{d_ref}'"
            for cid, did, c_ref, d_ref in presence_mismatch
        )
    )

    assert not composite_mismatch, (
        "For *-C-000-* rules, -D- dependencies with Function='Composite' must have matching Reference "
        "for the composite D rule *and* all nested -D- rules it references:\n"
        + "\n".join(
            f"- Column {cid} (Column.Ref='{c_ref}') via D dep {did}: mismatches="
            + ", ".join(f"{nid} (Ref='{nref}')" for nid, nref in mismatches)
            for cid, c_ref, did, mismatches in composite_mismatch
        )
    )
