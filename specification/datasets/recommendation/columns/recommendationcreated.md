# Recommendation Created

Recommendation Created is the timestamp when the recommendation was generated. This timestamp facilitates analysis of how recommendations and their estimated savings change over time.

## Requirements

RecommendationCreated MUST adhere to the following requirements:

* RecommendationCreated MUST be of type Date/Time.
* RecommendationCreated MUST conform to [DateTimeFormat](#attributes.date/timeformat) requirements.
* RecommendationCreated MUST NOT be null.
* RecommendationCreated MUST represent the moment in time the recommendation was generated.

## Column ID

RecommendationCreated

## Display Name

Recommendation Created

## Description

The timestamp when the recommendation was generated.

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
