#!/usr/bin/env python3
import json
import subprocess
import sys
from pathlib import Path
import pytest


ROOT = Path(__file__).resolve().parents[3]
MODEL_DIR = ROOT / "specification" / "requirements_model"
BUILD_SCRIPT = MODEL_DIR / "build_json.py"
MODEL_DETAILS = MODEL_DIR / "model_details.json"

@pytest.fixture(scope="session")
def cr_json():
    proc = subprocess.run([sys.executable, str(BUILD_SCRIPT), "--build-only"],
                          cwd=MODEL_DIR, capture_output=True, text=True)
    if proc.returncode != 0:
        raise AssertionError(
            f"build_json.py failed (exit {proc.returncode})\n"
            f"STDOUT:\n{proc.stdout}\n\nSTDERR:\n{proc.stderr}"
        )
    with open(MODEL_DETAILS, encoding="utf-8") as f:
        details = json.load(f)
    assert isinstance(details, dict), f"Expected dict, got {type(details)}"
    assert "ModelVersion" in details['Details'], "Missing Details.ModelVersion"
    OUTPUT_JSON = MODEL_DIR / f"build/model-{details['Details']['ModelVersion']}.json"
    with OUTPUT_JSON.open(encoding="utf-8") as f:
        doc = json.load(f)
    assert isinstance(doc, dict), f"Expected dict, got {type(doc)}"
    return doc
