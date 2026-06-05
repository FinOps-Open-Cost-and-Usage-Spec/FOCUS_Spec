# Data Generator Name

Data Generator Name is the name of the entity that generated the recommendation. Data Generator Name is used to attribute recommendations to their source and to deduplicate overlapping recommendations produced by multiple tools.

Data Generator Name MAY differ from the [Service Provider Name](#datasets.recommendation.serviceprovidername). For example, a third-party tool may generate a recommendation about [*resources*](#glossary:resource) or [*services*](#glossary:service) provided by another service provider.

## Requirements

DataGeneratorName MUST adhere to the following requirements:

* DataGeneratorName MUST be of type String.
* DataGeneratorName MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* DataGeneratorName MUST NOT be null.

## Column ID

DataGeneratorName

## Display Name

Data Generator Name

## Description

The name of the entity that generated the recommendation.

## Content Constraints

| Constraint      | Value                                          |
| :-------------- | :--------------------------------------------- |
| Dataset         | [Recommendation](#datasets.recommendation)     |
| Column type     | Dimension                                      |
| Feature level   | Mandatory                                      |
| Allows nulls    | False                                          |
| Data type       | String                                         |
| Value format    | \<not specified>                               |

## Version Introduced

1.5
