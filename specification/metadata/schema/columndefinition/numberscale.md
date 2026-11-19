# Number Scale

The number scale of the data provides the maximum number of digits after the decimal point in decimal numbers.

NumberScale adheres to the following requirements:

* NumberScale SHOULD be present in an object within the [ColumnDefinition](#metadata.schema.columndefinition) collection when the column is of Decimal data type.
* NumberScale MUST be of type Integer.
* NumberScale MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* NumberScale MUST NOT be null.

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
| Value format  | [Numeric Format](#attributes.numericformat) |

## Version Introduced

1.0
