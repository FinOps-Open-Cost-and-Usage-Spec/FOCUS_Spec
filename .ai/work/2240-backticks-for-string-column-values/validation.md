# Validation

## Interim Branch Update

* Merged `origin/working_draft_interim` at `12770c1` locally, preserving later specification changes while applying the string-value convention to the updated content.
* The original manifests and their fixed-base validators have not been regenerated for the interim branch; their results below are historical and do not validate the current merge.
* The classifier identified candidates in the current tracked Markdown, including new SKU Price, AI billing, and supported-feature material. Reviewed values were converted while JSON, code syntax, prefixes, and ordinary quotations were retained.
* Classifier regression tests: 16 passed.
* Specification component tests: 191 passed.
* Specification source Markdown, the assembled Markdown, and updated audit notes passed linting.
* Specification build completed in separate steps: source lint, include validation and assembly in the Linux container; assembled Markdown lint on the host; HTML and a 459-page PDF generation plus component tests in the container.
* Requirements-model tests: 181 passed and 51 skipped. The container reported unknown pytest marker warnings for dependency and order markers.
* A comparison against the interim branch found that non-guidance Markdown changes are quote-to-backtick edits, including three previously reviewed punctuation adjustments.
* Whitespace validation against the interim branch passed with `core.whitespace=cr-at-eol`.

## Original Results (August 2026)

* Quote-classifier regression tests: 16 passed.
* Evidence validation: 960 baseline occurrences have one-to-one review decisions; 520 replacements and 416 residual decisions match fresh scans from the fixed base commit.
* Applied-manifest validation: 520 replacements across 81 Markdown files match the base-to-worktree changes exactly; five contributor-guidance files are separately reviewed allowlist entries.
* Markdown lint delta: the fixed base and current tracked files each have 421 legacy diagnostics, with zero new diagnostic occurrences by file, line, and rule. The new issue working Markdown is clean.
* Requirements-model tests: 180 passed and 44 skipped.
* Clean Linux/amd64 specification build: assembled `spec.md`, generated `spec.html` and the 360-page `spec.pdf`, and passed all 132 specification component tests.
* Whitespace validation: `git -c core.whitespace=cr-at-eol diff --check` passed. The option accounts for the existing CRLF source file `specification/appendix/invoice_and_billing_period_handling.md`.

## Build Environment

The host does not have Pandoc or the repository's Python lint/test dependencies installed. The complete build uses the preserved `tools/Containerfile`, derived from the repository's `pandoc/extra:latest-ubuntu` CI image with the workflow's wkhtmltopdf and Python dependencies. The rebuilt image ID was `6af0d3a53f9430f10cbedaccafa2c0adcaac6d0a0d05d7bd5b7cdf3fc9823eb4`. The Linux/amd64 Podman commands in `README.md` exercise source linting, include validation, code-fence alignment, Pandoc HTML generation, wkhtmltopdf PDF generation, specification component tests, and requirements-model tests.
