# Quantity Tier Minimum

[Quantity Tier Minimum](#col) represents the exclusive lower boundary of a quantity-based pricing tier for the specified [SKU Price](#term). This value is measured in the quantity of the designated [Pricing Unit](#col).

When combined with [Quantity Tier Maximum](#col), this column defines the exact quantity envelope for which a specific unit price applies. Service providers frequently vary the unit price by the quantity consumed, and [Quantity Tier Minimum](#col) defines the quantity threshold above which the specified unit price becomes applicable. For flat-rate or non-tiered pricing models, this value is typically zero.

## Requirements

[QuantityTierMinimum](#col) MUST adhere to the following requirements:

* [QuantityTierMinimum](#col) MUST be of type Decimal.
* [QuantityTierMinimum](#col) MUST conform to [NumericFormat](#attr) requirements.
* [QuantityTierMinimum](#col) MUST NOT be null.
* [QuantityTierMinimum](#col) MUST be a non-negative decimal value.
* [QuantityTierMinimum](#col) MUST represent a quantity denominated in the [PricingUnit](#col).
* [QuantityTierMinimum](#col) MUST be the exclusive lower bound of the quantity-based pricing tier.

## Column ID

QuantityTierMinimum

## Display Name

Quantity Tier Minimum

## Description

The exclusive lower boundary of a quantity-based pricing tier, measured in the designated [Pricing Unit](#col).

## Content Constraints

| Constraint                 | Value                                                |
| :------------------------- | :--------------------------------------------------- |
| Dataset                    | [SKU Price](#ds)                                     |
| Operating Model Conditions | [Includes Quantity Tier Pricing](#omc)                                                  |
| Column type                | Metric                                               |
| Feature level              | Conditional                                          |
| Allows nulls               | False                                                |
| Data type                  | Decimal                                              |
| Value format               | [Numeric Format](#attr)                              |
| Number range               | Any valid non-negative decimal value                 |

## Version Introduced

Preview: 1.5
