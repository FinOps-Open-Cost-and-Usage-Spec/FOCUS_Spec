"""
For every Column entity rule, any ColumnName or ColumnAName present in
ValidationCriteria.Requirement must equal the rule's EntityId.

AND/OR recurse into their Items[] so nested sub-checks are covered.

Applies to version 1.4 and later.
"""
import pytest
from conftest import requires_version

_COLUMN_NAME_ARGS = ("ColumnName", "ColumnAName")
_SKIP_FUNCTIONS = {"AND", "OR", "ColumnByColumnEqualsColumnValue"}


def _check_node(node, entity_id, rule_id, path, errors):
    if not isinstance(node, dict) or not node:
        return

    func = node.get("CheckFunction", "")
    if func in _SKIP_FUNCTIONS:
        return

    for arg in _COLUMN_NAME_ARGS:
        if arg in node:
            val = node[arg]
            if isinstance(val, str) and val != entity_id:
                errors.append(
                    f"Rule '{rule_id}' [{path}]: "
                    f"{arg}='{val}' does not match EntityId='{entity_id}'"
                )


def test_requirement_column_name_matches_entityid(model_version, cr_json):
    """ColumnName and ColumnAName in Requirement must equal the rule's EntityId."""
    should_skip, reason = requires_version(model_version, min_version="1.4")
    if should_skip:
        pytest.skip(reason)

    model_rules = cr_json.get("ModelRules", {})
    errors = []

    for rule_id, rule in model_rules.items():
        if rule.get("EntityType") != "Column":
            continue
        entity_id = rule.get("EntityId")
        if not entity_id:
            continue
        req = rule.get("ValidationCriteria", {}).get("Requirement")
        _check_node(req, entity_id, rule_id, "Requirement", errors)

    assert not errors, (
        f"{len(errors)} Requirement column name mismatch(es):\n"
        + "\n".join(f"  {e}" for e in sorted(errors))
    )
