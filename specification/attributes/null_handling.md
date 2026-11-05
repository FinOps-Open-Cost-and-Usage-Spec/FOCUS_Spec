# Null Handling

[FOCUS dataset](#term) records that don't have a value that can be presented for a column must be handled in a consistent way to reduce friction for FinOps practitioners who consume the data for analysis, reporting, and other use cases.

## Requirements

Column conforming to [NullHandling](#attr) attribute MUST adhere to the following requirements:

* [FOCUS dataset column](#term) MUST use `null` for absent values when the [FOCUS dataset column](#term) is defined as nullable.
* [FOCUS dataset column](#term) MUST NOT contain empty strings or placeholder strings (e.g., `Not Applicable`) for absent values when the [FOCUS dataset column](#term) contains string values.
* [FOCUS dataset column](#term) MUST NOT contain placeholder numeric values (e.g., `0`) for absent values when the [FOCUS dataset column](#term) contains numeric values.

## Attribute ID

NullHandling

## Attribute Name

Null Handling

## Description

Indicates how to handle columns that don't have a value.

## Version Introduced

0.5
