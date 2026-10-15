# AGENTS.md

This file provides guidance to AI coding assistants when working with this repository.

## Project Overview

This is the FinOps Open Cost and Usage Specification (FOCUS) repository - a technical specification for standardizing cloud, SaaS, and billing data schemas. The repository contains both human-readable specification documents (Markdown to HTML/PDF) and machine-readable validation rules (JSON).

FOCUS defines datasets for billing data from cloud providers (AWS, Azure, GCP), SaaS vendors, and on-premises systems. The primary dataset is **Cost and Usage**, which can be joined with the supplemental **Contract Commitment** dataset. Key concepts include account hierarchies (billing accounts, sub-accounts, resources) and service hierarchies (categories, names, SKUs). For detailed schema information, read the specification files in `specification/`.

## Build Commands

### Build the Specification (from `specification/` directory)

```bash
cd specification
make                          # Builds spec.md, spec.html, spec.pdf
make STYLE=working_draft      # Build as working draft (default)
make STYLE=main               # Build as publication version
make STYLE=candidate_release  # Build as candidate release
make clean                    # Clean generated files
```

### Build Requirements Model JSON

```bash
cd specification/requirements_model
./build_json.py --build-only  # Generate model JSON only
./build_json.py               # Run tests then generate JSON
```

### Run Tests

```bash
cd specification/requirements_model
pytest tests/                 # Run all requirements model tests
pytest tests/test_schema.py   # Run a single test file
```

### Lint Markdown

Linting is automatically run as part of `make`. The build will stop if the linter detects issues and will not create the spec.md, spec.html, or spec.pdf files.

To force the build to continue despite linter errors (useful for previewing changes or CI/CD), use:

```bash
make force=1
```

To lint individual files:

```bash
cd specification
python3 enhanced_markdown_lint.py --config markdownlnt.cfg scan <file.md>
```

Note: The enhanced linter provides contextual error messages showing actual vs expected values.

## Architecture

### Document Build Pipeline

