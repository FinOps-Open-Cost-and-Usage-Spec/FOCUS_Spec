# PreviousColumnName

The PreviousColumnName field indicates that on that schema the column where the key is included was renamed.

In cases where the PreviousColumnName is present, the following applies:

* The PreviousColumnName MUST not be Null
* The PreviousColumnNameof must by of type string and be the name use in previous versions of the schema. 
* The PreviousColumnName MUST NOT be present on schema versions created after the rename. 

## Metadata ID

PreviousColumnName

## Metadata Name

Previous Column Name


## Content constraints

| Constraint      | Value            |
|:----------------|:-----------------|
| Feature level   | Conditional      |
| Allows nulls    | False            |
| Data type       | Boolean          |
| Value format    | \<not specified> |

## Introduced (version)

1.2
