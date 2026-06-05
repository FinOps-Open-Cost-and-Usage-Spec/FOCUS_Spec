# Recommendation Action

Recommendation Action represents the type of optimization activity a recommendation proposes. Recommendation Action can be used to route recommendations to the team responsible for the corresponding optimization activity.

## Requirements

RecommendationAction MUST adhere to the following requirements:

* RecommendationAction MUST be of type String.
* RecommendationAction MUST NOT be null.
* RecommendationAction MUST be one of the allowed values.

## Allowed Values

| Value                 | Description                                                                                                  |
|:----------------------|:-----------------------------------------------------------------------------------------------------------|
| Rate Optimization     | Reducing the rate paid for [*resources*](#glossary:resource) or [*services*](#glossary:service) through commitment-based discounts or negotiated pricing. |
| Workload Optimization | Adjusting resource configuration or usage to improve efficiency (e.g., rightsizing, scheduling, removing idle resources). |
| Licensing & SaaS      | Optimizing software licensing or SaaS subscriptions (e.g., reclaiming unused entitlements).                 |
| Other                 | An optimization activity not covered by another allowed value.                                              |

## Column ID

RecommendationAction

## Display Name

Recommendation Action

## Description

Represents the type of optimization activity a recommendation proposes.

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
