"""
EntityName must use "ID" (uppercase) not "Id" as a standalone word.

Applies to version 1.4 and later.
"""
import re
import pytest
from conftest import requires_version

_ID_PATTERN = re.compile(r'\bId\b')


def test_entityname_id_casing(model_version, cr_json):
    """EntityName must not contain 'Id' as a standalone word -- use 'ID'."""
    should_skip, reason = requires_version(model_version, min_version="1.4")
    if should_skip:
        pytest.skip(reason)

    errors = []
    for rule_id, rule in cr_json.get("ModelRules", {}).items():
        name = rule.get("EntityName", "")
        if _ID_PATTERN.search(name):
            errors.append(f"Rule '{rule_id}': EntityName={name!r} contains 'Id' (use 'ID')")

    assert not errors, (
        f"{len(errors)} rule(s) with incorrect 'Id' casing in EntityName:\n"
        + "\n".join(f"  {e}" for e in sorted(errors))
    )
