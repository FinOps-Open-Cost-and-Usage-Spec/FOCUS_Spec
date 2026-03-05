# Column Handling

A [*FOCUS dataset*](#glossary:FOCUS-dataset) consists of a set of columns that convey information about the charges incurred with a service provider. Each column describes an aspect of the charge, including but not limited to:

* Who is responsible for incurring or delivering the service.
* What the charge is for.
* When the charge was incurred.
* Where the service was delivered.
* Why the charge was incurred for a specific price.
* How much the charge is and how that cost is calculated.

While FOCUS establishes the core structure and standardizes columns for consistent reporting of cost and usage data, the diverse and evolving landscape of service providers and service offerings may require [*data generators*](#metadata.datagenerator) to include custom columns in a *FOCUS dataset*. These additional columns enable deeper analysis and provide more detailed descriptions of usage that may not be fully captured by standard FOCUS columns. See the [Dataset Completeness](#attributes.datasetcompleteness) attribute for requirements on what custom columns to include.

Columns within FOCUS include an ID and a display name. Column IDs are used in files and database tables and display names can be used in report output and other descriptive content, like documentation. Column IDs provided in a *FOCUS dataset* follow consistent naming and documentation conventions for FinOps practitioners who consume the data for analysis, reporting, and other use cases.

All columns defined in the FOCUS specification MUST follow the naming and documentation requirements listed below.

## Attribute ID

ColumnHandling

## Attribute Name

Column Handling

## Description

Naming and documentation conventions for columns appearing in a *FOCUS dataset*.

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
  * Custom columns MUST be documented, including description, purpose, and relationship to [*native dataset*](#glossary:native-dataset) columns.

## Exceptions

* Identifiers will use the "Id" abbreviation since this is a standard pattern across the industry.
* Product offerings that incur charges will use the "Sku" abbreviation because it is a well-understood term both within and outside the industry.

## Introduced (version)

0.5
