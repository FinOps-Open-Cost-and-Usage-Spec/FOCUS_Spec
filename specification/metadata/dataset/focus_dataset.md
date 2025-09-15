# FOCUS Dataset

The name of the FOCUS dataset for which the schema and its data conform to. This indicates which FOCUS dataset the data artifact aligns with, such as "FOCUS Cost and Usage" or "FOCUS Contract."

FOCUS Dataset MUST be provided in the metadata. FOCUS Dataset MUST be of type String and MUST NOT contain null values. FOCUS Dataset MUST match one of the published [*FOCUS datasets*](#glossary:FOCUS-dataset) of the FOCUS specification.

## Metadata ID

FOCUSDataset

## Metadata Name

FOCUS Dataset

## Content constraints

| Constraint    | Value                                     |
|:--------------|:------------------------------------------|
| Feature level | Mandatory                                 |
| Allows nulls  | False                                     |
| Data type     | String                                    |
| Value format  | Must align with a published FOCUS Dataset |

## Introduced (version)

1.3
