import pytest

@pytest.mark.order(3)
@pytest.mark.dependency(name="dependencies_reference_existing_rules", scope="session")
def test_dependencies_reference_existing_rules(cr_json):
    rules = cr_json.get("ModelRules") or {}
    defined_ids = set(rules.keys())

    missing = []   # (rule_id, dep_id)
    badtype = []   # (rule_id, dep_value_type)

    for rid, rule in rules.items():
        vc = rule.get("ValidationCriteria") or {}
        deps = vc.get("Dependencies") or []
        for dep in deps:
            if not isinstance(dep, str):
                badtype.append((rid, type(dep).__name__))
                continue
            if dep not in defined_ids:
                missing.append((rid, dep))

    assert not badtype, (
        "Dependencies must be strings (rule id references):\n" +
        "\n".join(f"- Rule {rid}: dependency has type {t}" for rid, t in badtype)
    )
    assert not missing, (
        "Dependencies pointing to non-existent ModelRules:\n" +
        "\n".join(f"- Rule {rid} depends on {dep}" for rid, dep in missing)
    )
