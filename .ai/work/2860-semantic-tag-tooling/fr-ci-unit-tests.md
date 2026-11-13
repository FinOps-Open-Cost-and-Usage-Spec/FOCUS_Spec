# [FR] Run unit tests for the repository's Python tooling in CI

## Requester Information

### Problem Statement

The specification is built and checked by Python scripts in this repository, but CI does not test the scripts themselves. On every push, the `gen_pdf` job in `working_draft.yml` and `main.yml` runs `make`, which runs `specification/tests/`, and `build_json.py`, which runs `specification/requirements_model/tests/`. Both suites check content (the built specification and the Requirements Model JSON). None of their tests imports a repository script.

The scripts that build and check the specification have no tests in CI:

* `custom_linter_rules/rule_md_990.py` and `rule_md_991.py`. `custom_linter_rules/tests/test_title_case.py` tests `rule_md_991` but prints its results instead of asserting, and runs only by hand.
* `specification/enhanced_markdown_lint.py`, `specification/validate_includes.py`, and `specification/requirements_model/build_json.py`, `build_helpers.py`, and `build_dag.py`, which have no tests.
* The semantic tag tools that AI #2860 adds under `specification/tools/semantic/`, which come with a pytest suite (48 tests) that runs locally only.

A change to one of these scripts can therefore pass CI while changing how the specification is linted, assembled, or checked. A reviewer has to run the tests by hand, when they exist, to find out.

### Use Case / User Story

**As a** contributor who changes the repository's build or check scripts
**I need** the unit tests for those scripts to run in CI
**So that** a change that breaks a script is reported in the pull request that makes it, instead of when a later build behaves differently

### Success Criteria

* A pull request that changes a Python script used to build or check the specification runs that script's unit tests in CI, and a failing test fails the check.
* The repository states where unit tests for its tooling live and how they are named, so new scripts follow one pattern.
* Unit tests for tooling run separately from the content checks, so a failure says whether a script or the specification content is at fault.
* The existing content checks (`specification/tests/` and the Requirements Model suite) keep running as they do today.

### Type of Request

* [ ] Standardization
* [ ] Enhancement
* [ ] Net New
* [ ] Enablement/Supporting Content
* [x] Tech Debt - Addressing technical debt or maintenance items

### Organizations Requesting This Feature

* **Coinbase** - Nice to Have - Catches regressions in the build and check scripts in the pull request that causes them

## Optional Sections

### Data Generator Support (Optional)

Not applicable. This request affects how the repository's tooling is tested, not FOCUS data.

### Supporting Documentation (Optional)

* Related: #2779 (verifiable entity references), whose AI #2860 adds `specification/tools/semantic/` and its tests, run locally for now so CI can be discussed here.
* Current CI: `.github/workflows/working_draft.yml` and `main.yml` (`gen_pdf` job), and `.github/workflows/rm_extraction.yml`.
* Test dependencies: `requirements.txt` already includes `pytest`.

### Proposed Solution / Approach (Optional)

Open for discussion. Questions to settle:

* Where tooling tests live: next to each tool (e.g., `specification/tools/semantic/tests/`, `custom_linter_rules/tests/`), or in one folder.
* Which workflow runs them: a step in the existing `gen_pdf` job, or a separate job that runs only when Python files change.
* Whether `test_title_case.py` is converted to assertions so it can run in CI.

### Additional Context (Optional)

* The repository naming conventions already require `test_*.py` names in snake_case for Python tests.
