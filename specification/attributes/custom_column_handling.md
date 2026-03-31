# Custom Column Handling

A [*FOCUS dataset*](#glossary:FOCUS-dataset) consists of a set of columns that convey information about the records provided by a [*data generator*](#metadata.datagenerator). While FOCUS establishes the core structure and defins standardized [*FOCUS columns*](#glossary:FOCUS-column) for consistent reporting, the diverse and evolving landscape of service providers and service offerings may require [*data generators*](#metadata.datagenerator) to include [*custom columns*](#glossary:custom-column) in a *FOCUS dataset*.

The Custom Column Handling attribute defines column ID naming, formatting, and value requirements for *custom columns* appearing in a *FOCUS dataset*.

Each column describes an aspect of the record, including but not limited to:

* Who is responsible for or associated with the activity.
* What the record represents.
* When the activity occurred.
* Where the activity took place.
* Why the record exists or has specific values.
* How values are calculated or determined.

These additional columns enable deeper analysis and provide more detailed information that may not be fully captured by standard [*FOCUS columns*](#glossary:FOCUS-column). See the [Dataset Completeness](#attributes.datasetcompleteness) attribute for requirements on what *custom columns* to include.

## Attribute ID

CustomColumnHandling

## Attribute Name

Custom Column Handling

## Description

Column ID naming, formatting, and value requirements for *custom columns* appearing in a *FOCUS dataset*.

## Requirements

Column conforming to CustomColumnHandling attribute MUST adhere to the following requirements:

* *Custom column* MUST adhere to the following Column ID naming requirements:
  * *Custom column* MUST include the `x_` prefix in the Column ID to identify it as an external *custom column* and to distinguish it from *FOCUS columns* to avoid conflicts in future releases.
  * *Custom column* SHOULD use [*Pascal case*](#glossary:pascalcase) in the Column ID.
  * *Custom column* SHOULD use only alphanumeric characters in the Column ID.
  * *Custom column* SHOULD NOT include special characters in the Column ID.
  * *Custom column* SHOULD NOT use abbreviations other than `Id` in the Column ID.
  * *Custom column* SHOULD NOT use acronyms other than `Sku` in the Column ID.
  * *Custom column* SHOULD NOT exceed 50 characters in the Column ID to accommodate column length restrictions of various data repositories.
  * *Custom column* SHOULD include the `Id` suffix in the Column ID when the *custom column* represents an identifier.
  * *Custom column* SHOULD include the `Name` suffix in the Column ID when the *custom column* represents a name.
* *Custom column* MUST conform to [NullHandling](#attributes.nullhandling) requirements.
* *Custom column* MUST conform to [DataGeneratorCalculatedSplitCostAllocationHandling](#attributes.datagenerator-calculatedsplitcostallocationhandling) requirements when the data generator supports data generator-calculated split cost allocation.
* *Custom column* containing date/time values MUST conform to [DateTimeFormat](#attributes.datetimeformat) requirements.
* *Custom column* containing JSON objects MUST conform to [JsonObjectFormat](#attributes.jsonobjectformat) requirements.
* *Custom column* containing numeric values MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* *Custom column* containing string values MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* *Custom column* representing national currencies MUST conform to [CurrencyFormat](#attributes.currencyformat) requirements.
* *Custom column* representing measurement units SHOULD conform to [UnitFormat](#attributes.unitformat) requirements.

## Introduced (version)

1.4
