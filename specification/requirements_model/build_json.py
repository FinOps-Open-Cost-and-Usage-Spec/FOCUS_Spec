#!/usr/bin/env python3
import argparse
import json
import os
from json.decoder import JSONDecodeError
from build_helpers import init_logger
import sys
import subprocess
from pathlib import Path

def get_args():
    parser = argparse.ArgumentParser(description='Model JSON Generator.')
    parser.add_argument('--logging-level', type=str, default='INFO', choices={"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}, help='Logging level to use')
    parser.add_argument('--build-only', action='store_true', help='Write out JSON file instead of running the test process')
    parser.add_argument('--version', type=str, default=None, help='Specific version to build (e.g., 1.3). If not specified, all versions will be built.')
    return parser.parse_args()

def build_version(version):
    """Build the model JSON for a specific version."""
    model = {}
    version_dir = os.path.join('releases', version)
    
    if not os.path.exists(version_dir):
        logger.error(f'❌ Version directory not found: {version_dir}')
        return False
    
    files = [
        'model_details.json',
        'applicability_criteria.json',
        'check_functions.json',
        'model_datasets.json'
    ]
    
    for filename in files:
        filepath = os.path.join(version_dir, filename)
        if not os.path.exists(filepath):
            logger.warning(f'⚠️  File not found: {filepath}')
            continue
        with open(filepath, 'rb') as f:
            try:
              details = json.loads(f.read())
            except JSONDecodeError as e:
                logger.error(f'❌ Unable to read {filepath}')
                logger.error(repr(e))
                return False
            model.update(details)

    # Load Model rule files
    model_rules = {}
    rules_dir = os.path.join(version_dir, 'model_rules')

    if os.path.exists(rules_dir):
        for root, _, filenames in os.walk(rules_dir):
            for filename in filenames:
                if filename.endswith('.json'):
                    path = os.path.join(root, filename)
                    with open(path, 'rb') as f:
                        rules = json.loads(f.read())
                        model_rules.update(rules)
    model['ModelRules'] = model_rules

    model_output_file = f"build/model-{model['Details']['ModelVersion']}.json"
    try:
        os.makedirs('build', exist_ok=True)
        with open(model_output_file, 'w', encoding='utf-8') as out_file:
            json.dump(model, out_file, indent=2)
        logger.info(f"✅ {model_output_file} written")
        return True
    except Exception as e:
        logger.error(f"❌ Output of {model_output_file} failed {repr(e)}")
        return False

def build(version=None):
    """Build model JSON for specified version or all versions."""
    if version:
        # Build specific version
        logger.info(f"Building version {version}")
        success = build_version(version)
        if not success:
            exit(1)
    else:
        # Build all versions
        releases_dir = 'releases'
        if not os.path.exists(releases_dir):
            logger.error(f'❌ Releases directory not found: {releases_dir}')
            exit(1)
        
        versions = [d for d in os.listdir(releases_dir) 
                   if os.path.isdir(os.path.join(releases_dir, d)) 
                   and not d.startswith('.') 
                   and not os.path.islink(os.path.join(releases_dir, d))]
        versions.sort()
        
        if not versions:
            logger.error(f'❌ No version directories found in {releases_dir}')
            exit(1)
        
        logger.info(f"Building all versions: {', '.join(versions)}")
        all_success = True
        for ver in versions:
            logger.info(f"\nBuilding version {ver}...")
            if not build_version(ver):
                all_success = False
        
        if not all_success:
            exit(1) 

if __name__ == "__main__":
    args = get_args()
    logger = init_logger(args.logging_level)
    if args.build_only:
        build(args.version)
        sys.exit(0)
    else:
        # Build first, then run tests
        build(args.version)
        tests_dir = Path(__file__).parent / "tests"
        if args.version:
            # Run tests for specific version
            result = subprocess.call(["pytest", str(tests_dir), "-k", args.version])
        else:
            # Run tests for all versions
            result = subprocess.call(["pytest", str(tests_dir)])
        sys.exit(result)
