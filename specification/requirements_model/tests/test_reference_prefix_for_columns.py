import pytest
import re
from conftest import requires_version

@pytest.mark.dependency(name="reference_matches_rule_key_prefix_for_columns", scope="session")
def test_reference_matches_rule_key_prefix_for_columns_and_objects(version, cr_json):
    # EntityId field was introduced in v1.3
    should_skip, reason = requires_version(version, min_version="1.3")
    if should_skip:
        pytest.skip(reason)
    
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

            # Validate entity type is Dataset, Column or Object for new format
            if entity_type not in ["Dataset", "Column", "Object"]:
                violations.append((rid, ref, f"{entity_type} rules should not use 3-letter prefix format"))
                continue

            # Special handling for Dataset rules
            if entity_type == "Dataset":
                # For Dataset rules, Reference can be either the dataset name (main rules)
                # or a column name (column requirement rules)
                # Both patterns are valid for dataset rules
                pass  # No validation needed for Dataset rules
            else:
                # For Column and Object rules, reference part should match Reference field
                if reference_part != ref:
                    violations.append((rid, ref, f"Expected reference '{reference_part}' to match Reference field"))

            # Validate entity type letter matches
            expected_letter = "D" if entity_type == "Dataset" else ("C" if entity_type == "Column" else "O")
            if entity_letter != expected_letter:
                violations.append((rid, ref, f"Expected entity letter '{expected_letter}' for {entity_type}, got '{entity_letter}'"))
        else:
            # Rule does not use new format - this is now an error for Dataset/Column/Object rules
            if entity_type in ["Dataset", "Column", "Object"]:
                violations.append((rid, ref, f"{entity_type} rules must use 3-letter prefix format: <PREFIX>-<Reference>-{entity_type[0]}-<Number>-<Severity>"))
            else:
                # For non-Dataset/Column/Object rules, validate old format
                if not rid.startswith(ref):
                    violations.append((rid, ref, "Rule ID should start with Reference"))

    assert not violations, (
        "ModelRules.EntityId must match the expected pattern in the rule key:\n"
        + "\n".join(f"- Rule {rid}: EntityId='{ref}' - {issue}" for rid, ref, issue in violations)
    )