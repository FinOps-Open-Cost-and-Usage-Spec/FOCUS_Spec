# SKU Price ID

SKU Price ID is a provider-specified unique identifier that represents a specific [*SKU Price*](#glossary:sku-price) associated with a [*resource*](#glossary:resource) or [*service*](#glossary:service) used or purchased. It serves as a key reference for a *SKU Price* in a [*price list*](#glossary:price-list) published by a provider, allowing practitioners to look up detailed information about the *SKU Price*.

The composition of properties associated with the SKU Price ID may differ across providers and across *SKUs* within the same provider. However, the exclusion of dynamic or negotiable pricing properties, such as unit price amount, currency (and related exchange rates), temporal validity (e.g., effective dates), and contract- or negotiation-specific elements (e.g., contract or account identifiers, and negotiable discounts), ensures that the SKU Price ID remains consistent across different billing periods and billing accounts within a provider. This consistency enables efficient filtering of [*charges*](#glossary:charge) to track price fluctuations (e.g., changes in unit price amounts) over time and across billing accounts, for both list and contracted unit prices. Additionally, the SKU Price ID is commonly used to analyze costs based on pricing properties such as terms and tiers.

The SkuPriceId column adheres to the following requirements:

* SkuPriceId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports unit pricing concepts and publishes *price lists*, publicly or as part of contracting.
* SkuPriceId MUST be of type String.
* SkuPriceId MUST conform to [String Handling](#stringhandling) requirements.
* SkuPriceId nullability is defined as follows:
  * SkuPriceId MUST be null when [ChargeCategory](#chargecategory) is "Tax".
  * SkuPriceId MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
  * SkuPriceId MAY be null in all other cases.
* When SkuPriceId is not null, SkuPriceId adheres to the following additional requirements:
  * SkuPriceId MUST have one and only one parent [SkuId](#skuid).
  * SkuPriceId MUST remain consistent over time.
  * SkuPriceId MUST remain consistent across [*billing accounts*](#glossary:billing-account) or contracts.
  * SkuPriceId MAY equal SkuId.
  * SkuPriceId MUST be associated with a given [*resource*](#glossary:resource) or [*service*](#glossary:service) used or purchased.
  * SkuPriceId MUST serve as a reference for a *SKU price* in a provider-supplied *price list*, allowing lookup of detailed information about the *SKU Price*.
  * SkuPriceId MUST enable lookup of the given [ListUnitPrice](#listunitprice) in a provider-supplied *price list* when the provider publishes unit prices exclusive of discounts.
  * SkuPriceId MUST enable lookup of the given [ContractedUnitPrice](#contractedunitprice) in a provider-supplied *price list* when the provider supports negotiated pricing concepts.

## Column ID

SkuPriceId

## Display Name

SKU Price ID

## Description

A provider-specified unique identifier that represents a specific *SKU Price* associated with a *resource* or *service* used or purchased.

## Content constraints

| Constraint       | Value          |
| :--------------- | :------------- |
| Column type      | Dimension      |
| Feature level    | Conditional    |
| Allows nulls     | True           |
| Data type        | String         |
| Value format     | \<not specified> |

## Introduced (version)

1.0-preview
