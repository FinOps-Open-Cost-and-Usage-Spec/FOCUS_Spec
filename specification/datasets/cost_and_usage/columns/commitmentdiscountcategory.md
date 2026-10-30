# Commitment Discount Category

[Commitment Discount Category](#col) indicates whether the [commitment discount](#term) identified in the [Commitment Discount ID](#col) column is based on usage quantity or cost (aka "spend"). The [Commitment Discount Category](#col) column is only applicable to [commitment discounts](#term) and not [negotiated discounts](#term).

## Requirements

[CommitmentDiscountCategory](#col) MUST adhere to the following requirements:

* [CommitmentDiscountCategory](#col) MUST be of type String.
* [CommitmentDiscountCategory](#col) MUST adhere to the following nullability requirements:
  * [CommitmentDiscountCategory](#col) MUST be null when [CommitmentDiscountId](#col) is null.
  * [CommitmentDiscountCategory](#col) MUST NOT be null when [CommitmentDiscountId](#col) is not null.
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

Indicates whether the [commitment discount](#term) identified in the [Commitment Discount ID](#col) column is based on usage quantity or cost (aka "spend").

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

1.0-preview
