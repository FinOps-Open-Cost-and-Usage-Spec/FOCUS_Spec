# Plan: #2758 Display Name casing lint rule and automatic lint fixes

Split from #2740. The content fixes are in PR #2757, which must merge first. This branch is stacked on it.

## 1. MD992 rule: `custom_linter_rules/rule_md_992.py`

* Applies only to files under a `columns/` directory.
* Reads the Display Name from the `## Display Name` section, falling back to the `# ` heading.
* A match of the Display Name (ignoring case) is a Display Name reference when:
  * it is the subject of the introduction (first words of the first paragraph, optionally after an article and inside a link);
  * a word after the first is capitalized. All-lowercase concept text, sentence case and acronyms written as in the Display Name are not flagged.
* Skips code blocks and headings.
* Fix mode rewrites the matched text to the Display Name casing. Articles and other words are unchanged.
* Line-based (`next_line`) so the fix can use `set_current_fix_line`.

Tests in `custom_linter_rules/tests/test_display_name_casing.py`:

* Fixtures copied from the real column files with the #2740 errors, plus negative cases and `edge_cases.md`, `acronym_edge_cases.md`.
* `scan` reports each expected error, and `fix` changes only the expected line.

Validation done: across all 127 column files the rule reports only the four #2740 errors. A mutation test (casing broken in every column file) found one false positive (acronyms such as "resource ID"), which is fixed and covered by a test.

## 2. Makefile

* `lint-fix`: runs pymarkdownlnt `fix` on the same files as `lint`, then scans for anything left. pymarkdownlnt `fix` exits with 3 when it changed files. This is the only Makefile change.

## 3. CI: extend `working_draft.yml`

`working_draft.yml` already runs `make` (including lint) on every branch push, and its `gen_pdf` check shows on same-repo PRs. Instead of a new workflow:

* Register `.github/lint-problem-matcher.json` before the build, so lint errors show as annotations on the PR diff.
* Run the MD992 tests after the build (`if: !cancelled()`), since `custom_linter_rules/tests/` did not run in CI before.
* Fork PRs still get no lint check, as today (2 of the last 40 PRs). A separate `pull_request` workflow can be added later if that matters.

Verified in Actions (PR #2757 run before the split): the matcher registers and the MD992 tests pass in the `pandoc/extra` container. Not yet verified: that annotations map container paths to the diff. Test with a throwaway branch containing one deliberate error.

## 4. Pre-commit: `.pre-commit-config.yaml`

* Local hooks: the linter on changed spec `.md` files (fix, then scan; run from `specification/`), and the include check.
* Opt-in with `pre-commit install`. Uses `language: system` (the `make` environment); an isolated hook env failed on a default Python older than 3.10.
* Documented in `markdownpp-guidelines.md` (Troubleshooting), with `make lint-fix`.

## Open follow-ups (not in this PR)

* Write the linked-subject casing convention into `editorial-guidelines.md`.
* Check references to other columns' Display Names.
* Other rule groups from the #2509 review (#2715/#2750, #2528, #2703/#2660, #2608/#2573).
