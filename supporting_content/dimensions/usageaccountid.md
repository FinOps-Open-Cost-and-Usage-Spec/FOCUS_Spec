# Column: Usage Account ID

## Example provider mappings 

Current column mappings found in available data sets:

| Provider  | Data set | Column |
|-----------|----------|--------|
| AWS       | CUR | lineItem/UsageAccountId |
| GCP       | Big Query Billing Export | project.id |
| Microsoft | Cost details | SubscriptionGuid |
| Microsoft | Price sheet | |

## Example usage scenarios

Current values observed in billing data for various scenarios:

| Provider  | Data set | Example Value |
|-----------|----------|--------|
| AWS       | CUR | 987456321 |
| GCP       | Big Query Billing Export | project-name <br>project-name-789456 |
| Microsoft | Cost details | 072fe543-fa61-465e-adaf-04d09c829c4a |
| Microsoft | Price sheet | |

## Discussion / Scratch space:

- Use provider terminology - or customers will get confused
- How about if we start with a definition: 
  - Logical grouping of resources
  - May contain access restrictions 
  - Billing Account (L1), Account Group (L2), Account (L3)
    - Will there be confusion about Account vs Billing Account
    - What about “Usage Account” for L3
    - Billing account could say “grouping of Usage accounts”
- Other descriptions considered:
  - Logical grouping of resources based on usage, access and/or billing boundaries.
  - Base level organizing entity of resources / resource container
  - A usage account is an organizing entity of provider resources.
  - (Combined) A usage account is a base-level organizing entity of provider resources often used to manage access and cost. A usage account is one of several structural elements of provider hierarchies.


| | Billing Account | Usage Account Group (optional) | Usage Account | | |
| Provider | Level 1 | Level 2 | Level 3 | Level 4 | Level 5 |
|----------|---------|---------|---------|---------|---------|
| AWS | Payer Account | Org | Account | Resource Group | Resource |
| Azure | Tenant Root Account / Billing Account | Management Group | Subscription | Resource Group | Resource |
| GCP | Billing Account | Folder | Project | | Resource |