## Spec Content

### SKUID

A SKU ID is an identifier assigned to the SKU that’s associated with a charge. SKU ID can be referenced on a price list published by a provider to look up detailed information about the SKU including the different unit prices associated with the SKU.

The SkuId column MUST be present in the billing data. This column MUST be of type String. The SkuId MUST NOT be null when Charge Type is ‘Purchase’ or ‘Usage’. The SkuId SHOULD NOT be null when Adjustment Type is ‘Refund’.

SkuId may have a collection of nullable attributes such as Service, Region, instance type, etc. Future versions of the FOCUS specification may include more precise definitions of those attributes.  In the interim, the SkuId can be used in concert with an externally-sourced price sheet to facilitate practitioner data modeling and analysis. 

A SkuId doesn’t necessarily define the price as there may be additional attributes such as tier, region, etc. of the SkuId that map to a price. 

Every SKU has one or more SKU Prices.  For providers that define their prices at the SKU level, the SkuId and SkuPriceId shall be the same.


#### Column ID

SkuId


#### Display name

SKU ID


#### Description

A provider-assigned identifier that maps to a unique product offering that has a charge associated with it.


#### Content constraints

|         Constraint   | Value              |
| -------------------- | ------------------ |
| Column required      | True               |
|  Data type           | String             |
|  Allows nulls        | True               |
| Value format         | \<not specified>          |


#### Introduced (version)

1.0
