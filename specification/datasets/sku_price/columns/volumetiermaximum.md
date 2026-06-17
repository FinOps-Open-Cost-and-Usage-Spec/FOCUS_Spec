# Volume Tier Maximum

Volume Tier Maximum represents the exclusive upper boundary of a volume-based pricing tier for the specified [*SKU Price*](#glossary:sku-price). This value is measured in the quantity of the designated [Pricing Unit](#datasets.skuprice.pricingunit).

When combined with [Volume Tier Minimum](#datasets.skuprice.volumetierminimum), this column defines the exact volume envelope for which a specific unit price applies. If a unit price represents the highest volume tier (or if the offering uses a flat-rate pricing model with no volume limits), this value remains null to indicate there is no upper bound.

## Requirements

VolumeTierMaximum MUST adhere to the following requirements:

* VolumeTierMaximum MUST be of type Decimal.
* VolumeTierMaximum MUST adhere to the following nullability requirements:
  * VolumeTierMaximum MUST be null when there is no upper limit for the pricing tier.
  * VolumeTierMaximum MUST NOT be null when a subsequent, higher-volume pricing tier exists for the same offering.
* When VolumeTierMaximum is not null, VolumeTierMaximum MUST adhere to the following requirements:
  * VolumeTierMaximum MUST represent a quantity denominated in the [PricingUnit](#datasets.skuprice.pricingunit).
  * VolumeTierMaximum MUST be strictly greater than [VolumeTierMinimum](#datasets.skuprice.volumetierminimum).
  * VolumeTierMaximum MUST be the exclusive upper bound of the volume-based pricing tier.

## Implementation Guidance

Because `Volume Tier Minimum` is the inclusive lower bound and `Volume Tier Maximum` is the exclusive upper bound, the two columns define a half-open volume interval. Practitioners route a usage quantity to the tier where the quantity is greater than or equal to `Volume Tier Minimum` and strictly less than `Volume Tier Maximum`. The highest tier carries a null `Volume Tier Maximum` and has no upper bound, and adjacent tiers meet at a shared boundary value with no gap or overlap.

## Column ID

VolumeTierMaximum

## Display Name

Volume Tier Maximum

## Description

The exclusive upper boundary of a volume-based pricing tier, measured in the designated Pricing Unit.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [SKU Price](#datasets.skuprice)                      |
| Column type     | Metric                                               |
| Feature level   | Conditional                                          |
| Condition       | [Includes volume tier pricing](#conditions.includesvolumetierpricing) |
| Allows nulls    | True                                                 |
| Data type       | Decimal                                              |
| Value format    | \<not specified>                                     |

## Version Introduced

1.5
