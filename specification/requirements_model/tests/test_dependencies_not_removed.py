import pytest

@pytest.mark.dependency(name="dependencies_not_removed", scope="session")
def test_dependencies_not_removed(cr_json):
    """
    Test that no rules depend on rules with Status: "Removed".
    Rules with any status (Active, Deprecated, etc.) should not depend on removed rules.
    """
    rules = cr_json.get("ModelRules") or {}
    violations = []

    # Build a map of rule ID to Status
    rule_status_map = {}
    for rule_id, rule in rules.items():
        status = rule.get("Status", "Active")  # Default to Active if not specified
        rule_status_map[rule_id] = status

    # Check each rule's Dependencies array for removed dependencies
    for rule_id, rule in rules.items():
        dependencies = rule.get("ValidationCriteria", {}).get("Dependencies", [])
        
        if not dependencies:
            continue  # No dependencies to check

        for dep_id in dependencies:
            if dep_id not in rule_status_map:
                # Dependency doesn't exist - this should be caught by another test
                continue
            
            dep_status = rule_status_map[dep_id]
            
            if dep_status == "Removed":
                violations.append({
                    "rule_id": rule_id,
                    "removed_dependency": dep_id,
                    "issue": f"Rule {rule_id} depends on removed rule {dep_id}"
                })

    assert not violations, (
        "No rules may depend on removed rules. All dependencies must not have Status: 'Removed':\n" +
        "\n".join(f"- {v['issue']}" for v in violations)
    )
