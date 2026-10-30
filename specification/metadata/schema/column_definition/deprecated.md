# Deprecated

The deprecation status of a column in a [Dataset Instance](#meta).

[Deprecated](#meta) adheres to the following requirements:

* [Deprecated](#meta) MUST be present in an object within the [ColumnDefinition](#meta) collection when the column is planned for removal.
* [Deprecated](#meta) MUST be of type Boolean.
* [Deprecated](#meta) MUST NOT contain null values.
* [Deprecated](#meta) SHOULD only be "true" when the column is deprecated.
* [Deprecated](#meta) MUST be "true" when the data generator removes a column at a future date, or the column has been identified for deprecation for the FOCUS version identified in the schema definition.

## Metadata ID

Deprecated

## Metadata Name

Deprecated

## Content Constraints

| Constraint      | Value            |
|:----------------|:-----------------|
| Feature level   | Conditional      |
| Allows nulls    | False            |
| Data type       | Boolean          |
| Value format    | \<not specified> |

## Version Introduced

1.2
