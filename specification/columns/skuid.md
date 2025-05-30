# SKU ID

A SKU ID is a provider-specified unique identifier that represents a specific [*SKU*](#glossary:sku). *SKUs* are quantifiable goods or service offerings in a [*FOCUS dataset*](#glossary:FOCUS-dataset) that represent specific functionality and technical specifications. Examples of *SKUs* include but are not limited to:

* A product license that is purchased or subscribed to.
* Usage of a deployed resource from direct user interaction (e.g., request count).
* Usage by a deployed resource based on the resource's configuration (e.g., running hours, storage space).

Each SKU ID represents a unique set of features that can be sold at different price points or [*SKU Prices*](#glossary:sku-price). SKU ID is consistent across all pricing variations, which may differ based on multiple factors beyond the common functionality and technical specifications. Examples include but are not limited to:

* Date the [*charge*](#glossary:charge) was incurred.
* Pricing tiers (e.g., free tier or volume-based tiers).
* Commitment discount pricing terms (e.g., 1 year, 3 years).
* Negotiated discounts or other contractual terms or conditions.

SKU ID should be consistent across pricing variations of a good or service to facilitate price comparisons for the same functionality, like where the functionality is provided or how it's paid for. SKU ID can be referenced on a catalog or [*price list*](#glossary:price-list) published by a provider to look up detailed information about the *SKU*. The composition of the properties associated with the SKU ID may differ across providers. SKU ID is commonly used for analyzing and comparing costs for the same SKU across different price details (e.g., term, tier, location).

The SkuId column adheres to the following requirements:

* SkuId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports unit pricing concepts and publishes price lists, publicly or as part of contracting.
* SkuId MUST be of type String.
* SkuId MUST conform to [StringHandling](#stringhandling) requirements.
* SkuId nullability is defined as follows:
  * SkuId MUST be null when [ChargeCategory](#chargecategory) is "Tax".
  * SkuId MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
  * SkuId MAY be null in all other cases.
* SkuId for a given *SKU* adheres to the following additional requirements:
  * SkuId MUST remain consistent across [*billing accounts*](#glossary:billing-account) or contracts.
  * SkuId MUST remain consistent across [PricingCategory](#pricingcategory) values.
  * SkuId MUST remain consistent regardless of any other factors that might impact the price but do not affect the functionality of the *SKU*.
* SkuId MUST be associated with a given [*resource*](#glossary:resource) or [*service*](#glossary:service) when ChargeCategory is "Usage" or "Purchase".
* SkuId MAY equal [SkuPriceId](#SkuPriceId).

## Column ID

SkuId

## Display Name

SKU ID

## Description

Provider-specified unique identifier that represents a specific *SKU* (e.g., a quantifiable good or service offering).

## Content constraints

| Constraint    | Value            |
| :------------ | :--------------- |
| Column type   | Dimension        |
| Feature level | Conditional      |
| Allows nulls  | True             |
| Data type     | String           |
| Value format  | \<not specified> |

## Introduced (version)

1.0-preview
