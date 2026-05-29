import pytest
import re
from conftest import requires_version

def _collect_reference_prefix_violations(cr_json, expect_att_attribute_prefix: bool):
    rules = cr_json.get("ModelRules") or {}
    violations = []

    for rid, rule in rules.items():
        entity_type = rule.get("EntityType")
        ref = rule.get("EntityId")

        if not isinstance(ref, str):
            violations.append((rid, f"<missing or non-str: {ref}>", "Missing or invalid EntityId field"))
            continue

        # Check if rule ID follows the new 3-letter-prefix pattern
        # Pattern: <3-letter-prefix>-<Reference>-<EntityType>-<Number>-<Severity>
        new_pattern_match = re.match(r'^([A-Z]{3})-(.+?)-([CADO])-\d+-[A-Z]$', rid)

        if new_pattern_match:
            # Rule uses new format - validate it properly
            prefix, reference_part, entity_letter = new_pattern_match.groups()

            # For 1.4+, Attribute rules must use ATT-<EntityId>-A-<Number>-<Severity>.
            if expect_att_attribute_prefix and entity_type == "Attribute":
                if prefix != "ATT":
                    violations.append((rid, ref, "Attribute rules must use ATT prefix"))
                    continue
                if entity_letter != "A":
                    violations.append((rid, ref, "Attribute rules must use entity letter 'A'"))
                    continue
                if reference_part != ref:
                    violations.append((rid, ref, f"Expected reference '{reference_part}' to match EntityId field"))
                continue

            # Validate entity type is Dataset, Column, or Object for new format
            if entity_type not in ["Dataset", "Column", "Object"]:
                violations.append((rid, ref, f"{entity_type} rules should not use 3-letter prefix format"))
                continue

            # Special handling for Dataset rules
            if entity_type == "Dataset":
                # For Dataset rules, EntityId can be either the dataset name (main rules)
                # or a column name (column requirement rules)
                # Both patterns are valid for dataset rules
                pass  # No validation needed for Dataset rules
            else:
                # For Column and Object rules, reference part should match EntityId field
                if reference_part != ref:
                    violations.append((rid, ref, f"Expected reference '{reference_part}' to match EntityId field"))

            # Validate entity type letter matches
            expected_letter = "D" if entity_type == "Dataset" else ("C" if entity_type == "Column" else "O")
            if entity_letter != expected_letter:
                violations.append((rid, ref, f"Expected entity letter '{expected_letter}' for {entity_type}, got '{entity_letter}'"))
        else:
            # Rule does not use new format - this is now an error for Dataset/Column/Object rules
            if entity_type in ["Dataset", "Column", "Object"]:
                violations.append((rid, ref, f"{entity_type} rules must use 3-letter prefix format: <PREFIX>-<Reference>-{entity_type[0]}-<Number>-<Severity>"))
            else:
                # For Attribute rules in 1.4+, validate ATT-prefixed format.
                if expect_att_attribute_prefix and entity_type == "Attribute":
                    attribute_pattern = rf'^ATT-{re.escape(ref)}-A-\d+-[A-Z]$'
                    if not re.match(attribute_pattern, rid):
                        violations.append((rid, ref, "Attribute rules must use ATT prefix format: ATT-<EntityId>-A-<Number>-<Severity>"))
                # For non-Dataset/Column rules before 1.4, validate legacy format.
                elif not expect_att_attribute_prefix:
                    if not rid.startswith(ref):
                        violations.append((rid, ref, "Rule ID should start with Reference"))

    return violations


@pytest.mark.dependency(name="reference_matches_rule_key_prefix_for_columns_and_objects_pre_1_4", scope="session")
def test_reference_matches_rule_key_prefix_for_columns_and_objects_pre_1_4(cr_json, model_version):
    # This test applies to version 1.3 only.
    should_skip, reason = requires_version(model_version, min_version="1.3", max_version="1.3")
    if should_skip:
        pytest.skip(reason)

    violations = _collect_reference_prefix_violations(cr_json, expect_att_attribute_prefix=False)

    assert not violations, (
        "ModelRules.EntityId must match the expected pattern in the rule key:\n"
        + "\n".join(f"- Rule {rid}: EntityId='{ref}' - {issue}" for rid, ref, issue in violations)
    )


@pytest.mark.dependency(name="reference_matches_rule_key_prefix_for_columns_and_objects_1_4_plus", scope="session")
def test_reference_matches_rule_key_prefix_for_columns_and_objects_1_4_plus(cr_json, model_version):
    # This test applies to version 1.4 and above.
    should_skip, reason = requires_version(model_version, min_version="1.4")
    if should_skip:
        pytest.skip(reason)

    violations = _collect_reference_prefix_violations(cr_json, expect_att_attribute_prefix=True)

    assert not violations, (
        "ModelRules.EntityId must match the expected pattern in the rule key:\n"
        + "\n".join(f"- Rule {rid}: EntityId='{ref}' - {issue}" for rid, ref, issue in violations)
    )