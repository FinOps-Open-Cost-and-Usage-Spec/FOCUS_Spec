# Column: ChargeFrequency

## Example provider mappings

Current column mappings found in available data sets:

| Provider  | Data set                 | Column                                                                                                                                            |
| --------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS       | CUR                      | Bill_BillType                                                                                                                                     |
| GCP       | Big Query Billing Export | NA (No column name has been currently identified that performs partially or fully the function that the proposed dimension ChargeFrequency would) |
| Microsoft | Cost details             | Frequency                                                                                                                                         |
                                             

## Example usage scenarios

Current values observed in billing data for various scenarios:

| Provider  | Data set                 | Example Value                |
| --------- | ------------------------ | ---------------------------- |
| AWS       | CUR                      | Anniversary,Purchase,Refund  |
| GCP       | Big Query Billing Export | NA                           |
| Microsoft | Cost details             | Recurring,Monthly,UsageBased |



## Reference
- Microsoft: [understand-usage-details-fields](https://learn.microsoft.com/en-us/azure/cost-management-billing/automate/understand-usage-details-fields)
- AWS: [understand-bill-details-fields](https://docs.aws.amazon.com/cur/latest/userguide/billing-columns.html)

## Discussion / Scratch space

- What are the different types of spend that we want to group?
- Use cases:
  - Usage for cost reporting use cases / driving accountability
  - Tax needs to be filterable for special accounting treatments within companies
  - Fees are important for cost allocation / amortization - sometimes needs to be isolated from other cost
  - How would recurring refunds or credits be handled? Like AWS MAP credits
-AWS handling for SPs might be a concern - Anniversary charge (BillType) Savings Plan for $1 and a negation for UsageType (for -0.30)
- What Charge Types can BE recurring? Would usage under free tier be recurring since every month that charge is $0 or would it be usage based? 