1. **Source files**: `*.md` and `*.mdpp` files in `specification/` subdirectories
2. **pymarkdownlnt**: Lints the source markdown files (the build stops on errors unless `make force=1`)
3. **validate_includes.py**: Ensures all `.md` files in each directory are included in corresponding `.mdpp` templates
4. **Code fence check**: Warns about code block markers (` ``` `) that are not aligned to the start of the line
5. **markdown-pp**: Processes `spec.mdpp` template, resolving `!INCLUDE` directives to assemble `spec.md`
6. **pymarkdownlnt**: Lints the assembled `spec.md`
7. **Pandoc**: Converts assembled markdown to HTML with custom filters
8. **wkhtmltopdf**: Generates PDF from HTML
9. **pytest**: Validates specification components and build outputs (`specification/tests/`)

* **Anchors:** MarkdownPP generates `<a name="">` anchors for headings when assembling `spec.md` (see [MarkdownPP Guidelines](guidelines/contributors/markdownpp-guidelines.md)), so source files do not need them. DO NOT flag missing HTML `<a name="">` tags.

### Specification Structure

* `specification/spec.mdpp` - Main template that includes all sections
* `specification/datasets/` - Supported datasets
* `specification/datasets/{dataset}/columns/` - Column definitions per dataset
* `specification/attributes/` - Rules that govern datasets, rows, columns, and values
* `specification/metadata/` - Dataset metadata schemas
* `specification/supported_features/` - Catalog of FinOps capabilities enabled by FOCUS datasets
* `specification/operating_model_conditions/` - Operating model conditions
* `specification/schemas/` - Machine-readable JSON Schema definitions for JSON-formatted columns
* `specification/data/` - Example data files used by appendix examples
* `specification/appendix/` - Examples and supplementary content
* `supporting_content/` - Background info from spec development

### Requirements Model (JSON Validation Rules)

`specification/requirements_model/` contains a machine-readable representation of spec requirements. See:

* [Requirements Model README](specification/requirements_model/README.md) for structure, build, and tests
* [Writing Requirements Model Guidelines](guidelines/contributors/writing-requirements-model-guidelines.md) for rule properties and RMId naming

## Writing Specification Content & Review Guidelines

AI agents generating or reviewing content MUST act as strict technical editors enforcing the FOCUS standards. Focus entirely on specification documents, schema definitions, and markdown formatting.

The contributor guidelines in [`guidelines/contributors/`](guidelines/contributors/) are the source of truth, including the [Editorial Guidelines](guidelines/contributors/editorial-guidelines.md), [Normative Requirements Guidelines](guidelines/contributors/normative-requirements-guidelines.md), [MarkdownPP Guidelines](guidelines/contributors/markdownpp-guidelines.md), and [AI Usage Guidelines](guidelines/contributors/ai-usage-guidelines.md). Use them for keywords, requirement structure, terminology, linking, lists, notes, and formatting. When this file and a guideline disagree, the guideline wins. Use [`specification/glossary.md`](specification/glossary.md) for FOCUS terminology and `.ai/memory/` for saved context across sessions.

### Validation & Schema Accuracy

* **Mathematical & Schema Accuracy:** AI reviewers MUST rigorously calculate, parse, and verify all data within examples (especially JSON snippets and tables). Flag any mathematical inconsistencies or hallucinated data. Verify that JSON is structurally valid.

### File Organization

* Each section has a `.mdpp` template that includes individual `.md` files
* All `.md` files in a directory must be included in the corresponding `.mdpp`
* Code blocks must be aligned to start of line (not indented)

### Review Conduct

* **Suggestion-first feedback:** When a concrete fix exists, post it as a GitHub `suggestion` block so the author can accept with one click. Use plain-text comments only when the feedback requires discussion rather than a specific replacement.
* **Self-contained comments:** Every review comment or suggestion MUST include all context needed for the author to evaluate it independently. Do not reference other comments (e.g., "same as above" or "see my comment on line X").
* **Diff-scope discipline:** Only flag issues on lines changed or added by the PR. Pre-existing problems are out of scope unless they create a direct inconsistency with new content in the same PR.
* **Deduplication:** If your tooling can read PR threads, do not flag already-raised issues or post competing suggestions. To add details, reply to the existing thread.
* **Guideline-permitted content:** Do not flag content that a guideline explicitly permits. When flagging an issue, cite the specific guideline section that supports it.

### Issue and Pull Request Templates

GitHub does not auto-apply templates when issues or PRs are created via API. AI agents MUST include the required template content in the body.

#### Pull Requests

PR bodies MUST complete `.github/pull_request_template.md`, including the summary, "Type of Change", and "Author Checklist" (with [AI Usage Guidelines](guidelines/contributors/ai-usage-guidelines.md) attestation).

#### Issues

Issue templates are `.yml` form definitions in `.github/ISSUE_TEMPLATE/`. Use the correct title prefix and fill all fields marked required in the template.

| Type            | Title Prefix     | Template              |
| --------------- | ---------------- | --------------------- |
| Action Item     | `[AI] `          | `action-item.yml`     |
| Feature Request | `[FR] `          | `feature-request.yml` |
| Feedback        | `[Feedback] `    | `feedback.yml`        |
| Maintenance     | `[Maintenance] ` | `maintenance.yml`     |
| Work Item       | `[WI]`           | `work-item.yml`       |

## Context Files

### Working Files

Per-issue working files are stored in `.ai/work/<issue-number>-<kebab-case-name>/`:

* `research.md` - Investigation findings and synthesized issue requirements
* `plan.md` - Implementation approach
* `tasks.md` - Execution tracking

**Naming convention**: Use `<issue-number>-<kebab-case-name>` matching your branch name (e.g., branch `1805-ai-usage-policy` → folder `.ai/work/1805-ai-usage-policy/`).

Fetch issue details from GitHub (`gh issue view`) rather than saving locally. Summarize relevant requirements into research.md.

These files are committed during active work. After the PR is approved but before merging, delete the working folder. This is a manual step - do not delete working files until final approval is received. Valuable research should be moved to `supporting_content/` before approval.

### Memory Files

Persistent learnings are stored in `.ai/memory/` and are not deleted.

## Dependencies

**Python packages**: See [`requirements.txt`](requirements.txt) (and [`specification/requirements_model/requirements.txt`](specification/requirements_model/requirements.txt) for the requirements model).

**System tools**:

* Pandoc (markdown processing)
* wkhtmltopdf (PDF generation)
* GNU Make

## AI Usage Policy

AI-assisted contributions are permitted and follow the same review standards as human-authored content. See [AI Usage Guidelines](guidelines/contributors/ai-usage-guidelines.md) for details.
