# Column: SkuId

## Example provider mappings

Current column mappings found in available data sets:

|              |                             |                 |
| ------------ | --------------------------- | --------------- |
| **Provider** | **Data set**                | **Column**      |
| AWS          | CUR                         | product/sku     |
| Azure        | Cost details export or API  | PartNumber      |
| GCP          | Big Query Export            | sku.id          |
| OCI          | Cost Reports                | cost/productSku |
|              |                             |                 |


## Documentation

- GCP: [SKU List](https://cloud.google.com/skus/sku-groups/global-skus)
- AWS: [Product Details](https://docs.aws.amazon.com/cur/latest/userguide/product-columns.html#product-details-S)
- OCI: [Public Cloud list pillar document](https://www.oracle.com/content/published/api/v1.1/assets/CONT95B931480DF242229DF530A64F0D0245/native/Oracle%20PaaS%20and%20IaaS%20Public%20Cloud%20Services%20Pillar%20Document.pdf?cb=_cache_a99f&channelToken=117bec9b3b4e4e90a1c4c9069d210baf&download=false)


## Example usage scenarios

Current values observed in billing data for various scenarios:

|              |                            |                  |
| ------------ | -------------------------- | ---------------- |
| **Provider** | **Scenario**               | **Pattern**      |
| AWS          | CUR                        | FFNT87MQSCR328W6 |
| Azure        | Cost Details export or API |  ABC-12345       |
| GCP          | Big Query                  | F1ED-0732-5BDA   |
| OCI          | Cost Reports               | B91962           |
|              |                            |                  |


## Discussion / Scratch space:

References

AWS - (<https://docs.aws.amazon.com/cur/latest/userguide/product-columns.html#product-details-P>)

Azure - (<https://learn.microsoft.com/en-us/azure/cost-management-billing/automate/understand-usage-details-fields>)

Big Query - (<https://cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage>)

OCI - (<https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/usagereportsoverview.htm>)

Potato / Tomato v1 discussion: <https://docs.google.com/document/d/1-flGM09zj3QkjSk8hlJolujZiCzVVmwi3TxDTaFJ7qM/edit#heading=h.u4wfvautplvp>

Potato / Tomato v2 discussion:\
<https://docs.google.com/document/d/18eL6G8WhbmEIHtrjqQlWqckgMRUQSs1aZwmwuRKQfqU/edit#heading=h.swm58hl317f3>
