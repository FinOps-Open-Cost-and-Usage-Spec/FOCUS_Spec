# Recommendation Update Date

Recommendation Update Date is the timestamp when the recommendation was last updated. This timestamp helps a [*practitioner*](#glossary:practitioner) identify the most current version of a recommendation, particularly when its estimated savings or status change after it was first generated.

## Requirements

RecommendationUpdateDate MUST adhere to the following requirements:

* RecommendationUpdateDate MUST be of type Date/Time.
* RecommendationUpdateDate MUST conform to [DateTimeFormat](#attributes.date/timeformat) requirements.
* RecommendationUpdateDate MUST NOT be null.
* RecommendationUpdateDate MUST represent the most recent moment in time when any column value of the recommendation record was created or modified.
* RecommendationUpdateDate MUST be greater than or equal to [RecommendationCreateDate](#datasets.recommendation.recommendationcreatedate).

## Column ID

RecommendationUpdateDate

## Display Name

Recommendation Update Date

## Description

The timestamp when the recommendation was last updated.

## Content Constraints

| Constraint      | Value                                              |
| :-------------- | :------------------------------------------------- |
| Dataset         | [Recommendation](#datasets.recommendation)         |
| Column type     | Dimension                                          |
| Feature level   | Mandatory                                          |
| Allows nulls    | False                                              |
| Data type       | Date/Time                                          |
| Value format    | [Date/Time Format](#attributes.date/timeformat)    |

## Version Introduced

1.5
