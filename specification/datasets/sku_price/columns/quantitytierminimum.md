# Quantity Tier Minimum

Quantity Tier Minimum represents the exclusive lower boundary of a quantity-based pricing tier for the specified [*SKU Price*](#glossary:sku-price). This value is measured in the quantity of the designated [Pricing Unit](#datamodel.skuprice.pricingunit).

When combined with [Quantity Tier Maximum](#datamodel.skuprice.quantitytiermaximum), this column defines the exact quantity envelope for which a specific unit price applies. Service providers frequently vary the unit price by the quantity consumed, and Quantity Tier Minimum defines the quantity threshold above which the specified unit price becomes applicable. For flat-rate or non-tiered pricing models, this value is typically zero.

## Requirements

QuantityTierMinimum MUST adhere to the following requirements:

* QuantityTierMinimum MUST be of type Decimal.
* QuantityTierMinimum MUST NOT be null.
* QuantityTierMinimum MUST represent a quantity denominated in the [PricingUnit](#datamodel.skuprice.pricingunit).
* QuantityTierMinimum MUST be strictly less than [QuantityTierMaximum](#datamodel.skuprice.quantitytiermaximum) when QuantityTierMaximum is not null.
* QuantityTierMinimum MUST be the exclusive lower bound of the quantity-based pricing tier.

## Column ID

QuantityTierMinimum

## Display Name

Quantity Tier Minimum

## Description

The exclusive lower boundary of a quantity-based pricing tier, measured in the designated Pricing Unit.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [SKU Price](#datamodel.skuprice)                      |
| Conditions      | [Includes Quantity Tier Pricing](#conditions.includesquantitytierpricing) |
| Column type     | Metric                                               |
| Feature level   | Conditional                                          |
| Allows nulls    | False                                                |
| Data type       | Decimal                                              |
| Value format    | \<not specified>                                     |

## Version Introduced

1.5
