# Dataset Instance ID

The Dataset Instance ID provides the reference item to associate which Dataset Instance the recency metadata is for.

DatasetInstanceId adheres to the following requirements:

* DatasetInstanceId MUST be present in an object within the [Recency](#recency) collection.
* DatasetInstanceId MUST be of type String.
* DatasetInstanceId MUST NOT be null.
* DatasetInstanceId SHOULD be a Globally Unique Identifier (GUID).

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
