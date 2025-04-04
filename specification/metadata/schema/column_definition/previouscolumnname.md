# PreviousColumnName

The PreviousColumnName field indicates that on that schema the column where the key is included was renamed.

In cases where the PreviousColumnName is present, the following applies:

* PreviousColumnName MUST not be null.
* PreviousColumnName MUST be of type String.
* PreviousColumnName MUST be the name used in previous versions of the schema.
* PreviousColumnName MUST NOT be present in schema versions created after the rename.

## Metadata ID

PreviousColumnName

## Metadata Name

Previous Column Name

## Content constraints

| Constraint      | Value            |
|:----------------|:-----------------|
| Feature level   | Conditional      |
| Allows nulls    | False            |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

1.2
