### SKUPriceID

A SKU Price ID is a unique identifier that defines the price of a SKU that incurred a charge. This identifier represents a unique collection of nullable attributes that determine the price. SKU Price ID can be referenced on a price list published by a provider to look up detailed information about the SKU and the unit price associated with the SKU. The composition of the detailed information associated with the price may differ from one provider to the next.

Every SKU has one or more SKU Prices.  For providers that define their prices at the SKU level, the SKU ID and SKU Price ID shall be the same.

The SKUPriceId column MUST be present in the billing data. This column MUST be of type String. The SKUId MUST NOT be null when the corresponding SKUId is not null. When SKUId is null, SKUPriceId MUST be null.

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
|  Value format    |  \<none specified\> |


#### Introduced (version)

1.0


## Supporting content

#### Example provider mappings 

Current column mappings found in available data sets:

| **Provider** | **Data set**                | **Column**                             |
| ------------ | --------------------------- | -------------------------------------- |
| AWS          | CUR                         | pricing/rate\_code \| pricing/rate\_id |
| Azure        | Cost details export or API  | ProductID                              |
| GCP          | Big Query Export            | sku.id                                 |
| OCI          | Cost Reports                | cost/productSKU (no price level ID)    |


#### Example scenarios for current provider data

Current values observed in billing data for various scenarios:

| **Provider** | **Scenario**               | **Pattern**                                                              |
| ------------ | -------------------------- | ------------------------------------------------------------------------ |
| AWS          | CUR                        | rate\_code: KF338J7FCKZPUBD9.JRTCKXETXF.6YS6EN2CT7 rate\_id: 20457007287 |
| Azure        | Cost Details export or API | DZH318Z0BNZH006F                                                                         |
| GCP          | Big Query                  | F1ED-0732-5BDA                                                           |
| OCI          | Cost Reports               | B93382 (no price level ID)                                               |


### Discussion / Scratch space

References

AWS - (<https://docs.aws.amazon.com/cur/latest/userguide/pricing-columns.html>)

Azure - (<https://learn.microsoft.com/en-us/azure/cost-management-billing/automate/understand-usage-details-fields>)

Big Query - (<https://cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage>)

OCI - (<https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/usagereportsoverview.htm>)

Potato / Tomato v1 discussion: <https://docs.google.com/document/d/1-flGM09zj3QkjSk8hlJolujZiCzVVmwi3TxDTaFJ7qM/edit#heading=h.u4wfvautplvp>

Potato / Tomato v2 discussion:\
<https://docs.google.com/document/d/18eL6G8WhbmEIHtrjqQlWqckgMRUQSs1aZwmwuRKQfqU/edit#heading=h.swm58hl317f3>
