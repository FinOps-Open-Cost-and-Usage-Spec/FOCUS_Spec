import pytest

@pytest.mark.order(5)
@pytest.mark.dependency(name="provider_supports_requires_applicabilitycriteria", scope="session")
def test_provider_supports_requires_applicabilitycriteria(cr_json):
    rules = cr_json.get("ModelRules") or {}
    violations = []

    for rid, rule in rules.items():
        vc = rule.get("ValidationCriteria") or {}
        mustsatisfy = vc.get("MustSatisfy") or ""
        ac = rule.get("ApplicabilityCriteria")

        if isinstance(mustsatisfy, str) and "when the provider supports" in mustsatisfy.lower():
            if ac == [] or ac is None:
                violations.append((rid, mustsatisfy))

    assert not violations, (
        "Rules whose MustSatisfy mentions 'when the provider supports' must define at least one ApplicabilityCriteria:\n"
        + "\n".join(
            f"- Rule {rid}: MustSatisfy='{ms}' has empty ApplicabilityCriteria"
            for rid, ms in violations
        )
    )
