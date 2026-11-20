# Plan: #2758 Display Name casing lint rule and automatic lint fixes

Split from #2740. The content fixes are in PR #2757, which must merge first. This branch is stacked on it.

## 1. MD992 rule: `custom_linter_rules/rule_md_992.py`

* Applies only to files under a `columns/` directory.
* Reads the Display Name from the `## Display Name` section, falling back to the `# ` heading.
* Checks only the subject of the introduction: the first words of the first paragraph, optionally after an article and inside a link. When it matches the Display Name ignoring case, it must use the exact casing.
* Fix mode rewrites the subject to the Display Name casing. Articles and other words are unchanged.
* Line-based (`next_line`) so the fix can use `set_current_fix_line`.

Decision (assignee, 2026-10-08): Display Name references elsewhere in the file (e.g., `Sub account Name`) are not checked. An earlier version flagged them when a word after the first was capitalized, but outside the introduction subject the text cannot reliably be told apart from the concept or sentence case, so it risks flagging or rewriting correct text. A future rule could warn without fixing or blocking.

Tests in `custom_linter_rules/tests/test_display_name_casing.py`:

* Fixtures copied from the real column files with the #2740 errors, plus negative cases and `edge_cases.md`. `subaccountname.md` documents that body text is not checked.
* `scan` reports each expected error, and `fix` changes only the expected line.

Validation done: on `working_draft`, across all 127 column files, the rule reports only the three #2740 errors. 126 of 127 introductions open with the Display Name as subject; a mutation test that lowercased each subject was caught and fixed in every file.

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
* A warn-only rule (no fix, not blocking) for miscased Display Names in body text (e.g., `Sub account Name`).
* Check references to other columns' Display Names.
* Other rule groups from the #2509 review (#2715/#2750, #2528, #2703/#2660, #2608/#2573).
