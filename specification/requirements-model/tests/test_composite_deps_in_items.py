"""
For every Composite rule, each Dependency with the same EntityType as the
composite rule must appear as a ModelRuleId somewhere within the
Requirement Items[] tree (recurses through AND/OR nesting).

Applies to version 1.4 and later.
"""
import pytest
from conftest import requires_version


def _collect_references(node, rule_ids, entity_ids):
    """Recursively collect ModelRuleId values and ColumnName/ColumnAName EntityId references."""
    if not isinstance(node, dict):
        return
    if "ModelRuleId" in node:
        rule_ids.add(node["ModelRuleId"])
    for key in ("ColumnName", "ColumnAName"):
        if isinstance(node.get(key), str):
            entity_ids.add(node[key])
    for item in node.get("Items", []):
        _collect_references(item, rule_ids, entity_ids)


def test_composite_deps_in_items(model_version, cr_json):
    """Composite rule dependencies with the same EntityType must appear in Requirement Items."""
    should_skip, reason = requires_version(model_version, min_version="1.4")
    if should_skip:
        pytest.skip(reason)

    rules = cr_json.get("ModelRules", {})
    errors = []

    for rule_id, rule in rules.items():
        if rule.get("Function") != "Composite":
            continue
        if rule.get("EntityType") != "Column":
            continue

        own_entity_type = rule.get("EntityType")
        own_entity_id = rule.get("EntityId")
        vc = rule.get("ValidationCriteria", {})
        deps = vc.get("Dependencies", [])

        model_rule_ids = set()
        referenced_entity_ids = set()
        _collect_references(vc.get("Requirement", {}), model_rule_ids, referenced_entity_ids)
        _collect_references(vc.get("Condition", {}), model_rule_ids, referenced_entity_ids)

        for dep_id in deps:
            dep_rule = rules.get(dep_id)
            if dep_rule is None:
                continue
            if dep_rule.get("EntityType") != own_entity_type:
                continue
            if dep_rule.get("EntityId") != own_entity_id:
                continue
            if dep_id not in model_rule_ids and dep_rule.get("EntityId") not in referenced_entity_ids:
                errors.append(
                    f"Rule '{rule_id}': dependency '{dep_id}' (EntityType='{own_entity_type}') "
                    f"not found in Requirement or Condition Items"
                )

    assert not errors, (
        f"{len(errors)} Composite rule(s) with same-EntityType dependencies missing from Items:\n"
        + "\n".join(f"  {e}" for e in sorted(errors))
    )
