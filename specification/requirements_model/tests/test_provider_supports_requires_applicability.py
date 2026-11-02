import pytest
from conftest import get_conditions, conditions_key

@pytest.mark.order(5)
@pytest.mark.dependency(name="provider_supports_requires_applicabilitycriteria", scope="session")
def test_provider_supports_requires_applicabilitycriteria(cr_json, model_version):
    rules = cr_json.get("ModelRules") or {}
    violations = []

    for rid, rule in rules.items():
        vc = rule.get("ValidationCriteria") or {}
        mustsatisfy = vc.get("MustSatisfy") or ""
        ac = get_conditions(rule, model_version)

        if isinstance(mustsatisfy, str) and "when the provider supports" in mustsatisfy.lower():
            if not ac:
                violations.append((rid, mustsatisfy))

    key = conditions_key(model_version)
    assert not violations, (
        f"Rules whose MustSatisfy mentions 'when the provider supports' must define at least one {key}:\n"
        + "\n".join(
            f"- Rule {rid}: MustSatisfy='{ms}' has empty {key}"
            for rid, ms in violations
        )
    )
