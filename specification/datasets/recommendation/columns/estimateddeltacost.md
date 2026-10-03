# Estimated Delta Cost

Estimated Delta Cost represents the estimated change in [Effective Cost](#datamodel.costandusage.effectivecost) over a 30-day period, projected from acting on a recommendation. A negative value represents a cost saving while a positive value represents an increase in cost. The 30-day period is independent of the [evaluation period](#datamodel.recommendation.evaluationperiodstart) a recommendation was derived from. Estimated Delta Cost is commonly used to prioritize recommendations.

## Requirements

EstimatedDeltaCost MUST adhere to the following requirements:

* EstimatedDeltaCost MUST be of type Decimal.
* EstimatedDeltaCost MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* EstimatedDeltaCost MUST adhere to the following nullability requirements:
  * EstimatedDeltaCost MUST NOT be null when [RecommendationCategory](#datamodel.recommendation.recommendationcategory) is "Cost".
  * EstimatedDeltaCost MAY be null when RecommendationCategory is not "Cost".
* EstimatedDeltaCost MUST be denominated in the [RecommendationCurrency](#datamodel.recommendation.recommendationcurrency).
* EstimatedDeltaCost MUST represent the estimated change in CostAndUsage.EffectiveCost over a 30-day period projected from acting on a recommendation.
* EstimatedDeltaCost MUST be negative when acting on a recommendation is projected to decrease CostAndUsage.EffectiveCost.
* EstimatedDeltaCost MUST be positive when acting on a recommendation is projected to increase CostAndUsage.EffectiveCost.

## Column ID

EstimatedDeltaCost

## Display Name

Estimated Delta Cost

## Description

The estimated change in effective cost over a 30-day period from acting on a recommendation.

## Content Constraints

| Constraint                 | Value                                       |
| :------------------------- | :------------------------------------------ |
| Dataset                    | [Recommendation](#datamodel.recommendation) |
| Operating Model Conditions | Not applicable                              |
| Column type                | Metric                                      |
| Feature level              | Mandatory                                   |
| Allows nulls               | True                                        |
| Data type                  | Decimal                                     |
| Value format               | [Numeric Format](#attributes.numericformat) |
| Number range               | Any valid decimal value                     |

## Version Introduced

1.5
