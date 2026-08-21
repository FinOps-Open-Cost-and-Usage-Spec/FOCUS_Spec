# Implementation Risk

Implementation Risk represents the relative level of risk associated with acting on a recommendation, as assessed by the [Recommendation Provider Name](#datasets.recommendation.recommendationprovidername). Implementation Risk is commonly used alongside [Implementation Effort](#datasets.recommendation.implementationeffort) and [Estimated Monthly Cost Impact](#datasets.recommendation.estimatedmonthlycostimpact) to prioritize recommendations against possible disruptions they may cause.

## Requirements

ImplementationRisk MUST adhere to the following requirements:

* ImplementationRisk MUST be of type String.
* ImplementationRisk MUST adhere to the following nullability requirements:
  * ImplementationRisk SHOULD NOT be null when the level of risk associated with a recommendation is known to the [data generator](#metadata.datagenerator).
  * ImplementationRisk MAY be null when the level of risk associated with a recommendation is not known to the data generator.
* ImplementationRisk MUST be one of the allowed values when not null.

## Allowed Values

| Value     | Description                                                      |
|:----------|:----------------------------------------------------------------|
| Very Low  | Minimal risk of disruption. |
| Low       | Small risk of disruption. |
| Medium    | Moderate risk of disruption. |
| High      | Significant risk of disruption. |
| Very High | Extensive risk of disruption. |

## Column ID

ImplementationRisk

## Display Name

Implementation Risk

## Description

Represents the relative level of risk associated with acting on a recommendation.

## Content Constraints

| Constraint      | Value                                          |
| :-------------- | :--------------------------------------------- |
| Dataset         | [Recommendation](#datasets.recommendation)     |
| Column type     | Dimension                                      |
| Feature level   | Optional                                       |
| Allows nulls    | True                                           |
| Data type       | String                                         |
| Value format    | Allowed values                                 |

## Version Introduced

1.5
