import pytest

@pytest.mark.dependency(name="dependencies_not_deprecated", scope="session")
def test_dependencies_not_deprecated(cr_json):
    """
    Test that all dependencies of active rules reference rules with Status: "Active".
    Active rules should not depend on deprecated rules.
    Deprecated rules are allowed to depend on other deprecated rules.
    """
    rules = cr_json.get("ModelRules") or {}
    violations = []

    # Build a map of rule ID to Status
    rule_status_map = {}
    for rule_id, rule in rules.items():
        status = rule.get("Status", "Active")  # Default to Active if not specified
        rule_status_map[rule_id] = status

    # Check each active rule's Dependencies array for deprecated dependencies
    for rule_id, rule in rules.items():
        rule_status = rule.get("Status", "Active")
        
        # Skip deprecated rules - they can depend on anything
        if rule_status == "Deprecated":
            continue
        
        dependencies = rule.get("ValidationCriteria", {}).get("Dependencies", [])
        
        if not dependencies:
            continue  # No dependencies to check

        for dep_id in dependencies:
            if dep_id not in rule_status_map:
                # Dependency doesn't exist - this should be caught by another test
                continue
            
            dep_status = rule_status_map[dep_id]
            
            if dep_status == "Deprecated":
                violations.append({
                    "rule_id": rule_id,
                    "deprecated_dependency": dep_id,
                    "issue": f"Active rule {rule_id} depends on deprecated rule {dep_id}"
                })

    assert not violations, (
        "Active rules must not depend on deprecated rules. All dependencies must have Status: 'Active':\n" +
        "\n".join(f"- {v['issue']}" for v in violations)
    )
