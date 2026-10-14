import pytest
from collections import defaultdict

from conftest import parse_version

@pytest.mark.dependency(name="dependencies_order", scope="session")
def test_dependencies_order(cr_json, model_version):
    """
    Test that Dependencies arrays are ordered according to the Order field of referenced rules.
    Rules without an Order field are ignored for ordering purposes.
    Rules with Order == -1 are treated as hidden and ignored for ordering purposes.
    Only dependencies with the same Reference as the parent rule are checked for ordering.
    Dependencies with different References should appear last (in any order).
    From model version 1.5, dataset rules referenced by a non-Dataset rule are treated as
    trailing dependencies, even when they share the parent's EntityId: they assert column
    presence at the dataset level rather than extending the parent rule's own sequence, so
    they must follow it. Earlier versions interleave them by Order and are exempt.
    """
    rules = cr_json.get("ModelRules") or {}
    violations = []

    # The trailing-dataset-dependency convention was introduced in 1.5. Released models
    # before that place these dependencies in their Order position and are left as-is.
    dataset_deps_trail = parse_version(model_version) >= parse_version("1.5")

    # Build maps of rule ID to Order value and EntityId
    rule_info_map = {}
    for rule_id, rule in rules.items():
        order = rule.get("Order")
        entity_id = rule.get("EntityId")
        rule_info_map[rule_id] = {
            "order": order,
            "entity_id": entity_id,
            "entity_type": rule.get("EntityType")
        }

    # Check each rule's Dependencies array for proper ordering
    for rule_id, rule in rules.items():
        if (rule.get("Status") or "").strip() == "Removed":
            continue

        dependencies = rule.get("ValidationCriteria", {}).get("Dependencies", [])
        parent_entity_id = rule.get("EntityId")
        parent_entity_type = rule.get("EntityType")
        
        if not dependencies or len(dependencies) <= 1:
            continue  # Nothing to order

        # Separate dependencies into same-entity_id and different-entity_id groups.
        # Same-EntityId dependencies with Order == -1 are hidden and ignored entirely.
        same_ref_deps = []
        diff_ref_deps = []
        own_dataset_dep_ids = set()
        
        for dep_id in dependencies:
            if dep_id not in rule_info_map:
                continue  # Skip dependencies not in the model
            
            dep_info = rule_info_map[dep_id]
            dep_entity_id = dep_info["entity_id"]
            dep_order = dep_info["order"]
            dep_entity_type = dep_info["entity_type"]

            # A dataset rule for the parent's own entity asserts that entity's presence in
            # the dataset rather than extending the parent's rule sequence. From 1.5 it is
            # grouped with the trailing dependencies and must follow all same-EntityId ones;
            # before 1.5 it is ordered inline with them.
            own_dataset_rule = (
                dataset_deps_trail
                and dep_entity_id == parent_entity_id
                and dep_entity_type == "Dataset"
                and parent_entity_type != "Dataset"
            )

            if own_dataset_rule:
                own_dataset_dep_ids.add(dep_id)

            same_entity = dep_entity_id == parent_entity_id and not own_dataset_rule

            # Hidden same-entity dependencies are ignored for all ordering checks.
            if same_entity and dep_order == -1:
                continue
            
            if same_entity and dep_order is not None and dep_order != -1:
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

        # Check that different-reference dependencies appear after same-reference dependencies.
        # Dataset rules are exempt: their primary deps are cross-EntityId column presence rules
        # by design, so enforcing same-before-diff ordering is not meaningful for them.
        if same_ref_deps and diff_ref_deps and rule.get("EntityType") != "Dataset":
            # Find the position of the last same-reference dependency in the original list
            last_same_ref_id = same_ref_deps[-1][0]
            last_same_ref_pos = dependencies.index(last_same_ref_id)
            
            # Check if any different-reference dependencies appear before this position
            for diff_ref_id in diff_ref_deps:
                diff_ref_pos = dependencies.index(diff_ref_id)
                if diff_ref_pos < last_same_ref_pos:
                    dep_reference = rule_info_map[diff_ref_id]["entity_id"]
                    if diff_ref_id in own_dataset_dep_ids:
                        issue = (
                            f"Dataset dependency {diff_ref_id} should appear after all "
                            f"'{parent_entity_id}' column dependencies"
                        )
                    else:
                        issue = (
                            f"Dependency {diff_ref_id} with different EntityId "
                            f"'{dep_reference}' should appear after all same-EntityId dependencies"
                        )
                    violations.append({
                        "rule_id": rule_id,
                        "dependency_pair": f"{diff_ref_id} (EntityId: {dep_reference})",
                        "issue": issue
                    })

    assert not violations, (
        "Dependencies arrays must be ordered according to the Order field of referenced rules with the same EntityId:\n" +
        "\n".join(f"- Rule {v['rule_id']}: {v['issue']}" 
                 for v in violations)
    )


@pytest.mark.dependency(name="no_duplicate_orders", scope="session")
def test_no_duplicate_order_values(cr_json):
    """
    Test that rules with the same EntityId, EntityType, and DatasetId do not have duplicate Order values.
    Rules without an Order field are ignored.
    """
    rules = cr_json.get("ModelRules") or {}
    violations = []
    
    # Group rules by (EntityId, EntityType, DatasetId)
    entity_groups = defaultdict(list)
    
    for rule_id, rule in rules.items():
        if (rule.get("Status") or "").strip() == "Removed":
            continue

        entity_id = rule.get("EntityId")
        entity_type = rule.get("EntityType")
        dataset_id = rule.get("DatasetId")
        order = rule.get("Order")
        
        # Skip rules without Order field or missing EntityId/EntityType
        if order is None or not entity_id or not entity_type:
            continue
            
        entity_groups[(entity_id, entity_type, dataset_id)].append({
            "rule_id": rule_id,
            "order": order
        })
    
    # Check for duplicate Order values within each group
    for (entity_id, entity_type, dataset_id), group_rules in entity_groups.items():
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
                    "dataset_id": dataset_id,
                    "order": order_value,
                    "rule_ids": rule_ids
                })
    
    assert not violations, (
        "Rules with the same EntityId, EntityType, and DatasetId must not have duplicate Order values:\n" +
        "\n".join(
            f"- EntityId='{v['entity_id']}', EntityType='{v['entity_type']}', DatasetId='{v['dataset_id']}', Order={v['order']}: "
            f"duplicate in rules {', '.join(v['rule_ids'])}"
            for v in violations
        )
    )
