# Custom Column Handling

A [FOCUS dataset](#term) consists of a set of columns that convey information about the records provided by a [*data generator*](#metadata.datagenerator). While FOCUS establishes the core structure and defines standardized [FOCUS columns](#term) for consistent reporting, the diverse and evolving landscape of service providers and service offerings may require *data generators* to include [custom columns](#term) in a [FOCUS dataset](#term).

The [Custom Column Handling](#attr) attribute defines column ID naming, formatting, and value requirements for [custom columns](#term) appearing in a [FOCUS dataset](#term).

Each column describes an aspect of the record, including but not limited to:

* Who is responsible for or associated with the activity.
* What the record represents.
* When the activity occurred.
* Where the activity took place.
* Why the record exists or has specific values.
* How values are calculated or determined.

These additional columns enable deeper analysis and provide more detailed information that may not be fully captured by standard [FOCUS columns](#term). See the [Dataset Completeness](#attr) attribute for requirements on what [custom columns](#term) to include.

## Requirements

Column conforming to [CustomColumnHandling](#attr) attribute MUST adhere to the following requirements:

* [Custom column](#term) MUST adhere to the following Column ID naming requirements:
  * [Custom column](#term) MUST include the `x_` prefix in the Column ID to identify it as an external [custom column](#term) and to distinguish it from [FOCUS columns](#term) to avoid conflicts in future releases.
  * [Custom column](#term) SHOULD use [Pascal case](#term) in the portion of the Column ID following the required `x_` prefix.
  * [Custom column](#term) SHOULD use only alphanumeric characters in the portion of the Column ID following the required `x_` prefix.
  * [Custom column](#term) SHOULD NOT include special characters other than the underscore in the required `x_` prefix.
  * [Custom column](#term) SHOULD NOT use abbreviations other than `Id` in the Column ID.
  * [Custom column](#term) SHOULD NOT use acronyms other than `Sku` in the Column ID.
  * [Custom column](#term) SHOULD NOT exceed 50 characters in the Column ID to accommodate column length restrictions of various data repositories.
  * [Custom column](#term) SHOULD include the `Id` suffix in the Column ID when the [custom column](#term) represents an identifier.
  * [Custom column](#term) SHOULD include the `Name` suffix in the Column ID when the [custom column](#term) represents a name.
* [Custom column](#term) SHOULD conform to [DataGeneratorCalculatedSplitCostAllocationHandling](#attr) requirements when the data generator supports data generator-calculated split cost allocation.
* [Custom column](#term) SHOULD conform to [NullHandling](#attr) requirements.
* [Custom column](#term) containing date/time values SHOULD conform to [DateTimeFormat](#attr) requirements.
* [Custom column](#term) containing JSON objects MUST have its object schema documented by the data generator and accessible to practitioners.
* [Custom column](#term) containing numeric values MUST contain a single numeric value.
* [Custom column](#term) containing numeric values SHOULD conform to [NumericFormat](#attr) requirements.
* [Custom column](#term) containing string values SHOULD conform to [StringHandling](#attr) requirements.
* [Custom column](#term) representing a currency SHOULD conform to [CurrencyFormat](#attr) requirements.
* [Custom column](#term) representing a measurement unit SHOULD conform to [UnitFormat](#attr) requirements.
* [Custom column](#term) documentation SHOULD specify how to determine whether a value represents a [national currency](#term) when the [custom column](#term) represents a currency.

## Attribute ID

CustomColumnHandling

## Attribute Name

Custom Column Handling

## Description

Column ID naming, formatting, and value requirements for [custom columns](#term) appearing in a [FOCUS dataset](#term).

## Version Introduced

1.4
