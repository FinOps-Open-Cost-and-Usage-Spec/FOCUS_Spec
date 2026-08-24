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

* **BCP-14 Keywords:** Use MUST, MUST NOT, SHOULD, SHOULD NOT, MAY (uppercase). NEVER use: "REQUIRED", "SHALL", "SHALL NOT", "RECOMMENDED", "NOT RECOMMENDED", "OPTIONAL".
* **Location:** Capitalized BCP-14 keywords MUST NOT appear outside "Requirements" sections in files under `specification/attributes/`, `specification/conditions/`, and `specification/datasets/` unless quoted. 

* **Structure:** Use bulleted lists. Each bullet MUST express exactly one verifiable state. Split bullets that combine multiple obligations.
* **Nested Requirements:** Apply the following rules:
  * Introduce nested bullets only when expressing composite requirements.
  * Preserve the established indentation hierarchy.
  * Never skip nesting levels.
* **Requirement Ownership (DRY):** Apply the following rules:
   * Each normative requirement MUST be defined exactly once. 
   * When the same normative behavior applies in multiple locations, authors MUST reference the existing requirement or reusable Attribute rather than duplicating the requirement text.
* **Structural Grouping Bullets:** Organizational bullets (such as headings introducing groups of requirements) MUST NOT be authored as normative requirements. They exist solely to organize subordinate normative requirements and are not independently verifiable.
* **Composite Requirements:** Apply the following rules: 
   * When a requirement introduces multiple subordinate requirements, the parent requirement MUST establish the applicability or scope while nested requirements define the independently verifiable normative obligations. 
   * Each nested bullet MUST remain independently verifiable.
* **Allowed Subjects:** MUST be schema-level entities (e.g., `FOCUS dataset`, `BilledCost`). Actors (e.g., Data Generator) and Processes MUST NOT be subjects.
* **State vs. Behavior:** Describe a state, not behavior. Prohibited process verbs: *ensure, handle, support, provide, alter, prefix, document* (though they MAY appear in conditional clauses).
* **Conditional Phrasing:** Use ONLY: `when / unless / only when / except when`. (DO NOT use `if`).
* **Mathematical Accuracy:** `and/or` is permitted ONLY in mathematical validations or conditional clauses.
* **Comparison Terminology:** Select comparison terminology according to the semantics of the comparison:
  * use `equal` for numeric comparisons;
  * use `match` for identifiers and string values;
  * use `be` when evaluating states or enumerated values;
  * use `greater than or equal to` or `less than or equal to` for inequalities;
  * use `equivalent` for semantic equivalence; and
  * use `remain consistent` when requiring a value to be stable across time, records, or another defined scope.
* **Structural Anchors:** Apply the following rules: 
   * Requirements sections, including reusable Attribute requirement sections, MUST begin with a non-verifiable anchor phrase ending in a colon (e.g., `<Entity> MUST adhere to the following requirements:`). 
   * Anchor requirements exist solely to establish the parsing structure of subordinate requirements 
   * Anchor requirements MUST NOT be interpreted as independently verifiable normative requirements.
* **Terminology:** Apply the following rules:
  * Normative references to columns MUST use `ColumnId`s, never column Display Names. 
  * Requirements governing a specific dataset MUST use its `DatasetId` as the subject (e.g., `SkuPrice`). 
  * Requirements applying generically to all FOCUS datasets MUST use `FOCUS dataset`. 
  * Otherwise, authors MUST use the abstraction that precisely matches the requirement (e.g., `dataset instance` or `dataset artifact`) 
  * When a narrower abstraction is intended, authors MUST avoid using `FOCUS dataset`.
* **Tone:** Use formal language. Contractions (e.g., *don't, can't*) MUST NOT be used in normative requirements.
* **Inline Examples:** Any non-normative examples embedded within a requirement MUST be enclosed in parentheses using "e.g." (e.g., `...without lossy transformations (e.g., rounding)`).
* **Subsection Ordering:** When generating new specification entities, preserve the subsection ordering already established for that entity type within the specification. Do not invent alternative subsection sequences.

### Editorial Conventions

* **Column/Attribute IDs:** PascalCase without spaces (e.g., PricingQuantity). Entity IDs MUST be used in normative text sections.
* **Column/Attribute References in Non-Normative Content:**
  * Display Names SHOULD be used for conceptual, reader-facing references.
  * Canonical IDs MAY be used for schema-facing references.
  * A reference is schema-facing when it identifies a field in code, JSON, SQL, a schema, a table header, or an object/property path, or when the surrounding sentence describes that field being populated, omitted, null, serialized, validated, matched, compared, grouped, filtered, joined, aggregated, or repeated.
  * When none of the schema-facing conditions above applies, treat the reference as conceptual.
  * Reviewers MUST NOT create a finding solely because a schema-facing non-normative reference uses its canonical ID.
  * A canonical ID used for a conceptual non-normative reference MAY produce a suggestion. 
  * A canonical ID used for a conceptual non-normative reference MUST NOT produce an error or warning.
