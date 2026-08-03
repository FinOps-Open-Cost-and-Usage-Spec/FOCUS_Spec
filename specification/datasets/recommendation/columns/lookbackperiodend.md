# Lookback Period End

Lookback Period End represents the [*exclusive end bound*](#glossary:exclusiveendbound) of the period of observed behavior a recommendation was derived from. For example, a recommendation derived from 30 days of observed utilization where [Lookback Period Start](#datasets.recommendation.lookbackperiodstart) is '2024-01-01T00:00:00Z' and Lookback Period End is '2024-01-31T00:00:00Z' includes behavior observed on January 1 since Lookback Period Start represents the [*inclusive start bound*](#glossary:inclusivestartbound), but does not include behavior observed on January 31 since Lookback Period End represents the *exclusive end bound*. Lookback Period End is commonly the moment the recommendation was generated, but may be earlier, since a data generator may observe behavior through the end of a prior [*period*](#glossary:period) rather than through the moment of generation. Lookback Period End never follows Recommendation Create Date, since a recommendation cannot be derived from behavior observed after the recommendation was generated.

## Requirements

LookbackPeriodEnd MUST adhere to the following requirements:

* LookbackPeriodEnd MUST be of type Date/Time.
* LookbackPeriodEnd MUST conform to [DateTimeFormat](#attributes.date/timeformat) requirements.
* LookbackPeriodEnd MUST be the *exclusive end bound* of the period of observed behavior a recommendation was derived from.
* LookbackPeriodEnd MUST adhere to the following nullability requirements:
  * LookbackPeriodEnd MUST NOT be null when a recommendation is derived from a period of observed behavior.
  * LookbackPeriodEnd MUST be null when a recommendation is not derived from a period of observed behavior.
* When LookbackPeriodEnd is not null, LookbackPeriodEnd MUST be less than or equal to [RecommendationCreateDate](#datasets.recommendation.recommendationcreatedate).

## Column ID

LookbackPeriodEnd

## Display Name

Lookback Period End

## Description

The *exclusive end bound* of the period of observed behavior a recommendation was derived from.

## Content Constraints

| Constraint      | Value                                              |
| :-------------- | :------------------------------------------------- |
| Dataset         | [Recommendation](#datasets.recommendation)         |
| Column type     | Dimension                                          |
| Feature level   | Optional                                           |
| Allows nulls    | True                                               |
| Data type       | Date/Time                                          |
| Value format    | [Date/Time Format](#attributes.date/timeformat)    |

## Version Introduced

1.5
