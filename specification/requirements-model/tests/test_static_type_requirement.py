import pytest

@pytest.mark.dependency(name="static_rules_have_non_empty_requirement", scope="session")
def test_static_rules_have_non_empty_requirement(cr_json):
    rules = cr_json.get("ModelRules") or {}
    violations = []

    for rid, rule in rules.items():
        if rule.get("Type") == "Static":
            vc = rule.get("ValidationCriteria") or {}
            requirement = vc.get("Requirement")
            if requirement == {}:
                violations.append(rid)

    assert not violations, (
        "Static rules must have non-empty ValidationCriteria.Requirement:\n"
        + "\n".join(f"- Rule {rid} has empty Requirement" for rid in violations)
    )