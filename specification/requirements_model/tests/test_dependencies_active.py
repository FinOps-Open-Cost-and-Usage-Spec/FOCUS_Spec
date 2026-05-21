"""
Every active rule's Dependencies must not point to a Removed rule.

Applies to version 1.2 and later.
"""
import pytest
from conftest import requires_version


def test_dependencies_point_to_active_rules(model_version, cr_json):
    """All dependency rule IDs must reference Active rules."""
    should_skip, reason = requires_version(model_version, min_version="1.2")
    if should_skip:
        pytest.skip(reason)

    rules = cr_json.get("ModelRules") or {}

    errors = []
    for rule_id, rule in rules.items():
        if rule.get("Status") != "Active":
            continue
        deps = (rule.get("ValidationCriteria") or {}).get("Dependencies") or []
        for dep_id in deps:
            if not isinstance(dep_id, str):
                continue
            dep_rule = rules.get(dep_id)
            if dep_rule is None:
                continue  # covered by test_dependencies_exist
            if dep_rule.get("Status") == "Removed":
                errors.append(
                    f"Rule '{rule_id}': dependency '{dep_id}' has Status='{dep_rule.get('Status')}'"
                )

    assert not errors, (
        f"{len(errors)} dependency(ies) point to Removed rules:\n"
        + "\n".join(f"  {e}" for e in sorted(errors))
    )
