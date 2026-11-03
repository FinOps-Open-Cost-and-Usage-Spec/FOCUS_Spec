# tests/test_no_spurious_composite.py
import pytest

@pytest.mark.dependency(name="no_composite_without_and_or_with_rule_item", scope="session")
def test_no_composite_without_and_or_with_rule_item(cr_json):
    rules = cr_json.get("ModelRules") or {}
    violations = []

    for rid, rule in rules.items():
        if rule.get("Function") != "Composite":
            continue

        vc = rule.get("ValidationCriteria") or {}
        req = vc.get("Requirement")
        if not isinstance(req, dict):
            violations.append((rid, "missing Requirement"))
            continue

        cf = req.get("CheckFunction")
        items = req.get("Items")
        has_rule_item = isinstance(items, list) and any(
            isinstance(it, dict) and it.get("CheckFunction") == "CheckModelRule"
            for it in items
        )

        if cf not in {"AND", "OR"} or not has_rule_item:
            reason = []
            if cf not in {"AND", "OR"}:
                reason.append(f"CheckFunction={cf!r}")
            if not has_rule_item:
                reason.append("no CheckModelRule item")
            violations.append((rid, ", ".join(reason)))

    assert not violations, (
        "Rules marked Function='Composite' must have Requirement.CheckFunction AND/OR "
        "and include at least one Items[*].CheckFunction == 'CheckModelRule':\n"
        + "\n".join(f"- {rid}: {why}" for rid, why in violations)
    )
