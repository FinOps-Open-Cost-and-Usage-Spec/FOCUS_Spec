# Recommendation Category

Recommendation Category is the highest-level classification of a recommendation based on the domain of optimization it addresses. Each recommendation should have one and only one category that best aligns with its primary purpose. Recommendation Category is commonly used to filter recommendations to the area of practice a [*practitioner*](#glossary:practitioner) is responsible for.

## Requirements

RecommendationCategory MUST adhere to the following requirements:

* RecommendationCategory MUST be of type String.
* RecommendationCategory MUST NOT be null.
* RecommendationCategory MUST be one of the allowed values.

## Allowed Values

| Value                  | Description                                                                              |
| :--------------------- | :--------------------------------------------------------------------------------------- |
| Cost                   | Recommendations that reduce the monetary cost of resources or services.                  |
| Performance            | Recommendations that improve the performance of resources or services.                   |
| Reliability            | Recommendations that improve the resiliency or availability of resources or services.    |
| Security               | Recommendations that reduce the security risk associated with resources or services.     |
| Sustainability         | Recommendations that reduce the environmental impact of resources or services.           |
| Operational Excellence | Recommendations that improve operational processes and efficiency.                       |
| Other                  | Recommendations that do not fall into one of the defined categories.                     |

## Column ID

RecommendationCategory

## Display Name

Recommendation Category

## Description

Highest-level classification of a recommendation based on the domain of optimization it addresses.

## Content Constraints

| Constraint      | Value                                          |
| :-------------- | :--------------------------------------------- |
| Dataset         | [Recommendation](#datasets.recommendation)     |
| Column type     | Dimension                                      |
| Feature level   | Mandatory                                      |
| Allows nulls    | False                                          |
| Data type       | String                                         |
| Value format    | Allowed values                                 |

## Version Introduced

1.5
