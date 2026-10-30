# Commitment Discount ID

A [Commitment Discount ID](#col) is the identifier assigned to a [commitment discount](#term) by the service provider. [Commitment Discount ID](#col) is commonly used for scenarios like chargeback for [commitments](#term) and savings per [commitment discount](#term). The [Commitment Discount ID](#col) column is only applicable to [commitment discounts](#term) and not [negotiated discounts](#term).

## Requirements

[CommitmentDiscountId](#col) MUST adhere to the following requirements:

* [CommitmentDiscountId](#col) MUST be of type String.
* [CommitmentDiscountId](#col) MUST conform to [StringHandling](#attr) requirements.
* [CommitmentDiscountId](#col) MUST adhere to the following nullability requirements:
  * [CommitmentDiscountId](#col) MUST be null when a [charge](#term) is not related to a [commitment discount](#term).
  * [CommitmentDiscountId](#col) MUST NOT be null when a [charge](#term) is related to a [commitment discount](#term).
* When [CommitmentDiscountId](#col) is not null, [CommitmentDiscountId](#col) MUST adhere to the following requirements:
  * [CommitmentDiscountId](#col) MUST be a unique identifier within the service provider.
  * [CommitmentDiscountId](#col) MUST be equal to [ResourceId](#col) when [ChargeCategory](#col) is ["Purchase"](#val:CostAndUsage.ChargeCategory) and the [charge](#term) represents a purchase of that [commitment discount](#term).
  * [CommitmentDiscountId](#col) MUST be equal to [ResourceId](#col) when [ChargeCategory](#col) is ["Usage"](#val:CostAndUsage.ChargeCategory) and the [charge](#term) represents an unused portion of that [commitment discount](#term).
  * [CommitmentDiscountId](#col) SHOULD be a fully-qualified identifier.

## Column ID

CommitmentDiscountId

## Display Name

Commitment Discount ID

## Description

The identifier assigned to a [commitment discount](#term) by the service provider.

## Content Constraints

| Constraint                 | Value                                     |
| :------------------------- | :---------------------------------------- |
| Dataset                    | [Cost and Usage](#ds)                     |
| Operating model conditions | [Includes Commitment Discounts](#omc)                                                  |
| Column type                | Dimension                                 |
| Feature level              | Conditional                               |
| Allows nulls               | True                                      |
| Data type                  | String                                    |
| Value format               | \<not specified>                          |

## Version Introduced

1.0-preview
