# SKU Price ID

A SKU Price ID is a unique identifier that defines the unit price associated with the SKU of the charge. SKU Price ID can be referenced on a price list published by a provider to look up detailed information about the SKU and the unit price associated with the SKU. The composition of the detailed information associated with the price may differ from one provider to the next.

Every SKU has one or more SKU Prices.  For providers that define their prices at the SKU level, the SKU ID and SKU Price ID shall be the same.

The SkuPriceId column MUST be present in the billing data. This column MUST be of type String. The SkuPriceId MUST NOT be null when the corresponding SkuId is not null. When SkuId is null, SkuPriceId MUST be null.

## Column ID

SkuPriceID


## Display name

SKU Price ID


## Description

An identifier assigned to the Unit Price associated with the SKU that incurred a charge.


## Content constraints

|  Constraint      |  Value         |
| -------------------- | ------------------ |
|  Column required |  True          |
|  Data type       |  String        |
|  Allows nulls    |  True          |
|  Value format    |  \<not specified\> |


#### Introduced (version)

1.0
