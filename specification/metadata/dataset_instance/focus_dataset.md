# FOCUS Dataset ID

The identifier of the FOCUS dataset for which the schema and its data conform to. This indicates which FOCUS dataset the data artifact aligns with, such as "FOCUS Cost and Usage" or "FOCUS Contract."

The FocusDatasetId property adheres to the following requirements:

* FocusDatasetId MUST be present in an object within the [DatasetInstance](#datasetinstance) collection.
* FocusDatasetId MUST be of type String.
* FocusDatasetId MUST NOT be null.
* FocusDatasetId MUST match the Dataset ID of one of the [*FOCUS datasets*](#glossary:FOCUS-dataset) defined in the FOCUS specification.

## Metadata ID

FocusDatasetId

## Metadata Name

FOCUS Dataset ID

## Content constraints

| Constraint    | Value            |
|:--------------|:-----------------|
| Feature level | Mandatory        |
| Allows nulls  | False            |
| Data type     | String           |
| Value format  | \<not specified> |

## Introduced (version)

1.3
