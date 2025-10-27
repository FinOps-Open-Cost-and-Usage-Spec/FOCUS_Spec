# Numeric Precision

Numeric Precision is the maximum number of digits for the values in the column.

The NumericPrecision property adheres to the following requirements:

* NumericPrecision SHOULD be provided in the FOCUS Metadata schema for Numeric Format columns.
* NumericPrecision MUST be of type Integer.
* NumericPrecision MUST NOT contain null values.

## Metadata ID

NumericPrecision

## Metadata Name

Numeric Precision

## Content constraints

| Constraint    | Value                            |
|:--------------|:---------------------------------|
| Feature level | Conditional                      |
| Allows nulls  | False                            |
| Data type     | Integer                          |
| Value format  | [Numeric Format](#numericformat) |

## Introduced (version)

1.0
