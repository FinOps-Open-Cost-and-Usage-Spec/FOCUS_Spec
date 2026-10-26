import pytest

@pytest.mark.order(2)
@pytest.mark.dependency(name="all_dependencies_reference_existing_rules", scope="session")
def test_all_dependencies_reference_existing_rules(cr_json):
    rules = cr_json.get("ModelRules") or {}
    rule_ids = set(rules.keys())
    missing = []

    for rid, rule in rules.items():
        vc = rule.get("ValidationCriteria") or {}
        deps = vc.get("Dependencies") or []
        for dep in deps:
            if dep not in rule_ids:
                missing.append((rid, dep))

    assert not missing, (
        "Dependencies pointing to non-existent ModelRules:\n" +
        "\n".join(f"- Rule {rid} depends on {dep}" for rid, dep in missing)
    )