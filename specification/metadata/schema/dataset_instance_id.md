# Dataset Instance ID

The Dataset Instance ID is a unique identifier for the specific dataset instance provided by the data generator. It identifies the dataset instance that this schema and the corresponding dataset artifacts are aligned with.

Dataset Instance ID MUST be provided in the schema metadata. Dataset Instance ID MUST be of type String and MUST NOT contain null values. Dataset Instance ID MUST be a unique identifier within a data generator.

## Metadata ID

DatasetInstanceId

## Metadata Name

Dataset Instance ID

## Content constraints

| Constraint    | Value                                     |
|:--------------|:------------------------------------------|
| Feature level | Mandatory                                 |
| Allows nulls  | False                                     |
| Data type     | String                                    |
| Value format  | Must align with a published FOCUS Dataset |

## Introduced (version)

1.3
