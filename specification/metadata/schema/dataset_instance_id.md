# Dataset Instance ID

The Dataset Instance ID is a unique identifier for the specific dataset instance provided by the data generator. It identifies the dataset instance that this schema and the corresponding dataset artifacts are aligned with.

DatasetInstanceId adheres to the following requirements:

* DatasetInstanceId MUST be present in an object within the [Schema](#schema) collection.
* DatasetInstanceID MUST be of type String.
* DatasetInstanceID MUST NOT be null.
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
