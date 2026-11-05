# Pricing Quantity

The [Pricing Quantity](#col) represents the volume of a given [SKU](#term) associated with a [resource](#term) or [service](#term) used or purchased, based on the [Pricing Unit](#col). Distinct from [Consumed Quantity](#col) (complementary to [Consumed Unit](#col)), it focuses on pricing and cost, not [resource](#term) and [service](#term) consumption.

## Requirements

[PricingQuantity](#col) MUST adhere to the following requirements:

* [PricingQuantity](#col) MUST be of type Decimal.
* [PricingQuantity](#col) MUST conform to [NumericFormat](#attr) requirements.
* [PricingQuantity](#col) MUST adhere to the following nullability requirements:
  * [PricingQuantity](#col) MUST be null when [SkuPriceId](#col) is null.
  * [PricingQuantity](#col) MUST be null when [ChargeCategory](#col) is ["Tax"](#val:CostAndUsage.ChargeCategory).
  * [PricingQuantity](#col) MUST NOT be null when [ChargeCategory](#col) is ["Usage"](#val:CostAndUsage.ChargeCategory) or "Purchase" and [ChargeClass](#col) is not ["Correction"](#val:CostAndUsage.ChargeClass).
  * [PricingQuantity](#col) MAY be null in all other cases.

## Usability Constraints

**Aggregation:** When aggregating [Pricing Quantity](#col) per [SKU ID](#col) for a SKU that includes both [covering charges](#term) and their [covered charges](#term), exclude one or the other, based on the specific use case, to avoid double counting. The appropriate set to exclude depends on the relevant cost basis for the use case. Exclude [covered charges](#term) when aggregating on a billed basis, or [covering charges](#term) when aggregating on an accrual basis.

## Column ID

PricingQuantity

## Display Name

Pricing Quantity

## Description

The volume of a given [SKU](#term) associated with a [resource](#term) or [service](#term) used or purchased, based on the [Pricing Unit](#col).

## Content Constraints

| Constraint                 | Value                                       |
| :------------------------- | :------------------------------------------ |
| Dataset                    | [Cost and Usage](#ds)                       |
| Operating model conditions | Not applicable                              |
| Column type                | Metric                                      |
| Feature level              | Mandatory                                   |
| Allows nulls               | True                                        |
| Data type                  | Decimal                                     |
| Value format               | [Numeric Format](#attr)                     |
| Number range               | Any valid decimal value                     |

## Version Introduced

1.0-preview