* **No Mixing:** Do not mix Entity IDs and Display Names within the same normative requirement.
* **Column values:** Apply the following rules:
  * When a column value appears in prose or normative text, enclose it in double quotation marks (e.g., `"Usage"`, `"Tax"`). 
  * In an Allowed Values table, list values without quotation marks because the `Value` column identifies them as literals, unless quotation marks are part of the value itself.
* **Glossary terms:** Link with `[*term*](#glossary:term)` format.
* **Linking Rule:** For each distinct entity or glossary destination in a source Markdown file:
  * Ignore occurrences in document titles and section headings.
  * Link the first remaining occurrence in reading order.
  * Leave all later occurrences unlinked.
  * When no remaining occurrence exists, no link is required.
  Exceptions:
  * A link whose anchor text is not an entity name or glossary term does not count toward first occurrence.
  * Content Constraints sections link every entity reference.
  * Glossary entries apply this rule independently within each entry.
  * An entity catalog table MAY link the entity that identifies each row, even when that entity was linked earlier in the file. Treat a table as an entity catalog only when each data row represents and identifies a distinct specification entity.
  * Each normative requirement bullet MAY link its first reference to each distinct FOCUS entity, glossary term, or FOCUS Condition, even when the same destination was linked earlier in the file. 
  * Later references to the same destination within that bullet MUST remain unlinked.
* **Lists:** All unordered lists MUST use asterisks (`*`), never dashes (`-`) or plus signs (`+`). Nested bullet points MUST use exactly two spaces per level.
* **Notes:** Important notes must use the blockquote format (`> **Note:**`).
* **Notes versus Exceptions:** Apply the following rules:
  * Notes MUST contain only informative or explanatory material. 
  * Normative conditions and exceptions MUST be expressed as requirements.
* **Anchors:** Pandoc auto-generates custom heading anchors. DO NOT flag missing HTML `<a name="">` tags.
* **Markdown Tables:** Select spacing by maximum row width:
  * Below 120 characters, prefer padding cells to align the vertical pipes.
  * At 120 characters or more, prefer one space after each cell value without alignment padding.
* **Numbers in Prose: Apply the following rules:** 
  * In explanatory prose, spell out numbers zero through nine.
  * In explanatory prose, use numerals beginning at 10. 
  * Preserve numeric notation in JSON, mathematics, schema constraints, identifiers, and technical examples.
* **Dash Usage:** Apply dash formatting by purpose:
  * Use an unspaced hyphen (`-`) for compound words and ranges.
  * Use a spaced hyphen (` - `) to set off parenthetical phrases.
  * Avoid HTML entities and special Unicode dash characters.

### Validation & Schema Accuracy

* **Mathematical & Schema Accuracy:** AI reviewers MUST rigorously calculate, parse, and verify all data within examples (especially JSON snippets and tables). Flag any mathematical inconsistencies or hallucinated data.
* **JSON Formatting:** JSON blocks MUST use double quotation marks for keys. Verify that the JSON is structurally valid.
* **JSON Object Requirements:**  Apply the following rules: 
  * Requirements governing a JSON object MUST be authored with the object definition. 
  * Column-level requirements MUST remain with the column definition. 
  * Requirements for object properties SHOULD reference properties using dot notation where appropriate to distinguish object-level constraints from property-level constraints.
* **Example Disclaimer:** Top-level sections with examples and no normative requirements MUST begin with: `> Note: The following section is informative and non-normative. It does not define requirements.` Enforce ONLY on Level-2 headings in `spec.md` or major section overview files (e.g., `appendix_overview.md`). Ignore nested .md files.

### File Organization

* Each section has a `.mdpp` template that includes individual `.md` files
* All `.md` files in a directory must be included in the corresponding `.mdpp`
* Code blocks must be aligned to start of line (not indented)

### Review Conduct

* **Suggestion-first feedback:** When a concrete fix exists, post it as a GitHub `suggestion` block so the author can accept with one click. Use plain-text comments only when the feedback requires discussion rather than a specific replacement.
* **Self-contained comments:** Every review comment or suggestion MUST include all context needed for the author to evaluate it independently. Do not reference other comments (e.g., "same as above" or "see my comment on line X").
* **Diff-scope discipline:** Only flag issues on lines changed or added by the PR. Pre-existing problems are out of scope unless they create a direct inconsistency with new content in the same PR.
* **Deduplication:** If your tooling can read PR threads, do not flag already-raised issues or post competing suggestions. To add details, reply to the existing thread.
* **BCP-14 rule applicability:** When the BCP-14 keyword location rule does not apply, continue applying all other relevant Markdown, editorial, example-accuracy, and review-conduct rules.

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
