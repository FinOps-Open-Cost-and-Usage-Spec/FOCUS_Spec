# Column Handling

A [*FOCUS dataset*](#glossary:FOCUS-dataset) consists of a set of columns that convey information about the charges incurred with a service provider. Each column describes an aspect of the charge, including but not limited to:

* Who is responsible for incurring or delivering the service.
* What the charge is for.
* When the charge was incurred.
* Where the service was delivered.
* Why the charge was incurred for a specific price.
* How much the charge is and how that cost is calculated.

While FOCUS establishes the core structure and standardizes columns for consistent reporting of cost and usage data, the diverse and evolving landscape of service providers and service offerings may require service providers and data generators to include supplemental columns in the FOCUS dataset. These additional columns may enable deeper analysis and provide more detailed descriptions of usage that may not be fully captured by standard FOCUS dataset columns.

In such cases, service providers and data generators are responsible for ensuring that their usage and cost data is accurately and comprehensively represented by including necessary supplemental columns without duplicating data in FOCUS columns. Rows in a FOCUS dataset may be aggregated or split differently than non-FOCUS datasets to align with FOCUS requirements (e.g., Discount Handling), while enriching the dataset, providers and data generators must maintain the integrity of FOCUS-defined dimensions and metrics. When performing these transformations, providers and data generators must ensure the accuracy of all dimensions and metrics, particularly summable values such as costs and quantities.

Columns within FOCUS include an ID and a display name. Column IDs are used in files and database tables and display names can be used in report output and other descriptive content, like documentation. Column IDs provided in a *FOCUS dataset* follow consistent naming and ordering conventions for FinOps practitioners who consume the data for analysis, reporting, and other use cases.

## Attribute ID

ColumnHandling

## Attribute Name

Column Handling

## Description

Naming and ordering convention for columns appearing in a *FOCUS dataset*.

## Requirements (FOCUS 1.4)

ColumnHandling MUST adhere to the following requirements:

* FOCUS column MUST adhere to the following requirements:
  * FOCUS column MUST use Pascal case in the Column ID.
  * FOCUS column MUST NOT use abbreviations in the Column ID.
  * FOCUS column MUST use only alphanumeric characters in the Column ID.
  * FOCUS column MUST NOT include special characters in the Column ID.
  * FOCUS column SHOULD NOT use acronyms in the Column ID.
  * FOCUS column SHOULD NOT exceed 50 characters in the Column ID to accommodate column length restrictions of various data repositories.
  * FOCUS column representing an identifier MUST include the `Id` suffix in the Column ID.
  * FOCUS column representing a name MUST include the `Name` suffix in the Column ID.
  * FOCUS column representing a product offerings that incured the charge MUST include the `Sku` prefix in the Column ID.
  * FOCUS column MUST use a Display Name consistent with the Column ID, with spaces inserted between words (e.g., Column ID "BillingAccountName" and Display Name "Billing Account Name").
  * FOCUS column with `Category` suffix MUST be normalized.
* Custom column (e.g., service-provider-defined column included in FOCUS dataset) MUST adhere to the following requirements:
  * Custom column MUST include the `x_` prefix in the Column ID to identify it as an external, custom column and to distinguish it from FOCUS columns to avoid conflicts in future releases.
  * Custom column SHOULD use Pascal case in the Column ID.
  * Custom column SHOULD NOT use abbreviations in the Column ID.
  * Custom column SHOULD use only alphanumeric characters in the Column ID.
  * Custom column SHOULD NOT include special characters in the Column ID.
  * Custom column SHOULD NOT use acronyms in the Column ID.
  * Custom column SHOULD NOT exceed 50 characters in the Column ID to accommodate column length restrictions of various data repositories.
  * Custom column representing an identifier SHOULD include the `Id` suffix in the Column ID.
  * Custom column representing a name SHOULD include the `Name` suffix in the Column ID.
* FOCUS dataset MUST adhere to the following column ordering requirements:
  * FOCUS dataset SHOULD list all FOCUS columns before all Custom columns.
  * FOCUS dataset SHOULD sort FOCUS columns alphabetically by their Column ID within the FOCUS columns group.
  * FOCUS dataset SHOULD sort Custom columns alphabetically by their Column ID within the Custom columns group.
  * FOCUS dataset SHOULD NOT intermix FOCUS columns and Custom columns.

## Requirements

### Column Names

* All columns defined by FOCUS MUST follow the following rules:
  * Column IDs MUST use [Pascal case](#glossary:pascalcase).
  * Column IDs MUST NOT use abbreviations.
  * Column IDs MUST be alphanumeric with no special characters.
  * Column IDs SHOULD NOT use acronyms.
  * Column IDs SHOULD NOT exceed 50 characters to accommodate column length restrictions of various data repositories.
  * Columns that have an ID and a Name MUST have the `Id` or `Name` suffix in the Column ID.
  * Column display names MUST be consistent with their Column IDs, with spaces inserted between words (e.g., Column ID "BillingAccountName" and display name "Billing Account Name").
  * Columns with the `Category` suffix MUST be normalized.
* <a name="column_handling:custom-column"></a>Custom (e.g., service-provider-defined) columns that are not defined by FOCUS but included in a *FOCUS dataset* MUST follow the following rules:
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
