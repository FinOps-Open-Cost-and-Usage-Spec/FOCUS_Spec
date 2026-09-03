#!/usr/bin/env python3
"""Run FOCUS Validator against specification example CSV files."""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUMMARY_RE = re.compile(
    r"Total:\s*(?P<total>\d+)\s*\|\s*Pass:\s*(?P<passed>\d+)\s*\|\s*Fail:\s*(?P<failed>\d+)\s*\|\s*Skipped:\s*(?P<skipped>\d+)"
)
FAILURE_RULE_RE = re.compile(r"^- (?P<rule>[A-Za-z0-9-]+): violations=", re.MULTILINE)


@dataclass
class ValidationResult:
    path: Path
    total: int
    passed: int
    failed: int
    skipped: int
    failed_rules: list[str]
    exit_code: int


GROUP_PATTERNS = {
    "commitment_discount_scenarios": "commitment_discount_scenarios/*.csv",
    "commitment_discount_flexibility": "commitment_discount_flexibility/*.csv",
    "saas_simple_agreements": "saas_examples/simple_agreements/*.csv",
    "saas_spend_agreements": "saas_examples/spend_agreements/*.csv",
    "saas_virtual_currency": "saas_examples/virtual_currency_pricing_model_*.csv",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate FOCUS specification example CSVs.")
    parser.add_argument(
        "--group",
        action="append",
        choices=sorted(GROUP_PATTERNS.keys()),
        help="Example group(s) to validate. Defaults to all groups in this script.",
    )
    parser.add_argument(
        "--validate-version",
        default="1.2",
        help="FOCUS version passed to the validator.",
    )
    parser.add_argument(
        "--applicability-criteria",
        default="ALL",
        help="Applicability criteria passed to the validator.",
    )
    parser.add_argument(
        "--filter-rules",
        default=None,
        help="Optional validator rule prefix filter (for example: CommitmentDiscount).",
    )
    parser.add_argument(
        "--allow-failures",
        type=int,
        default=0,
        help="Allowed failures per file before returning non-zero exit code.",
    )
    parser.add_argument(
        "--exclude-rule",
        action="append",
        default=[],
        help="Rule ID to exclude from threshold checks. Repeat for multiple rules.",
    )
    parser.add_argument(
        "--exclude-rules-file",
        default=None,
        help="Optional file containing one Rule ID per line to exclude from threshold checks.",
    )
    return parser.parse_args()


def iter_files(data_dir: Path, groups: Iterable[str]) -> list[Path]:
    files: list[Path] = []
    for group in groups:
        pattern = GROUP_PATTERNS[group]
        files.extend(sorted(data_dir.glob(pattern)))
    return files


def load_excluded_rules(exclude_rule_args: list[str], exclude_rules_file: str | None) -> set[str]:
    excluded_rules = {rule_id.strip() for rule_id in exclude_rule_args if rule_id.strip()}
    if not exclude_rules_file:
        return excluded_rules

    rules_path = Path(exclude_rules_file).resolve()
    if not rules_path.exists():
        raise FileNotFoundError(f"Exclude rules file does not exist: {rules_path}")

    for line in rules_path.read_text(encoding="utf-8").splitlines():
        rule = line.strip()
        if not rule or rule.startswith("#"):
            continue
        excluded_rules.add(rule)
    return excluded_rules


def run_validator(
    focus_spec_root: Path,
    csv_path: Path,
    validate_version: str,
    applicability_criteria: str,
    filter_rules: str | None,
) -> ValidationResult:
    validator_cwd = focus_spec_root / "focus_validator"
    cmd = [
        sys.executable,
        "-m",
        "focus_validator.main",
        "--data-file",
        str(csv_path),
        "--validate-version",
        validate_version,
        "--applicability-criteria",
        applicability_criteria,
    ]
    if filter_rules:
        cmd.extend(["--filter-rules", filter_rules])

    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    process = subprocess.run(
        cmd,
        cwd=validator_cwd,
        text=True,
        capture_output=True,
        encoding="utf-8",
        env=env,
        check=False,
    )
    match = SUMMARY_RE.search(process.stdout)
    if not match:
        raise RuntimeError(
            f"Could not parse validation summary for {csv_path}.\nSTDOUT:\n{process.stdout}\nSTDERR:\n{process.stderr}"
        )
    failed_rules = FAILURE_RULE_RE.findall(process.stdout)

    return ValidationResult(
        path=csv_path,
        total=int(match.group("total")),
        passed=int(match.group("passed")),
        failed=int(match.group("failed")),
        skipped=int(match.group("skipped")),
        failed_rules=failed_rules,
        exit_code=process.returncode,
    )


def main() -> int:
    args = parse_args()
    script_path = Path(__file__).resolve()
    data_dir = script_path.parent
    focus_spec_root = data_dir.parent.parent

    groups = args.group or list(GROUP_PATTERNS.keys())
    files = iter_files(data_dir, groups)
    if not files:
        print("No files found for selected groups.")
        return 1

    excluded_rules = load_excluded_rules(args.exclude_rule, args.exclude_rules_file)

    print(f"Validating {len(files)} file(s)...")
    if excluded_rules:
        print(f"Excluding {len(excluded_rules)} rule(s) from threshold checks: {', '.join(sorted(excluded_rules))}")
    results: list[ValidationResult] = []
    for csv_path in files:
        result = run_validator(
            focus_spec_root=focus_spec_root,
            csv_path=csv_path,
            validate_version=args.validate_version,
            applicability_criteria=args.applicability_criteria,
            filter_rules=args.filter_rules,
        )
        results.append(result)
        excluded_fail_count = sum(1 for rule_id in result.failed_rules if rule_id in excluded_rules)
        adjusted_failures = result.failed - excluded_fail_count
        print(
            f"{csv_path.relative_to(focus_spec_root)} => "
            f"Total: {result.total} | Pass: {result.passed} | Fail: {result.failed} | "
            f"AdjustedFail: {adjusted_failures} | Skipped: {result.skipped}"
        )

    worst_failures = max(
        r.failed - sum(1 for rule_id in r.failed_rules if rule_id in excluded_rules)
        for r in results
    )
    if worst_failures > args.allow_failures:
        print(
            f"\nValidation failed threshold check: worst AdjustedFail={worst_failures}, "
            f"allowed={args.allow_failures}."
        )
        return 2

    print("\nValidation completed within allowed failure threshold.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
