# SKU ID

A SKU ID is a provider-specified unique identifier that represents a specific [*SKU*](#glossary:sku). SKUs are quantifiable goods or service offerings in a [*FOCUS dataset*](#glossary:FOCUS-dataset) that represent specific functionality and technical specifications. Examples of SKUs include but are not limited to:

* A product license that is purchased or subscribed to.
* Usage of a deployed resource from direct user interaction (e.g., request count).
* Usage by a deployed resource based on the resource's configuration (e.g., running hours, storage space).

Each SKU ID represents a unique set of features can be sold at different price points or [*SKU Prices*](#glossary:sku-price). SKU ID is consistent across all pricing variations, which may differ based on multiple factors beyond the common functionality and technical specifications. Examples include but are not limited to:

* Date the charge was incurred.
* Provider agreements and contracts.
* Pricing models (e.g., flat rate, tiered, committed).
* Geographic region.
* Service Level Agreements (SLAs).
* Availability (e.g., spot VMs).

SKU ID should be consistent across pricing variations of a good or service to facilitate price comparisons for the same functionality, like where the functionality is provided or how it's paid for. SKU ID can be referenced on a catalog or [*price list*](#glossary:price-list) published by a provider to look up detailed information about the *SKU*. The composition of the properties associated with the SKU ID may differ across providers. SKU ID is commonly used for analyzing and comparing costs for the same SKU in different regions, tiers, and more.

The SkuId column adheres to the following requirements:

* SkuId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports unit pricing concepts and publishes price lists, publicly or as part of contracting.
* SkuId MUST be of type String.
* SkuId MUST conform to [String Handling](#stringhandling) requirements.
* SkuId nullability is defined as follows:
  * SkuId MUST be null when [ChargeCategory](#chargecategory) is "Tax".
  * SkuId MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
  * SkuId MAY be null in all other cases.
* SkuId MUST equal the SkuId for all other charges for the same *SKU* regardless of factors that impact the price but not the functionality.
  * SkuId MUST be consistent across billing accounts or agreements.
  * SkuId MUST be consistent across [PricingCategory](#pricingcategory) values.
  * SkuId MUST be consistent across regions.
  * SkuId MUST be consistent across service level agreement (SLA) variations..
  * SkuId MUST be consistent across availability options.
* SkuId MUST equal SkuPriceId when a provider does not offer the *SKU* with multiple pricing variations.

## Column ID

SkuId

## Display Name

SKU ID

## Description

Provider-specified unique identifier that represents a specific *SKU* (e.g., quantifiable good or service offering).

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
