# Dataset Instance ID

The [Dataset Instance ID](#meta) is a unique identifier for the specific dataset instance provided by the data generator. It identifies the dataset instance that this schema and the corresponding dataset artifacts are aligned with.

[DatasetInstanceId](#meta) adheres to the following requirements:

* [DatasetInstanceId](#meta) MUST be present in an object within the [Schema](#meta) collection.
* DatasetInstanceID MUST be of type String.
* DatasetInstanceID MUST NOT be null.
* DatasetInstanceID MUST be a unique identifier within a data generator.

## Metadata ID

DatasetInstanceId

## Metadata Name

Dataset Instance ID

## Content Constraints

| Constraint    | Value              |
|:--------------|:-------------------|
| Feature level | Mandatory          |
| Allows nulls  | False              |
| Data type     | String             |
| Value format  | GUID (recommended) |

## Version Introduced

1.3
