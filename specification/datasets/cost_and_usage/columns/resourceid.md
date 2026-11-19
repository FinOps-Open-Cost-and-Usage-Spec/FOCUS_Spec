# Resource ID

A [Resource ID](#col) is an identifier assigned to a [resource](#term) by the service provider. The [Resource ID](#col) is commonly used for cost reporting, analysis, and allocation scenarios.

## Requirements

[ResourceId](#col) MUST adhere to the following requirements:

* [ResourceId](#col) MUST be of type String.
* [ResourceId](#col) MUST conform to [StringHandling](#attr) requirements.
* [ResourceId](#col) MUST adhere to the following nullability requirements:
  * [ResourceId](#col) MUST be null when a [charge](#term) is not related to a [resource](#term).
  * [ResourceId](#col) MUST NOT be null when a [charge](#term) is related to a [resource](#term).
* When [ResourceId](#col) is not null, [ResourceId](#col) MUST adhere to the following requirements:
  * [ResourceId](#col) MUST be a unique identifier within the service provider.
  * [ResourceId](#col) SHOULD be a fully-qualified identifier.
  * [ResourceId](#col) MUST be the identifier of the [resource](#term) that received the [commitment discount](#term) when [CommitmentDiscountStatus](#col) is ["Used"](#val:CostAndUsage.CommitmentDiscountStatus).

## Column ID

ResourceId

## Display Name

Resource ID

## Description

Identifier assigned to a [resource](#term) by the service provider.

## Content Constraints

| Constraint                 | Value                                     |
| :------------------------- | :---------------------------------------- |
| Dataset                    | [Cost and Usage](#ds)                     |
| Operating model conditions | [Includes Provisioned Resources](#omc)                                                   |
| Column type                | Dimension                                 |
| Feature level              | Conditional                               |
| Allows nulls               | True                                      |
| Data type                  | String                                    |
| Value format               | \<not specified>                          |

## Version Introduced

0.5
