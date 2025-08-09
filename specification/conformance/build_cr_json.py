#!/usr/bin/env python3
import argparse
import json
import os
from json.decoder import JSONDecodeError
from jsonschema import Draft7Validator
from jsonschema.exceptions import ValidationError, SchemaError 
from build_helpers import init_logger


def get_args():
    parser = argparse.ArgumentParser(description='CR JSON Generator.')
    parser.add_argument('--logging-level', type=str, default='INFO', choices={"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}, help='Logging level to use')
    parser.add_argument('--write-on-check-failure', action='store_true', help='Write out JSON file even on failure to verify')
    return parser.parse_args()

def validate_check_functions(spec, logger):
    valid_functions = set(spec.get("CheckFunctions", {}).keys())
    errors = []

    def check_function_recurse(obj, path):
        if isinstance(obj, dict):
            if "CheckFunction" in obj:
                fn_name = obj["CheckFunction"]
                if fn_name is not None and fn_name not in valid_functions:
                    errors.append(f"Invalid CheckFunction '{fn_name}' at {path}")
            for key, val in obj.items():
                check_function_recurse(val, f"{path}.{key}")
        elif isinstance(obj, list):
            for idx, item in enumerate(obj):
                check_function_recurse(item, f"{path}[{idx}]")

    for rule_id, rule in spec.get("ConformanceRules", {}).items():
        vc = rule.get("ValidationCriteria", {})
        check_function_recurse(vc.get("Requirement", {}), f"{rule_id}.ValidationCriteria.Requirement")
        check_function_recurse(vc.get("Condition", {}), f"{rule_id}.ValidationCriteria.Condition")

    if errors:
        for err in errors:
            logger.error(f"❌ - {err}")
    else:
        logger.info("✅ All CheckFunctions references are valid.")
    return errors

if __name__ == "__main__":
    args = get_args()
    logger = init_logger(args.logging_level)

    cr = {}
    files = [
        'cr_details.json',
        'applicability_criteria.json',
        'check_functions.json',
        'conformance_datasets.json'
    ]
    for filename in files:
        with open(filename, 'rb') as f:
            try:
              details = json.loads(f.read())
            except JSONDecodeError as e:
                logger.error(f'❌ Unable to read {filename}')
                logger.error(repr(e))
                exit(1)
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

    errors = validate_check_functions(cr, logger)
    if errors and not args.write_on_check_failure:
        logger.warning('Exiting as --write-on-check-failure is not flagged')
        exit(1)
    # Load schema
    with open('cr_schema.json', 'r', encoding='utf-8') as schema_file:
        schema = json.load(schema_file)

    # Validate json against the schema and collect all errors
    try:
      validator = Draft7Validator(schema)
      errors = sorted(validator.iter_errors(cr), key=lambda e: e.path)
    except ValidationError as e:
      logger.error(f'Validation error {repr(e)}')
      exit(1)
    except SchemaError as e:
      logger.error(f'Schema error {repr(e)}')
      exit(1)

    if errors:
        logger.error("❌ Validation failed with the following issues:")
        for error in errors:
            path = ".".join(str(p) for p in error.path)
            logger.error(f" - [{path}] {error.message}")
        if not args.write_on_check_failure:
          logger.warning('Exiting as --write-on-check-failure is not flagged')
          exit(1)

    else:
        logger.info("✅ JSON is valid according to cr_schema.json")

    cr_output_file = f'cr-{cr['Details']['CRVersion']}.json'
    try:
        with open(cr_output_file, 'w', encoding='utf-8') as out_file:
            json.dump(cr, out_file, indent=2)
        logger.info(f"✅ {cr_output_file} written")
    except Exception as e:
        logger.error(f"❌ Output of {cr_output_file} failed {repr(e)}")
        exit(1)
