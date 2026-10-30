# SKU Price ID

[SKU Price ID](#col) is a service-provider-specified unique identifier that represents a specific [SKU Price](#term). It serves as the primary reference key for a [SKU Price](#term) in a [price list](#term) published by a service provider, allowing practitioners to uniquely identify specific pricing combinations for a given [SKU](#term).

The composition of properties associated with the [SKU Price ID](#col) may differ across service providers and across [SKUs](#term) within the same service provider. However, the exclusion of dynamic or negotiable pricing properties - such as unit price amount; currency (and related exchange rates); temporal validity (e.g., effective dates); and contract- or negotiation-specific elements (e.g., contract or account identifiers, and negotiable discounts) - ensures that the [SKU Price ID](#col) remains consistent across different billing periods and billing accounts within a service provider. This consistency enables efficient tracking of price fluctuations (e.g., changes in unit price amounts) over time and across accounts. Additionally, the [SKU Price ID](#col) is commonly used to differentiate prices based on properties such as [periods](#term) and tiers.

## Requirements

[SkuPriceId](#col) MUST adhere to the following requirements:

* [SkuPriceId](#col) MUST be of type String.
* [SkuPriceId](#col) MUST conform to [StringHandling](#attr) requirements.
* [SkuPriceId](#col) MUST NOT be null.
* [SkuPriceId](#col) MUST have one and only one parent [SkuId](#col).
* [SkuPriceId](#col) MUST have one and only one [PricingUnit](#col).
* [SkuPriceId](#col) MUST have one and only one [ChargeCategory](#col).
* [SkuPriceId](#col) MUST have one and only one [QuantityTierMinimum](#col) when the [operating model](#term) [includes quantity tier pricing](#omc).
* [SkuPriceId](#col) MUST have one and only one [QuantityTierMaximum](#col) (including null) when the [operating model](#term) includes quantity tier pricing.
* [SkuPriceId](#col) MUST remain consistent over time.
* [SkuPriceId](#col) MUST remain consistent across contracts or billing agreements.
* [SkuPriceId](#col) MAY match [SkuId](#col).

## Column ID

SkuPriceId

## Display Name

SKU Price ID

## Description

A service-provider-specified unique identifier that represents a specific [SKU Price](#term).

## Content Constraints

| Constraint                 | Value                                                |
| :------------------------- | :--------------------------------------------------- |
| Dataset                    | [SKU Price](#ds)                                     |
| Operating Model Conditions | Not applicable                                       |
| Column type                | Dimension                                            |
| Feature level              | Mandatory                                            |
| Allows nulls               | False                                                |
| Data type                  | String                                               |
| Value format               | \<not specified>                                     |

## Version Introduced

Preview: 1.5
