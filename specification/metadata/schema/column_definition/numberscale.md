# Number Scale

The number scale of the data provides the maximum number of digits after the decimal point in decimal numbers.

[NumberScale](#meta) adheres to the following requirements:

* [NumberScale](#meta) SHOULD be present in an object within the [ColumnDefinition](#meta) collection when the column is of Decimal data type.
* [NumberScale](#meta) MUST be of type Integer.
* [NumberScale](#meta) MUST conform to [NumericFormat](#attr) requirements.
* [NumberScale](#meta) MUST NOT be null.

## Metadata ID

NumberScale

## Metadata Name

Number Scale

## Content Constraints

| Constraint    | Value                            |
|:--------------|:---------------------------------|
| Feature level | Recommended                      |
| Allows nulls  | False                            |
| Data type     | Integer                          |
| Value format  | [Numeric Format](#attr)                     |

## Version Introduced

1.0
