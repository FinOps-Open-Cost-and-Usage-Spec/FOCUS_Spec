import pytest

@pytest.mark.dependency(name="dependencies_order", scope="session")
def test_dependencies_order(cr_json):
    """
    Test that Dependencies arrays are ordered according to the Order field of referenced rules.
    Rules without an Order field are ignored for ordering purposes.
    """
    rules = cr_json.get("ModelRules") or {}
    violations = []

    # Build a map of rule ID to Order value for rules that have an Order field
    rule_order_map = {}
    for rule_id, rule in rules.items():
        order = rule.get("Order")
        if order is not None:
            rule_order_map[rule_id] = order

    # Check each rule's Dependencies array for proper ordering
    for rule_id, rule in rules.items():
        dependencies = rule.get("ValidationCriteria", {}).get("Dependencies", [])
        
        if not dependencies or len(dependencies) <= 1:
            continue  # Nothing to order

        # Filter dependencies to only those that have an Order field
        ordered_dependencies = []
        for dep_id in dependencies:
            if dep_id in rule_order_map:
                ordered_dependencies.append((dep_id, rule_order_map[dep_id]))

        if len(ordered_dependencies) <= 1:
            continue  # Nothing to check

        # Check if the dependencies are in ascending order by their Order values
        for i in range(1, len(ordered_dependencies)):
            prev_dep_id, prev_order = ordered_dependencies[i-1]
            curr_dep_id, curr_order = ordered_dependencies[i]
            
            if prev_order > curr_order:
                violations.append({
                    "rule_id": rule_id,
                    "dependency_pair": f"{prev_dep_id} (Order: {prev_order}) -> {curr_dep_id} (Order: {curr_order})",
                    "issue": f"Dependency {prev_dep_id} with Order {prev_order} should come after {curr_dep_id} with Order {curr_order}"
                })

    assert not violations, (
        "Dependencies arrays must be ordered according to the Order field of referenced rules:\n" +
        "\n".join(f"- Rule {v['rule_id']}: {v['issue']} in dependencies: {v['dependency_pair']}" 
                 for v in violations)
    )