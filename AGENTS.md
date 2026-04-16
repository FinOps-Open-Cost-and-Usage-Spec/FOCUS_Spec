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

```bash
pymarkdownlnt --config specification/markdownlnt.cfg scan <file.md>
```

## Architecture

### Document Build Pipeline

1. **Source files**: `*.md` and `*.mdpp` files in `specification/` subdirectories
2. **markdown-pp**: Processes `spec.mdpp` template, resolving `!INCLUDE` directives to assemble the full spec
3. **validate_includes.py**: Ensures all `.md` files in each directory are included in corresponding `.mdpp` templates
4. **pymarkdownlnt**: Lints all markdown files
5. **Pandoc**: Converts assembled markdown to HTML with custom filters
6. **wkhtmltopdf**: Generates PDF from HTML

### Specification Structure

* `specification/spec.mdpp` - Main template that includes all sections
* `specification/datasets/` - Supported datasets
* `specification/datasets/{dataset}/columns/` - Column definitions per dataset
* `specification/attributes/` - Rules that govern datasets, rows, columns, and values
* `specification/metadata/` - Dataset metadata schemas
* `specification/supported_features/` - Catalog of FinOps capabilities enabled by FOCUS datasets
* `specification/appendix/` - Examples and supplementary content
* `supporting_content/` - Background info from spec development

### Requirements Model (JSON Validation Rules)

The `specification/requirements_model/` directory contains a machine-readable representation of spec requirements:

* `model_rules/` - JSON files defining validation rules (organized by attributes/, columns/, datasets/)
* `build_json.py` - Merges all JSON into `build/model-<version>.json`
* `tests/` - 32+ pytest tests validating rule structure and dependencies

**Rule ID Format**: `<ArtifactName>-<Type>-<NumericId>-<Status>`

* Types: C (Column), A (Attribute), D (Dataset)
* Status: M (Mandatory), O (Optional), C (Conditional)
* Example: `ListUnitPrice-C-001-M`

## Writing Specification Content & Review Guidelines

AI agents generating or reviewing content MUST act as strict technical editors enforcing the FOCUS standards. Focus entirely on specification documents, schema definitions, and markdown formatting. 

### Normative Language & Requirements

* Use BCP-14 keywords: MUST, MUST NOT, SHOULD, SHOULD NOT, MAY (all uppercase).
* DO NOT use: "REQUIRED", "SHALL", "SHALL NOT", "RECOMMENDED", "OPTIONAL"
* **Location:** In spec content, capitalized BCP-14 keywords MUST NOT appear outside "Requirements" sections unless quoted. Do not flag lowercase usage (e.g., "may", "should").
* **Format:** Write normative statements as bullet lists, not lengthy sentences.
* **Single Constraint:** Each normative bullet MUST express exactly one requirement. Do not combine multiple distinct obligations using "and"/"or", though these conjunctions are permitted within conditional clauses and mathematical validations.
* **Conditional Phrasing:** Normative statements with conditions MUST use standard phrasing: "when / if / unless / only when / only if / except when / except if".
* **State vs Behavior:** Normative requirements MUST describe a verifiable state, not an operational behavior. Do not use process-oriented verbs (e.g., *ensure*, *handle*, *support*, *provide*) as the primary constraint, though they MAY appear in conditional clauses.
* **Structural Anchors:** Requirements sections MUST begin with a non-verifiable anchor phrase ending in a colon (e.g., `<Entity> MUST adhere to the following requirements:`).

### Editorial Conventions

* **Column/Attribute IDs:** PascalCase without spaces (e.g., PricingQuantity). Entity IDs SHOULD be used in normative text sections.
* **Column/Attribute Display Names:** Normal text with spaces (e.g., "Pricing Quantity"). These SHOULD be used in introductory or explanatory non-normative text.
* **No Mixing:** Do not mix Entity IDs and Display Names within the same normative requirement.
* **Column values:** Enclosed in double quotes (e.g., `"Usage"`, `"Tax"`).
* **Glossary terms:** Link with `[*term*](#glossary:term)` format.
* **Linking Rule:** Link entity names and Glossary terms ONLY on their first occurrence per source file. Exception: Functional links using different anchor text are exempt.
* **Lists:** All unordered lists MUST use asterisks (`*`), never dashes (`-`) or plus signs (`+`). Nested bullet points MUST use exactly two spaces per level.
* **Notes:** Important notes must use the blockquote format (`> Important Consideration`).
* **Anchors:** Pandoc auto-generates custom heading anchors. DO NOT flag missing HTML `<a name="">` tags.

### Validation & Schema Accuracy

* **Mathematical & Schema Accuracy:** AI reviewers MUST rigorously calculate, parse, and verify all data within examples (especially JSON snippets and tables). Flag any mathematical inconsistencies or hallucinated data.
* **JSON Formatting:** JSON blocks MUST use double quotation marks for keys. Verify that the JSON is structurally valid.
* **Example Disclaimer:** Top-level sections with examples MUST begin with this exact note (skip all subsections): `> Note: The following examples are informative and non-normative. They do not define requirements.`

### File Organization

* Each section has a `.mdpp` template that includes individual `.md` files
* All `.md` files in a directory must be included in the corresponding `.mdpp`
* Code blocks must be aligned to start of line (not indented)

### Review Conduct

* **Suggestion-first feedback:** When a concrete fix exists, post it as a GitHub `suggestion` block so the author can accept with one click. Use plain-text comments only when the feedback requires discussion rather than a specific replacement.
* **Self-contained comments:** Every review comment or suggestion MUST include all context needed for the author to evaluate it independently. Do not reference other comments (e.g., "same as above" or "see my comment on line X").
* **Diff-scope discipline:** Only flag issues on lines changed or added by the PR. Pre-existing problems are out of scope unless they create a direct inconsistency with new content in the same PR.
* **Deduplication:** If your tooling can read PR threads, do not flag already-raised issues or post competing suggestions. To add details, reply to the existing thread.

### Issue and Pull Request Templates

GitHub does not auto-apply templates when issues or PRs are created via API. AI agents MUST include the required template content in the body.

#### Pull Requests

PR bodies MUST complete `.github/pull_request_template.md`, including the summary, "Type of Change", and "Author Checklist" (with [AI Usage Guidelines](guidelines/contributors/ai-usage-guidelines.md) attestation).

#### Issues

Issue templates are `.yml` form definitions in `.github/ISSUE_TEMPLATE/`. Use the correct title prefix and fill all fields marked required in the template.

| Type | Title Prefix | Template |
|---|---|---|
| Action Item | `[AI] ` | `action-item.yml` |
| Feature Request | `[FR] ` | `feature-request.yml` |
| Feedback | `[Feedback] ` | `feedback.yml` |
| Maintenance | `[Maintenance] ` | `maintenance.yml` |
| Work Item | `[WI]` | `work-item.yml` |

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

## Reference Files

* `.ai/memory/` - Saved context and memory across sessions
* `specification/glossary.md` - FOCUS terminology definitions
* `guidelines/` - Development processes and conventions

## Dependencies

**Python packages** (in requirements.txt):

* pymarkdownlnt, panflute, watchdog
* pytest, jsonschema (for requirements model tests)

**System tools**:

* Pandoc (markdown processing)
* wkhtmltopdf (PDF generation)
* GNU Make

## AI Usage Policy

AI-assisted contributions are permitted and follow the same review standards as human-authored content. See [AI Usage Guidelines](guidelines/contributors/ai-usage-guidelines.md) for details.
