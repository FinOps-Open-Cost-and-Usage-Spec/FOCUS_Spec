# Recommended Resource Configuration

Recommended Resource Configuration represents the configuration of the [*resource*](#glossary:resource) that a recommendation proposes to change to (e.g., a smaller instance size or a newer storage tier). Recommended Resource Configuration is commonly used to show the target state of a configuration-change recommendation.

## Requirements

RecommendedResourceConfiguration MUST adhere to the following requirements:

* RecommendedResourceConfiguration MUST be of type String.
* RecommendedResourceConfiguration MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* RecommendedResourceConfiguration MUST adhere to the following nullability requirements:
  * RecommendedResourceConfiguration MUST NOT be null when a recommendation proposes a change to the configuration of a *resource*, except when the recommended change is the removal of the *resource*.
  * RecommendedResourceConfiguration MUST be null when the recommended change is the removal of the *resource*.
  * RecommendedResourceConfiguration MUST be null when a recommendation does not propose a change to the configuration of a *resource*.

## Column ID

RecommendedResourceConfiguration

## Display Name

Recommended Resource Configuration

## Description

The configuration of the *resource* that a recommendation proposes to change to.

## Content Constraints

| Constraint      | Value                                          |
| :-------------- | :--------------------------------------------- |
| Dataset         | [Recommendation](#datasets.recommendation)     |
| Column type     | Dimension                                      |
| Feature level   | Conditional                                    |
| Allows nulls    | True                                           |
| Data type       | String                                         |
| Value format    | \<not specified>                               |

## Version Introduced

1.5
