# Recommendation Description

Recommendation Description is a human-readable summary of a recommendation. Recommendation Description is commonly used to convey the detail of a recommendation that is not captured by other columns.

## Requirements

RecommendationDescription MUST adhere to the following requirements:

* RecommendationDescription MUST be of type String.
* RecommendationDescription MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* RecommendationDescription MUST adhere to the following nullability requirements:
  * RecommendationDescription MUST NOT be null when a human-readable summary of the recommendation is available to the [data generator](#metadata.datagenerator).
  * RecommendationDescription MAY be null when a human-readable summary of the recommendation is not available to the data generator.

## Column ID

RecommendationDescription

## Display Name

Recommendation Description

## Description

A human-readable summary of a recommendation.

## Content Constraints

| Constraint      | Value                                          |
| :-------------- | :--------------------------------------------- |
| Dataset         | [Recommendation](#datamodel.recommendation)     |
| Column type     | Dimension                                      |
| Feature level   | Mandatory                                      |
| Allows nulls    | True                                           |
| Data type       | String                                         |
| Value format    | \<not specified>                               |

## Version Introduced

1.5
