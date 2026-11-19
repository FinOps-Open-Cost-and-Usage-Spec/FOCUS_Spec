# SKU ID

A [SKU ID](#col) is a service-provider-specified unique identifier that represents a specific [SKU](#term). [SKUs](#term) are quantifiable goods or service offerings in a [Cost and Usage](#ds) [FOCUS dataset](#term) that represent specific functionality and technical specifications. Examples of [SKUs](#term) include but are not limited to:

* A product license that is purchased or subscribed to.
* Usage of a deployed resource from direct user interaction (e.g., request count).
* Usage by a deployed resource based on the resource's configuration (e.g., running hours, storage space).

Each [SKU ID](#col) represents a unique set of features that can be sold at different price points or [SKU Prices](#term). [SKU ID](#col) is consistent across all pricing variations, which may differ based on multiple factors beyond the common functionality and technical specifications. Examples include but are not limited to:

* Date the [charge](#term) was incurred.
* Pricing tiers (e.g., free tier or volume-based tiers).
* Commitment discount pricing [period](#term) (e.g., 1 year, 3 years).
* Negotiated discounts or other contractual terms or conditions.

[SKU ID](#col) should be consistent across pricing variations of a good or service to facilitate price comparisons for the same functionality, like where the functionality is provided or how it's paid for. [SKU ID](#col) can be referenced on a catalog or [price list](#term) published by a service provider to look up detailed information about the [SKU](#term). The composition of the properties associated with the [SKU ID](#col) may differ across service providers. [SKU ID](#col) is commonly used for analyzing and comparing costs for the same SKU across different price details (e.g., [period](#term), tier, location).

## Requirements

[SkuId](#col) MUST adhere to the following requirements:

* [SkuId](#col) MUST be of type String.
* [SkuId](#col) MUST conform to [StringHandling](#attr) requirements.
* [SkuId](#col) MUST adhere to the following nullability requirements:
  * [SkuId](#col) MUST be null when [ChargeCategory](#col) is ["Tax"](#val:CostAndUsage.ChargeCategory).
  * [SkuId](#col) MUST NOT be null when [ChargeCategory](#col) is ["Usage"](#val:CostAndUsage.ChargeCategory) or "Purchase" and [ChargeClass](#col) is not ["Correction"](#val:CostAndUsage.ChargeClass).
  * [SkuId](#col) MAY be null in all other cases.
* [SkuId](#col) for a given [ServiceProviderName](#col) and [SKU](#term) MUST adhere to the following requirements:
  * [SkuId](#col) MUST remain consistent across [billing accounts](#term) or contracts.
  * [SkuId](#col) MUST remain consistent across [PricingCategory](#col) values.
  * [SkuId](#col) MUST remain consistent regardless of any other factors that might impact the price but do not affect the functionality of the [SKU](#term).
* [SkuId](#col) MUST be associated with a given [resource](#term) or [service](#term) when [ChargeCategory](#col) is ["Usage"](#val:CostAndUsage.ChargeCategory) or "Purchase".
* [SkuId](#col) MAY match [SkuPriceId](#col).

## Column ID

SkuId

## Display Name

SKU ID

## Description

Service-provider-specified unique identifier that represents a specific [SKU](#term) (e.g., a quantifiable good or service offering).

## Content Constraints

| Constraint                 | Value                                     |
| :------------------------- | :---------------------------------------- |
| Dataset                    | [Cost and Usage](#ds)                     |
| Operating model conditions | [Includes Unit Pricing](#omc)                                          |
| Column type                | Dimension                                 |
| Feature level              | Conditional                               |
| Allows nulls               | True                                      |
| Data type                  | String                                    |
| Value format               | \<not specified>                          |

## Version Introduced

1.0-preview
