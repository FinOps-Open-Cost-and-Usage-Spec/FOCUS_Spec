# SKU Price ID

A SKU Price ID is a unique identifier that defines the unit price used to calculate the charge. SKU Price ID can be referenced on a price list published by a provider to look up detailed information, including a corresponding list unit price. The composition of the properties associated with the SKU Price ID may differ across providers. SKU Price ID is commonly used for analyzing cost based on pricing properties such as Terms and Tiers.

The SkuPriceId column MUST be present in the billing data. This column MUST be of type String. SkuPriceId MUST define a single unit price used for calculating the charge. The ListUnitPrice MUST be associated with the SKUPriceID in the provider published price list. The SkuPriceId MUST NOT be null when ChargeType is "Purchase" or "Usage". SkuPriceId MUST NOT be null when ChargeSubcategory is "Refund" and the refund is related to charges with a specific SkuPriceId. A given value of SkuPriceId MUST be associated with one and only one SkuId.

## Column ID

SkuPriceId

## Display name

SKU Price ID

## Description

Unique identifier that defines the unit price used to calculate the charge.

## Content constraints

|  Constraint      |  Value         |
| :--------------- | :------------- |
|  Column required |  True          |
|  Allows nulls    |  True          |
|  Data type       |  String        |
|  Value format    |  \<not specified\> |

## Introduced (version)

1.0
