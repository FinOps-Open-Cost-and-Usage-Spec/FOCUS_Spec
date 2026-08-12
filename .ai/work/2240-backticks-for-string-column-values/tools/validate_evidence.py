#!/usr/bin/env python3

"""Validate issue 2240 inventories, decisions, and applied-manifest coverage."""

import argparse
import csv
import sys
from collections import Counter
from pathlib import Path

sys.dont_write_bytecode = True
import quote_audit


SCAN_FIELDS = ["classification", "reason", "file", "line", "column", "value", "context"]
OCCURRENCE_FIELDS = ["file", "line", "column", "value"]
REVIEW_DECISIONS = {
    "apply_audit_fix",
    "apply_existing",
    "apply_repo_review",
    "skip_guidance_reviewed",
    "skip_identifier",
    "skip_json",
    "skip_manual_review",
    "skip_non_string",
    "skip_quoted_requirement",
}


def load(path):
    with path.open(newline="", encoding="utf-8") as source:
        return list(csv.DictReader(source, delimiter="\t"))


def projection(records):
    return [tuple(record[field] for field in SCAN_FIELDS) for record in records]


def occurrences(records):
    return [tuple(record[field] for field in OCCURRENCE_FIELDS) for record in records]


def generated_projection(paths, source_ref=None):
    return [
        tuple(str(record[field]) for field in SCAN_FIELDS)
        for record in quote_audit.scan(paths, source_ref)
    ]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main(work_directory, base_ref):
    evidence = work_directory / "evidence"
    candidate = load(evidence / "candidate_manifest.tsv")
    review = load(evidence / "repository_review_manifest.tsv")
    residual = load(evidence / "residual_manifest.tsv")
    applied = load(evidence / "applied_manifest.tsv")
    tracked_paths = quote_audit.tracked_markdown_paths(base_ref)

    require(
        projection(candidate) == generated_projection(tracked_paths, base_ref),
        "Candidate manifest does not match a fresh base-ref scan",
    )
    require(
        projection(review) == projection(candidate),
        "Repository review does not cover the candidate manifest one-for-one",
    )
    require(
        projection(residual) == generated_projection(tracked_paths),
        "Residual manifest does not match a fresh worktree scan",
    )

    invalid_decisions = sorted(
        {record["decision"] for record in review} - REVIEW_DECISIONS
    )
    require(not invalid_decisions, f"Unknown review decisions: {invalid_decisions}")
    require(
        all(record["decision"] and record["rationale"] for record in review),
        "Every candidate requires a decision and rationale",
    )
    require(
        all(record["decision"].startswith("skip_") and record["rationale"] for record in residual),
        "Every residual occurrence requires an explicit skip decision and rationale",
    )

    reviewed_applies = Counter(
        occurrences([record for record in review if record["decision"].startswith("apply_")])
    )
    manifest_applies = Counter(occurrences(applied))
    require(
        reviewed_applies == manifest_applies,
        "Applied manifest does not exactly match candidate apply decisions",
    )
    print(
        f"Validated {len(candidate)} baseline occurrences, {len(applied)} replacements, "
        f"and {len(residual)} residual decisions against {base_ref}"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-ref", required=True)
    parser.add_argument("work_directory", type=Path)
    arguments = parser.parse_args()
    main(arguments.work_directory, arguments.base_ref)
