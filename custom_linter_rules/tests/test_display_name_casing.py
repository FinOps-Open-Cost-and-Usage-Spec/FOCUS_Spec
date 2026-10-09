"""
Tests for MD992 (display-name-casing).

The fixtures in fixtures/md992/columns are copies of real column files, taken
from working_draft when the rule was added, plus edge_cases.md. The errors in
them are the cases from issue #2740.
"""
import shutil
from pathlib import Path

import pytest
from pymarkdown.api import PyMarkdownApi

TESTS_DIR = Path(__file__).parent
RULE_FILE = TESTS_DIR.parent / "rule_md_992.py"
FIXTURES = TESTS_DIR / "fixtures" / "md992"


def detail(failure) -> str:
    """The rule's extra information, without the " [...]" wrapper the API adds."""
    return failure.extra_error_information.strip().removeprefix("[").removesuffix("]")


def scan(path: Path):
    """Scan a file with MD992 and return its MD992 failures."""
    result = (
        PyMarkdownApi()
        .add_plugin_path(str(RULE_FILE))
        .disable_rule_by_identifier("md013")
        .scan_path(str(path))
    )
    return [f for f in result.scan_failures if f.rule_id == "MD992"]


def fix(path: Path, tmp_path: Path) -> str:
    """Fix a copy of a fixture (kept under a columns directory) and return its text."""
    target = tmp_path / "columns" / path.name
    target.parent.mkdir()
    shutil.copy(path, target)
    PyMarkdownApi().add_plugin_path(str(RULE_FILE)).disable_rule_by_identifier(
        "md013"
    ).fix_path(str(target))
    return target.read_text(encoding="utf-8")


@pytest.mark.parametrize(
    "fixture, line, column, actual, expected",
    [
        ("cost_and_usage_billingcurrency.md", 3, 3, "Billing currency", "Billing Currency"),
        ("contract_commitment_billingcurrency.md", 3, 3, "Billing currency", "Billing Currency"),
        ("availabilityzone.md", 3, 6, "availability zone", "Availability Zone"),
        ("subaccountname.md", 3, 92, "Sub account Name", "Sub Account Name"),
    ],
)
def test_reports_issue_2740_cases(fixture, line, column, actual, expected):
    failures = scan(FIXTURES / "columns" / fixture)
    assert [(f.line_number, f.column_number) for f in failures] == [(line, column)]
    assert detail(failures[0]) == (
        f"Actual: '{actual}', Expected: '{expected}'"
    )


@pytest.mark.parametrize(
    "fixture, expected_line",
    [
        ("cost_and_usage_billingcurrency.md", "[*Billing Currency*](#glossary:billing-currency) is an identifier"),
        ("contract_commitment_billingcurrency.md", "[*Billing Currency*](#glossary:billing-currency) is an identifier"),
        ("availabilityzone.md", "An [*Availability Zone*](#glossary:availability-zone) is a host-provider-assigned"),
        ("subaccountname.md", "Sub Account Name is commonly used"),
    ],
)
def test_fixes_issue_2740_cases(fixture, expected_line, tmp_path):
    source = FIXTURES / "columns" / fixture
    original = source.read_text(encoding="utf-8").splitlines()
    fixed = fix(source, tmp_path).splitlines()

    changed = [i for i, (a, b) in enumerate(zip(original, fixed)) if a != b]
    assert len(original) == len(fixed)
    assert changed == [2]
    assert expected_line in fixed[2]
    assert not scan(tmp_path / "columns" / fixture)


@pytest.mark.parametrize(
    "fixture",
    ["invoice_detail_billingcurrency.md", "servicename.md"],
)
def test_correct_files_pass(fixture):
    assert not scan(FIXTURES / "columns" / fixture)


def test_ignores_files_outside_columns_directory():
    assert not scan(FIXTURES / "other" / "billingcurrency.md")


def test_edge_cases():
    """
    Line 3: intro subject after "The", all lowercase, is flagged. The later
            "Billing account name" may be sentence case and is not flagged.
    Line 5: a later word is capitalized, so it is flagged.
    Line 7: a later word is capitalized, so it is flagged.
    Line 10: inside a code block, not flagged.
    Line 24: the Display Name section itself matches.
    """
    failures = scan(FIXTURES / "columns" / "edge_cases.md")
    assert [(f.line_number, detail(f)) for f in failures] == [
        (3, "Actual: 'billing account name', Expected: 'Billing Account Name'"),
        (5, "Actual: 'Billing account Name', Expected: 'Billing Account Name'"),
        (7, "Actual: 'billing Account Name', Expected: 'Billing Account Name'"),
    ]


def test_acronym_edge_cases():
    """
    Line 3: correct intro subject.
    Line 5: "resource ID" keeps the acronym as written, so it is concept text.
    Line 7: "resource Id" miscases the acronym, so it is flagged.
    """
    failures = scan(FIXTURES / "columns" / "acronym_edge_cases.md")
    assert [(f.line_number, detail(f)) for f in failures] == [
        (7, "Actual: 'resource Id', Expected: 'Resource ID'"),
    ]
