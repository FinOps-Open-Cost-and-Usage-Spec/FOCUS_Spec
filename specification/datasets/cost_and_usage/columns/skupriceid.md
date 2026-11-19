# SKU Price ID

[SKU Price ID](#col) is a service-provider-specified unique identifier that represents a specific [SKU Price](#term) associated with a [resource](#term) or [service](#term) used or purchased. It serves as a key reference for a [SKU Price](#term) in a [price list](#term) published by a service provider, allowing practitioners to look up detailed information about the [SKU Price](#term).

The composition of properties associated with the [SKU Price ID](#col) may differ across service providers and across [SKUs](#term) within the same service provider. However, the exclusion of dynamic or negotiable pricing elements - such as unit price amounts, currency, [foreign exchange](#term) rates, effective dates, contract or account identifiers, and negotiated discounts - ensures that the [SKU Price ID](#col) remains consistent across different billing periods and billing accounts within a service provider. Modifications to the pricing structure itself (such as a negotiated tier configuration), however, are included in the [SKU Price](#term) and therefore result in a distinct [SKU Price ID](#col).

This consistency enables efficient filtering of [charges](#term) to track price fluctuations (e.g., changes in unit price amounts) over time and across billing accounts, for both list and contracted unit prices. Additionally, the [SKU Price ID](#col) is commonly used to analyze costs based on pricing properties such as [periods](#term) and tiers.

To maintain a strict relationship with a single unit price, pricing structures with multiple price points (e.g., tiered pricing) use a distinct [SKU Price ID](#col) for each individual pricing tier.

## Requirements

[SkuPriceId](#col) MUST adhere to the following requirements:

* [SkuPriceId](#col) MUST be of type String.
* [SkuPriceId](#col) MUST conform to [StringHandling](#attr) requirements.
* [SkuPriceId](#col) MUST adhere to the following nullability requirements:
  * [SkuPriceId](#col) MUST be null when [ChargeCategory](#col) is ["Tax"](#val:CostAndUsage.ChargeCategory).
  * [SkuPriceId](#col) MUST NOT be null when [ChargeCategory](#col) is ["Usage"](#val:CostAndUsage.ChargeCategory) or "Purchase" and [ChargeClass](#col) is not ["Correction"](#val:CostAndUsage.ChargeClass).
  * [SkuPriceId](#col) MAY be null in all other cases.
* When [SkuPriceId](#col) is not null, [SkuPriceId](#col) MUST adhere to the following requirements:
  * [SkuPriceId](#col) MUST have one and only one parent [SkuId](#col) for a given [ServiceProviderName](#col).
  * [SkuPriceId](#col) MUST have one and only one [PricingUnit](#col) for a given [ServiceProviderName](#col).
  * [SkuPriceId](#col) MUST NOT be associated with both a "Usage" [ChargeCategory](#col) and a "Purchase" [ChargeCategory](#col) for a given [ServiceProviderName](#col).
  * [SkuPriceId](#col) for a given [ServiceProviderName](#col) and [SKU Price](#term) MUST adhere to the following requirements:
    * [SkuPriceId](#col) MUST remain consistent over time.
    * [SkuPriceId](#col) MUST remain consistent across [billing accounts](#term) or [contracts](#term).
  * [SkuPriceId](#col) MAY match [SkuId](#col).
  * [SkuPriceId](#col) MUST be associated with a given [resource](#term) or [service](#term) when [ChargeCategory](#col) is ["Usage"](#val:CostAndUsage.ChargeCategory) or "Purchase".
  * [SkuPriceId](#col) MUST reference a [SKU Price](#term) in a service-provider-supplied [price list](#term), enabling the lookup of detailed information about the [SKU Price](#term).
  * [SkuPriceId](#col) MUST have one and only one [ListUnitPrice](#col) for a given [ServiceProviderName](#col), [BillingCurrency](#col), and [ChargePeriodStart](#col).
  * [SkuPriceId](#col) MUST have one and only one [ContractedUnitPrice](#col) for a given [ServiceProviderName](#col), [contract](#term), [BillingAccountId](#col), [BillingCurrency](#col), and [ChargePeriodStart](#col).

See [Examples: Commitment Discount Flexibility](#appendix.examples:commitmentdiscountflexibility) for more details around [commitment discount flexibility](#term).

## Column ID

SkuPriceId

## Display Name

SKU Price ID

## Description

A service-provider-specified unique identifier that represents a specific [SKU Price](#term) associated with a [resource](#term) or [service](#term) used or purchased.

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
