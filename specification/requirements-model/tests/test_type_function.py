import pytest

skipped_check_functions = {}

@pytest.mark.dependency(name="mustsatisfy_of_type_requires_function_type", scope="session")
def test_mustsatisfy_of_type_requires_function_type(cr_json):
    rules = cr_json.get("ModelRules") or {}
    violations = []

    for rid, rule in rules.items():
        func = rule.get("Function")
        if func == "Composite":
            continue  # skip composite rules

        vc = rule.get("ValidationCriteria") or {}
        mustsatisfy = vc.get("MustSatisfy")
        check_function = vc.get("Requirement", {}).get("CheckFunction", "")
        if check_function in skipped_check_functions:
            continue  # skip for specific check functions
        
        if isinstance(mustsatisfy, str) and "of type" in mustsatisfy.lower():
            if func != "Type":
                violations.append((rid, func, mustsatisfy))

    assert not violations, (
        "Any non-Composite rule whose MustSatisfy contains 'of type' must have Function='Type':\n"
        + "\n".join(
            f"- Rule {rid}: Function='{func}', MustSatisfy='{ms}'"
            for rid, func, ms in violations
        )
    )
