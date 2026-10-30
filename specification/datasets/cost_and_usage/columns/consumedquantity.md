# Consumed Quantity

The [Consumed Quantity](#col) represents the volume of a metered SKU associated with a [resource](#term) or [service](#term) used, based on the [Consumed Unit](#col). [Consumed Quantity](#col) is often derived at a finer granularity or over a different time interval when compared to the [Pricing Quantity](#col) (complementary to [Pricing Unit](#col)) and focuses on [resource](#term) and [service](#term) consumption, not pricing and cost.

## Requirements

[ConsumedQuantity](#col) MUST adhere to the following requirements:

* [ConsumedQuantity](#col) MUST be of type Decimal.
* [ConsumedQuantity](#col) MUST conform to [NumericFormat](#attr) requirements.
* [ConsumedQuantity](#col) MUST adhere to the following nullability requirements:
  * [ConsumedQuantity](#col) MUST be null when [SkuPriceId](#col) is null.
  * [ConsumedQuantity](#col) MUST be null when [ChargeCategory](#col) is not ["Usage"](#val:CostAndUsage.ChargeCategory), or when [ChargeCategory](#col) is ["Usage"](#val:CostAndUsage.ChargeCategory) and [CommitmentDiscountStatus](#col) is ["Unused"](#val:CostAndUsage.CommitmentDiscountStatus).
  * When [ChargeCategory](#col) is ["Usage"](#val:CostAndUsage.ChargeCategory) and [CommitmentDiscountStatus](#col) is not ["Unused"](#val:CostAndUsage.CommitmentDiscountStatus), [ConsumedQuantity](#col) MUST adhere to the following requirements:
    * [ConsumedQuantity](#col) MUST NOT be null when [ChargeClass](#col) is not ["Correction"](#val:CostAndUsage.ChargeClass).
    * [ConsumedQuantity](#col) MAY be null when [ChargeClass](#col) is ["Correction"](#val:CostAndUsage.ChargeClass).
* [ConsumedQuantity](#col) MUST NOT include [tokens](#term) counted on a different row with TokenCacheAction "Read" or "Write" in [SkuPriceDetails](#col) when [SkuPriceDetails](#col) on the same row includes neither value (e.g., a cached token that a usage report also counts inside a prompt token total is counted on the "Read" row only).

## Column ID

ConsumedQuantity

## Display Name

Consumed Quantity

## Description

The volume of a metered SKU associated with a [resource](#term) or [service](#term) used, based on the [Consumed Unit](#col).

## Content Constraints

| Constraint                 | Value                                       |
| :------------------------- | :------------------------------------------ |
| Dataset                    | [Cost and Usage](#ds)                       |
| Operating model conditions | [Includes Usage Measurement](#omc)                                               |
| Column type                | Metric                                      |
| Feature level              | Conditional                                 |
| Allows nulls               | True                                        |
| Data type                  | Decimal                                     |
| Value format               | [Numeric Format](#attr)                     |
| Number range               | Any valid decimal value                     |

## Version Introduced

1.0
