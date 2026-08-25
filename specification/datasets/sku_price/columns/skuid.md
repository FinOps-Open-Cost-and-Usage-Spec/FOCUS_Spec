# SKU ID

A SKU ID is a service-provider-specified unique identifier that represents a specific [*SKU*](#glossary:sku). *SKUs* are quantifiable goods or service offerings in a [*FOCUS dataset*](#glossary:FOCUS-dataset) that represent specific functionality and technical specifications. Examples of *SKUs* across different technology categories include but are not limited to:

* A recurring software license or subscription (e.g., a per-user SaaS seat).
* Usage by a deployed infrastructure resource based on its configuration (e.g., compute running hours, provisioned storage space).
* Usage driven by direct interaction, transactions, or processing volume (e.g., API request counts, AI model tokens, network data transfer).
* A discrete professional service or support offering (e.g., consulting hours, an enterprise support retainer).

Each SKU ID represents a unique set of features that can be sold at different price points or [*SKU Prices*](#glossary:sku-price). SKU ID is consistent across all pricing variations, which may differ based on multiple factors beyond the common functionality and technical specifications. Examples include but are not limited to:

* Pricing tiers (e.g., free tier or quantity-based tiers).
* Commitment discount pricing [*period*](#glossary:period) (e.g., 1 year, 3 years).
* Negotiated discounts or other contractual terms or conditions.

SKU ID is the primary identifier used to look up detailed information about the *SKU* within a catalog or [*price list*](#glossary:price-list) published by a service provider. SKU ID is commonly used to join rate card data with actual usage or to analyze price variations for the same SKU across different price details (e.g., *period*, tier, location).

## Requirements

SkuId MUST adhere to the following requirements:

* SkuId MUST be of type String.
* SkuId MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* SkuId MUST NOT be null.
* SkuId for a given *SKU* MUST adhere to the following requirements:
  * SkuId MUST remain consistent across contracts or billing agreements.
  * SkuId MUST remain consistent regardless of any other factors that might impact the price but do not affect the functionality of the *SKU*.
  * SkuId SHOULD be consistent across pricing variations of a good or service.

## Column ID

SkuId

## Display Name

SKU ID

## Description

Service-provider-specified unique identifier that represents a specific *SKU* (e.g., a quantifiable good or service offering).

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [SKU Price](#datamodel.skuprice)                      |
| Conditions      | Not applicable                                        |
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | False                                                |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Version Introduced

1.5
