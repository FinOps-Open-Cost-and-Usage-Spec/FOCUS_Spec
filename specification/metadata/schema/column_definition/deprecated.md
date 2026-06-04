# Deprecated

The deprecation status of a column in a [Dataset Instance](#datasetinstance).

Deprecated adheres to the following requirements:

* Deprecated MUST be present in an object within the [ColumnDefinition](#columndefinition) collection when the column is planned for removal.
* Deprecated MUST be of type Boolean.
* Deprecated MUST NOT contain null values.
* Deprecated SHOULD only be "true" if the column is deprecated.
* Deprecated MUST be "true" when the data generator removes a column at a future date, or the column has been identified for deprecation for the FOCUS version identified in the schema definition.

## Metadata ID

Deprecated

## Metadata Name

Deprecated

## Content constraints

| Constraint      | Value            |
|:----------------|:-----------------|
| Feature level   | Conditional      |
| Allows nulls    | False            |
| Data type       | Boolean          |
| Value format    | \<not specified> |

## Introduced (version)

1.2
