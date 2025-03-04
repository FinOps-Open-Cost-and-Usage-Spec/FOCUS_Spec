# SKU ID

A SKU ID is a unique identifier that defines a provider-supported construct for organizing properties that are common across one or more [*SKU Prices*](#glossary:sku-price). SKU ID can be referenced on a catalog or [*price list*](#glossary:price-list) published by a provider to look up detailed information about the SKU. The composition of the properties associated with the SKU ID may differ across providers. Some providers may not support the [*SKU*](#glossary:sku) construct and instead associate all such properties directly with the *SKU Price*. SKU ID is commonly used for analyzing cost based on *SKU*-related properties above the pricing constructs.

The SkuId column adheres to the following requirements:

* SkuId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider publishes a SKU list.
* SkuId MUST be of type String.
* SkuId MUST conform to [StringHandling](#stringhandling) requirements.
* SkuId nullability is defined as follows:
  * SkuId MUST be null when [ChargeCategory](#chargecategory) is "Tax".
  * SkuId MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
  * SkuId MAY be null in all other cases.
* SkuId MUST equal SkuPriceId when a provider does not support an overarching SKU ID construct.

## Column ID

SkuId

## Display Name

SKU ID

## Description

A unique identifier that defines a provider-supported construct for organizing properties that are common across one or more *SKU Prices*.

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
