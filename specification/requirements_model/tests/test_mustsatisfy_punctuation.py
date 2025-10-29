import pytest

@pytest.mark.dependency(name="mustsatisfy_ends_with_colon_or_period", scope="session")
def test_mustsatisfy_ends_with_colon_or_period(cr_json):
    """
    Ensure that every ValidationCriteria.MustSatisfy string ends with ':' or '.'.
    This enforces consistent sentence/phrase termination.
    """
    rules = cr_json.get("ModelRules") or {}
    violations = []

    for rid, rule in rules.items():
        vc = rule.get("ValidationCriteria") or {}
        mustsatisfy = vc.get("MustSatisfy")
        if isinstance(mustsatisfy, str) and mustsatisfy.strip():
            if not (mustsatisfy.rstrip().endswith(":") or mustsatisfy.rstrip().endswith(".")):
                violations.append((rid, mustsatisfy))

    assert not violations, (
        "The following MustSatisfy strings do not end with ':' or '.':\n"
        + "\n".join(f"- {rid}: '{ms}'" for rid, ms in violations)
    )
