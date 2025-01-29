# SKU ID

ORIGINAL:
A SKU ID is a unique identifier that defines a provider-supported construct for organizing properties that are common across one or more [*SKU Prices*](#glossary:sku-price). SKU ID can be referenced on a catalog or [*price list*](#glossary:price-list) published by a provider to look up detailed information about the SKU. The composition of the properties associated with the SKU ID may differ across providers. Some providers may not support the [*SKU*](#glossary:sku) construct and instead associate all such properties directly with the *SKU Price*. SKU ID is commonly used for analyzing cost based on *SKU*-related properties above the pricing constructs.

PROPOSED:
A SKU ID is a provider-specified unique identifier that represents a specific [*SKU*](#glossary:sku) (e.g., billable good or service offering) that can be used or purchased. Each SKU ID represents specific functionality and technical specifications of a single *SKU* that are common across one or more [*SKU Prices*](#glossary:sku-price). SKU ID is consistent across different billing accounts, pricing models (e.g., flat-rate, tiered, committed, spot pricing), and regions for a single provider to facilitate price comparisons for the same functionality, regardless of where the functionality is provided or how it's paid for.

SKU ID can be referenced on a catalog or [*price list*](#glossary:price-list) published by a provider to look up detailed information about the *SKU*. The composition of the properties associated with the SKU ID may differ across providers. SKU ID is commonly used for analyzing and comparing costs for the same SKU in different regions, tiers, and more.

NOTES:
- SKU == functionality that you're getting
- SkuId should be the same no matter how the billing account is configured
- SkuId should support comparing before/after negotiations
- SkuId should support comparing with a public/retail price list
- Concepts that are part of a SKU: Publisher, parent product, pricing unit, size/shape, SLA (dev/test or prod), tech specs
- Concepts that are part of a SKU price: State (preview or GA), SKU region, CD type, term, tier, SKU meter
- External factors that impact price: Billing account type, negotiated discounts, billing/charge period

The SkuId column adheres to the following requirements:

* SkuId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider publishes a SKU list.
* SkuId MUST be of type String.
* SkuId MUST NOT be null when [ChargeClass](#chargeclass) is not "Correction" and [ChargeCategory](#chargecategory) is "Usage" or "Purchase".
* SkuId MUST be null when ChargeCategory is "Tax".
* SkuId MAY be null for all other combinations of ChargeClass and ChargeCategory.
* ~SkuId MUST equal SkuPriceId when a provider does not support an overarching SKU ID construct.~
  > NOTE: This seems wrong. SkuId is the primary identifier. SkuPriceId is the secondary identifier to account for different pricing options for that SkuId. I don't think we should be defining SkuId based on SkuPriceId. It should be the other way around.

## Column ID

SkuId

## Display Name

SKU ID

## Description

ORIGINAL:
A unique identifier that defines a provider-supported construct for organizing properties that are common across one or more *SKU Prices*.

PROPOESED:
Provider-specified unique identifier that represents a specific *SKU* (e.g., billable good or service offering) that can be used or purchased.

## Content constraints

| Constraint      | Value            |
| :-------------- | :--------------- |
| Column type     | Dimension        |
| Feature level   | Conditional      |
| Allows nulls    | True             |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

1.0-preview
