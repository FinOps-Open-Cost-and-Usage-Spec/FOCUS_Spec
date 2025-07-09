#!/usr/bin/env python3
import json
from jsonschema import Draft7Validator
import os

scr = {}
files = [
    'scr_details.json',
    'preconditions.json',
    'attributes.json',
    'check_functions.json',
    'conformance_tables.json',
    'conformance_rulesets.json',
]
for filename in files:
    with open(filename, 'rb') as f:
        details = json.loads(f.read())
        scr.update(details)

# Load conformance rule files
conformance_rules = []
rules_dir = 'conformance_rules'

for root, _, filenames in os.walk(rules_dir):
    for filename in filenames:
        if filename.endswith('.json'):
            path = os.path.join(root, filename)
            with open(path, 'rb') as f:
                rule = json.loads(f.read())
                conformance_rules.append(rule)
scr['ConformanceRules'] = conformance_rules

try:
    with open('scr.json', 'w', encoding='utf-8') as out_file:
        json.dump(scr, out_file, indent=2)
    print("✅ scr.json written")
except Exception as e:
    print(f"❌ Output of scr.json failed {repr(e)}")
    exit(1)

# Load schema
with open('scr_schema.json', 'r', encoding='utf-8') as schema_file:
    schema = json.load(schema_file)

# Validate scr.json against the schema and collect all errors
validator = Draft7Validator(schema)
errors = sorted(validator.iter_errors(scr), key=lambda e: e.path)

if errors:
    print("❌ Validation failed with the following issues:")
    for error in errors:
        path = ".".join(str(p) for p in error.path)
        print(f" - [{path}] {error.message}")
    exit(1)
else:
    print("✅ scr.json is valid according to scr_schema.json")
