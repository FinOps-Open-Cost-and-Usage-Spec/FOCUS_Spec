import pytest

@pytest.mark.dependency(name="dependencies_order", scope="session")
def test_dependencies_order(cr_json):
    """
    Test that Dependencies arrays are ordered according to the Order field of referenced rules.
    Rules without an Order field are ignored for ordering purposes.
    Only dependencies with the same Reference as the parent rule are checked for ordering.
    Dependencies with different References should appear last (in any order).
    """
    rules = cr_json.get("ModelRules") or {}
    violations = []

    # Build maps of rule ID to Order value and Reference
    rule_info_map = {}
    for rule_id, rule in rules.items():
        order = rule.get("Order")
        reference = rule.get("Reference")
        rule_info_map[rule_id] = {
            "order": order,
            "reference": reference
        }

    # Check each rule's Dependencies array for proper ordering
    for rule_id, rule in rules.items():
        dependencies = rule.get("ValidationCriteria", {}).get("Dependencies", [])
        parent_reference = rule.get("Reference")
        
        if not dependencies or len(dependencies) <= 1:
            continue  # Nothing to order

        # Separate dependencies into same-reference and different-reference groups
        same_ref_deps = []
        diff_ref_deps = []
        
        for dep_id in dependencies:
            if dep_id not in rule_info_map:
                continue  # Skip dependencies not in the model
            
            dep_info = rule_info_map[dep_id]
            dep_reference = dep_info["reference"]
            dep_order = dep_info["order"]
            
            if dep_reference == parent_reference and dep_order is not None:
                same_ref_deps.append((dep_id, dep_order))
            else:
                diff_ref_deps.append(dep_id)

        # Check that same-reference dependencies are ordered correctly
        if len(same_ref_deps) > 1:
            for i in range(1, len(same_ref_deps)):
                prev_dep_id, prev_order = same_ref_deps[i-1]
                curr_dep_id, curr_order = same_ref_deps[i]
                
                if prev_order > curr_order:
                    violations.append({
                        "rule_id": rule_id,
                        "dependency_pair": f"{prev_dep_id} (Order: {prev_order}) -> {curr_dep_id} (Order: {curr_order})",
                        "issue": f"Dependency {prev_dep_id} with Order {prev_order} should come after {curr_dep_id} with Order {curr_order}"
                    })

        # Check that different-reference dependencies appear after same-reference dependencies
        if same_ref_deps and diff_ref_deps:
            # Find the position of the last same-reference dependency in the original list
            last_same_ref_id = same_ref_deps[-1][0]
            last_same_ref_pos = dependencies.index(last_same_ref_id)
            
            # Check if any different-reference dependencies appear before this position
            for diff_ref_id in diff_ref_deps:
                diff_ref_pos = dependencies.index(diff_ref_id)
                if diff_ref_pos < last_same_ref_pos:
                    dep_reference = rule_info_map[diff_ref_id]["reference"]
                    violations.append({
                        "rule_id": rule_id,
                        "dependency_pair": f"{diff_ref_id} (Reference: {dep_reference})",
                        "issue": f"Dependency {diff_ref_id} with different Reference '{dep_reference}' should appear after all same-Reference dependencies"
                    })

    assert not violations, (
        "Dependencies arrays must be ordered according to the Order field of referenced rules with the same Reference:\n" +
        "\n".join(f"- Rule {v['rule_id']}: {v['issue']}" 
                 for v in violations)
    )