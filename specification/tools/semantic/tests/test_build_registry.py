"""Tests for build_registry.py's output options. Run with: pytest specification/tools/semantic/tests"""

import json
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parent.parent / "build_registry.py"

FILES = {
    "datasets/data_model.md": "# Data Model\n",
    # The folder name differs from the dataset ID on purpose, so REG016 is reported
    "datasets/cost_and_usage/dataset.md":
        "# Cost and Usage\n\n## Dataset ID\n\nCostAndUsage\n\n## Display Name\n\nCost and Usage\n",
    "datasets/cost_and_usage/columns/billedcost.md":
        "---\nsemantic:\n  col: mechanical\n---\n\n"
        "# Billed Cost\n\n## Column ID\n\nBilledCost\n\n## Display Name\n\nBilled Cost\n\n"
        "## Content Constraints\n\n| Constraint | Value |\n| :--- | :--- |\n| Dataset | Cost and Usage |\n",
    "attributes/attributes_overview.md": "# Attributes\n",
    "operating_model_conditions/operating_model_conditions_overview.md": "# Operating Model Conditions\n",
    "schemas/schemas.mdpp": "# Schemas\n",
    "glossary.md": '# Glossary\n\n<a name="glossary:charge"><b>Charge</b></a>\n',
}


@pytest.fixture
def spec_dir(tmp_path):
    for path, text in FILES.items():
        (tmp_path / path).parent.mkdir(parents=True, exist_ok=True)
        (tmp_path / path).write_text(text, encoding="utf-8")
    return tmp_path


def build(spec_dir, *args):
    return subprocess.run([sys.executable, str(SCRIPT), "--spec-dir", str(spec_dir), "--rm-release", "none", *args],
                          capture_output=True, text=True)


def test_out_dash_writes_the_registry_to_stdout(spec_dir):
    result = build(spec_dir, "--out", "-")
    assert result.returncode == 0
    entities = json.loads(result.stdout)
    assert {(e["type"], e["id"]) for e in entities} == {("ds", "CostAndUsage"), ("col", "BilledCost"),
                                                        ("term", "charge")}
    assert "Wrote stdout" in result.stderr


def test_out_file_keeps_stdout_for_the_summary(spec_dir, tmp_path):
    out = tmp_path / "registry.json"
    result = build(spec_dir, "--out", str(out))
    assert result.returncode == 0
    assert len(json.loads(out.read_text(encoding="utf-8"))) == 3
    assert result.stdout.startswith(f"Wrote {out}")


def test_semantic_front_matter_is_a_known_key(spec_dir):
    assert "REG011" not in build(spec_dir, "--out", "-").stderr


def test_fail_on_exits_non_zero_only_for_reported_codes(spec_dir):
    assert build(spec_dir, "--out", "-", "--fail-on", "REG016").returncode == 1
    assert build(spec_dir, "--out", "-", "--fail-on", "REG017").returncode == 0
