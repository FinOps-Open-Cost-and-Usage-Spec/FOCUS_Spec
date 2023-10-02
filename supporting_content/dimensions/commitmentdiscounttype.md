# Column: CommitmentDiscountType

## Example provider mappings

Current column mappings found in available data sets:

| Provider | Data set                 | Column                    |  Example Values  |
|----------|--------------------------|---------------------------|------------------|
| AWS | CUR                      | Not available   | N/A |
| Google Cloud | BigQuery Billing Export | credit.type              | COMMITTED_USAGE_DISCOUNT, COMMITTED_USAGE_DISCOUNT_DOLLAR_BASE |
| Microsoft | Cost Details             | Not available               | N/A |

## Example usage scenarios

Current values observed in billing data for various scenarios:

| Provider | Data set                 | CommitmentDiscountType     | CommitmentDiscountProgram (Name TBD)     |
|----------|--------------------------|----------------------------|------------------------------------------|
| AWS | CUR                           |                            |                                          |
| Google Cloud | BigQuery Billing Export (credit.type) |                         |                                          |
| Microsoft | Cost Details (PricingModel)| Spend-Based                     | Savings Plan                             |
| Microsoft | Cost Details (PricingModel)| Spend-Based                     | Reservation                              |



## Documentation
- Microsoft
  - Azure:  Understand usage details fields: https://learn.microsoft.com/en-us/azure/cost-management-billing/automate/understand-usage-details-fields
- GCP
  - Google Commitment Types:  https://cloud.google.com/docs/cuds#spend_versus_resource_commitments (This is the most similar to our selected implementation)
  - https://cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage - see credit.type
- AWS
  - Amazon: Reservation details - https://docs.aws.amazon.com/cur/latest/userguide/reservation-columns.html

## Discussion Topics
It was discussed whether or not this field should be a normalized list of values OR if we should make it a suggestive, freeform text field as different cloud providers have different names for their implementation of Commitment Usage Discounts. For example:
  - Savings Plan
  - RI/CUD
  - Flexible CUDs

It was agreed that another column would be added (ideally in V1.0) that would identify the CUD name as termed by the Cloud Provider and that this column would be normalized to allow practitioners to have a standard interface to group and compare CUDs from multiple sources. This would be a non-normalized string.

The name of this additional column is yet to be determined but could be something like:
- Commitment Discount Program
- Commitment Discount Plan
- Commitment Discount Plan Name
- Other