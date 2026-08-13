# Evaluation Period Start

Evaluation Period Start represents the [*inclusive start bound*](#glossary:inclusivestartbound) of the period a recommendation was derived from. For example, a recommendation derived from 30 days of observed utilization where Evaluation Period Start is '2024-01-01T00:00:00Z' and Evaluation Period End is '2024-01-31T00:00:00Z' includes behavior observed on January 1 since Evaluation Period Start represents the *inclusive start bound*, but does not include behavior observed on January 31 since Evaluation Period End represents the [*exclusive end bound*](#glossary:exclusiveendbound). A recommendation derived from the configuration of a *resource* rather than from behavior over time has an evaluation period covering the moment the configuration was assessed. Evaluation Period Start, together with Evaluation Period End, allows a [*practitioner*](#glossary:practitioner) to assess the confidence of a recommendation and to compare recommendations produced by data generators that evaluate different periods.

## Requirements

EvaluationPeriodStart MUST adhere to the following requirements:

* EvaluationPeriodStart MUST be of type Date/Time.
* EvaluationPeriodStart MUST conform to [DateTimeFormat](#attributes.date/timeformat) requirements.
* EvaluationPeriodStart MUST be the *inclusive start bound* of the period a recommendation was derived from.
* EvaluationPeriodStart MUST adhere to the following nullability requirements:
  * EvaluationPeriodStart MUST NOT be null when a recommendation is derived from a period of evaluation.
  * EvaluationPeriodStart MUST be null when a recommendation is not derived from a period of evaluation.
* When EvaluationPeriodStart is not null, EvaluationPeriodStart MUST adhere to the following requirements:
  * EvaluationPeriodStart MUST be less than [EvaluationPeriodEnd](#datasets.recommendation.evaluationperiodend).
  * EvaluationPeriodStart MUST be less than [RecommendationCreated](#datasets.recommendation.recommendationcreated).

## Column ID

EvaluationPeriodStart

## Display Name

Evaluation Period Start

## Description

The *inclusive start bound* of the period a recommendation was derived from.

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
