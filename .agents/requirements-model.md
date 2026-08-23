# Requirements Model (JSON Validation Rules)

Instructions for working with the machine-readable requirements model used for specification validation.

The `specification/requirements_model/` directory contains a machine-readable representation of spec requirements:

* `model_rules/` - JSON files defining validation rules (organized by attributes/, columns/, datasets/)
* `build_json.py` - Merges all JSON into `build/model-<version>.json`
* `tests/` - 32+ pytest tests validating rule structure and dependencies

**Rule ID Format**: `<ArtifactName>-<Type>-<NumericId>-<Status>`

* Types: C (Column), A (Attribute), D (Dataset)
* Status: M (Mandatory), O (Optional), C (Conditional)
* Example: `ListUnitPrice-C-001-M`

For build and test commands (generating the model JSON, running pytest), see `.agents/build-and-test.md`.
