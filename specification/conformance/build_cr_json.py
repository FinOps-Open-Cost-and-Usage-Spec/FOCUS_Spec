#!/usr/bin/env python3
import argparse
import json
import os
from json.decoder import JSONDecodeError
from jsonschema import Draft7Validator
from jsonschema.exceptions import ValidationError, SchemaError 
from build_helpers import init_logger
import sys
import subprocess
from pathlib import Path

def get_args():
    parser = argparse.ArgumentParser(description='CR JSON Generator.')
    parser.add_argument('--logging-level', type=str, default='INFO', choices={"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}, help='Logging level to use')
    parser.add_argument('--build-only', action='store_true', help='Write out JSON file instead of running the test process')
    return parser.parse_args()

def build():
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

    cr_output_file = f"build/cr-{cr['Details']['CRVersion']}.json"
    try:
        with open(cr_output_file, 'w', encoding='utf-8') as out_file:
            json.dump(cr, out_file, indent=2)
        logger.info(f"✅ {cr_output_file} written")
    except Exception as e:
        logger.error(f"❌ Output of {cr_output_file} failed {repr(e)}")
        exit(1) 

if __name__ == "__main__":
    args = get_args()
    logger = init_logger(args.logging_level)
    if args.build_only:
        build()
        sys.exit(0)
    else:
        tests_dir = Path(__file__).parent / "tests"
        sys.exit(subprocess.call(["pytest", str(tests_dir)]))
