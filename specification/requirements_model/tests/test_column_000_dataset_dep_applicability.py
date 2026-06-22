"""
For every -000- Column rule, check that each -D- rule in its Dependencies
carries the same ApplicabilityCriteria as the -000- rule itself.

Applies to version 1.4 and later.
"""
import pytest
from conftest import requires_version


def test_column_000_dataset_dep_applicability_matches(model_version, cr_json):
    should_skip, reason = requires_version(model_version, min_version="1.4")
    if should_skip:
        pytest.skip(reason)

    model_rules = cr_json.get("ModelRules", {})
    errors = []

    for rule_id, rule in model_rules.items():
        if "-000-" not in rule_id or rule.get("EntityType") != "Column":
            continue

        col_ac = sorted(rule.get("ApplicabilityCriteria") or [])
        deps = rule.get("ValidationCriteria", {}).get("Dependencies", [])

        for dep_id in deps:
            if "-D-" not in dep_id:
                continue
            dep_rule = model_rules.get(dep_id)
            if dep_rule is None:
                continue
            dep_ac = sorted(dep_rule.get("ApplicabilityCriteria") or [])
            if col_ac != dep_ac:
                errors.append(
                    f"  {rule_id}  ApplicabilityCriteria={col_ac}\n"
                    f"    -> {dep_id}  ApplicabilityCriteria={dep_ac}"
                )

    assert not errors, (
        f"{len(errors)} -000- Column rule(s) whose -D- dependency has "
        f"mismatched ApplicabilityCriteria:\n" + "\n".join(errors)
    )
