# Commitment Discount Status

[Commitment Discount Status](#col) indicates whether the [charge](#term) corresponds with the consumption of a [commitment discount](#term) identified in the [Commitment Discount ID](#col) column or the unused portion of the committed amount. The [Commitment Discount Status](#col) column is only applicable to [commitment discounts](#term) and not [negotiated discounts](#term).

## Requirements

[CommitmentDiscountStatus](#col) MUST adhere to the following requirements:

* [CommitmentDiscountStatus](#col) MUST be of type String.
* [CommitmentDiscountStatus](#col) MUST adhere to the following nullability requirements:
  * [CommitmentDiscountStatus](#col) MUST be null when [CommitmentDiscountId](#col) is null.
  * [CommitmentDiscountStatus](#col) MUST NOT be null when [CommitmentDiscountId](#col) is not null and [ChargeCategory](#col) is ["Usage"](#val:CostAndUsage.ChargeCategory).
* [CommitmentDiscountStatus](#col) MUST be one of the allowed values.
* [CommitmentDiscountStatus](#col) MUST be ["Used"](#val:CommitmentDiscountStatus) when the [charge](#term) utilizes a specific amount of a given [CommitmentDiscountId](#col).
* [CommitmentDiscountStatus](#col) MUST be ["Unused"](#val:CommitmentDiscountStatus) when the [charge](#term) represents the unused portion of the given [CommitmentDiscountId](#col).

## Allowed Values

| Value  | Description                                                             |
| :----- | :---------------------------------------------------------------------- |
| Used   | *Charges* that utilized a specific amount of a commitment discount. |
| Unused | *Charges* that represent the unused portion of the commitment discount. |

## Column ID

CommitmentDiscountStatus

## Display Name

Commitment Discount Status

## Description

Indicates whether the [charge](#term) corresponds with the consumption of a [commitment discount](#term) or the unused portion of the committed amount.

## Content Constraints

| Constraint                 | Value                                     |
| :------------------------- | :---------------------------------------- |
| Dataset                    | [Cost and Usage](#ds)                     |
| Operating model conditions | [Includes Commitment Discounts](#omc)                                                  |
| Column type                | Dimension                                 |
| Feature level              | Conditional                               |
| Allows nulls               | True                                      |
| Data type                  | String                                    |
| Value format               | Allowed values                            |

## Version Introduced

1.0
