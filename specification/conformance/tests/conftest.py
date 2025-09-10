#!/usr/bin/env python3
import json
import subprocess
import sys
from pathlib import Path
import pytest


ROOT = Path(__file__).resolve().parents[3]
CONFORMANCE = ROOT / "specification" / "conformance"
BUILD_SCRIPT = CONFORMANCE / "build_cr_json.py"
CR_DETAILS = CONFORMANCE / "cr_details.json"

@pytest.fixture(scope="session")
def cr_json():
    proc = subprocess.run([sys.executable, str(BUILD_SCRIPT), "--build-only"],
                          cwd=CONFORMANCE, capture_output=True, text=True)
    if proc.returncode != 0:
        raise AssertionError(
            f"build_cr_json.py failed (exit {proc.returncode})\n"
            f"STDOUT:\n{proc.stdout}\n\nSTDERR:\n{proc.stderr}"
        )
    with open(CR_DETAILS, encoding="utf-8") as f:
        details = json.load(f)
    assert isinstance(details, dict), f"Expected dict, got {type(details)}"
    assert "CRVersion" in details['Details'], "Missing Details.CRVersion"
    OUTPUT_JSON = CONFORMANCE / f"cr-{details['Details']['CRVersion']}.json"
    with OUTPUT_JSON.open(encoding="utf-8") as f:
        doc = json.load(f)
    assert isinstance(doc, dict), f"Expected dict, got {type(doc)}"
    return doc
