"""Tests for tag_sources.py's kind filter, conversion status, and check mode.
Run with: pytest specification/tools/semantic/tests"""

import json
import subprocess
import sys
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from registry import Registry  # noqa: E402
from tag_sources import Tagger, set_front_matter  # noqa: E402
from test_resolve_semantic import ENTRIES  # noqa: E402

SCRIPT = HERE.parent / "tag_sources.py"
COLUMN_FILE = "datasets/cost_and_usage/columns/billedcost.md"
LINE = "ChargeCategory MUST be null for a *charge*.\n"


def convert(text, kinds=None, path=COLUMN_FILE):
    return Tagger(Registry(ENTRIES), path, kinds=kinds).run(text)


def test_all_kinds_by_default():
    assert convert(LINE) == "[ChargeCategory](#col) MUST be null for a [charge](#term).\n"


def test_kinds_limit_what_is_converted():
    assert convert(LINE, ["col"]) == "[ChargeCategory](#col) MUST be null for a *charge*.\n"
    assert convert(LINE, ["term"]) == "ChargeCategory MUST be null for a [charge](#term).\n"


def test_hand_written_links_of_other_kinds_stay():
    text = "See [*charge*](#glossary:charge) and [Charge Category](#datamodel.costandusage.chargecategory).\n"
    assert convert(text, ["col"]) == "See [*charge*](#glossary:charge) and [Charge Category](#col).\n"


def test_set_front_matter_keeps_other_keys():
    text = "---\naliases: [bill]\nsemantic:\n  term: reviewed\n---\n\n# Title\n"
    result = set_front_matter(text, semantic={"col": "mechanical", "term": "reviewed"})
    assert result == "---\naliases: [bill]\nsemantic:\n  col: mechanical\n  term: reviewed\n---\n\n# Title\n"
    assert set_front_matter("# Title\n", semantic={"col": "mechanical"}) == \
        "---\nsemantic:\n  col: mechanical\n---\n\n# Title\n"
    assert set_front_matter("# Title\n") == "# Title\n"


@pytest.fixture
def spec(tmp_path):
    registry = tmp_path / "registry.json"
    registry.write_text(json.dumps(ENTRIES), encoding="utf-8")
    source = tmp_path / COLUMN_FILE
    source.parent.mkdir(parents=True)
    source.write_text("# Billed Cost\n\n" + LINE, encoding="utf-8")
    return tmp_path, registry, source


def tag(spec, *args):
    spec_dir, registry, source = spec
    return subprocess.run([sys.executable, str(SCRIPT), "--registry", str(registry), "--spec-dir", str(spec_dir),
                           *args, str(source)], capture_output=True, text=True)


def test_conversion_records_mechanical_status(spec):
    assert tag(spec, "--kinds", "col").returncode == 0
    assert spec[2].read_text(encoding="utf-8") == (
        "---\nsemantic:\n  col: mechanical\n---\n\n# Billed Cost\n\n"
        "[ChargeCategory](#col) MUST be null for a *charge*.\n")


def test_reviewed_status_is_kept(spec):
    source = spec[2]
    source.write_text("---\nsemantic:\n  col: reviewed\n---\n\n" + source.read_text(encoding="utf-8"),
                      encoding="utf-8")
    tag(spec, "--kinds", "col,term")
    assert source.read_text(encoding="utf-8").startswith(
        "---\nsemantic:\n  col: reviewed\n  term: mechanical\n---\n")


def test_check_passes_after_conversion_and_reports_a_later_plain_reference(spec):
    source = spec[2]
    tag(spec, "--kinds", "col")
    assert tag(spec, "--check").returncode == 0
    source.write_text(source.read_text(encoding="utf-8") + "ChargeCategory is a column.\n", encoding="utf-8")
    result = tag(spec, "--check")
    assert result.returncode == 1
    assert f"{COLUMN_FILE}:9: ERROR FOCUS021" in result.stderr
    assert "[ChargeCategory](#col) is a column." in result.stderr
    # --check changes nothing
    assert source.read_text(encoding="utf-8").endswith("ChargeCategory is a column.\n")


def test_check_ignores_files_without_mechanical_kinds(spec):
    assert tag(spec, "--check").returncode == 0
    spec[2].write_text("---\nsemantic:\n  col: reviewed\n---\n\nChargeCategory\n", encoding="utf-8")
    assert tag(spec, "--check").returncode == 0


def test_unknown_kind_is_rejected(spec):
    result = tag(spec, "--kinds", "column")
    assert result.returncode == 2
    assert "unknown kind" in result.stderr
