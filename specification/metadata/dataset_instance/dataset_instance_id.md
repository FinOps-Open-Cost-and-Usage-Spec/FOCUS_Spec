# Dataset Instance ID

The [Dataset Instance ID](#meta) is a data generator-specified unique identifier that represents a specific FOCUS dataset instance provided by the data generator.

[DatasetInstanceId](#meta) adheres to the following requirements:

* [DatasetInstanceId](#meta) MUST be present in an object within the [DatasetInstance](#meta) collection.
* [DatasetInstanceId](#meta) MUST be of type String.
* [DatasetInstanceId](#meta) MUST NOT contain null values.
* [DatasetInstanceId](#meta) MUST be a unique identifier within a data generator.
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
