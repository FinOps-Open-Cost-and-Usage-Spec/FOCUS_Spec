# Column: CommitmentDiscountType

## Documentation
- Microsoft
  - Azure:  Understand usage details fields: https://learn.microsoft.com/en-us/azure/cost-management-billing/automate/understand-usage-details-fields
- GCP
  - Google Commitment Types:  https://cloud.google.com/docs/cuds#spend_versus_resource_commitments (This is the most similar to our selected implementation)
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