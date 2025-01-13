# SKU Price ID

A SKU Price ID is a unique identifier that defines the unit price used to calculate the charge. It can serve as a key reference to a [*price list*](#glossary:price-list) published by a provider, allowing practitioners to look up detailed information, including the associated list unit prices and pricing properties. Although the composition of properties associated with the SKU Price ID may differ across providers, the SKU Price ID is designed to represent the core, stable properties of a [*SKU Price*](#glossary:sku-price), excluding dynamic or negotiable properties such as unit price amount, currency (and related exchange rates), temporal validity (e.g., effective dates), and customer- or negotiation-specific elements (e.g., contract or account identifiers, and negotiable discounts). This ensures that the SKU Price ID remains consistent across different pricing scenarios, even though variable aspects (e.g., unit price, currency, effective dates) might fluctuate, facilitating the filtering of charges with the same stable SKU Price properties and allowing for tracking price fluctuations (e.g., changes in unit price amount) over time — for both list unit prices and contracted prices. The SKU Price ID is also commonly used to analyze costs based on pricing properties such as Terms and Tiers.

The SkuPriceId column adheres to the following requirements:

* SkuPriceId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider publishes a SKU price list and MUST be of type String.
* SkuPriceId MUST define a single unit price used for calculating the charge, reflecting a stable grouping of core properties of a SKU Price while excluding fluctuations in dynamic or negotiable properties such as unit price amount, currency, temporal validity (e.g., effective dates), and customer- or negotiation-specific elements.
* [ListUnitPrice](#listunitprice) MUST be associated with the SkuPriceId in the provider published price list but is not inherently part of the SkuPriceId itself.
* SkuPriceId MUST NOT be null when [ChargeClass](#chargeclass) is not "Correction" and [ChargeCategory](#chargecategory) is "Usage" or "Purchase", MUST be null when ChargeCategory is "Tax", and MAY be null for all other combinations of ChargeClass and ChargeCategory.
* A given value of SkuPriceId MUST be associated with one and only one [SkuId](#skuid), except in cases of [commitment discount flexibility](#glossary:commitment-discount-flexibility).
* If a provider does not have a SkuPriceId and wants to include information in columns linked to SkuPriceId such as ListUnitPrice or [SkuPriceDetails](#skupricedetails), the SkuId MAY be used in the SkuPriceId column as long as it adheres to the above conditions.

## Column ID

SkuPriceId

## Display Name

SKU Price ID

## Description

A unique identifier that defines the unit price used to calculate the charge.

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
