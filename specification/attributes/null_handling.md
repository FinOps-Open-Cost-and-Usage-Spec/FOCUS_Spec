# Null Handling

[*FOCUS dataset*](#glossary:FOCUS-dataset) records that don't have a value that can be presented for a column must be handled in a consistent way to reduce friction for FinOps practitioners who consume the data for analysis, reporting, and other use cases.

## Attribute ID

NullHandling

## Attribute Name

Null Handling

## Description

Indicates how to handle columns that don't have a value.

## Requirements

Column conforming to NullHandling attribute MUST adhere to the following requirements:

* [*FOCUS column*](#glossary:FOCUS-column) MUST adhere to the following requirements:
  * *FOCUS column* MUST use NULL for absent values when the *FOCUS column* is defined as nullable.
  * *FOCUS column* MUST NOT contain empty strings or placeholder strings (e.g., "Not Applicable") for absent values when the *FOCUS column* contains string values.
  * *FOCUS column* MUST NOT contain placeholder numeric values (e.g., 0) for absent values when the *FOCUS column* contains numeric values.
* [*Custom column*](#glossary:custom-column) MUST adhere to the following requirements:
  * *Custom column* SHOULD use NULL for absent values when the *custom column* is defined as nullable.
  * *Custom column* SHOULD NOT contain empty strings or placeholder strings (e.g., "Not Applicable") for absent values when the *custom column* contains string values.
  * *Custom column* SHOULD NOT contain placeholder numeric values (e.g., 0) for absent values when the *custom column* contains numeric values.

## Introduced (version)

0.5
