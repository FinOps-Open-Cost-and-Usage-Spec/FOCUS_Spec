# Dataset Instance ID

The Dataset Instance ID is a data generator-specified unique identifier that represents a specific FOCUS dataset instance provided by the data generator.

DatasetInstanceId adheres to the following requirements:

* DatasetInstanceId MUST be present in an object within the [DatasetInstance](#metadata.datasetinstance) collection.
* DatasetInstanceId MUST be of type String.
* DatasetInstanceId MUST NOT contain null values.
* DatasetInstanceId MUST be a unique identifier within a data generator.
* DatasetInstanceId SHOULD be a Globally Unique Identifier (GUID).

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
