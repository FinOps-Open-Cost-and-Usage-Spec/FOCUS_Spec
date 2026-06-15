# Volume Tier Minimum

Volume Tier Minimum represents the inclusive lower boundary of a volume-based pricing tier for the specified [*SKU Price*](#glossary:sku-price). This value is measured in the quantity of the designated [Pricing Unit](#datasets.skuprice.pricingunit).

When combined with [Volume Tier Maximum](#datasets.skuprice.volumetiermaximum), this column defines the exact volume envelope for which a specific unit price applies. Service providers frequently employ step-tiered pricing models where the unit price decreases as consumption volume increases. The Volume Tier Minimum explicitly defines the volume threshold at which the specified unit price becomes applicable. For flat-rate or non-tiered pricing models, this value is typically zero.

## Requirements

VolumeTierMinimum MUST adhere to the following requirements:

* VolumeTierMinimum MUST be of type Decimal.
* VolumeTierMinimum MUST NOT be null.
* VolumeTierMinimum MUST represent a quantity denominated in the [PricingUnit](#datasets.skuprice.pricingunit).
* VolumeTierMinimum MUST be strictly less than [VolumeTierMaximum](#datasets.skuprice.volumetiermaximum) when VolumeTierMaximum is not null.

## Column ID

VolumeTierMinimum

## Display Name

Volume Tier Minimum

## Description

The inclusive lower boundary of a volume-based pricing tier, measured in the designated Pricing Unit.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [SKU Price](#datasets.skuprice)                      |
| Column type     | Metric                                               |
| Feature level   | Conditional                                          |
| Condition       | [Includes volume tier pricing](#conditions.includesvolumetierpricing) |
| Allows nulls    | False                                                |
| Data type       | Decimal                                              |
| Value format    | \<not specified>                                     |

## Version Introduced

1.5
