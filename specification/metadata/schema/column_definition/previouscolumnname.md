# Previous Column Name

The [PreviousColumnName](#meta) field indicates that on that schema the column where the key is included was renamed.

[PreviousColumnName](#meta) adheres to the following requirements:

* [PreviousColumnName](#meta) MUST be present in an object within the [ColumnDefinition](#meta) collection when the column was renamed.
* When [PreviousColumnName](#meta) is present, [PreviousColumnName](#meta) adheres to the following normative requirements:
  * [PreviousColumnName](#meta) MUST be of type String.
  * [PreviousColumnName](#meta) MUST not be null.
  * [PreviousColumnName](#meta) MUST be the name used in previous versions of the schema.
  * [PreviousColumnName](#meta) MUST NOT be present in schema versions created after the rename.

## Metadata ID

PreviousColumnName

## Metadata Name

Previous Column Name

## Content Constraints

| Constraint      | Value            |
|:----------------|:-----------------|
| Feature level   | Conditional      |
| Allows nulls    | False            |
| Data type       | String           |
| Value format    | \<not specified> |

## Version Introduced

1.2
