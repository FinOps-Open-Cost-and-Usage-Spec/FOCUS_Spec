# Quantity Tier Name

Quantity Tier Name represents a service-provider-specified display name or label for a specific quantity-based pricing tier associated with a [*SKU Price*](#glossary:sku-price).

While [Quantity Tier Minimum](#datasets.skuprice.quantitytierminimum) and [Quantity Tier Maximum](#datasets.skuprice.quantitytiermaximum) define the strict mathematical boundaries of the quantity envelope, Quantity Tier Name provides a human-readable identifier. This column is commonly used for displaying rate cards in reports, reconciling against vendor pricing pages, or understanding the sequential order of tiers (e.g., "First 1000 Units", "Tier 1", "Over 50 TB").

## Requirements

QuantityTierName MUST adhere to the following requirements:

* QuantityTierName MUST be of type String.
* QuantityTierName MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* QuantityTierName MAY be null.
* QuantityTierName MUST be semantically equal to the tier name or label provided in the service-provider-published [*price list*](#glossary:price-list).

## Column ID

QuantityTierName

## Display Name

Quantity Tier Name

## Description

A service-provider-specified display name or label for a quantity-based pricing tier.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [SKU Price](#datasets.skuprice)                      |
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Condition       | [Includes quantity tier pricing](#conditions.includesquantitytierpricing) |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Version Introduced

1.5
