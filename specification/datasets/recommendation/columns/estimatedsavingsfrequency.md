# Estimated Savings Frequency

Estimated Savings Frequency represents the time basis over which the [EstimatedCostSavings](#datasets.recommendation.estimatedcostsavings) is expressed. Estimated Savings Frequency is used to normalize and compare savings estimates across recommendations and sources.

## Requirements

EstimatedSavingsFrequency MUST adhere to the following requirements:

* EstimatedSavingsFrequency MUST be of type String.
* EstimatedSavingsFrequency MUST adhere to the following nullability requirements:
  * EstimatedSavingsFrequency MUST NOT be null when EstimatedCostSavings is not null.
  * EstimatedSavingsFrequency MAY be null when EstimatedCostSavings is null.
* EstimatedSavingsFrequency MUST be one of the allowed values when not null.

## Allowed Values

| Value    | Description                                                       |
|:---------|:-----------------------------------------------------------------|
| Monthly  | The estimated savings is expressed over a one-month period.       |
| Annually | The estimated savings is expressed over a one-year period.        |
| One-Time | The estimated savings is a single, non-recurring amount.          |

## Column ID

EstimatedSavingsFrequency

## Display Name

Estimated Savings Frequency

## Description

The time basis over which the estimated cost savings is expressed.

## Content Constraints

| Constraint      | Value                                          |
| :-------------- | :--------------------------------------------- |
| Dataset         | [Recommendation](#datasets.recommendation)     |
| Column type     | Dimension                                      |
| Feature level   | Conditional                                    |
| Allows nulls    | True                                           |
| Data type       | String                                         |
| Value format    | Allowed values                                 |

## Version Introduced

1.5
