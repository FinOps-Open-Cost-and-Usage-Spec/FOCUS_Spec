# Data Originator Name

Data Originator Name is the name of the entity that generated the underlying financial record for the row. It preserves data provenance for the financial source when practitioners union datasets or when intermediary entities inject net-new custom charges.

## Requirements

DataOriginatorName MUST adhere to the following requirements:

* DataOriginatorName MUST be of type String.
* DataOriginatorName MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* DataOriginatorName MUST NOT be null.
* DataOriginatorName MUST represent the entity that generated the underlying financial record for the row.

## Column ID

DataOriginatorName

## Display Name

Data Originator Name

## Description

The name of the entity that generated the underlying financial record for the row.

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
