import pytest

@pytest.mark.dependency(name="dynamic_rules_have_empty_requirement", scope="session")
def test_dynamic_rules_have_empty_requirement(cr_json):
    rules = cr_json.get("ModelRules") or {}
    violations = []

    for rid, rule in rules.items():
        if rule.get("Type") == "Dynamic":
            vc = rule.get("ValidationCriteria") or {}
            requirement = vc.get("Requirement")
            if requirement != {}:
                violations.append((rid, requirement))

    assert not violations, (
        "Dynamic rules must have ValidationCriteria.Requirement = {}:\n"
        + "\n".join(f"- Rule {rid} has Requirement={req}" for rid, req in violations)
    )