# Column Handling

A [*FOCUS dataset*](#glossary:FOCUS-dataset) consists of a set of columns that convey information about the charges incurred with a provider. Each column describes an aspect of the charge, including but not limited to:

* Who is responsible for incurring or delivering the service.
* What the charge is for.
* When the charge was incurred.
* Where the service was delivered.
* Why the charge was incurred for a specific price.
* How much the charge is and how that cost is calculated.

Given the broad range of ever-evolving providers and service offerings, FOCUS as a specification may not define all the columns needed to comprehensively describe every provider's unique cost and usage charges. Providers and data generators are responsible for including additional information required to *accurately* and *completely* describe the charges included within a *FOCUS dataset*. Rows in a *FOCUS dataset* may be aggregated or split differently than non-FOCUS datasets to meet the requirements defined by FOCUS columns and attributes (e.g., [Discount Handling](#discounthandling)). Data generators are responsible for ensuring the accuracy of dimensions and metrics when aggregating or splitting rows, especially summable metrics like costs and quantities.

Columns within FOCUS include an ID and a display name. Column IDs are used in files and database tables and display names can be used in report output and other descriptive content, like documentation. Column IDs provided in a *FOCUS dataset* follow consistent naming and ordering conventions to reduce friction for FinOps practitioners who consume the data for analysis, reporting, and other use cases.

All columns defined in the FOCUS specification MUST follow the naming and ordering requirements listed below.

## Attribute ID

ColumnHandling

## Attribute Name

Column Handling

## Description

Naming, ordering, and inclusion criteria for columns appearing in a *FOCUS dataset*.

## Requirements

### Column Inclusion

When the provider publishes a non-FOCUS cost and usage dataset, the following applies:

* Custom columns MUST be included for all information not covered by FOCUS columns that exists in the latest version of non-FOCUS cost and usage datasets.
* Data generators MAY allow practitioners to select a subset of FOCUS or custom columns.

### Column Names

* All columns defined by FOCUS MUST follow the following rules:
  * Column IDs MUST use [Pascal case](#glossary:pascalcase).
  * Column IDs MUST NOT use abbreviations.
  * Column IDs MUST be alphanumeric with no special characters.
  * Column IDs SHOULD NOT use acronyms.
  * Column IDs SHOULD NOT exceed 50 characters to accommodate column length restrictions of various data repositories.
  * Columns that have an ID and a Name MUST have the `Id` or `Name` suffix in the Column ID.
  * Column display names MAY avoid the `Name` suffix if there are no other columns with the same name prefix.
  * Columns with the `Category` suffix MUST be normalized.
* Custom (e.g., provider-defined) columns that are not defined by FOCUS but included in a *FOCUS dataset* MUST follow the following rules:
  * Custom columns MUST be prefixed with a consistent `x_` prefix to identify them as external, custom columns and distinguish them from FOCUS columns to avoid conflicts in future releases.
  * Custom columns SHOULD follow the same rules listed above for FOCUS columns.

### Column Order

* All FOCUS columns SHOULD be first in the provided dataset.
* Custom columns SHOULD be listed after all FOCUS columns and SHOULD NOT be intermixed.
* Columns MAY be sorted alphabetically, but custom columns SHOULD be after all FOCUS columns.

## Exceptions

* Identifiers will use the "Id" abbreviation since this is a standard pattern across the industry.
* Product offerings that incur charges will use the "Sku" abbreviation because it is a well-understood term both within and outside the industry.

## Introduced (version)

0.5
