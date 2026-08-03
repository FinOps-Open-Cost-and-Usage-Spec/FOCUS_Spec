# FOCUS Specification Repository Naming Conventions

This document outlines naming conventions for directories and files in the FOCUS Specification [GitHub repository](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec).

## Directory Naming Conventions

### FOCUS-defined Directories

To ensure consistency, ease of maintenance, and portability, all directories in this repository, except [GitHub directories](#github-directories), MUST follow these naming conventions:

* Directory names MUST use lowercase characters.
* Directory names MUST NOT contain spaces.
* Directory names SHOULD be descriptive and reflect the primary content of the directory.
* Directory names consisting of multiple words MUST adhere to the following requirements:
  * Directory names for directories defining FOCUS entities (e.g., FOCUS datasets, FOCUS columns, FOCUS attributes) MUST NOT use any word separator, so that the directory name matches the FOCUS entity identifier in lowercase.
  * All other directory names MUST use hyphens (`-`) as the word separator (i.e., kebab-case).

### GitHub Directories

GitHub directories (e.g., `.github` and its subdirectories such as `ISSUE_TEMPLATE`, `workflows`) are exempt from these rules and MUST follow common GitHub directory naming conventions.

### Directory Name Examples

The following examples illustrate correct and incorrect directory names based on the rules above.

**Directories defining FOCUS entities** (no word separator):

| Correct         | Incorrect                                           |
|-----------------|-----------------------------------------------------|
| `costandusage`  | `cost-and-usage`, `CostAndUsage`, `cost_and_usage`  |
| `invoicedetail` | `invoice-detail`, `InvoiceDetail`, `invoice_detail` |

**Other FOCUS-defined directories** (kebab-case):

| Correct              | Incorrect                                                                             |
|----------------------|---------------------------------------------------------------------------------------|
| `supported-features` | `supported_features`, `supportedFeatures`, `SupportedFeatures`, `Supported Features`  |

## File Naming Conventions

### FOCUS-defined Markdown and MarkdownPP files

To ensure consistency, ease of maintenance, and portability, all Markdown and MarkdownPP files (`.md`, `.mdpp`) in this repository, except [key repository files](#key-repository-files), MUST follow these naming conventions:

* File names MUST use lowercase characters.
* File names MUST NOT contain spaces.
* File names SHOULD be descriptive and reflect the primary content of the file.
* File names consisting of multiple words MUST adhere to the following requirements:
  * File names for files defining FOCUS entities (e.g., FOCUS datasets, FOCUS columns, FOCUS attributes) MUST NOT use any word separator, so that the file name matches the FOCUS entity identifier in lowercase.
  * All other file names MUST use hyphens (`-`) as the word separator (i.e., kebab-case).

### Other File Types

Files that are not Markdown or MarkdownPP MUST follow these naming conventions:

* Python files (`.py`) and Python-adjacent JSON files consumed as Python test fixtures or package data MUST use `snake_case`, per [PEP 8](https://peps.python.org/pep-0008/#package-and-module-names).
* JSON files that define a FOCUS entity's requirements model rules MUST match the FOCUS entity identifier in lowercase, consistent with the [FOCUS-defined Markdown and MarkdownPP files](#focus-defined-markdown-and-markdownpp-files) rule.
* Configuration files owned by a specific tool (e.g., `.github/workflows`, `.gemini`, linters, formatters) MUST follow that tool's expected file naming convention, even when it conflicts with the rules above.
* All other JSON, YAML, CSS, CSV, and image files MUST use kebab-case with hyphens (`-`) as the word separator.

### Key Repository Files

Key repository files (e.g., `README.md`, `CHANGELOG.md`, `CONTRIBUTING.md`) are exempt from these rules and MUST follow common GitHub file naming conventions.

### File Name Examples

The following examples illustrate correct and incorrect file names based on the rules above.

**Files defining FOCUS entities** (no word separator):

| Correct                | Incorrect                                                          |
|------------------------|--------------------------------------------------------------------|
| `costandusage.mdpp`    | `cost-and-usage.mdpp`, `CostAndUsage.mdpp`, `Cost And Usage.mdpp`  |
| `pricingquantity.md`   | `pricing-quantity.md`, `PricingQuantity.md`, `pricing_quantity.md` |
| `numericformat.md`     | `numeric-format.md`, `NumericFormat.md`, `numeric_format.md`       |

**Other FOCUS-defined Markdown and MarkdownPP files** (kebab-case):

| Correct                     | Incorrect                                                |
|-----------------------------|----------------------------------------------------------|
| `supported-features.mdpp`   | `supported_features.mdpp`, `supportedFeatures.mdpp`      |
| `spec-change-guidelines.md` | `spec_change_guidelines.md`, `spec change guidelines.md` |

**Python and Python-adjacent files** (`snake_case`):

| Correct           | Incorrect                                       |
|--------------------|----------------------------------------------------|
| `build_json.py`   | `build-json.py`, `buildJson.py`, `BuildJson.py` |
| `test_schema.py`  | `test-schema.py`, `testSchema.py`               |

**Requirements model rule JSON files defining FOCUS entities** (no word separator):

| Correct                | Incorrect                                      |
|--------------------------|---------------------------------------------------|
| `numericformat.json`   | `numeric-format.json`, `numeric_format.json`   |
| `stringhandling.json`  | `string-handling.json`, `string_handling.json` |

**Tool-owned configuration files** (align to tooling convention):

| Correct                                | Notes                                            |
|-------------------------------------------|------------------------------------------------------|
| `.github/workflows/working_draft.yml`  | Follows GitHub Actions workflow file conventions |
| `.gemini/config.yaml`                  | Follows Gemini CLI configuration file conventions |

**Other JSON, YAML, CSS, CSV, and image files** (kebab-case):

| Correct                   | Incorrect                                         |
|-----------------------------|------------------------------------------------------|
| `model-schema.json`       | `model_schema.json`, `modelSchema.json`           |
| `all-upfront-100pct.csv`  | `all_upfront_100pct.csv`, `AllUpfront100pct.csv`  |
| `spec-styles.css`         | `spec_styles.css`, `SpecStyles.css`               |

## Renaming Directories or Files After Publication

Directory and file names may be referenced by external hyperlinks (e.g., within FinOps Foundation assets), and those within the `specification/` directory are additionally used by the specification build process (e.g., `!INCLUDE` statements, Makefile dependencies). See [MarkdownPP Guidelines](markdownpp-guidelines.md) for details.

Directory and file names SHOULD remain stable after publication to maintain repository consistency and external hyperlink integrity.

If a rename is necessary, all affected build references, dependencies, and external links MUST be updated accordingly.
