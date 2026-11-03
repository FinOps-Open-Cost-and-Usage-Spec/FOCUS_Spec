"""
The top-level Conditions registry and the Condition (CON-) model rules must stay
in sync. Every registry entry must link to an existing Condition root rule whose
EntityId matches the registry key, and every Condition -000- root rule must be
registered.

Applies to model version 1.5 and later (the Conditions registry was introduced in 1.5).
"""
import pytest
from conftest import requires_version, get_conditions_catalog


@pytest.mark.dependency(name="conditions_registry_consistent_1_5_plus", scope="session")
def test_conditions_registry_consistent(cr_json, model_version):
    should_skip, reason = requires_version(model_version, min_version="1.5")
    if should_skip:
        pytest.skip(reason)

    registry = get_conditions_catalog(cr_json, model_version)
    rules = cr_json.get("ModelRules") or {}
    errors = []

    # Forward: every registry entry resolves to an existing Condition root rule
    # whose EntityId equals the registry key.
    for eid, entry in registry.items():
        rule_id = (entry or {}).get("ModelRuleId")
        if not rule_id:
            errors.append(f"Registry entry '{eid}' is missing ModelRuleId")
            continue
        rule = rules.get(rule_id)
        if rule is None:
            errors.append(f"Registry entry '{eid}' ModelRuleId '{rule_id}' does not resolve to a model rule")
            continue
        if rule.get("EntityType") != "Condition":
            errors.append(
                f"Registry entry '{eid}' ModelRuleId '{rule_id}' is EntityType "
                f"'{rule.get('EntityType')}', expected 'Condition'"
            )
        if rule.get("EntityId") != eid:
            errors.append(
                f"Registry key '{eid}' does not match rule EntityId "
                f"'{rule.get('EntityId')}' for '{rule_id}'"
            )

    # Reverse: every Condition -000- root rule is registered with a matching ModelRuleId.
    for rid, rule in rules.items():
        if rule.get("EntityType") != "Condition" or "-000-" not in rid:
            continue
        eid = rule.get("EntityId")
        entry = registry.get(eid)
        if entry is None:
            errors.append(f"Condition root rule '{rid}' (EntityId '{eid}') is not in the Conditions registry")
        elif entry.get("ModelRuleId") != rid:
            errors.append(
                f"Condition root rule '{rid}' is registered as "
                f"'{entry.get('ModelRuleId')}' instead of itself"
            )

    assert not errors, "Conditions registry inconsistencies:\n" + "\n".join(f"- {e}" for e in errors)
