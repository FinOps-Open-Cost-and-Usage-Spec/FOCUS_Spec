# String Encoding

The string encoding scheme of the column provided in the [*FOCUS dataset*](#glossary:FOCUS-dataset).

The StringEncoding property adheres to the following requirements:

* StringEncoding SHOULD be present in [ColumnDefinition](#columndefinition) object when it is required to know this information in order to successfully read the data.
* StringEncoding MUST be of type String.
* StringEncoding MUST NOT be null.

## Metadata ID

StringEncoding

## Metadata Name

StringEncoding

## Content constraints

| Constraint      | Value            |
|:----------------|:-----------------|
| Feature level   | Conditional      |
| Allows nulls    | False            |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

1.0
