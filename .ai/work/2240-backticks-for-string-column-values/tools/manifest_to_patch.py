#!/usr/bin/env python3

"""Render approved review records as an apply_patch patch without editing files."""

import argparse
import csv
import subprocess
from collections import defaultdict
from pathlib import Path


def replacement(value):
    if value.endswith((",", ".")):
        return f"`{value[:-1]}`{value[-1]}"
    return f"`{value}`"


def source_lines(path, source_ref):
    result = subprocess.run(
        ["git", "show", f"{source_ref}:{path.as_posix()}"],
        check=True,
        stdout=subprocess.PIPE,
    )
    return result.stdout.decode("utf-8").splitlines()


def main(manifest_path, selected_file, source_ref):
    with open(manifest_path, newline="", encoding="utf-8") as source:
        records = [
            record
            for record in csv.DictReader(source, delimiter="\t")
            if record["file"] == selected_file
            and record.get("decision", "").startswith("apply_")
        ]
    if not records:
        raise RuntimeError(f"No approved manifest records for {selected_file}")

    path = Path(selected_file)
    lines = source_lines(path, source_ref)
    by_line = defaultdict(list)
    for record in records:
        by_line[int(record["line"])].append(record)

    print("*** Begin Patch")
    print(f"*** Update File: {path.resolve()}")
    for line_number in sorted(by_line):
        old_line = lines[line_number - 1]
        new_line = old_line
        for record in sorted(
            by_line[line_number], key=lambda item: int(item["column"]), reverse=True
        ):
            start = int(record["column"]) - 1
            original = f'"{record["value"]}"'
            if new_line[start : start + len(original)] != original:
                raise RuntimeError(
                    f"Manifest drift at {selected_file}:{line_number}:{start + 1}"
                )
            new_line = (
                new_line[:start]
                + replacement(record["value"])
                + new_line[start + len(original) :]
            )
        print("@@")
        print(f"-{old_line}")
        print(f"+{new_line}")
    print("*** End Patch")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-ref", required=True)
    parser.add_argument("manifest")
    parser.add_argument("file")
    arguments = parser.parse_args()
    main(arguments.manifest, arguments.file, arguments.source_ref)
