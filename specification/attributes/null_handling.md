# Null Handling

Cost data rows that don't have a value that can be presented for a column must be handled in a consistent way to reduce
friction for FinOps practitioners that consume the data for analysis, reporting, and other use cases.

All columns defined in FOCUS MUST follow the null handling requirements listed below. Provider generated columns SHOULD
adopt these same null handling requirements over time.

## Attribute ID

NullHandling

## Attribute Name

Null Handling

## Description

Indicates how to handle columns that don't have a value.

## Requirements

* Columns MUST use NULL when there isn't a value that can be specified for a nullable column.
* Columns MUST NOT use empty strings or placeholder values such as 'Not Set' or 'Not Applicable' in columns, regardless
  of if the column allows nulls or not.

## Exceptions

None

## Introduced (version)

0.5
