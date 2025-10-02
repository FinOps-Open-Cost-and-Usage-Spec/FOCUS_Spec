# FOCUS Dataset ID

The identifier of the FOCUS dataset for which the schema and its data conform to. This indicates which FOCUS dataset the data artifact aligns with, such as "FOCUS Cost and Usage" or "FOCUS Contract."

FOCUS Dataset ID MUST be provided in the dataset instance metadata. FOCUS Dataset ID MUST be of type String and MUST NOT contain null values. FOCUS Dataset ID MUST match the Dataset ID of one of the [*FOCUS datasets*](#glossary:FOCUS-dataset) defined in the FOCUS specification.

## Metadata ID

FocusDatasetId

## Metadata Name

FOCUS Dataset ID

## Content constraints

| Constraint    | Value                                     |
|:--------------|:------------------------------------------|
| Feature level | Mandatory                                 |
| Allows nulls  | False                                     |
| Data type     | String                                    |
| Value format  | Must align with a published FOCUS Dataset |

## Introduced (version)

1.3
