# Commitment Discount Category

[Commitment Discount Category](#col) indicates whether the [commitment discount](#term) a [SKU Price](#ds) record relates to is based on usage quantity or cost (aka "spend"). The [CommitmentDiscountCategory](#col) column is only applicable to [commitment discounts](#term) and not [negotiated discounts](#term).

## Requirements

[CommitmentDiscountCategory](#col) MUST adhere to the following requirements:

* [CommitmentDiscountCategory](#col) MUST be of type String.
* [CommitmentDiscountCategory](#col) MUST adhere to the following nullability requirements:
  * [CommitmentDiscountCategory](#col) MUST be null when the SkuPrice record does not represent the purchase of a commitment discount or a usage rate that applies under a commitment discount.
  * [CommitmentDiscountCategory](#col) MUST NOT be null when the SkuPrice record represents the purchase of a commitment discount or a usage rate that applies under a commitment discount.
* [CommitmentDiscountCategory](#col) MUST be one of the allowed values.

## Allowed Values

| Value   | Description                                                              |
|:--------|:-------------------------------------------------------------------------|
| Spend   | Commitment discounts that require a predetermined amount of spend. |
| Usage   | Commitment discounts that require a predetermined amount of usage. |

## Column ID

CommitmentDiscountCategory

## Display Name

Commitment Discount Category

## Description

Indicates whether the [commitment discount](#term) a SKU Price record relates to is based on usage quantity or cost (aka "spend").

## Content Constraints

| Constraint                 | Value                                     |
| :------------------------- | :---------------------------------------- |
| Dataset                    | [SKU Price](#ds)                 |
| Operating Model Conditions | [Includes Commitment Discounts](#omc)                                                  |
| Column type                | Dimension                                 |
| Feature level              | Conditional                               |
| Allows nulls               | True                                      |
| Data type                  | String                                    |
| Value format               | Allowed values                            |

## Version Introduced

Preview: 1.5
