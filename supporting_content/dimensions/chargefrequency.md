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
| Microsoft | Cost details             | OneTime, Recurring, Monthly, UsageBased |


## Example Usecases

- Finops team identify and handle large one-time purchases to avoid (or educate on) large scary spikes in cloud monitoring tools/platforms. 
- Finance teams identify and allocate one-time purchases either by amortization or cost recovery from the right entity. 
- Engineering managers are able to identify usage-based charges to include in their budget or forecasting processes.

## Clarifications

- "Usage-Based" value means that charges will be incurred when usage occurs. If there's a charge that happens monthly, even if it's based on usage, it would have a frequency 'recurring' as it's occurrence does not depend on usage consumption but other contractual terms. 
- An upfront RI is a cost incurred in one billing period, similar to EC2 usage. Although neither will recur into another billing period, the upfront RI will be a 'one-time' charge and EC2 usage will be 'usage-based'. Another separate and distinct upfront RI or record of EC2 usage can be charged in the next period, if they occur. If a upfront RI is bought every month, they will be individual 'one-time' charges and cannot be considered as 'recurring'. 

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
- There was a discussion about using the word periodic vs. recurring to indicate that a charge would show up on a certain schedule. Based on multiple inputs, we decided to go with recurring simply becuase it is more commonly used although periodic might have been the better fitting English word per standard definitions. 


