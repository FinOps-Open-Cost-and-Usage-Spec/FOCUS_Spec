# Current Resource Configuration

Current Resource Configuration represents the configuration of the [*resource*](#glossary:resource) targeted by a recommendation before the recommended change is applied (e.g., an instance size or a storage tier). Current Resource Configuration is commonly used to show the starting point of a configuration-change recommendation.

## Requirements

CurrentResourceConfiguration MUST adhere to the following requirements:

* CurrentResourceConfiguration MUST be of type String.
* CurrentResourceConfiguration MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* CurrentResourceConfiguration MUST adhere to the following nullability requirements:
  * CurrentResourceConfiguration MUST NOT be null when a recommendation proposes a change to the configuration of a *resource*.
  * CurrentResourceConfiguration MUST be null when a recommendation does not propose a change to the configuration of a *resource*.

## Column ID

CurrentResourceConfiguration

## Display Name

Current Resource Configuration

## Description

The configuration of the *resource* targeted by a recommendation before the recommended change is applied.

## Content Constraints

| Constraint      | Value                                          |
| :-------------- | :--------------------------------------------- |
| Dataset         | [Recommendation](#datasets.recommendation)     |
| Column type     | Dimension                                      |
| Feature level   | Conditional                                    |
| Allows nulls    | True                                           |
| Data type       | String                                         |
| Value format    | \<not specified>                               |

## Version Introduced

1.5
