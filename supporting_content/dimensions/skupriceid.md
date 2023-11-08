## Example provider mappings 

Current column mappings found in available data sets:

| Provider | Data set                | Column                             |
| ------------ | --------------------------- | -------------------------------------- |
| AWS          | CUR                         | pricing/rate\_code \| pricing/rate\_id |
| Azure        | Cost details export or API  | ProductID                              |
| GCP          | BigQuery Billing Export            | Not available, but can be derived from sku.id and price.tier_start_amount                                 |
| OCI          | Cost Reports                | Not available (no price level ID)    |


## Example scenarios for current provider data

Current values observed in billing data for various scenarios:

| Provider | Scenario               | Pattern                                                              |
| ------------ | -------------------------- | ------------------------------------------------------------------------ |
| AWS          | CUR                        | rate\_code: KF338J7FCKZPUBD9.JRTCKXETXF.6YS6EN2CT7 rate\_id: 20457007287 |
| Azure        | Cost Details export or API | DZH318Z0BNZH006F                                                                         |
| GCP          | BigQuery Billing Export                  | sku.id: 947D-3B46-7781 price.tier_start_amount: 10                                                          |
| OCI          | Cost Reports               | Not available                                               |

## Discussion / Scratch space

### References

AWS - <https://docs.aws.amazon.com/cur/latest/userguide/pricing-columns.html>

Azure - <https://learn.microsoft.com/en-us/azure/cost-management-billing/automate/understand-usage-details-fields>

Big Query - <https://cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage>

OCI - <https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/usagereportsoverview.htm>

Potato / Tomato v1 discussion: <https://docs.google.com/document/d/1-flGM09zj3QkjSk8hlJolujZiCzVVmwi3TxDTaFJ7qM/edit#heading=h.u4wfvautplvp>

Potato / Tomato v2 discussion:\
<https://docs.google.com/document/d/18eL6G8WhbmEIHtrjqQlWqckgMRUQSs1aZwmwuRKQfqU/edit#heading=h.swm58hl317f3>
