# Dataset Instance Complete

Complete provides a boolean value to indicate that the time sector is considered complete by the DataGenerator.  The definition of complete is determined by the DataGenerator and should be provided in documentation provided by the DataGenerator. For Datasets that are time series, the Complete value indicates that the time sector is complete and therefore is located in as key value in a time sector.

The Complete MUST be present in the recency metadata. The Complete MUST be of type Boolean.

## Metadata ID

Complete

## Metadata Name

Complete

## Content constraints

| Constraint    | Value             |
|:--------------|:------------------|
| Feature level | Mandatory         |
| Allows nulls  | False             |
| Data type     | BOOLEAN           |
| Value format  | \<not specified>  |

## Introduced (version)

1.3
