
import pytest

@pytest.mark.dependency(name="requirement_and_or_with_rule_items_requires_function_composite", scope="session")
def test_requirement_and_or_with_rule_items_requires_function_composite(cr_json):
    rules = cr_json.get("ModelRules") or {}
    violations = []

    for rid, rule in rules.items():
        vc = rule.get("ValidationCriteria") or {}
        req = vc.get("Requirement")
        if not isinstance(req, dict):
            continue

        cf = req.get("CheckFunction")
        if cf not in {"AND", "OR"}:
            continue

        items = req.get("Items")
        if not isinstance(items, list):
            continue

        # Trigger only if there's at least one CheckModelRule item
        has_rule_item = any(
            isinstance(it, dict) and it.get("CheckFunction") == "CheckModelRule"
            for it in items
        )
        if not has_rule_item:
            continue

        if rule.get("Function") != "Composite":
            violations.append((rid, cf, rule.get("Function")))

    assert not violations, (
        "Rules with Requirement.CheckFunction AND/OR and at least one "
        "Items[*].CheckFunction == 'CheckModelRule' must have Function='Composite':\n"
        + "\n".join(f"- {rid}: CheckFunction={cf}, Function={fn}" for rid, cf, fn in violations)
    )
