# tests/test_c000_d_deps_presence_reference.py
import re

C000_RE = re.compile(r"-C-000-")

def test_c000_rules_have_d_deps_and_presence_refs_match(cr_json):
    rules = cr_json.get("ConformanceRules") or {}
    missing_any_d = []        # *-C-000-* with no -D- deps at all
    presence_mismatch = []    # *-C-000-* with -D- deps of Function=Presence that don't match Reference

    for rid, rule in rules.items():
        # Only check Column "000" rules by ID pattern
        if not isinstance(rid, str) or C000_RE.search(rid) is None:
            continue

        vc = rule.get("ValidationCriteria") or {}
        deps = vc.get("Dependencies") or []
        if not isinstance(deps, list):
            deps = []

        # Gather valid -D- dependencies that exist as rules
        d_dep_ids = [d for d in deps if isinstance(d, str) and "-D-" in d and d in rules]

        if not d_dep_ids:
            missing_any_d.append(rid)
            continue

        # Column rule's Reference (must match D 'Presence' rule's Reference)
        c_ref = rule.get("Reference")

        # For all D deps with Function == "Presence", enforce Reference match
        mismatches = []
        for d_id in d_dep_ids:
            d_rule = rules.get(d_id) or {}
            if (d_rule.get("Function") == "Presence"):  # only enforce on Presence
                d_ref = d_rule.get("Reference")
                if c_ref != d_ref:
                    mismatches.append((d_id, d_ref))

        if mismatches:
            presence_mismatch.append((rid, c_ref, mismatches))

    assert not missing_any_d, (
        "Every *-C-000-* rule must declare at least one -D- dependency:\n"
        + "\n".join(f"- {rid}" for rid in sorted(missing_any_d))
    )

    assert not presence_mismatch, (
        "For *-C-000-* rules, all -D- dependencies with Function='Presence' must have matching Reference:\n"
        + "\n".join(
            f"- {rid}: Column Reference='{c_ref}', mismatched D deps: "
            + ", ".join(f"{d_id} (D.Reference='{d_ref}')" for d_id, d_ref in mismatches)
            for rid, c_ref, mismatches in presence_mismatch
        )
    )
