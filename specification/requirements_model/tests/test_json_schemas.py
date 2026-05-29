import pytest
from conftest import requires_version
from jsonschema import Draft202012Validator
from jsonschema.exceptions import SchemaError


def _get_json_schemas(cr_json):
    return cr_json.get("Schemas") or {}


def _walk_nodes(node):
    if isinstance(node, dict):
        yield node
        for value in node.values():
            yield from _walk_nodes(value)
    elif isinstance(node, list):
        for item in node:
            yield from _walk_nodes(item)


@pytest.mark.dependency(name="json_schemas_top_level_key_exists", scope="session")
def test_json_schemas_top_level_key_exists(cr_json, model_version):
    # This test only applies to model version 1.4 and above
    should_skip, reason = requires_version(model_version, min_version="1.4")
    if should_skip:
        pytest.skip(reason)

    assert "Schemas" in cr_json, "Missing top-level key 'Schemas' in build output"


@pytest.mark.dependency(name="json_schemas_are_dereferenced", scope="session")
def test_json_schemas_are_dereferenced(cr_json, model_version):
    # This test only applies to model version 1.4 and above
    should_skip, reason = requires_version(model_version, min_version="1.4")
    if should_skip:
        pytest.skip(reason)

    schemas = _get_json_schemas(cr_json)
    violations = []

    for schema_id, entry in schemas.items():
        schema_value = (entry or {}).get("Schema")
        if isinstance(schema_value, str):
            violations.append(f"{schema_id}: Schema is still a string reference")
        elif not isinstance(schema_value, dict):
            violations.append(f"{schema_id}: Schema is not an object (found {type(schema_value).__name__})")

    assert not violations, "Schemas entries must contain dereferenced Schema objects:\n" + "\n".join(
        f"- {v}" for v in violations
    )


@pytest.mark.dependency(name="json_schemas_valid_json_schema", scope="session")
def test_json_schemas_valid_json_schema(cr_json, model_version):
    # This test only applies to model version 1.4 and above
    should_skip, reason = requires_version(model_version, min_version="1.4")
    if should_skip:
        pytest.skip(reason)

    schemas = _get_json_schemas(cr_json)
    violations = []

    for schema_id, entry in schemas.items():
        schema_value = (entry or {}).get("Schema")
        if not isinstance(schema_value, dict):
            violations.append(f"{schema_id}: Schema is not an object")
            continue
        try:
            Draft202012Validator.check_schema(schema_value)
        except SchemaError as exc:
            violations.append(f"{schema_id}: invalid JSON Schema ({exc.message})")

    assert not violations, "Dereferenced schemas must be valid JSON Schemas:\n" + "\n".join(
        f"- {v}" for v in violations
    )


@pytest.mark.dependency(name="json_schema_id_matches_dataset_type", scope="session")
def test_json_schema_id_matches_dataset_type(cr_json, model_version):
    # This test only applies to model version 1.4 and above
    should_skip, reason = requires_version(model_version, min_version="1.4")
    if should_skip:
        pytest.skip(reason)

    schemas = _get_json_schemas(cr_json)
    violations = []

    for schema_id, entry in schemas.items():
        dataset_type = (entry or {}).get("DatasetType")
        if not isinstance(dataset_type, str) or not dataset_type:
            violations.append(f"{schema_id}: missing/invalid DatasetType")
            continue
        expected_prefix = f"{dataset_type}-"
        if not schema_id.startswith(expected_prefix):
            violations.append(
                f"{schema_id}: expected ID to start with '{expected_prefix}' based on DatasetType"
            )

    assert not violations, "Schemas IDs must start with their DatasetType prefix:\n" + "\n".join(
        f"- {v}" for v in violations
    )


@pytest.mark.dependency(name="json_schema_entity_type_is_schema", scope="session")
def test_json_schema_entity_type_is_schema(cr_json, model_version):
    # This test only applies to model version 1.4 and above
    should_skip, reason = requires_version(model_version, min_version="1.4")
    if should_skip:
        pytest.skip(reason)

    schemas = _get_json_schemas(cr_json)
    violations = []

    for schema_id, entry in schemas.items():
        entity_type = (entry or {}).get("EntityType")
        if entity_type != "Schema":
            violations.append(f"{schema_id}: EntityType is '{entity_type}'")

    assert not violations, "All Schemas entries must have EntityType='Schema':\n" + "\n".join(
        f"- {v}" for v in violations
    )


@pytest.mark.dependency(name="check_json_schema_uses_valid_json_schema_id", scope="session")
def test_check_json_schema_uses_valid_json_schema_id(cr_json, model_version):
    # This test only applies to model version 1.4 and above
    should_skip, reason = requires_version(model_version, min_version="1.4")
    if should_skip:
        pytest.skip(reason)

    schemas = _get_json_schemas(cr_json)
    valid_schema_ids = set(schemas.keys())
    rules = cr_json.get("ModelRules") or {}
    violations = []

    for rule_id, rule in rules.items():
        vc = (rule or {}).get("ValidationCriteria") or {}
        for req_node in _walk_nodes(vc.get("Requirement")):
            if req_node.get("CheckFunction") != "CheckJSONSchema":
                continue

            schema_id = req_node.get("SchemaId")
            if not isinstance(schema_id, str) or not schema_id:
                violations.append(f"{rule_id}: CheckJSONSchema has missing/invalid SchemaId")
                continue
            if schema_id not in valid_schema_ids:
                violations.append(
                    f"{rule_id}: CheckJSONSchema SchemaId '{schema_id}' not found in Schemas"
                )

    assert not violations, "CheckJSONSchema SchemaId values must exist in Schemas:\n" + "\n".join(
        f"- {v}" for v in violations
    )
