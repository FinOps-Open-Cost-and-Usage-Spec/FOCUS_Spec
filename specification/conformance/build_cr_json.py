#!/usr/bin/env python3
import json
from jsonschema import Draft7Validator
import os

cr = {}
files = [
    'cr_details.json',
    'applicability_criteria.json',
    'check_functions.json',
    'conformance_tables.json'
]
for filename in files:
    with open(filename, 'rb') as f:
        details = json.loads(f.read())
        cr.update(details)

# Load conformance rule files
conformance_rules = {}
rules_dir = 'conformance_rules'

for root, _, filenames in os.walk(rules_dir):
    for filename in filenames:
        if filename.endswith('.json'):
            path = os.path.join(root, filename)
            with open(path, 'rb') as f:
                rules = json.loads(f.read())
                conformance_rules.update(rules)
cr['ConformanceRules'] = conformance_rules

cr_output_file = f'cr-{cr['Details']['CRVersion']}.json'
try:
    with open(cr_output_file, 'w', encoding='utf-8') as out_file:
        json.dump(cr, out_file, indent=2)
    print(f"✅ {cr_output_file} written")
except Exception as e:
    print(f"❌ Output of {cr_output_file} failed {repr(e)}")
    exit(1)

# Load schema
with open('cr_schema.json', 'r', encoding='utf-8') as schema_file:
    schema = json.load(schema_file)

# Validate json against the schema and collect all errors
validator = Draft7Validator(schema)
errors = sorted(validator.iter_errors(cr), key=lambda e: e.path)

if errors:
    print("❌ Validation failed with the following issues:")
    for error in errors:
        path = ".".join(str(p) for p in error.path)
        print(f" - [{path}] {error.message}")
    exit(1)
else:
    print(f"✅ {cr_output_file} is valid according to cr_schema.json")
