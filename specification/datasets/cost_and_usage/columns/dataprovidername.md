# Data Provider Name

Data Provider Name is the name of the entity responsible for delivering the [*dataset artifact*](#glossary:dataset-artifact). It identifies the immediate upstream source that finalized and distributed the file, explicitly separating the entity delivering the data from the entity that originated the financial records.

## Requirements

DataProviderName MUST adhere to the following requirements:

* DataProviderName MUST be of type String.
* DataProviderName MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* DataProviderName MUST NOT be null.
* DataProviderName MUST represent the entity that delivered the *dataset artifact*.
* DataProviderName MUST contain the identical value for every row within the *dataset artifact*.

## Column ID

DataProviderName

## Display Name

Data Provider Name

## Description

The name of the entity responsible for delivering the *dataset artifact*.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [Cost and Usage](#datasets.costandusage)             |
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | False                                                |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Version Introduced

1.5
