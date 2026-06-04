# Numeric Precision

Numeric Precision is the maximum number of digits for the values in the column.

NumericPrecision adheres to the following requirements:

* NumberPrecision SHOULD be present in an object within the [ColumnDefinition](#columndefinition) collection when the column is of Decimal data type.
* NumericPrecision MUST be of type Integer.
* NumericPrecision MUST NOT contain null values.

## Metadata ID

NumericPrecision

## Metadata Name

Numeric Precision

## Content constraints

| Constraint    | Value                            |
|:--------------|:---------------------------------|
| Feature level | Recommended                      |
| Allows nulls  | False                            |
| Data type     | Integer                          |
| Value format  | [Numeric Format](#numericformat) |

## Introduced (version)

1.0
