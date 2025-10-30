import json
from pathlib import Path
from jsonschema import Draft202012Validator
import pytest


# Adjust these if your paths differ
HERE = Path(__file__).resolve().parent
REQUIREMENTS_MODEL = HERE.parent  # .../specification/conformance
SCHEMA_PATH = REQUIREMENTS_MODEL / "model_schema.json"          # your schema file

@pytest.mark.order(1)
@pytest.mark.dependency(name="cr_json_matches_schema", scope="session")
def test_cr_json_matches_schema(cr_json):
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))

    # Precompile validator (catches schema errors early)
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(cr_json), key=lambda e: e.path)
    assert not errors, "\n".join(
        f"- {'/'.join(map(str, e.path)) or '<root>'}: {e.message}"
        for e in errors
    )