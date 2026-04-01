# Copilot Cloud Agent Instructions

## Repository Summary

This is the **FinOps Open Cost and Usage Specification (FOCUS)** -- a community-driven technical specification for standardizing cloud, SaaS, and billing data schemas. It is primarily a **documentation/specification project**, not a software application. Content is Markdown (`.md` and `.mdpp` files) assembled into HTML/PDF. Python (95%) is used only for build tooling, linting, and the requirements model. The default branch is `working_draft`.

## Build & Validation

The CI pipeline (`working_draft.yml`) runs on every push to non-main/non-candidate branches using a `pandoc/extra:latest-ubuntu` container on `ubuntu-24.04`. It runs two jobs:

**Job 1 -- Build the specification:**

```bash
pip install -r requirements.txt
cd specification
make STYLE=working_draft
```

**Job 2 -- Build Requirements Model JSON:**

```bash
cd specification/requirements_model
pip install -r requirements.txt
./build_json.py
```

**Lint a single file:**

```bash
pymarkdownlnt --config specification/markdownlnt.cfg scan path/to/file.md
```

**Run tests only:**

```bash
cd specification/requirements_model && pytest tests/
```

**Clean build artifacts:**

```bash
cd specification && make clean
```

The `make STYLE=working_draft` target runs in order: copies version file, runs `validate_includes.py` on every content directory, checks code block alignment, runs `markdown-pp` to assemble `spec.md`, then lints all source `.md` files and `spec.md`.

## Critical Rules That Will Break CI

- **validate_includes.py**: Every `.md` file in a spec subdirectory MUST have a matching `!INCLUDE "filename.md"` line in the directory's `.mdpp` file -- and vice versa. **If you add or rename a `.md` file, always update the `.mdpp` or the build fails.**
- **Code blocks at column 0**: All fenced code block markers (` ``` `) MUST be aligned to the start of the line. Indented code block markers trigger build failures.
- **No smart characters**: Custom linter rule `MD990` (`custom_linter_rules/rule_md_990.py`) rejects Unicode smart quotes, en-dashes, and ellipses. Always use straight ASCII equivalents.
- **pymarkdownlnt config** (`specification/markdownlnt.cfg`): MD033 (inline HTML), MD013 (line length), MD031 (fenced code blocks), MD041 (first line heading) are disabled; MD004 requires asterisk-style lists; MD024 checks siblings only.
- **AI working folder cleanup**: The `cleanup-context.yml` workflow blocks PR merges if `.ai/work/<branch-name>/` still exists. Delete it before the final push.
- **Generated files are gitignored -- never commit**: `spec.md`, `spec.html`, `*.pdf`, `specification/version.md`, `specification/requirements_model/build/*`.

## Project Layout

```
/ (repo root)
+-- .github/
|   +-- copilot-instructions.md    <- THIS FILE
|   +-- pull_request_template.md
|   +-- CODEOWNERS
|   +-- workflows/
|       +-- working_draft.yml      <- CI for all branches except main/candidate_recommendation
|       +-- main.yml               <- CI for main branch
|       +-- candidate_release.yml  <- CI for candidate_recommendation branch
|       +-- cleanup-context.yml    <- Blocks merge if .ai/work/ folder exists
+-- specification/                 <- MAIN CONTENT AREA
|   +-- Makefile
|   +-- spec.mdpp                  <- Top-level template (includes all sections)
|   +-- markdownlnt.cfg
|   +-- validate_includes.py
|   +-- glossary.md
|   +-- datasets/                  <- Dataset definitions
|   |   +-- {dataset}/columns/     <- Column definitions per dataset
|   +-- attributes/                <- Attribute definitions
|   +-- metadata/                  <- Metadata schemas
|   +-- supported_features/        <- FinOps feature catalog
|   +-- appendix/                  <- Examples and supplementary content
|   +-- schemas/                   <- JSON schemas
|   +-- versions/                  <- Version stamp files
|   +-- requirements_model/        <- Machine-readable validation rules
|   |   +-- build_json.py
|   |   +-- model_rules/           <- JSON rule files (attributes/, columns/, datasets/)
|   |   +-- tests/                 <- pytest tests for rule validation
|   |   +-- requirements.txt       <- Separate Python deps for this subsystem
|   +-- styles/                    <- CSS for HTML/PDF output
+-- custom_linter_rules/
|   +-- rule_md_990.py             <- No smart characters rule
+-- guidelines/contributors/       <- Editorial, normative, and process guidelines
+-- supporting_content/            <- Background info from spec development
+-- vendored/                      <- Vendored tools (markdown-pp, pandoc filter)
+-- requirements.txt               <- Root Python deps
+-- AGENTS.md                      <- Detailed AI agent instructions
```

## Writing Conventions

- **Normative language**: BCP-14 keywords in ALL CAPS: MUST, MUST NOT, SHOULD, SHOULD NOT, MAY. Deprecated: "REQUIRED" -> MUST, "SHALL" -> MUST, "OPTIONAL" -> MAY, "RECOMMENDED" -> SHOULD.
- **Column/Attribute IDs**: PascalCase (`PricingQuantity`). Display names use spaces ("Pricing Quantity").
- **Column values**: Enclosed in double quotes (`"Usage"`, `"Tax"`).
- **Glossary links**: `[*term*](#glossary:term)` format, first occurrence per section.
- **File organization**: Each directory has a `.mdpp` template including `.md` files via `!INCLUDE "filename.md"`. Always keep in sync.

## Requirements Model Rule IDs

Format: `<ArtifactName>-<Type>-<NumericId>-<Status>`

- Types: C (Column), A (Attribute), D (Dataset)
- Status: M (Mandatory), O (Optional), C (Conditional)
- Example: `ListUnitPrice-C-001-M`

## AI Working Files

Per-issue working files go in `.ai/work/<branch-name>/` (e.g., `research.md`, `plan.md`, `tasks.md`). **Delete this folder before final push** -- the `cleanup-context.yml` workflow blocks merges otherwise. Persistent learnings go in `.ai/memory/` (never deleted).

## Dependencies

- **Root `requirements.txt`**: `watchdog==3.0.0`, `pymarkdownlnt==0.9.36`, `panflute==2.3.1`
- **`specification/requirements_model/requirements.txt`**: `jsonschema==4.24.0`, `graphviz==0.21`, `pytest==8.4.2`, `pytest-dependency==0.6.0`, `pytest-order==1.3.0`
- **`specification/supported_features/helpers/requirements.txt`**: `sqlglot>=20.0.0`
- **System tools (CI container)**: Pandoc, wkhtmltopdf, GNU Make
- **Vendored (in repo)**: `vendored/bin/markdown-pp`, pandoc-project-relative-links filter

## Trust These Instructions

These instructions are accurate as of the time of writing. Trust this information and only perform additional repository exploration if something described here is found to be missing or incorrect when you try to use it.
