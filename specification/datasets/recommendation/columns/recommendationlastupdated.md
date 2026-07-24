# Recommendation Last Updated

Recommendation Last Updated is the timestamp when the recommendation was last updated. This timestamp helps a [*practitioner*](#glossary:practitioner) identify the most current version of a recommendation, particularly when its estimated savings or status change after it was first generated.

## Requirements

RecommendationLastUpdated MUST adhere to the following requirements:

* RecommendationLastUpdated MUST be of type Date/Time.
* RecommendationLastUpdated MUST conform to [DateTimeFormat](#attributes.date/timeformat) requirements.
* RecommendationLastUpdated MUST NOT be null.
* RecommendationLastUpdated MUST represent the most recent moment in time when any column value of the recommendation record was created or modified.
* RecommendationLastUpdated MUST be greater than or equal to [RecommendationCreated](#datasets.recommendation.recommendationcreated).

## Column ID

RecommendationLastUpdated

## Display Name

Recommendation Last Updated

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
