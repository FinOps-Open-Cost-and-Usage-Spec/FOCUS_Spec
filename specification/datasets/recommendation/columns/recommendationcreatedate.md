# Recommendation Create Date

Recommendation Create Date is the timestamp when the recommendation was generated. This timestamp facilitates analysis of how recommendations and their estimated savings change over time.

## Requirements

RecommendationCreateDate MUST adhere to the following requirements:

* RecommendationCreateDate MUST be of type Date/Time.
* RecommendationCreateDate MUST conform to [DateTimeFormat](#attributes.date/timeformat) requirements.
* RecommendationCreateDate MUST NOT be null.
* RecommendationCreateDate MUST represent the moment in time the recommendation was generated.

## Column ID

RecommendationCreateDate

## Display Name

Recommendation Create Date

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
