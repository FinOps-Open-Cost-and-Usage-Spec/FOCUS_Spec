# Deprecated

The deprecation status of any column in a [*FOCUS dataset*](#glossary:FOCUS-dataset).

Deprecated MUST be provided in the FOCUS Metadata schema when a column will be removed in a future delivered schema definition. DataType MUST be of type Boolean and MUST NOT contain null values. The value of deprecated should only be "true" if the column is deprecated. Providers can choose to always provide the deprecation key or elect to only include it when the deprecation status of a column is "true". Deprecated must be "true" when the provider removes a column at a future date, or the column has been identified for deprecation for the FOCUS version identified in the schema definition.

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
