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
| Value format         | Undefined          |


#### Introduced (version)

1.0


## Supporting content

#### Example provider mappings 

Current column mappings found in available data sets:

|              |                             |                 |
| ------------ | --------------------------- | --------------- |
| **Provider** | **Data set**                | **Column**      |
| AWS          | CUR                         | product/sku     |
| Azure        | Cost details export or API  | PartNumber      |
| GCP          | Big Query Export            | sku.id          |
| OCI          | Cost Reports                | cost/productSku |
|              |                             |                 |


#### Example scenarios for current provider data

Current values observed in billing data for various scenarios:

|              |                            |                  |
| ------------ | -------------------------- | ---------------- |
| **Provider** | **Scenario**               | **Pattern**      |
| AWS          | CUR                        | FFNT87MQSCR328W6 |
| Azure        | Cost Details export or API |  ABC-12345       |
| GCP          | Big Query                  | F1ED-0732-5BDA   |
| OCI          | Cost Reports               | B91962           |
|              |                            |                  |


### Discussion / Scratch space

References

AWS - (<https://docs.aws.amazon.com/cur/latest/userguide/product-columns.html#product-details-P>)

Azure - (<https://learn.microsoft.com/en-us/azure/cost-management-billing/automate/understand-usage-details-fields>)

Big Query - (<https://cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage>)

OCI - (<https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/usagereportsoverview.htm>)

Potato / Tomato v1 discussion: <https://docs.google.com/document/d/1-flGM09zj3QkjSk8hlJolujZiCzVVmwi3TxDTaFJ7qM/edit#heading=h.u4wfvautplvp>

Potato / Tomato v2 discussion:\
<https://docs.google.com/document/d/18eL6G8WhbmEIHtrjqQlWqckgMRUQSs1aZwmwuRKQfqU/edit#heading=h.swm58hl317f3>
