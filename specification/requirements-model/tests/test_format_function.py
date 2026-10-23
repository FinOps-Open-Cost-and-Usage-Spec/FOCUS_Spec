import re
import pytest

@pytest.mark.dependency(name="mustsatisfy_format_requires_function_format", scope="session")
def test_mustsatisfy_format_requires_function_format(cr_json):
    rules = cr_json.get("ModelRules") or {}
    violations = []

    for rid, rule in rules.items():
        func = rule.get("Function")
        if func == "Composite":
            continue  # skip composite rules

        vc = rule.get("ValidationCriteria") or {}
        mustsatisfy = vc.get("MustSatisfy")

        if isinstance(mustsatisfy, str) and re.search(r"\bformat\b", mustsatisfy, re.IGNORECASE):
            if func != "Format":
                violations.append((rid, func, mustsatisfy))


    assert not violations, (
        "Any non-Composite rule whose MustSatisfy contains 'format' must have Function='Format':\n"
        + "\n".join(
            f"- Rule {rid}: Function='{func}', MustSatisfy='{ms}'"
            for rid, func, ms in violations
        )
    )
