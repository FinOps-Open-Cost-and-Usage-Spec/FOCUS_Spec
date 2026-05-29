# Volume Tier Name

Volume Tier Name represents a service-provider-specified display name or label for a specific volume-based pricing tier associated with a [*SKU Price*](#glossary:sku-price). 

While [Volume Tier Minimum](#datasets.skuprice.volumetierminimum) and [Volume Tier Maximum](#datasets.skuprice.volumetiermaximum) define the strict mathematical boundaries of the volume envelope, Volume Tier Name provides a human-readable identifier. This column is commonly used for displaying rate cards in reports, reconciling against vendor pricing pages, or understanding the sequential order of tiers (e.g., "First 1000 Units", "Tier 1", "Over 50 TB").

## Requirements

VolumeTierName MUST adhere to the following requirements:

* VolumeTierName MUST be of type String.
* VolumeTierName MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* VolumeTierName MAY be null.
* VolumeTierName MUST be semantically equal to the tier name or label provided in the service-provider-published [*price list*](#glossary:price-list).

## Column ID

VolumeTierName

## Display Name

Volume Tier Name

## Description

A service-provider-specified display name or label for a volume-based pricing tier.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [SKU Price](#datasets.skuprice)                      |
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Condition       | [Includes volume tier pricing](#conditions.includesvolumetierpricing) |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Version Introduced

1.5
