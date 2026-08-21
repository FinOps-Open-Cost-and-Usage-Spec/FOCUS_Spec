# Sub Account Name

A Sub Account Name is a display name assigned to a [*sub account*](#glossary:sub-account). In the Recommendation dataset, the Sub Account Name is commonly used to make sub-account-scoped recommendations readable without resolving the [Sub Account ID](#datasets.recommendation.subaccountid). Sub account names are commonly used for scenarios like grouping based on organizational constructs, access management needs, and cost allocation strategies.

## Requirements

SubAccountName MUST adhere to the following requirements:

* SubAccountName MUST be of type String.
* SubAccountName MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* SubAccountName MUST adhere to the following nullability requirements:
  * SubAccountName MUST NOT be null when a display name is assigned to the *sub account* and available to the [data generator](#metadata.datagenerator).
  * SubAccountName MAY be null when no display name is assigned to the *sub account*, or when the display name is not available to the data generator.

## Column ID

SubAccountName

## Display Name

Sub Account Name

## Description

The display name assigned to a *sub account*.

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
