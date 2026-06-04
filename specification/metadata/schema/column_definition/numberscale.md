# Number Scale

The number scale of the data provides the maximum number of digits after the decimal point in decimal numbers.

NumberScale adheres to the following requirements:

* NumberScale SHOULD be present in an object within the [ColumnDefinition](#columndefinition) collection when the column is of Decimal data type.
* NumberScale MUST be of type Integer.
* NumberScale MUST conform to [NumericFormat](#numericformat) requirements.
* NumberScale MUST NOT be null.

## Metadata ID

NumberScale

## Metadata Name

Number Scale

## Content constraints

| Constraint    | Value                            |
|:--------------|:---------------------------------|
| Feature level | Recommended                      |
| Allows nulls  | False                            |
| Data type     | Integer                          |
| Value format  | [Numeric Format](#numericformat) |

## Introduced (version)

1.0
