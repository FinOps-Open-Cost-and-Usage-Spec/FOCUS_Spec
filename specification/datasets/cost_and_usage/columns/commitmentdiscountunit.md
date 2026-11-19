# Commitment Discount Unit

[Commitment Discount Unit](#col) represents the service-provider-specified measurement unit indicating how a service provider measures the [Commitment Discount Quantity](#col) of a [commitment discount](#term). The [Commitment Discount Unit](#col) column is only applicable to [commitment discounts](#term) and not [negotiated discounts](#term).

## Requirements

[CommitmentDiscountUnit](#col) MUST adhere to the following requirements:

* [CommitmentDiscountUnit](#col) MUST be of type String.
* [CommitmentDiscountUnit](#col) MUST conform to [StringHandling](#attr) requirements.
* [CommitmentDiscountUnit](#col) SHOULD conform to [UnitFormat](#attr) requirements.
* [CommitmentDiscountUnit](#col) MUST adhere to the following nullability requirements:
  * [CommitmentDiscountUnit](#col) MUST be null when [CommitmentDiscountQuantity](#col) is null.
  * [CommitmentDiscountUnit](#col) MUST NOT be null when [CommitmentDiscountQuantity](#col) is not null.
* When [CommitmentDiscountUnit](#col) is not null, [CommitmentDiscountUnit](#col) MUST adhere to the following requirements:
  * [CommitmentDiscountUnit](#col) MUST remain consistent over time for a given [CommitmentDiscountId](#col).
  * [CommitmentDiscountUnit](#col) MUST represent the unit used to measure the [commitment discount](#term).
  * When accounting for [commitment discount flexibility](#term), the [CommitmentDiscountUnit](#col) value SHOULD reflect this consideration.

See [Examples: Commitment Discount Flexibility](#appendix.examples:commitmentdiscountflexibility) for more details around [commitment discount flexibility](#term).

## Column ID

CommitmentDiscountUnit

## Display Name

Commitment Discount Unit

## Description

The service-provider-specified measurement unit indicating how a service provider measures the [Commitment Discount Quantity](#col) of a [commitment discount](#term).

## Content Constraints

| Constraint                 | Value                                     |
| :------------------------- | :---------------------------------------- |
| Dataset                    | [Cost and Usage](#ds)                     |
| Operating model conditions | [Includes Commitment Discounts](#omc)                                                  |
| Column type                | Dimension                                 |
| Feature level              | Conditional                               |
| Allows nulls               | True                                      |
| Data type                  | String                                    |
| Value format               | [Unit Format](#attr)                      |

## Version Introduced

1.1
