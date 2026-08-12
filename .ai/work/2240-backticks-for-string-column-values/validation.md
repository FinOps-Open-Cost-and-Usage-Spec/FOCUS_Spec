# Validation

## Current Results

* Quote-classifier regression tests: 16 passed.
* Evidence validation: 960 baseline occurrences have one-to-one review decisions; 520 replacements and 416 residual decisions match fresh scans from the fixed base commit.
* Applied-manifest validation: 520 replacements across 81 Markdown files match the base-to-worktree changes exactly; five contributor-guidance files are separately reviewed allowlist entries.
* Markdown lint delta: the fixed base and current tracked files each have 421 legacy diagnostics, with zero new diagnostic occurrences by file, line, and rule. The new issue working Markdown is clean.
* Requirements-model tests: 180 passed and 44 skipped.
* Clean Linux/amd64 specification build: assembled `spec.md`, generated `spec.html` and the 360-page `spec.pdf`, and passed all 132 specification component tests.
* Whitespace validation: `git -c core.whitespace=cr-at-eol diff --check` passed. The option accounts for the existing CRLF source file `specification/appendix/invoice_and_billing_period_handling.md`.

## Build Environment

The host does not have Pandoc or the repository's Python lint/test dependencies installed. The complete build uses the preserved `tools/Containerfile`, derived from the repository's `pandoc/extra:latest-ubuntu` CI image with the workflow's wkhtmltopdf and Python dependencies. The rebuilt image ID was `6af0d3a53f9430f10cbedaccafa2c0adcaac6d0a0d05d7bd5b7cdf3fc9823eb4`. The Linux/amd64 Podman commands in `README.md` exercise source linting, include validation, code-fence alignment, Pandoc HTML generation, wkhtmltopdf PDF generation, specification component tests, and requirements-model tests.
