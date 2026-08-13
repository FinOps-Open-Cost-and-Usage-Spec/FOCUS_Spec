# Evaluation Period End

Evaluation Period End represents the [*exclusive end bound*](#glossary:exclusiveendbound) of the period a recommendation was derived from. For example, a recommendation derived from 30 days of observed utilization where [Evaluation Period Start](#datasets.recommendation.evaluationperiodstart) is '2024-01-01T00:00:00Z' and Evaluation Period End is '2024-01-31T00:00:00Z' includes behavior observed on January 1 since Evaluation Period Start represents the [*inclusive start bound*](#glossary:inclusivestartbound), but does not include behavior observed on January 31 since Evaluation Period End represents the *exclusive end bound*. Evaluation Period End is commonly the moment the recommendation was generated, but may be earlier, since a data generator may evaluate through the end of a prior [*period*](#glossary:period) rather than through the moment of generation. Evaluation Period End never follows Recommendation Created, since a recommendation cannot be derived from an evaluation performed after the recommendation was generated.

## Requirements

EvaluationPeriodEnd MUST adhere to the following requirements:

* EvaluationPeriodEnd MUST be of type Date/Time.
* EvaluationPeriodEnd MUST conform to [DateTimeFormat](#attributes.date/timeformat) requirements.
* EvaluationPeriodEnd MUST be the *exclusive end bound* of the period a recommendation was derived from.
* EvaluationPeriodEnd MUST adhere to the following nullability requirements:
  * EvaluationPeriodEnd MUST NOT be null when a recommendation is derived from a period of evaluation.
  * EvaluationPeriodEnd MUST be null when a recommendation is not derived from a period of evaluation.
* When EvaluationPeriodEnd is not null, EvaluationPeriodEnd MUST be less than or equal to [RecommendationCreated](#datasets.recommendation.recommendationcreated).

## Column ID

EvaluationPeriodEnd

## Display Name

Evaluation Period End

## Description

The *exclusive end bound* of the period a recommendation was derived from.

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
