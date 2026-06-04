import pytest

@pytest.mark.dependency(name="deprecated_composite_rules", scope="session")
def test_deprecated_composite_rules(cr_json):
    """
    Test that composite rules with Status: "Deprecated" only contain child rules
    that are also Status: "Deprecated".
    Active child rules should not be part of deprecated composite rules.
    """
    rules = cr_json.get("ModelRules") or {}
    violations = []

    # Build a map of rule ID to Status
    rule_status_map = {}
    for rule_id, rule in rules.items():
        status = rule.get("Status", "Active")  # Default to Active if not specified
        rule_status_map[rule_id] = status

    # Check each deprecated composite rule's Items array
    for rule_id, rule in rules.items():
        rule_status = rule.get("Status", "Active")
        
        # Only check deprecated rules
        if rule_status != "Deprecated":
            continue
        
        # Check if this is a composite rule (has Items in ValidationCriteria)
        items = rule.get("ValidationCriteria", {}).get("Items", [])
        
        if not items:
            continue  # Not a composite rule

        # Check each child rule
        for item in items:
            child_id = item.get("ModelRuleId")
            if not child_id:
                continue
            
            if child_id not in rule_status_map:
                # Child doesn't exist - this should be caught by another test
                continue
            
            child_status = rule_status_map[child_id]
            
            # Child must be Deprecated
            if child_status != "Deprecated":
                violations.append({
                    "rule_id": rule_id,
                    "child_id": child_id,
                    "child_status": child_status,
                    "issue": f"Deprecated composite rule {rule_id} contains child rule {child_id} with Status: '{child_status}'"
                })

    assert not violations, (
        "Deprecated composite rules must only contain child rules with Status: 'Deprecated':\n" +
        "\n".join(f"- {v['issue']}" for v in violations)
    )
