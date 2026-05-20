"""
Verify that every CheckFunction invocation in ValidationCriteria.Requirement
and ValidationCriteria.Condition supplies all Arguments declared in the
version's check_functions.json.

AND/OR are handled by recursing into their Items[] array.
"""
import json
import pytest


def _validate_node(node, check_functions, rule_id, path, errors):
    """
    Validate a single CheckFunction invocation.  Recurses into Items[] for
    AND/OR so nested sub-checks are validated too.
    """
    if not isinstance(node, dict) or not node:
        return

    func_name = node.get("CheckFunction")
    if not func_name:
        return

    func_def = check_functions.get(func_name)
    if func_def is None:
        # Unknown function reference - already caught by test_all_checkfunction_refs_exist
        return

    for arg in func_def.get("Arguments", []):
        if arg not in node:
            errors.append(
                f"Rule '{rule_id}' [{path}]: "
                f"CheckFunction='{func_name}' missing required argument '{arg}'"
            )

    if func_name in ("AND", "OR"):
        for i, item in enumerate(node.get("Items", [])):
            _validate_node(
                item, check_functions, rule_id, f"{path}.Items[{i}]", errors
            )


def test_checkfunction_required_args_present(version_dir, cr_json):
    """All Arguments for each CheckFunction invocation must be present."""
    cf_path = version_dir / "check_functions.json"
    with open(cf_path, encoding="utf-8") as f:
        check_functions = json.load(f).get("CheckFunctions", {})

    model_rules = cr_json.get("ModelRules", {})
    errors = []

    for rule_id, rule in model_rules.items():
        vc = rule.get("ValidationCriteria", {})
        for field in ("Requirement", "Condition"):
            node = vc.get(field)
            _validate_node(
                node, check_functions, rule_id,
                f"ValidationCriteria.{field}", errors
            )

    assert not errors, (
        f"{len(errors)} CheckFunction invocation(s) with missing Arguments:\n"
        + "\n".join(f"  {e}" for e in sorted(errors))
    )
