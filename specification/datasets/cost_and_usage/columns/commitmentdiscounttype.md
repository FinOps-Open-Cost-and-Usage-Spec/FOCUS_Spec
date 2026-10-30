# Commitment Discount Type

[Commitment Discount Type](#col) is a service-provider-assigned name to identify the type of [commitment discount](#term) applied to the [row](#term). The [Commitment Discount Type](#col) column is only applicable to [commitment discounts](#term) and not [negotiated discounts](#term).

## Requirements

[CommitmentDiscountType](#col) MUST adhere to the following requirements:

* [CommitmentDiscountType](#col) MUST be of type String.
* [CommitmentDiscountType](#col) MUST conform to [StringHandling](#attr) requirements.
* [CommitmentDiscountType](#col) MUST adhere to the following nullability requirements:
  * [CommitmentDiscountType](#col) MUST be null when [CommitmentDiscountId](#col) is null.
  * [CommitmentDiscountType](#col) MUST NOT be null when [CommitmentDiscountId](#col) is not null.

## Column ID

CommitmentDiscountType

## Display Name

Commitment Discount Type

## Description

A service-provider-assigned identifier for the type of [commitment discount](#term) applied to the [row](#term).

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
