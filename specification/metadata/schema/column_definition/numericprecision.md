# Numeric Precision

[Numeric Precision](#meta) is the maximum number of digits for the values in the column.

[NumericPrecision](#meta) adheres to the following requirements:

* [NumericPrecision](#meta) SHOULD be present in an object within the [ColumnDefinition](#meta) collection when the column is of Decimal data type.
* [NumericPrecision](#meta) MUST be of type Integer.
* [NumericPrecision](#meta) MUST NOT contain null values.

## Metadata ID

NumericPrecision

## Metadata Name

Numeric Precision

## Content Constraints

| Constraint    | Value                            |
|:--------------|:---------------------------------|
| Feature level | Recommended                      |
| Allows nulls  | False                            |
| Data type     | Integer                          |
| Value format  | [Numeric Format](#attr)                     |

## Version Introduced

1.0
