# Implementation Effort

Implementation Effort represents the relative level of effort to act on a recommendation, as assessed by the [Data Generator Name](#datasets.recommendation.datageneratorname). Implementation Effort is commonly used to balance [Estimated Monthly Cost Impact](#datasets.recommendation.estimatedmonthlycostimpact) against the work needed to realize it.

## Requirements

ImplementationEffort MUST adhere to the following requirements:

* ImplementationEffort MUST be of type String.
* ImplementationEffort MAY be null when the level of effort to act on a recommendation is not available.
* ImplementationEffort MUST be one of the allowed values when not null.

## Allowed Values

| Value     | Description                                            |
|:----------|:-------------------------------------------------------|
| Very Low  | Requires minimal effort to implement.                  |
| Low       | Requires a small amount of effort to implement.        |
| Medium    | Requires a moderate amount of effort to implement.     |
| High      | Requires a significant amount of effort to implement.  |
| Very High | Requires an extensive amount of effort to implement.   |

## Column ID

ImplementationEffort

## Display Name

Implementation Effort

## Description

Represents the relative level of effort to act on a recommendation.

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
