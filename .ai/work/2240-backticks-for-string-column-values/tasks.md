# Tasks

## Implementation and Validation

* [x] Review issue 2240 and define the formatting boundary.
* [x] Fix a stable pre-change base commit and generate a repository-wide candidate manifest.
* [x] Record a per-occurrence apply or skip decision for every baseline candidate.
* [x] Apply only approved replacements.
* [x] Update authoring guidance and render-safe examples.
* [x] Verify source changes against the applied manifest.
* [x] Record explicit decisions for every residual double-quoted occurrence.
* [x] Obtain three independent audits of the approach, exclusions, changes, and AI workflow.
* [x] Correct the Markdown-link/JSON classifier defect and add regression tests.
* [x] Expand scope to all Markdown tracked at the stable base commit.
* [x] Preserve reproducible tooling, decisions, and the Linux/amd64 build recipe.
* [x] Correct quote pairing across inline-code spans and add regression coverage.
* [x] Convert the requirements-model prose values identified by the final audit.
* [x] Make patch generation read from the fixed base revision.
* [x] Compare repository-wide Markdown diagnostics with the fixed base and verify no new diagnostics.
* [x] Rerun classifier/evidence validation, requirements-model tests, whitespace validation, and the full build after the final edits.
* [x] Record human scope decisions for metadata, nested wildcard, historical values, key prefixes, and code-like assignments.

## Human and PR Workflow

* [x] Human-review the changed contributor guidance and targeted ambiguous formatting cases.
* [x] Confirm that quoted values inside whole-requirement inline code spans in `normative-requirements-guidelines.md` remain code-format exceptions.
* [ ] Have the CLA-covered contributor complete final self-review and accept responsibility for correctness and quality.
* [ ] Have the CLA-covered contributor verify third-party intellectual-property and AI-tool licensing compatibility.
* [ ] Complete `.github/pull_request_template.md`, including summary, type of change, author checklist, and AI Usage Guidelines attestation.
* [ ] Submit the PR through the responsible human contributor unless the AI agent has completed Linux Foundation CLA onboarding.
* [ ] Obtain Task Force technical review, Working Group strategic review, and standard approval.
* [ ] After PR approval and before merge, preserve any broadly useful research and delete this working folder in a final commit.
