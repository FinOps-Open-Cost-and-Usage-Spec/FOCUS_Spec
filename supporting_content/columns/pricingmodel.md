# Column: PricingModel - WIP

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
- Microsoft
  - Azure:  Understand usage details fields: https://learn.microsoft.com/en-us/azure/cost-management-billing/automate/understand-usage-details-fields
- GCP
  -
- AWS
  - Amazon:

## Discussion Topics
