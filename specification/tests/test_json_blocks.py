"""Validate JSON code blocks in the specification documentation.

Runs as part of the spec build (see the Makefile). Every ```json fenced code
block in a searched directory must contain parsable JSON.

To validate JSON blocks in additional sections, add the directory name to
``JSON_SEARCH_DIRS`` below.
"""

import json
import re
from pathlib import Path

import pytest

SPEC_DIR = Path(__file__).resolve().parent.parent

# Directories (relative to the specification/ root) searched for ```json blocks.
# Append more section names here to extend coverage over time.
JSON_SEARCH_DIRS = [
    SPEC_DIR / "appendix",
    SPEC_DIR / "conditions",
    SPEC_DIR / "datasets",
    SPEC_DIR / "supported_features",
]

# Match fenced ```json blocks whose fences sit at the start of a line, capturing
# the block body. Non-greedy so each block stops at its own closing fence.
_JSON_BLOCK_RE = re.compile(
    r"^```json[^\n]*\n(.*?)^```", re.MULTILINE | re.DOTALL | re.IGNORECASE
)


def _collect_json_blocks():
    """Return (id, json_text) pairs for every ```json block in searched dirs."""
    blocks = []
    md_files = sorted(
        {md for directory in JSON_SEARCH_DIRS for md in directory.rglob("*.md")}
    )
    for md_file in md_files:
        text = md_file.read_text(encoding="utf-8")
        rel = md_file.relative_to(SPEC_DIR)
        for match in _JSON_BLOCK_RE.finditer(text):
            line = text[: match.start()].count("\n") + 1
            blocks.append((f"{rel}:{line}", match.group(1)))
    return blocks


JSON_BLOCKS = _collect_json_blocks()

# Parametrize over discovered blocks; fall back to a single clean skip when the
# searched directories contain no JSON blocks.
_PARAMS = [pytest.param(text, id=block_id) for block_id, text in JSON_BLOCKS] or [
    pytest.param(None, id="no-json-blocks-found")
]


@pytest.mark.parametrize("json_text", _PARAMS)
def test_json_block_is_parsable(json_text):
    """Each ```json block parses as valid JSON."""
    if json_text is None:
        pytest.skip("no ```json blocks found in the searched directories")

    error = None
    try:
        json.loads(json_text)
    except json.JSONDecodeError as exc:
        error = str(exc)

    if error is not None:
        pytest.fail(f"Invalid JSON in block:\n{json_text}\n\n{error}", pytrace=False)
