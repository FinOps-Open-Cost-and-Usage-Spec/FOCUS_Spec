#!/usr/bin/env python3

"""Verify that Markdown edits exactly match an issue 2240 decision manifest."""

import argparse
import csv
import subprocess
from collections import defaultdict
from pathlib import Path


def base_text(path, base_ref):
    result = subprocess.run(
        ["git", "show", f"{base_ref}:{path}"],
        check=True,
        stdout=subprocess.PIPE,
    )
    return result.stdout.decode("utf-8").replace("\r\n", "\n")


def main(manifest_path, base_ref, allowed_files, allowed_prefixes):
    with open(manifest_path, newline="", encoding="utf-8") as source:
        records = list(csv.DictReader(source, delimiter="\t"))

    edits = defaultdict(list)
    for record in records:
        edits[record["file"]].append(record)

    changed = subprocess.run(
        ["git", "diff", "--name-only", base_ref, "--", "*.md"],
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    ).stdout.splitlines()
    unexpected = sorted(
        path
        for path in set(changed) - set(edits) - set(allowed_files)
        if not any(path.startswith(prefix) for prefix in allowed_prefixes)
    )
    if unexpected:
        raise RuntimeError(f"Markdown files changed outside manifest: {unexpected}")

    for path_string, file_records in edits.items():
        expected_lines = base_text(path_string, base_ref).splitlines(keepends=True)
        by_line = defaultdict(list)
        for record in file_records:
            by_line[int(record["line"])].append(record)

        for line_number, line_records in by_line.items():
            line = expected_lines[line_number - 1]
            for record in sorted(
                line_records, key=lambda item: int(item["column"]), reverse=True
            ):
                start = int(record["column"]) - 1
                original = f'"{record["value"]}"'
                if line[start : start + len(original)] != original:
                    raise RuntimeError(
                        f"Manifest source mismatch at {path_string}:{line_number}:{start + 1}"
                    )
                line = (
                    line[:start]
                    + record["replacement"]
                    + line[start + len(original) :]
                )
            expected_lines[line_number - 1] = line

        expected = "".join(expected_lines)
        actual = Path(path_string).read_text(encoding="utf-8").replace("\r\n", "\n")
        if actual != expected:
            raise RuntimeError(f"Worktree does not match manifest for {path_string}")

    print(
        f"Validated {len(records)} manifest-only replacements "
        f"across {len(edits)} Markdown files against {base_ref}"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-ref", required=True)
    parser.add_argument("--allow-file", action="append", default=[])
    parser.add_argument("--allow-prefix", action="append", default=[])
    parser.add_argument("manifest")
    arguments = parser.parse_args()
    main(
        arguments.manifest,
        arguments.base_ref,
        arguments.allow_file,
        arguments.allow_prefix,
    )
