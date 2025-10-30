# Dataset Instance Complete

Dataset Instance Complete provides a boolean value to indicate that the dataset instance is considered complete by the Data Generator.  The definition of complete is determined by the Data Generator and should be provided in documentation provided by the Data Generator. For Datasets that are time series, the Complete value indicates that the time sector is complete and therefore is located in as key value in a time sector. For datasets that are not time series, a value of "true" indicates that the dataset is complete and therefore is a property of the recency object.

DatasetInstanceComplete adheres to the following requirements:

* DatasetInstanceComplete MUST be present in an object within the [Recency](#recency) collection when the the dataset instance is not a time-series dataset.
* DatasetInstanceComplete MUST be of type Boolean.
* DatasetInstanceComplete MUST NOT be null.

## Metadata ID

DatasetInstanceComplete

## Metadata Name

Dataset Instance Complete

## Content constraints

| Constraint    | Value             |
|:--------------|:------------------|
| Feature level | Conditional       |
| Allows nulls  | False             |
| Data type     | Boolean           |
| Value format  | \<not specified>  |

## Introduced (version)

1.3
