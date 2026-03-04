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

- `specification/spec.mdpp` - Main template that includes all sections
- `specification/datasets/` - Supported datasets
- `specification/datasets/{dataset}/columns/` - Column definitions per dataset
- `specification/attributes/` - Rules that govern datasets, rows, columns, and values
- `specification/metadata/` - Dataset metadata schemas
- `specification/supported_features/` - Catalog of FinOps capabilities enabled by FOCUS datasets
- `specification/appendix/` - Examples and supplementary content
- `supporting_content/` - Background info from spec development

### Requirements Model (JSON Validation Rules)

The `specification/requirements_model/` directory contains a machine-readable representation of spec requirements:

- `model_rules/` - JSON files defining validation rules (organized by attributes/, columns/, datasets/)
- `build_json.py` - Merges all JSON into `build/model-<version>.json`
- `tests/` - 32+ pytest tests validating rule structure and dependencies

**Rule ID Format**: `<ArtifactName>-<Type>-<NumericId>-<Status>`

- Types: C (Column), A (Attribute), D (Dataset)
- Status: M (Mandatory), O (Optional), C (Conditional)
- Example: `ListUnitPrice-C-001-M`

## Writing Specification Content

### Normative Language

- Use BCP-14 keywords: MUST, MUST NOT, SHOULD, SHOULD NOT, MAY (all uppercase)
- "REQUIRED" is deprecated; use MUST instead
- "SHALL" is deprecated; use MUST instead
- "SHALL NOT" is deprecated; use MUST NOT instead
- "RECOMMENDED" is deprecated; use SHOULD instead
- "NOT RECOMMENDED" is deprecated; use SHOULD NOT instead
- "OPTIONAL" is deprecated; use MAY instead
- Write normative statements as bullet lists, not lengthy sentences

### Editorial Conventions

- Column/Attribute IDs: PascalCase without spaces (e.g., `PricingQuantity`)
- Column/Attribute Display Names: Normal text with spaces (e.g., "Pricing Quantity")
- Column values: Enclosed in double quotes (e.g., `"Usage"`, `"Tax"`)
- Glossary terms: Link with `[*term*](#glossary:term)` format (first occurrence per section)
- First mention of Column/Attribute names should link to their definition section

### File Organization

- Each section has a `.mdpp` template that includes individual `.md` files
- All `.md` files in a directory must be included in the corresponding `.mdpp`
- Code blocks must be aligned to start of line (not indented)

## Context Files

### Working Files

Per-issue working files are stored in `.ai/work/<issue-number>-<kebab-case-name>/`:

- `research.md` - Investigation findings and synthesized issue requirements
- `plan.md` - Implementation approach
- `tasks.md` - Execution tracking

**Naming convention**: Use `<issue-number>-<kebab-case-name>` matching your branch name (e.g., branch `1805-ai-usage-policy` → folder `.ai/work/1805-ai-usage-policy/`).

Fetch issue details from GitHub (`gh issue view`) rather than saving locally. Summarize relevant requirements into research.md.

These files are committed during active work. After the PR is approved but before merging, delete the working folder. This is a manual step - do not delete working files until final approval is received. Valuable research should be moved to `supporting_content/` before approval.

### Memory Files

Persistent learnings are stored in `.ai/memory/` and are not deleted.

## Reference Files

- `.ai/memory/` - Saved context and memory across sessions
- `specification/glossary.md` - FOCUS terminology definitions
- `guidelines/` - Development processes and conventions

## Dependencies

**Python packages** (in requirements.txt):

- pymarkdownlnt, panflute, watchdog
- pytest, jsonschema (for requirements model tests)

**System tools**:

- Pandoc (markdown processing)
- wkhtmltopdf (PDF generation)
- GNU Make

## AI Usage Policy

AI-assisted contributions are permitted and follow the same review standards as human-authored content. See [AI Usage Guidelines](guidelines/contributor/ai-usage-guidelines.md) for details.
