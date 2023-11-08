# SKU ID

A SKU ID is an unique identifier that defines a provider-supported construct for organizing properties that are common across one or more SKU Prices. SKU ID can be referenced on a catalog or price list published by a provider to look up detailed information about the SKU. The composition of the properties associated with the SKU ID may differ across providers. Some providers may not support the SKU construct and instead associate all such properties directly with the SKU Price. SKU ID is commonly used for analyzing cost based on SKU related properties above the pricing constructs.

The SkuId column MUST be present in the billing data. This column MUST be of type String. The SkuId MUST NOT be null when SkuPriceId is not null. The SkuId MUST be null when SkuPriceId is null. SkuId MUST equal SkuPriceId when a provider does not support an overarching SKU ID construct.

## Column ID

SkuId

## Display name

SKU ID

## Description

An unique identifier that defines a provider-supported construct for organizing properties that are common across one or more SKU Prices.

## Content constraints

| Constraint      | Value            |
| :-------------- | :--------------- |
| Column required | True             |
| Data type       | String           |
| Allows nulls    | True             |
| Value format    | \<not specified> |

## Introduced (version)

1.0
