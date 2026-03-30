# Column Handling

A [*FOCUS dataset*](#glossary:FOCUS-dataset) consists of a set of columns that convey information about the records provided by a [*data generator*](#metadata.datagenerator). Each column describes an aspect of the record, including but not limited to:

* Who is responsible for or associated with the activity.
* What the record represents.
* When the activity occurred.
* Where the activity took place.
* Why the record exists or has specific values.
* How values are calculated or determined.

While FOCUS establishes the core structure and standardizes columns for consistent reporting, the diverse and evolving landscape of service providers and service offerings may require [*data generators*](#metadata.datagenerator) to include *custom columns* in a *FOCUS dataset*. These additional columns enable deeper analysis and provide more detailed information that may not be fully captured by standard FOCUS columns. See the [Dataset Completeness](#attributes.datasetcompleteness) attribute for requirements on what *custom columns* to include.

Columns within FOCUS include an ID and a display name. Column IDs are used in files and database tables and display names can be used in report output and other descriptive content, like documentation. Column IDs provided in a *FOCUS dataset* follow consistent naming and documentation conventions for FinOps practitioners who consume the data for analysis, reporting, and other use cases.

## Attribute ID

ColumnHandling

## Attribute Name

Column Handling

## Description

Naming and documentation conventions for columns appearing in a *FOCUS dataset*.

## Requirements

Column conforming to ColumnHandling attribute MUST adhere to the following requirements:

* [*FOCUS column*](#glossary:FOCUS-column) MUST adhere to the following requirements:
  * *FOCUS column* MUST use a Display Name consistent with the Column ID, with spaces inserted between words (e.g., Column ID "BillingAccountName" and Display Name "Billing Account Name").
  * *FOCUS column* MUST use [*Pascal case*](#glossary:pascalcase) in the Column ID.
  * *FOCUS column* MUST use only alphanumeric characters in the Column ID.
  * *FOCUS column* MUST NOT include special characters in the Column ID.
  * *FOCUS column* MUST NOT use abbreviations other than `Id` in the Column ID.
  * *FOCUS column* SHOULD NOT use acronyms other than `Sku` in the Column ID.
  * *FOCUS column* SHOULD NOT exceed 50 characters in the Column ID to accommodate column length restrictions of various data repositories.
  * *FOCUS column* MUST include the `Id` suffix in the Column ID when the *FOCUS column* represents an identifier.
  * *FOCUS column* MUST include the `Name` suffix in the Column ID when the *FOCUS column* represents a name.
  * *FOCUS column* MUST include `Sku` in the Column ID when the *FOCUS column* represents a product offering that incurred a charge.
  * *FOCUS column* MUST contain one of the FOCUS-defined allowed values when the *FOCUS column* includes `Category` suffix in the Column ID and is not null.
* [*Custom column*](#glossary:custom-column) MUST adhere to the following requirements:
  * *Custom column* MUST include the `x_` prefix in the Column ID to identify it as an external *custom column* and to distinguish it from FOCUS columns to avoid conflicts in future releases.
  * *Custom column* SHOULD use *Pascal case* in the Column ID.
  * *Custom column* SHOULD use only alphanumeric characters in the Column ID.
  * *Custom column* SHOULD NOT include special characters in the Column ID.
  * *Custom column* SHOULD NOT use abbreviations other than `Id` in the Column ID.
  * *Custom column* SHOULD NOT use acronyms other than `Sku` in the Column ID.
  * *Custom column* SHOULD NOT exceed 50 characters in the Column ID to accommodate column length restrictions of various data repositories.
  * *Custom column* SHOULD include the `Id` suffix in the Column ID when the *custom column* represents an identifier.
  * *Custom column* SHOULD include the `Name` suffix in the Column ID when the *custom column* represents a name.

## Introduced (version)

0.5
