# SKU Price ID

SKU Price ID is a service-provider-specified unique identifier that represents a specific [*SKU Price*](#glossary:sku-price). It serves as the primary reference key for a *SKU Price* in a [*price list*](#glossary:price-list) published by a service provider, allowing practitioners to uniquely identify specific pricing combinations for a given [*SKU*](#glossary:sku).

The composition of properties associated with the SKU Price ID may differ across service providers and across *SKUs* within the same service provider. However, the exclusion of dynamic or negotiable pricing properties - such as unit price amount; currency (and related exchange rates); temporal validity (e.g., effective dates); and contract- or negotiation-specific elements (e.g., contract or account identifiers, and negotiable discounts) - ensures that the SKU Price ID remains consistent across different billing periods and billing accounts within a service provider. This consistency enables efficient tracking of price fluctuations (e.g., changes in unit price amounts) over time and across accounts. Additionally, the SKU Price ID is commonly used to differentiate prices based on properties such as [*periods*](#glossary:period) and tiers.

## Requirements

SkuPriceId MUST adhere to the following requirements:

* SkuPriceId MUST be of type String.
* SkuPriceId MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* SkuPriceId MUST NOT be null.
* SkuPriceId MUST have one and only one parent [SkuId](#datamodel.skuprice.skuid).
* SkuPriceId MUST remain consistent over time.
* SkuPriceId MUST remain consistent across contracts or billing agreements.
* SkuPriceId MAY match SkuId.

## Column ID

SkuPriceId

## Display Name

SKU Price ID

## Description

A service-provider-specified unique identifier that represents a specific *SKU Price*.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [SKU Price](#datamodel.skuprice)                      |
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | False                                                |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Version Introduced

1.5
