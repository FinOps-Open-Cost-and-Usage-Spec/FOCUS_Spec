# Estimated Monthly Cost Impact

Estimated Monthly Cost Impact represents the estimated change in cost, over a one-month period, projected from acting on a recommendation. A negative value represents a cost saving while a positive value represents an increase in cost. Estimated Monthly Cost Impact can be used to prioritize recommendations and to quantify the aggregate opportunity across a portfolio of recommendations without normalizing across different time windows.

## Requirements

EstimatedMonthlyCostImpact MUST adhere to the following requirements:

* EstimatedMonthlyCostImpact MUST be of type Decimal.
* EstimatedMonthlyCostImpact MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* EstimatedMonthlyCostImpact MUST be denominated in the [Currency](#datasets.recommendation.currency).
* EstimatedMonthlyCostImpact MUST represent the estimated cost change over a one-month period.
* EstimatedMonthlyCostImpact MUST adhere to the following nullability requirements:
  * EstimatedMonthlyCostImpact MUST NOT be null when [RecommendationCategory](#datasets.recommendation.recommendationcategory) is "Cost".
  * EstimatedMonthlyCostImpact MAY be null when RecommendationCategory is not "Cost".

## Column ID

EstimatedMonthlyCostImpact

## Display Name

Estimated Monthly Cost Impact

## Description

The estimated change in cost, over a one-month period, projected from acting on a recommendation, where a negative value is a saving and a positive value is a cost increase.

## Content Constraints

| Constraint      | Value                                          |
| :-------------- | :--------------------------------------------- |
| Dataset         | [Recommendation](#datasets.recommendation)     |
| Column type     | Metric                                         |
| Feature level   | Mandatory                                      |
| Allows nulls    | True                                           |
| Data type       | Decimal                                        |
| Value format    | [Numeric Format](#attributes.numericformat)    |
| Number range    | Any valid decimal value                        |

## Version Introduced

1.5
