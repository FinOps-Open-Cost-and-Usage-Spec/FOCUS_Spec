import pytest

@pytest.mark.parametrize("keyword,expected_function", [
    ("Format", "Format"),
    ("Type", "Type"),
])
def test_function_matches_checkfunction_keyword(cr_json, keyword, expected_function):
    """
    Verify that any ConformanceRule whose ValidationCriteria.Requirement.CheckFunction
    contains a given keyword (e.g., 'Format' or 'Type') has Function set to that same keyword.
    """
    failures = []
    model_rules = cr_json.get("ModelRules", {})
    for rule_id, rule in model_rules.items():
        # Navigate safely through nested structure
        vc = rule.get("ValidationCriteria", {})
        req = vc.get("Requirement", {})
        check_fn = req.get("CheckFunction", "")

        if keyword.lower() in check_fn.lower():
            function_value = rule.get("Function")
            if function_value != expected_function:
                failures.append(
                    f"{rule_id}: expected Function='{expected_function}' "
                    f"for CheckFunction='{check_fn}', got '{function_value}'"
                )

    assert not failures, (
        f"Found {len(failures)} rules with incorrect Function values:\n" +
        "\n".join(failures)
    )