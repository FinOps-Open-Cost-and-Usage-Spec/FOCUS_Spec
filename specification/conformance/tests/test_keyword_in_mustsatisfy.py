import pytest

@pytest.mark.xfail(reason="Known issue, fix pending")
def test_keyword_present_in_mustsatisfy(cr_json):
    rules = cr_json.get("ConformanceRules") or {}
    violations = []

    for rid, rule in rules.items():
        vc = rule.get("ValidationCriteria") or {}
        keyword = vc.get("Keyword")
        mustsatisfy = vc.get("MustSatisfy")

        # Only check when both fields exist and are strings
        if isinstance(keyword, str) and isinstance(mustsatisfy, str):
            if keyword not in mustsatisfy:
                violations.append((rid, keyword, mustsatisfy))

    assert not violations, (
        "ValidationCriteria.Keyword must be present inside ValidationCriteria.MustSatisfy:\n"
        + "\n".join(
            f"- Rule {rid}: keyword '{kw}' not in MustSatisfy='{ms}'"
            for rid, kw, ms in violations
        )
    )