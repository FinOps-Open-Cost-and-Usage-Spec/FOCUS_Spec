# Deprecated

The deprecation status of any column in a [*FOCUS dataset*](#glossary:FOCUS-dataset).

The Deprecated property adheres to the following requirements:

* Deprecated MUST be provided in the FOCUS Metadata schema when a column will be removed in a future delivered schema definition.
* Deprecated MUST be of type Boolean.
* Deprecated MUST NOT contain null values.
* Deprecated should only be "true" if the column is deprecated.
* Deprecated MUST be "true" when the provider removes a column at a future date, or the column has been identified for deprecation for the FOCUS version identified in the schema definition.
* Data generators MAY provide the deprecation key when the deprecation status of a column is "true".

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
