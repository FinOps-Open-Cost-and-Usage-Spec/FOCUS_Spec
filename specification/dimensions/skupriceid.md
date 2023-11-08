# SKU Price ID

A SKU Price ID is a unique identifier that defines the list unit price associated with the charge. SKU Price ID can be referenced on a price list published by a provider to look up detailed information about the list unit price. The composition of the detailed information associated with the SKU Price ID may differ across providers.

The SkuPriceId column MUST be present in the billing data. This column MUST be of type String. SkuPriceId MUST define a single list unit price. The ListUnitPrice corresponding to a SkuPriceId MUST be the same value as the list unit price in the provider published pricing sheet.

## Column ID

SkuPriceId

## Display name

SKU Price ID

## Description

A unique identifier that defines the list unit price associated with the charge. This can be referenced on a price list published by a provider to look up detailed information about the list unit price.

## Content constraints

|  Constraint      |  Value         |
| :--------------- | :------------- |
|  Column required |  True          |
|  Data type       |  String        |
|  Allows nulls    |  True          |
|  Value format    |  \<not specified\> |

#### Introduced (version)

1.0
