import pytest

@pytest.mark.dependency(name="reference_matches_rule_key_prefix_for_columns", scope="session")
def test_reference_matches_rule_key_prefix_for_columns(cr_json):
    rules = cr_json.get("ModelRules") or {}
    violations = []

    for rid, rule in rules.items():
        if rule.get("EntityType") != "Column":
            continue  # only enforce for Column rules
        
        ref = rule.get("Reference")
        if isinstance(ref, str):
            if not rid.startswith(ref):
                violations.append((rid, ref))
        else:
            violations.append((rid, f"<missing or non-str: {ref}>"))

    assert not violations, (
        "ModelRules.Reference must match the prefix of the rule key:\n"
        + "\n".join(f"- Rule {rid}: Reference='{ref}'" for rid, ref in violations)
    )