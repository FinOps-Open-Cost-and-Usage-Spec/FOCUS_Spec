# SKU ID

A [SKU ID](#col) is a service-provider-specified unique identifier that represents a specific [SKU](#term). [SKUs](#term) are quantifiable goods or service offerings in a [FOCUS dataset](#term) that represent specific functionality and technical specifications. Examples of [SKUs](#term) across different technology categories include but are not limited to:

* A recurring software license or subscription (e.g., a per-user SaaS seat).
* Usage by a deployed infrastructure resource based on its configuration (e.g., compute running hours, provisioned storage space).
* Usage driven by direct interaction, transactions, or processing volume (e.g., API request counts, AI model tokens, network data transfer).
* A discrete professional service or support offering (e.g., consulting hours, an enterprise support retainer).

Each [SKU ID](#col) represents a unique set of features that can be sold at different price points or [SKU Prices](#term). [SKU ID](#col) is consistent across all pricing variations, which may differ based on multiple factors beyond the common functionality and technical specifications. Examples include but are not limited to:

* Pricing tiers (e.g., free tier or quantity-based tiers).
* Commitment discount pricing [period](#term) (e.g., 1 year, 3 years).
* Negotiated discounts or other contractual terms or conditions.

[SKU ID](#col) is the primary identifier used to look up detailed information about the [SKU](#term) within a catalog or [price list](#term) published by a service provider. [SKU ID](#col) is commonly used to join rate card data with actual usage or to analyze price variations for the same SKU across different price details (e.g., [period](#term), tier, location).

## Requirements

[SkuId](#col) MUST adhere to the following requirements:

* [SkuId](#col) MUST be of type String.
* [SkuId](#col) MUST conform to [StringHandling](#attr) requirements.
* [SkuId](#col) MUST NOT be null.
* [SkuId](#col) for a given [SKU](#term) MUST adhere to the following requirements:
  * [SkuId](#col) MUST remain consistent across contracts or billing agreements.
  * [SkuId](#col) MUST remain consistent regardless of any other factors that might impact the price but do not affect the functionality of the [SKU](#term).

## Column ID

SkuId

## Display Name

SKU ID

## Description

Service-provider-specified unique identifier that represents a specific [SKU](#term) (e.g., a quantifiable good or service offering).

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
