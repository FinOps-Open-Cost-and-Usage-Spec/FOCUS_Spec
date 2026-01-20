import pytest
from collections import defaultdict

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

    # Build maps of rule ID to Order value and EntityId
    rule_info_map = {}
    for rule_id, rule in rules.items():
        order = rule.get("Order")
        entity_id = rule.get("EntityId")
        rule_info_map[rule_id] = {
            "order": order,
            "entity_id": entity_id
        }

    # Check each rule's Dependencies array for proper ordering
    for rule_id, rule in rules.items():
        dependencies = rule.get("ValidationCriteria", {}).get("Dependencies", [])
        parent_entity_id = rule.get("EntityId")
        
        if not dependencies or len(dependencies) <= 1:
            continue  # Nothing to order

        # Separate dependencies into same-entity_id and different-entity_id groups
        same_ref_deps = []
        diff_ref_deps = []
        
        for dep_id in dependencies:
            if dep_id not in rule_info_map:
                continue  # Skip dependencies not in the model
            
            dep_info = rule_info_map[dep_id]
            dep_entity_id = dep_info["entity_id"]
            dep_order = dep_info["order"]
            
            if dep_entity_id == parent_entity_id and dep_order is not None:
                same_ref_deps.append((dep_id, dep_order))
            else:
                diff_ref_deps.append(dep_id)

        # Check that same-entity_id dependencies are ordered correctly
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
                    dep_reference = rule_info_map[diff_ref_id]["entity_id"]
                    violations.append({
                        "rule_id": rule_id,
                        "dependency_pair": f"{diff_ref_id} (EntityId: {dep_reference})",
                        "issue": f"Dependency {diff_ref_id} with different EntityId '{dep_reference}' should appear after all same-EntityId dependencies"
                    })

    assert not violations, (
        "Dependencies arrays must be ordered according to the Order field of referenced rules with the same EntityId:\n" +
        "\n".join(f"- Rule {v['rule_id']}: {v['issue']}" 
                 for v in violations)
    )


@pytest.mark.dependency(name="no_duplicate_orders", scope="session")
def test_no_duplicate_order_values(cr_json):
    """
    Test that rules with the same EntityId and EntityType do not have duplicate Order values.
    Rules without an Order field are ignored.
    """
    rules = cr_json.get("ModelRules") or {}
    violations = []
    
    # Group rules by (EntityId, EntityType)
    entity_groups = defaultdict(list)
    
    for rule_id, rule in rules.items():
        entity_id = rule.get("EntityId")
        entity_type = rule.get("EntityType")
        order = rule.get("Order")
        
        # Skip rules without Order field or missing EntityId/EntityType
        if order is None or not entity_id or not entity_type:
            continue
            
        entity_groups[(entity_id, entity_type)].append({
            "rule_id": rule_id,
            "order": order
        })
    
    # Check for duplicate Order values within each group
    for (entity_id, entity_type), group_rules in entity_groups.items():
        # Build a map of order -> list of rule IDs
        order_map = defaultdict(list)
        for rule_info in group_rules:
            order_map[rule_info["order"]].append(rule_info["rule_id"])
        
        # Find duplicates
        for order_value, rule_ids in order_map.items():
            if len(rule_ids) > 1:
                violations.append({
                    "entity_id": entity_id,
                    "entity_type": entity_type,
                    "order": order_value,
                    "rule_ids": rule_ids
                })
    
    assert not violations, (
        "Rules with the same EntityId and EntityType must not have duplicate Order values:\n" +
        "\n".join(
            f"- EntityId='{v['entity_id']}', EntityType='{v['entity_type']}', Order={v['order']}: "
            f"duplicate in rules {', '.join(v['rule_ids'])}"
            for v in violations
        )
    )
