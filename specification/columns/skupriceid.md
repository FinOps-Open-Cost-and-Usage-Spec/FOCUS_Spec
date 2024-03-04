# SKU Price ID

A SKU Price ID is a unique identifier that defines the unit price used to calculate the charge. SKU Price ID can be referenced on a [*price list*](#glossary:price-list) published by a provider to look up detailed information, including a corresponding list unit price. The composition of the properties associated with the SKU Price ID may differ across providers. SKU Price ID is commonly used for analyzing cost based on pricing properties such as Terms and Tiers.

The SkuPriceId column MUST be present in the billing data when the provider publishes a SKU price list. This column MUST be of type String. SkuPriceId MUST define a single unit price used for calculating the charge. The [ListUnitPrice](#listunitprice) MUST be associated with the SkuPriceId in the provider-published _price list_*. The SkuPriceId MUST NOT be null when [ChargeCategory](#chargecategory) is "Purchase" or "Usage". SkuPriceId MUST NOT be null when [ChargeSubcategory](#chargesubcategory) is "Refund" and the refund is related to charges with a specific SkuPriceId. A given value of SkuPriceId MUST be associated with one and only one [SkuId](#skuid), except in cases of commitment discount flexibility.

## Column ID

SkuPriceId

## Display name

SKU Price ID

## Description

A unique identifier that defines the unit price used to calculate the charge.

## Content constraints

| Constraint       | Value          |
| :--------------- | :------------- |
| Column type      | Dimension      |
| FOCUS Essential | False            |
| Allows nulls     | True           |
| Data type        | String         |
| Value format     | \<not specified\> |

## Introduced (version)

1.0
