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

| Correct         | Incorrect                                                        |
|-----------------|------------------------------------------------------------------|
| `costandusage`  | `cost-and-usage`, `CostAndUsage`, `cost_and_usage`              |
| `invoicedetail` | `invoice-detail`, `InvoiceDetail`, `invoice_detail`        |

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

This document does not currently cover naming conventions for other file types (e.g., Python scripts, configuration files). These may be added in the future as needed.

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

## Renaming Directories or Files After Publication

Directory and file names may be referenced by external hyperlinks (e.g., within FinOps Foundation assets), and those within the `specification/` directory are additionally used by the specification build process (e.g., `!INCLUDE` statements, Makefile dependencies). See [MarkdownPP Guidelines](markdownpp-guidelines.md) for details.

Directory and file names SHOULD remain stable after publication to maintain repository consistency and external hyperlink integrity.

If a rename is necessary, all affected build references, dependencies, and external links MUST be updated accordingly.

---

# FOCUS Repository Naming Conventions

This document outlines 

## Directory Naming Conventions

To ensure consistency, ease of maintenance, and portability, all directories in the FOCUS Specification repository, except [GitHub-managed directories](#github-managed-directories), MUST follow these naming conventions:

* Directory names MUST use lowercase characters.
* Directory names MUST NOT contain spaces.
* Directory names SHOULD be descriptive and reflect the primary content of the directory.
* Directory names consisting of multiple words MUST adhere to the following requirements:
  * Directory names for directories defining FOCUS entities (e.g., FOCUS datasets, FOCUS columns, FOCUS attributes) MUST NOT use any word separator, so that the directory name matches the FOCUS entity identifier in lowercase.
  * All other directory names MUST use hyphens (`-`) as the word separator (i.e., kebab-case).

### GitHub Directories

GitHub-managed directories (e.g., `.github` and its subdirectories such as `ISSUE_TEMPLATE`, `workflows`) are exempt from these rules and MUST follow common GitHub directory naming conventions.

### Renaming Directories After Publication

Directory names are used by build processes (e.g., `!INCLUDE` statements) and may also appear in external hyperlinks (e.g., within FinOps Foundation assets). Directory names SHOULD remain stable after publication to maintain repository consistency and external hyperlink integrity.

If a rename is necessary, all affected `!INCLUDE` statements and build dependencies MUST be updated accordingly to avoid broken references.

### Preferred Directory Name Examples

```text
supported-features
costandusage
pricingquantity
numericformat
```

### Forbidden Directory Name Examples

```text
SupportedFeatures
Supported Features
supportedFeatures
supported_features
cost-and-usage
```

## File Naming Conventions

To ensure consistency, ease of maintenance, and portability, all Markdown and MarkdownPP files in the FOCUS Specification repository, except [key repository files](#key-repository-files), MUST follow these naming conventions:

* File names MUST use lowercase characters.
* File names MUST NOT contain spaces.
* File names SHOULD be descriptive and reflect the primary content of the file.
* File names consisting of multiple words MUST adhere to the following requirements:
  * File names for files defining FOCUS entities (e.g., FOCUS datasets, FOCUS columns, FOCUS attributes) MUST NOT use any word separator, so that the file name matches the FOCUS entity identifier in lowercase.
  * All other file names MUST use hyphens (`-`) as the word separator (i.e., kebab-case).

### Key Repository Files

Key repository files (e.g., `README.md`, `CHANGELOG.md`, `CONTRIBUTING.md`) are exempt from these rules and MUST follow common GitHub file naming conventions.

### Renaming Files After Publication

File names are used by build processes (e.g., `!INCLUDE` statements) and may also appear in external hyperlinks (e.g., within FinOps Foundation assets). File names SHOULD remain stable after publication to maintain repository consistency and external hyperlink integrity.

If a rename is necessary, all affected `!INCLUDE` statements and build dependencies MUST be updated accordingly to avoid broken references.

### Preferred File Name Examples

```text
supported-features.mdpp
costandusage.mdpp
pricingquantity.md
numericformat.md
```

### Forbidden File Name Examples

```text
PricingQuantity.md
Pricing Quantity.md
pricingQuantity.md
numeric_format.md
numeric-format.md
```
