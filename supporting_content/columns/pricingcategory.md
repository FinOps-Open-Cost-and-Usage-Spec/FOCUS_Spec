# Column: PricingCategory

## Example provider mappings

Current column mappings found in available data sets:

| Provider | Data set                 | Column                    |  Example Values  |
|----------|--------------------------|---------------------------|------------------|
| AWS | CUR                      |  product/PurchaseOption | On-Demand, Reserved Instances, Spot Instances, Dedicated Hosts |
| Google Cloud | BigQuery Billing Export |              |  |
| Microsoft | Cost Details             | PricingModel             | OnDemand, Spot, Reservation, SavingsPlan |

## Example usage scenarios

Current values observed in billing data for various scenarios:

| Provider | Data set                 | PricingModel     |      |
|----------|--------------------------|----------------------------|------------------------------------------|
| AWS | CUR ()                   |                 |              |
| AWS | CUR ()                   |                |                    |
| Google Cloud | BigQuery Billing Export |         |                            |
| Google Cloud | BigQuery Billing Export |         |                               |
| Microsoft | Cost Details (PricingModel)| Reservation                     | Savings Plan                     |
| Microsoft | Cost Details (PricingModel)| Reservation                    | Reservation                      |
| Microsoft | Cost Details (PricingModel)| Spot                    | Reservation                      |
| Microsoft | Cost Details (PricingModel)| OnDemand                    | Reservation                      |

## Documentation
- AWS: https://docs.aws.amazon.com/cur/latest/userguide/product-columns.html
- GCP
- Microsoft:  Understand usage details fields: https://learn.microsoft.com/azure/cost-management-billing/automate/understand-usage-details-fields

## Discussion Topics
