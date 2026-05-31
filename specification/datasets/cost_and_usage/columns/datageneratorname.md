# Data Generator Name

Data Generator Name is the name of the entity responsible for constructing and delivering a [*dataset artifact*](#glossary:dataset-artifact). It preserves per-row data provenance and traceability when practitioners union multiple *dataset artifacts* for multi-provider analysis, explicitly separating the entity providing services from the entity providing data.

## Requirements

DataGeneratorName MUST adhere to the following requirements:

* DataGeneratorName MUST be of type String.
* DataGeneratorName MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* DataGeneratorName MUST NOT be null.
* DataGeneratorName MUST represent the entity that generated the *dataset artifact*.
* DataGeneratorName MUST contain the identical value for every row within the *dataset artifact*.

## Column ID

DataGeneratorName

## Display Name

Data Generator Name

## Description

The name of the entity responsible for constructing and delivering a *dataset artifact*.

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
