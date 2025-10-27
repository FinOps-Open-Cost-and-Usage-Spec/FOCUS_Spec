# Dataset Instance ID

The Dataset Instance ID is a unique identifier for the specific dataset instance provided by the data generator. It identifies the dataset instance that this schema and the corresponding dataset artifacts are aligned with.

The DatasetInstanceId property adheres to the following requirements:

* DatasetInstanceID MUST be provided in the schema metadata.
* DatasetInstanceID MUST be of type String.
* DatasetInstanceID MUST NOT contain null values.
* DatasetInstanceID MUST be a unique identifier within a data generator.

## Metadata ID

DatasetInstanceId

## Metadata Name

Dataset Instance ID

## Content constraints

| Constraint    | Value              |
|:--------------|:-------------------|
| Feature level | Mandatory          |
| Allows nulls  | False              |
| Data type     | String             |
| Value format  | GUID (recommended) |

## Introduced (version)

1.3
