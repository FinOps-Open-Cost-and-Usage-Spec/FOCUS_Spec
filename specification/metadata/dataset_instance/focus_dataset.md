# FOCUS Dataset ID

The identifier of the FOCUS dataset for which the schema and its data conform to. This indicates which FOCUS dataset the data artifact aligns with, such as "FOCUS Cost and Usage" or "FOCUS Contract."

The [FocusDatasetId](#meta) property adheres to the following requirements:

* [FocusDatasetId](#meta) MUST be present in an object within the [DatasetInstance](#meta) collection.
* [FocusDatasetId](#meta) MUST be of type String.
* [FocusDatasetId](#meta) MUST NOT be null.
* [FocusDatasetId](#meta) MUST match the Dataset ID of one of the [FOCUS datasets](#term) defined in the FOCUS specification.

## Metadata ID

FocusDatasetId

## Metadata Name

FOCUS Dataset ID

## Content Constraints

| Constraint    | Value            |
|:--------------|:-----------------|
| Feature level | Mandatory        |
| Allows nulls  | False            |
| Data type     | String           |
| Value format  | \<not specified> |

## Version Introduced

1.3
