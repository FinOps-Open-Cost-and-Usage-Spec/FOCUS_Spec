# Dataset Instance ID

The Dataset Instance ID is a data generator-specified unique identifier that represents a specific FOCUS dataset instance provided by the data generator.

The DatasetInstanceId property adheres to the following requirements:

* DatasetInstanceId MUST be present in the [Dataset Instance](#datasetinstance) metadata section.
* DatasetInstanceId MUST be of type String.
* DatasetInstanceId MUST NOT contain null values.
* DatasetInstanceId MUST be a unique identifier within a data generator.

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
