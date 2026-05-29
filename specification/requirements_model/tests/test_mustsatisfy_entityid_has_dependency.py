"""
For every active Column or Object rule, if another active Column or Object
EntityId is mentioned in MustSatisfy, at least one entry in Dependencies must
contain that EntityId.

The rule's own EntityId is excluded from the check (self-references are fine).

Applies to version 1.4 and later.
"""
import re
import pytest
from conftest import requires_version


def test_mustsatisfy_entityid_has_dependency(model_version, cr_json):
    """Every Column/Object EntityId mentioned in MustSatisfy must appear in Dependencies."""
    should_skip, reason = requires_version(model_version, min_version="1.4")
    if should_skip:
        pytest.skip(reason)

    model_rules = cr_json.get("ModelRules", {})

    # Build the set of active Column/Object EntityIds to match against
    active_entity_ids = {
        rule["EntityId"]
        for rule in model_rules.values()
        if rule.get("Status") == "Active"
        and rule.get("EntityId")
        and rule.get("EntityType") in ("Column", "Object")
    }

    # Pre-compile patterns once for performance
    patterns = {eid: re.compile(r'(?<!\.)\b' + re.escape(eid) + r'\b') for eid in active_entity_ids}

    errors = []
    for rule_id, rule in model_rules.items():
        if rule.get("Status") != "Active":
            continue
        if rule.get("EntityType") not in ("Column", "Object"):
            continue

        vc = rule.get("ValidationCriteria", {})
        must_satisfy = vc.get("MustSatisfy", "")
        deps = vc.get("Dependencies", [])
        own_entity_id = rule.get("EntityId", "")

        if not must_satisfy:
            continue

        for eid, pattern in patterns.items():
            if eid == own_entity_id:
                continue
            if pattern.search(must_satisfy):
                if not any(eid in dep for dep in deps):
                    errors.append(
                        f"Column '{own_entity_id}' (Rule '{rule_id}'): "
                        f"MustSatisfy mentions '{eid}' but no Dependency contains it\n"
                        f"    MustSatisfy: {must_satisfy!r}"
                    )

    assert not errors, (
        f"{len(errors)} rule(s) mention a Column/Object EntityId in MustSatisfy "
        f"without a matching Dependency:\n"
        + "\n".join(f"  {e}" for e in sorted(errors))
    )
