# Numeric Precision

Numeric Precision is the maximum number of digits for the values in the column.

NumericPrecision adheres to the following requirements:

* NumberPrecision SHOULD be present in an object within the [ColumnDefinition](#metadata.schema.columndefinition) collection when the column is of Decimal data type.
* NumericPrecision MUST be of type Integer.
* NumericPrecision MUST NOT contain null values.

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
| Value format  | [Numeric Format](#attributes.numericformat) |

## Version Introduced

1.0
