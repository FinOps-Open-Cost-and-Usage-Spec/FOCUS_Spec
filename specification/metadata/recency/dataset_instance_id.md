# Dataset Instance ID

The [Dataset Instance ID](#meta) provides the reference item to associate which Dataset Instance the recency metadata is for.

[DatasetInstanceId](#meta) adheres to the following requirements:

* [DatasetInstanceId](#meta) MUST be present in an object within the [Recency](#meta) collection.
* [DatasetInstanceId](#meta) MUST be of type String.
* [DatasetInstanceId](#meta) MUST NOT be null.
* [DatasetInstanceId](#meta) SHOULD be a Globally Unique Identifier (GUID).

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
