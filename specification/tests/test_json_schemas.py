"""Validate the JSON Schema files under schemas/.

Runs as part of the spec build (see the Makefile). Each .json file under
schemas/ must be parseable JSON and a valid JSON Schema document for its
declared dialect.
"""

import json
from pathlib import Path

import pytest
from jsonschema.exceptions import SchemaError
from jsonschema.validators import validator_for

# schemas/ lives alongside tests/ under the specification/ directory.
SCHEMAS_DIR = Path(__file__).resolve().parent.parent / "schemas"

SCHEMA_FILES = sorted(SCHEMAS_DIR.rglob("*.json"))


def test_schema_files_found():
    """At least one JSON Schema file exists to validate."""
    assert SCHEMA_FILES, f"No .json files found under {SCHEMAS_DIR}"


@pytest.mark.parametrize(
    "schema_path",
    SCHEMA_FILES,
    ids=[str(p.relative_to(SCHEMAS_DIR)) for p in SCHEMA_FILES],
)
def test_json_schema_is_valid(schema_path):
    """Each .json file is valid JSON and a valid JSON Schema document."""
    error = None
    with schema_path.open(encoding="utf-8") as f:
        try:
            schema = json.load(f)
        except json.JSONDecodeError as exc:
            error = f"{schema_path} is not valid JSON: {exc}"
    if error is not None:
        pytest.fail(error, pytrace=False)

    # Select the validator class for the schema's declared $schema dialect
    # (falls back to the latest draft when $schema is absent).
    validator_cls = validator_for(schema)
    try:
        validator_cls.check_schema(schema)
    except SchemaError as exc:
        error = f"{schema_path} is not a valid JSON Schema: {exc.message}"
    if error is not None:
        pytest.fail(error, pytrace=False)
