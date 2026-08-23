# Sub Account ID

A Sub Account ID is a service-provider-assigned identifier for a [*sub account*](#glossary:sub-account). The Sub Account ID identifies the *sub account* in which the recommended change would be applied, supporting routing and roll-up of recommendations across organizational constructs.

## Requirements

SubAccountId MUST adhere to the following requirements:

* SubAccountId MUST be of type String.
* SubAccountId MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* SubAccountId MUST adhere to the following nullability requirements:
  * SubAccountId MUST be null when a recommendation is not associated with a single *sub account*.
  * SubAccountId SHOULD NOT be null when a recommendation is associated with a single *sub account*.
  * SubAccountId MAY be null when the associated *sub account* is not known to the [data generator](#metadata.datagenerator).

## Column ID

SubAccountId

## Display Name

Sub Account ID

## Description

An identifier assigned to a *sub account* by the service provider.

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
