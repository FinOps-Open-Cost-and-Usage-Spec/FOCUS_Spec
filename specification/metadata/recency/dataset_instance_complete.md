# Dataset Instance Complete

Dataset Instance Complete provides a boolean value to indicate that the dataset instance is considered complete by the DataGenerator.  The definition of complete is determined by the DataGenerator and should be provided in documentation provided by the DataGenerator. For Datasets that are time series, the Complete value indicates that the time sector is complete and therefore is located in as key value in a time sector. For datasets that are not time series, the Complete value indicates that the dataset is complete and therefore is a property of the recency object.

The Dataset Instance Complete MUST be present if the recency metadata the Dataset Instance is not a time-series dataset. For time-series datasets the field is optional. The DatasetInstanceComplete MUST be of type Boolean.

## Metadata ID

DatasetInstanceComplete

## Metadata Name

Dataset Instance Complete

## Content constraints

| Constraint    | Value             |
|:--------------|:------------------|
| Feature level | Mandatory         |
| Allows nulls  | False             |
| Data type     | BOOLEAN           |
| Value format  | \<not specified>  |

## Introduced (version)

1.3
