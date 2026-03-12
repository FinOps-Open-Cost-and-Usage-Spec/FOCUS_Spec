# Null Handling

Cost data [*rows*](#glossary:row) that don't have a value that can be presented for a column must be handled in a consistent way to reduce friction for FinOps practitioners who consume the data for analysis, reporting, and other use cases.

## Attribute ID

NullHandling

## Attribute Name

Null Handling

## Description

Indicates how to handle columns that don't have a value.

## Requirements

NullHandling MUST adhere to the following requirements:

* FOCUS column MUST adhere to the following requirements:
  * FOCUS column defined as nullable MUST use NULL when no value is applicable.
  * FOCUS column containing string values MUST NOT contain empty strings or placeholder strings (e.g., "Not Applicable") to indicate that no value is applicable.
  * FOCUS column containing numeric values MUST NOT contain placeholder numeric values (e.g., 0) to indicate that no value is applicable.
* Custom column MUST adhere to the following requirements:
  * Custom column defined as nullable SHOULD use NULL when no value is applicable.
  * Custom column containing string values SHOULD NOT contain empty strings or placeholder strings (e.g., "Not Applicable") to indicate that no value is applicable.
  * Custom column containing numeric values SHOULD NOT contain placeholder numeric values (e.g., 0) to indicate that no value is applicable.

## Introduced (version)

0.5
