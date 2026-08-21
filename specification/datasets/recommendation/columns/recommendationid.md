# Recommendation ID

A Recommendation ID is an identifier assigned to a recommendation by the [Recommendation Provider Name](#datasets.recommendation.recommendationprovidername). The Recommendation ID is commonly used to track a recommendation over time and to deduplicate recommendations that are reported across multiple refreshes.

## Requirements

RecommendationId MUST adhere to the following requirements:

* RecommendationId MUST be of type String.
* RecommendationId MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* RecommendationId MUST NOT be null.
* RecommendationId MUST be a unique identifier within the RecommendationProviderName.
* RecommendationId MUST remain consistent over time for the same recommendation.
* RecommendationId SHOULD be a fully-qualified identifier.

## Column ID

RecommendationId

## Display Name

Recommendation ID

## Description

An identifier assigned to a recommendation by the entity that generated it.

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
