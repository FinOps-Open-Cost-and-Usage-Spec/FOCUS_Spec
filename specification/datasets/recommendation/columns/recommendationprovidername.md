# Recommendation Provider Name

Recommendation Provider Name is the name of the entity that generated the recommendation. Recommendation Provider Name is used to attribute recommendations to their source and to deduplicate overlapping recommendations produced by multiple tools.

Recommendation Provider Name may differ from the [Service Provider Name](#datasets.recommendation.serviceprovidername). For example, a third-party tool may generate a recommendation about [*resources*](#glossary:resource) or [*services*](#glossary:service) provided by another service provider.

## Requirements

RecommendationProviderName MUST adhere to the following requirements:

* RecommendationProviderName MUST be of type String.
* RecommendationProviderName MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* RecommendationProviderName MUST NOT be null.

## Column ID

RecommendationProviderName

## Display Name

Recommendation Provider Name

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
