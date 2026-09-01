# Quantity Tier Maximum

Quantity Tier Maximum represents the inclusive upper boundary of a quantity-based pricing tier for the specified [*SKU Price*](#glossary:sku-price). This value is measured in the quantity of the designated [Pricing Unit](#datamodel.skuprice.pricingunit).

When combined with [Quantity Tier Minimum](#datamodel.skuprice.quantitytierminimum), this column defines the exact quantity envelope for which a specific unit price applies. When a unit price represents the highest quantity tier, or the offering uses a flat-rate pricing model with no quantity limits, this value remains null to indicate there is no upper bound.

## Requirements

QuantityTierMaximum MUST adhere to the following requirements:

* QuantityTierMaximum MUST be of type Decimal.
* QuantityTierMaximum MUST adhere to the following nullability requirements:
  * QuantityTierMaximum MUST be null when there is no upper limit for the pricing tier.
  * QuantityTierMaximum MUST NOT be null when a subsequent, higher-quantity pricing tier exists for the same offering.
* When QuantityTierMaximum is not null, QuantityTierMaximum MUST adhere to the following requirements:
  * QuantityTierMaximum MUST represent a quantity denominated in the [PricingUnit](#datamodel.skuprice.pricingunit).
  * QuantityTierMaximum MUST be strictly greater than [QuantityTierMinimum](#datamodel.skuprice.quantitytierminimum).
  * QuantityTierMaximum MUST be the inclusive upper bound of the quantity-based pricing tier.

## Implementation Guidance

Because Quantity Tier Minimum is the exclusive lower bound and Quantity Tier Maximum is the inclusive upper bound, the two columns define a half-open quantity interval. A quantity falls within a tier when it is strictly greater than Quantity Tier Minimum and less than or equal to Quantity Tier Maximum. The highest tier carries a null Quantity Tier Maximum and has no upper bound, and adjacent tiers meet at a shared boundary value with no gap or overlap. These boundaries identify the tier a quantity falls within; whether the resulting unit price applies only to the units inside that tier or retroactively to all units consumed is a property of the published pricing terms for the offering rather than of the tier boundaries.

## Column ID

QuantityTierMaximum

## Display Name

Quantity Tier Maximum

## Description

The inclusive upper boundary of a quantity-based pricing tier, measured in the designated Pricing Unit.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [SKU Price](#datamodel.skuprice)                      |
| Conditions      | [Includes Quantity Tier Pricing](#conditions.includesquantitytierpricing) |
| Column type     | Metric                                               |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | Decimal                                              |
| Value format    | \<not specified>                                     |

## Version Introduced

1.5
