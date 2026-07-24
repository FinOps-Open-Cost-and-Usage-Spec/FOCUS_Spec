# Recommendation Status

Recommendation Status represents the position of a recommendation within its lifecycle. Recommendation Status is used to distinguish recommendations that are still actionable from those that have already been resolved.

## Requirements

RecommendationStatus MUST adhere to the following requirements:

* RecommendationStatus MUST be of type String.
* RecommendationStatus MUST NOT be null.
* RecommendationStatus MUST be one of the allowed values.

## Allowed Values

| Value       | Description                                                                          |
|:------------|:-------------------------------------------------------------------------------------|
| Open        | The recommendation is active and available to be acted upon.                         |
| Deferred    | The recommendation is valid but action has been postponed to a later date.           |
| Dismissed   | The recommendation has been reviewed and a decision was made not to act upon it.     |
| Implemented | The action described by the recommendation has been performed.                       |
| Expired     | The recommendation is no longer valid.                                               |

## Column ID

RecommendationStatus

## Display Name

Recommendation Status

## Description

Represents the position of a recommendation within its lifecycle.

## Content Constraints

| Constraint      | Value                                          |
| :-------------- | :--------------------------------------------- |
| Dataset         | [Recommendation](#datasets.recommendation)     |
| Column type     | Dimension                                      |
| Feature level   | Mandatory                                      |
| Allows nulls    | False                                          |
| Data type       | String                                         |
| Value format    | Allowed values                                 |

## Version Introduced

1.5
