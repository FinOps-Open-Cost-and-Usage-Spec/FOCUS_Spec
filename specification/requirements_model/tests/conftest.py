#!/usr/bin/env python3
import json
import subprocess
import sys
import os
from pathlib import Path
from packaging import version
import pytest


ROOT = Path(__file__).resolve().parents[3]
MODEL_DIR = ROOT / "specification" / "requirements_model"
BUILD_SCRIPT = MODEL_DIR / "build_json.py"
RELEASES_DIR = MODEL_DIR / "releases"
EXTRACTED_ID = "extracted"
# The extraction tool lives outside this repo; its output folder is passed in via
# build_json.py --extract-folder, which forwards it through this environment variable.
EXTRACT_FOLDER_ENV = "FOCUS_EXTRACT_FOLDER"
EXTRACTED_DIR = Path(os.environ[EXTRACT_FOLDER_ENV]).resolve() if os.environ.get(EXTRACT_FOLDER_ENV) else None

def parse_version(ver: str):
    """Parse a version string into a comparable version object."""
    return version.parse(ver)

def requires_version(current_version: str, min_version: str = None, max_version: str = None):
    """
    Check if current_version meets the minimum and/or maximum version requirements.
    
    Args:
        current_version: The version being tested (e.g., "1.2", "1.3")
        min_version: Minimum required version (inclusive). Test skipped if current < min.
        max_version: Maximum allowed version (inclusive). Test skipped if current > max.
    
    Returns:
        tuple: (should_skip: bool, skip_reason: str)
    
    Example:
        should_skip, reason = requires_version(version, min_version="1.3")
        if should_skip:
            pytest.skip(reason)
    """
    current = parse_version(current_version)
    
    if min_version is not None:
        minimum = parse_version(min_version)
        if current < minimum:
            return True, f"Requires version >= {min_version} (current: {current_version})"
    
    if max_version is not None:
        maximum = parse_version(max_version)
        if current > maximum:
            return True, f"Requires version <= {max_version} (current: {current_version})"

    return False, ""

def conditions_key(model_version: str):
    """Return the key used for rule applicability conditions for a given model version.

    Renamed from "ApplicabilityCriteria" to "Conditions" in 1.5. Versions prior to
    1.5 continue to use "ApplicabilityCriteria".
    """
    if parse_version(model_version) >= parse_version("1.5"):
        return "Conditions"
    return "ApplicabilityCriteria"

def get_conditions(rule: dict, model_version: str):
    """Read a rule's applicability conditions using the version-appropriate key.

    Always returns a list (empty when the key is absent or null).
    """
    return rule.get(conditions_key(model_version)) or []

def get_conditions_catalog(cr_json: dict, model_version: str):
    """Read the top-level conditions/applicability-criteria catalog (flag definitions)."""
    return cr_json.get(conditions_key(model_version)) or {}

def get_all_versions():
    """Get all release version directories, excluding symlinks."""
    if not RELEASES_DIR.exists():
        return []
    versions = [d for d in os.listdir(RELEASES_DIR)
                if (RELEASES_DIR / d).is_dir()
                and not d.startswith('.')
                and not (RELEASES_DIR / d).is_symlink()]
    return sorted(versions)

def has_extracted():
    """True when an extraction output tree was supplied and is present."""
    return EXTRACTED_DIR is not None and (EXTRACTED_DIR / "model_details.json").exists()

def get_all_targets():
    """Release versions plus the extracted model, when present.

    The extracted model is parameterized under the id "extracted"; its source tree
    is the folder named by FOCUS_EXTRACT_FOLDER and its build artifact is
    build/extracted-model-<ver>.json.
    """
    targets = get_all_versions()
    if has_extracted():
        targets.append(EXTRACTED_ID)
    return targets

def source_dir_for(version):
    """Source tree for a parameterized target."""
    return EXTRACTED_DIR if version == EXTRACTED_ID else RELEASES_DIR / version

def pytest_generate_tests(metafunc):
    """Parameterize tests to run against all versions."""
    if "version" in metafunc.fixturenames:
        versions = get_all_targets()
        ids = [v if v == EXTRACTED_ID else f"v{v}" for v in versions]
        metafunc.parametrize("version", versions, ids=ids)

@pytest.fixture(scope="session")
def all_cr_jsons():
    """Build all versions and return a dict mapping version to model JSON."""
    builds = [["--build-only"]]
    if has_extracted():
        builds.append(["--extracted-only", "--build-only", "--extract-folder", str(EXTRACTED_DIR)])

    for build_args in builds:
        proc = subprocess.run([sys.executable, str(BUILD_SCRIPT), *build_args],
                              cwd=MODEL_DIR, capture_output=True, text=True)
        if proc.returncode != 0:
            raise AssertionError(
                f"build_json.py {' '.join(build_args)} failed (exit {proc.returncode})\n"
                f"STDOUT:\n{proc.stdout}\n\nSTDERR:\n{proc.stderr}"
            )

    result = {}
    for version in get_all_targets():
        version_dir = source_dir_for(version)
        model_details_path = version_dir / "model_details.json"

        with open(model_details_path, encoding="utf-8") as f:
            details = json.load(f)
        assert isinstance(details, dict), f"Expected dict, got {type(details)}"
        assert "ModelVersion" in details['Details'], f"Missing Details.ModelVersion in {version}"

        prefix = "extracted-model-" if version == EXTRACTED_ID else "model-"
        output_json = MODEL_DIR / f"build/{prefix}{details['Details']['ModelVersion']}.json"
        with output_json.open(encoding="utf-8") as f:
            doc = json.load(f)
        assert isinstance(doc, dict), f"Expected dict, got {type(doc)}"
        result[version] = doc

    return result

@pytest.fixture
def cr_json(version, all_cr_jsons):
    """Get the model JSON for a specific version."""
    return all_cr_jsons[version]

@pytest.fixture
def model_version(cr_json):
    """Extract model version string for version comparisons."""
    return cr_json.get("Details", {}).get("ModelVersion", "0.0")

@pytest.fixture
def version_dir(version):
    """Get the source directory path for a specific target."""
    return source_dir_for(version)
