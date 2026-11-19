import pytest

@pytest.mark.dependency(name="mustsatisfy_null_requires_function_nullability", scope="session")
def test_mustsatisfy_null_requires_function_nullability(cr_json):
    rules = cr_json.get("ModelRules") or {}
    violations = []

    for rid, rule in rules.items():
        func = rule.get("Function")
        if func == "Composite":
            continue  # skip composite rules

        vc = rule.get("ValidationCriteria") or {}
        mustsatisfy = vc.get("MustSatisfy")

        if isinstance(mustsatisfy, str) and "be null" in mustsatisfy.lower():
            if func != "Nullability":
                violations.append((rid, func, mustsatisfy))

    assert not violations, (
        "Any non-Composite rule whose MustSatisfy contains 'null' must have Function='Nullability':\n"
        + "\n".join(
            f"- Rule {rid}: Function='{func}', MustSatisfy='{ms}'"
            for rid, func, ms in violations
        )
    )
