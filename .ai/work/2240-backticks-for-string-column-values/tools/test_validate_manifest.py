#!/usr/bin/env python3

"""Exercise evidence validation and safe lint-baseline handling."""

import csv
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


VALIDATOR = Path(__file__).resolve().with_name("validate_manifest.py")
LINT_DELTA = Path(__file__).resolve().with_name("lint_markdown_delta.sh")
PATCH_GENERATOR = Path(__file__).resolve().with_name("manifest_to_patch.py")


class ValidateManifestTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.git("init", "-q")
        (self.root / "guidance.md").write_text('"Usage"\nOriginal guidance.\n')
        self.git("add", "guidance.md")
        self.git("-c", "user.name=Test", "-c", "user.email=test@example.com", "commit", "-qm", "baseline")
        self.base = self.git("rev-parse", "HEAD").stdout.strip()
        with (self.root / "manifest.tsv").open("w", newline="") as output:
            writer = csv.DictWriter(output, fieldnames=["file", "line", "column", "value", "replacement"], delimiter="\t")
            writer.writeheader()
            writer.writerow({"file": "guidance.md", "line": "1", "column": "1", "value": "Usage", "replacement": "`Usage`"})

    def git(self, *args):
        return subprocess.run(["git", *args], cwd=self.root, check=True, capture_output=True, text=True)

    def validate(self, allow, additional=None):
        args = [sys.executable, str(VALIDATOR), "--base-ref", self.base]
        if allow:
            args.extend(["--allow-file", "guidance.md"])
        if additional:
            args.extend(["--additional-manifest", additional])
        return subprocess.run([*args, "manifest.tsv"], cwd=self.root, capture_output=True, text=True)

    def test_allowlisted_file_accepts_other_reviewed_edits(self):
        (self.root / "guidance.md").write_text("`Usage`\nUpdated guidance.\n")
        self.assertEqual(self.validate(allow=True).returncode, 0)
        self.assertNotEqual(self.validate(allow=False).returncode, 0)

    def test_allowlisted_file_still_checks_recorded_replacement(self):
        (self.root / "guidance.md").write_text("`Tax`\nUpdated guidance.\n")
        result = self.validate(allow=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Worktree line does not match manifest", result.stderr)

    def test_allowlisted_file_rejects_missing_recorded_line(self):
        (self.root / "guidance.md").write_text("")
        self.assertNotEqual(self.validate(allow=True).returncode, 0)

    def test_additional_manifest_is_checked_against_worktree(self):
        (self.root / "additional.tsv").write_text((self.root / "manifest.tsv").read_text())
        (self.root / "manifest.tsv").write_text("file\tline\tcolumn\tvalue\treplacement\n")
        (self.root / "guidance.md").write_text("`Usage`\nOriginal guidance.\n")
        self.assertEqual(self.validate(allow=False, additional="additional.tsv").returncode, 0)
        (self.root / "guidance.md").write_text("`Tax`\nOriginal guidance.\n")
        self.assertNotEqual(self.validate(allow=False, additional="additional.tsv").returncode, 0)

    def test_lint_comparison_preserves_existing_baseline_directory(self):
        baseline = self.root / ".ai/work/2240-backticks-for-string-column-values/.lint-base"
        baseline.mkdir(parents=True)
        sentinel = baseline / "keep.txt"
        sentinel.write_text("Keep this file.\n")
        result = subprocess.run(["bash", str(LINT_DELTA), self.base], cwd=self.root, capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertTrue(sentinel.is_file())

    def test_patch_preview_uses_recorded_wildcard_replacement(self):
        (self.root / "wildcard.md").write_text('The value is "*".\n')
        self.git("add", "wildcard.md")
        self.git("-c", "user.name=Test", "-c", "user.email=test@example.com", "commit", "-qm", "wildcard baseline")
        base = self.git("rev-parse", "HEAD").stdout.strip()
        with (self.root / "wildcard.tsv").open("w", newline="") as output:
            writer = csv.DictWriter(output, fieldnames=["file", "line", "column", "value", "replacement", "decision"], delimiter="\t")
            writer.writeheader()
            writer.writerow({"file": "wildcard.md", "line": "1", "column": "14", "value": "*", "replacement": '`"*"`', "decision": "apply_repo_review"})
        result = subprocess.run([sys.executable, str(PATCH_GENERATOR), "--source-ref", base, "wildcard.tsv", "wildcard.md"], cwd=self.root, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('+The value is `"*"`.', result.stdout)


if __name__ == "__main__":
    unittest.main()
