# SKU ID

A SKU ID is a unique identifier that defines the SKU associated with the charge. SKU ID can be referenced on a price list published by a provider to look up detailed information about the SKU and the identified unit price associated with the SKU. The composition of the detailed information associated with the SKU may differ between providers.

The SkuId column MUST be present in the billing data. This column MUST be of type String. The SkuId MUST NOT be null when Charge Type is 'Purchase' or 'Usage'. The SkuId SHOULD NOT be null when Adjustment Type is 'Refund'.

## Column ID

SkuId

## Display name

SKU ID

## Description

A provider-assigned identifier that maps to a unique product offering that has a charge associated with it.

## Content constraints

| Constraint      | Value            |
| :-------------- | :--------------- |
| Column required | True             |
| Data type       | String           |
| Allows nulls    | True             |
| Value format    | \<not specified> |

## Introduced (version)

1.0
