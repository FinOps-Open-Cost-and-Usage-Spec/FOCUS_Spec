# Issue 2240 Audit Evidence

> **Note:** The inventories and validation commands below use the interim branch at `12770c1` as the baseline. Historical August 2026 evidence remains available in Git history.

This folder preserves the audit methodology for the repository-wide editorial rewrite. The classifier inventories candidates; it does not decide which quotation marks to replace. Every baseline occurrence has a decision in `evidence/repository_review_manifest.tsv`, every manifest-controlled replacement is recorded in `evidence/applied_manifest.tsv`, and every double-quoted occurrence retained in the worktree has an explicit skip decision in `evidence/residual_manifest.tsv`. Contributor-guidance files that required render-safe HTML or explanatory edits are reviewed separately and explicitly allowlisted by the source validator.

All comparisons use the fixed interim baseline commit `12770c1a7a0b1c84ba5ec24b87eea708bedb9897`. This keeps the workflow valid after changes are staged or committed and prevents generated files such as `specification/spec.md` from entering the inventory.

Run the following commands from the repository root.

## Classifier and Evidence Validation

```bash
issue_base_ref=12770c1a7a0b1c84ba5ec24b87eea708bedb9897
issue_work=.ai/work/2240-backticks-for-string-column-values

python3 "$issue_work/tools/test_quote_audit.py"
python3 "$issue_work/tools/test_validate_manifest.py"
python3 "$issue_work/tools/validate_evidence.py" --base-ref "$issue_base_ref" "$issue_work"
```

`validate_evidence.py` regenerates the base and worktree scans from all Markdown paths tracked at the base commit. It verifies one-to-one candidate decisions, exact applied-decision coverage, and explicit decisions for every residual occurrence.

## Validate Source Changes Against the Applied Manifest

```bash
issue_base_ref=12770c1a7a0b1c84ba5ec24b87eea708bedb9897
issue_work=.ai/work/2240-backticks-for-string-column-values

python3 "$issue_work/tools/validate_manifest.py" \
  --base-ref "$issue_base_ref" \
  --allow-file AGENTS.md \
  --allow-file guidelines/contributors/editorial-guidelines.md \
  --allow-file guidelines/contributors/feature-request-triage-guidelines.md \
  --allow-file guidelines/contributors/normative-requirements-guidelines.md \
  --allow-file guidelines/contributors/writing-requirements-model-guidelines.md \
  --allow-prefix "$issue_work/" \
  "$issue_work/evidence/applied_manifest.tsv"
```

The allowlisted files contain reviewed guidance changes that are not entirely represented by scanner candidates, including fenced Markdown examples. Recorded substitutions in these files are checked line by line; other changes in the allowlisted files require separate review. In particular, the raw HTML table in `guidelines/contributors/editorial-guidelines.md` uses `<code>...</code>` instead of literal Markdown backticks because inline Markdown is not reliably parsed inside raw HTML table blocks. The HTML element renders the same inline-code presentation without exposing backtick characters in the preview; normal Markdown prose continues to use backticks. The working folder contains the audit evidence itself.

## Inspect or Regenerate an Inventory

```bash
issue_base_ref=12770c1a7a0b1c84ba5ec24b87eea708bedb9897
issue_work=.ai/work/2240-backticks-for-string-column-values

python3 "$issue_work/tools/quote_audit.py" \
  --source-ref "$issue_base_ref" \
  --tracked-markdown-ref "$issue_base_ref" > /tmp/issue-2240-candidate.tsv
diff -u "$issue_work/evidence/candidate_manifest.tsv" /tmp/issue-2240-candidate.tsv

python3 "$issue_work/tools/quote_audit.py" \
  --tracked-markdown-ref "$issue_base_ref" > /tmp/issue-2240-residual.tsv
cut -f1-7 "$issue_work/evidence/residual_manifest.tsv" > /tmp/issue-2240-reviewed-residual.tsv
diff -u /tmp/issue-2240-reviewed-residual.tsv /tmp/issue-2240-residual.tsv
```

To prepare an `apply_patch` patch for the approved records in one file without editing it directly:

```bash
python3 "$issue_work/tools/manifest_to_patch.py" \
  --source-ref "$issue_base_ref" \
  "$issue_work/evidence/repository_review_manifest.tsv" \
  supporting_content/datasets/cost_and_usage/columns/pricingcategory.md
```

## Reproduce the Full Build

```bash
issue_work=.ai/work/2240-backticks-for-string-column-values

podman build \
  --platform linux/amd64 \
  --file "$issue_work/tools/Containerfile" \
  --tag localhost/focus-spec-build:2240 .

podman run --rm \
  --platform linux/amd64 \
  --userns keep-id \
  --volume "$PWD:/workspace" \
  --workdir /workspace/specification \
  localhost/focus-spec-build:2240 \
  make STYLE=working_draft

podman run --rm \
  --platform linux/amd64 \
  --userns keep-id \
  --volume "$PWD:/workspace" \
  --workdir /workspace/specification/requirements_model \
  localhost/focus-spec-build:2240 \
  pytest tests/
```

The full build lints specification sources. Other changed repository Markdown contains pre-existing diagnostics, so `lint_markdown_delta.sh` compares diagnostic occurrences by file, line, and rule against the fixed base rather than claiming those files are globally clean. It also requires the new issue working documents to be clean.

```bash
issue_base_ref=12770c1a7a0b1c84ba5ec24b87eea708bedb9897

bash .ai/work/2240-backticks-for-string-column-values/tools/lint_markdown_delta.sh \
  "$issue_base_ref"
```

The baseline inventory contains 1,465 occurrences: 855 recorded replacements and 610 retained occurrences. The applied manifest includes 24 scanner-visible substitutions in contributor guidance; fenced Markdown examples and explanatory guidance changes are reviewed separately. The residual inventory is intentionally reviewed rather than automatically applied. Retained cases include raw JSON, property names and `x_` key prefixes, Boolean literals, format notation, requirement quotations, comparison terminology, and ordinary prose quotations.
