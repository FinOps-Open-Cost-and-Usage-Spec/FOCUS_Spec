# Lookback Period Start

Lookback Period Start represents the [*inclusive start bound*](#glossary:inclusivestartbound) of the period of observed behavior a recommendation was derived from. For example, a recommendation derived from 30 days of observed utilization where Lookback Period Start is '2024-01-01T00:00:00Z' and [Lookback Period End](#datasets.recommendation.lookbackperiodend) is '2024-01-31T00:00:00Z' includes behavior observed on January 1 since Lookback Period Start represents the *inclusive start bound*, but does not include behavior observed on January 31 since Lookback Period End represents the [*exclusive end bound*](#glossary:exclusiveendbound). Lookback Period Start, together with Lookback Period End, allows a [*practitioner*](#glossary:practitioner) to assess the confidence of a recommendation and to compare recommendations produced by data generators that observe different windows.

## Requirements

LookbackPeriodStart MUST adhere to the following requirements:

* LookbackPeriodStart MUST be of type Date/Time.
* LookbackPeriodStart MUST conform to [DateTimeFormat](#attributes.date/timeformat) requirements.
* LookbackPeriodStart MUST be the *inclusive start bound* of the period of observed behavior a recommendation was derived from.
* LookbackPeriodStart MUST be less than LookbackPeriodEnd.
* LookbackPeriodStart MUST be less than [RecommendationCreateDate](#datasets.recommendation.recommendationcreatedate).
* LookbackPeriodStart MUST adhere to the following nullability requirements:
  * LookbackPeriodStart MUST NOT be null when a recommendation is derived from a period of observed behavior.
  * LookbackPeriodStart MUST be null when a recommendation is not derived from a period of observed behavior.

## Column ID

LookbackPeriodStart

## Display Name

Lookback Period Start

## Description

The *inclusive start bound* of the period of observed behavior a recommendation was derived from.

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
