import pytest

def _iter_values_for_key(node, target_key):
    """Yield all string values for a given key found anywhere under node."""
    if node is None:
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if k == target_key and isinstance(v, str):
                yield v
            # recurse into values
            yield from _iter_values_for_key(v, target_key)
    elif isinstance(node, list):
        for item in node:
            yield from _iter_values_for_key(item, target_key)

@pytest.mark.xfail(reason="Known issue, fix pending")
def test_conformance_ruleid_refs_listed_in_dependencies(cr_json):
    rules = cr_json.get("ConformanceRules") or {}
    violations = []

    for rid, rule in rules.items():
        vc = rule.get("ValidationCriteria") or {}
        deps = set(vc.get("Dependencies") or [])

        # Collect every ConformanceRuleId referenced under Requirement and Condition
        refs = set(_iter_values_for_key(vc.get("Requirement"), "ConformanceRuleId"))
        refs |= set(_iter_values_for_key(vc.get("Condition"), "ConformanceRuleId"))

        missing = refs - deps
        if missing:
            violations.append((rid, sorted(missing)))

    assert not violations, (
        "Any ConformanceRuleId referenced in Requirement/Condition must be listed in ValidationCriteria.Dependencies:\n"
        + "\n".join(f"- Rule {rid}: missing deps {missing}" for rid, missing in violations)
    )