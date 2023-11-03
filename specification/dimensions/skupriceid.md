### SKU Price ID

A SKU Price ID is a unique identifier that defines the price that is used to bill the SKU of the charge. This identifier represents a unique collection of nullable attributes that determine the price. SKU Price ID can be referenced on a price list published by a provider to look up detailed information about the SKU and the unit price associated with the SKU. The composition of the detailed information associated with the price may differ from one provider to the next.

Every SKU has one or more SKU Prices.  For providers that define their prices at the SKU level, the SKU ID and SKU Price ID shall be the same.

The SKUPriceId column MUST be present in the billing data. This column MUST be of type String. The SKUPriceId MUST NOT be null when the corresponding SKUId is not null. When SKUId is null, SKUPriceId MUST be null.

#### Column ID

SKUPriceID


#### Display name

SKU Price ID


#### Description

An identifier assigned to the Unit Price associated with the SKU that incurred a charge.


#### Content constraints

|  Constraint      |  Value         |
| -------------------- | ------------------ |
|  Column required |  True          |
|  Data type       |  String        |
|  Allows nulls    |  True          |
|  Value format    |  \<not specified\> |


#### Introduced (version)

1.0
