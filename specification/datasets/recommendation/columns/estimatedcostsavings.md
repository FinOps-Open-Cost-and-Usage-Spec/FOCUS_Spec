# Estimated Cost Savings

Estimated Cost Savings represents the estimated reduction in cost that may be realized by acting on a recommendation. Estimated Cost Savings can be used to prioritize recommendations and to quantify the aggregate opportunity across a portfolio of recommendations.

## Requirements

EstimatedCostSavings MUST adhere to the following requirements:

* EstimatedCostSavings MUST be of type Decimal.
* EstimatedCostSavings MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* EstimatedCostSavings MUST be denominated in the [BillingCurrency](#datasets.recommendation.billingcurrency).
* EstimatedCostSavings MAY be null when a savings estimate is not available.

## Column ID

EstimatedCostSavings

## Display Name

Estimated Cost Savings

## Description

The estimated reduction in cost that may be realized by acting on a recommendation.

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
