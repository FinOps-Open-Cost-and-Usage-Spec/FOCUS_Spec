# Commitment Discount Name

A [Commitment Discount Name](#col) is the display name assigned to a [commitment discount](#term). The [Commitment Discount Name](#col) column is only applicable to [commitment discounts](#term) and not [negotiated discounts](#term).

## Requirements

[CommitmentDiscountName](#col) MUST adhere to the following requirements:

* [CommitmentDiscountName](#col) MUST be of type String.
* [CommitmentDiscountName](#col) MUST conform to [StringHandling](#attr) requirements.
* [CommitmentDiscountName](#col) MUST adhere to the following nullability requirements:
  * [CommitmentDiscountName](#col) MUST be null when [CommitmentDiscountId](#col) is null.
  * When [CommitmentDiscountId](#col) is not null, [CommitmentDiscountName](#col) MUST adhere to the following requirements:
    * [CommitmentDiscountName](#col) MUST NOT be null when a display name can be assigned to a [commitment discount](#term).
    * [CommitmentDiscountName](#col) MAY be null when a display name cannot be assigned to a [commitment discount](#term).

## Column ID

CommitmentDiscountName

## Display Name

Commitment Discount Name

## Description

The display name assigned to a [commitment discount](#term).

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
