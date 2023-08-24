# Column: ListUnitPrice

## Example provider mappings

Current column mappings found in available data sets:

| Provider  | Data set                     | Column                   |
|:----------|:-----------------------------|:-------------------------|
| AWS       | CUR;<br>AWS Price List API   | pricing/publicOnDemandCost: The total cost for the line item based on public On-Demand Instance rates. If you have SKUs with multiple On-Demand public costs, the equivalent cost for the highest tier is displayed. For example, services offering free-tiers or tiered pricing.<br>Since the pricing/publicOnDemandCost currently doesn't provide the correct price in all tier-based pricing use cases, we need to rely on the AWS Price List API. |
| GCP       | BigQuery Pricing Data Export | Not available in BigQuery Billing Export, but can be resolved from the list_price Struct in the BigQuery Pricing Data Export |
| Microsoft | Cost details;<br>Azure Retail Prices REST API | pay-as-you-goPrice/payGPrice: Retail price for the resource<br>Note: Identified some discrepancy between the value in Cost details and the Retail Price obtained from the Azure Retail Prices REST API, particularly in the context of CSPs. Might be related to Partner Billing UC? |
| OCI       | List Pricing REST API        | Not available in Cost and Usage Report but can be resolved from the List Pricing REST API |

## Example scenarios for current provider data

Current values observed in billing data for various scenarios:

| Provider  | Scenario                                 | Pattern                   |
|:----------|:-----------------------------------------|:----------------------------|
| AWS       | Flat-rate and tier-based list unit price | See [Current ListUnitPrice UCs and Data Samples - AWS sheet](https://docs.google.com/spreadsheets/d/1TpoXiu3aW_ENXvbONsjb6S1fqC7tJ8RcBNtFbsS9Qjw/edit#gid=726782282) for current data samples, as available in CUR files and AWS Price List API |
| GCP       | Flat-rate and tier-based list unit price | See [Current ListUnitPrice UCs and Data Samples - GCP sheet](https://docs.google.com/spreadsheets/d/1TpoXiu3aW_ENXvbONsjb6S1fqC7tJ8RcBNtFbsS9Qjw/edit#gid=318165912) for current data samples, as available in BigQuery Pricing Data Export |
| Microsoft | Flat-rate and tier-based list unit price | See [Current ListUnitPrice UCs and Data Samples - Microsoft sheet](https://docs.google.com/spreadsheets/d/1TpoXiu3aW_ENXvbONsjb6S1fqC7tJ8RcBNtFbsS9Qjw/edit#gid=1938507497) for current data samples, as available in Cost details and Azure Retail Prices REST API |
| OCI       | Flat-rate and tier-based list unit price | See [Current ListUnitPrice UCs and Data Samples - OCI sheet](https://docs.google.com/spreadsheets/d/1TpoXiu3aW_ENXvbONsjb6S1fqC7tJ8RcBNtFbsS9Qjw/edit#gid=1214261403) for current data samples, as available in OCI List Pricing REST API |

## References and Resources

### AWS

- [Pricing details - AWS Cost and Usage Reports](https://docs.aws.amazon.com/cur/latest/userguide/pricing-columns.html)
- [Using the AWS Price List API - AWS Billing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/price-changes.html)

### GCP

- [Structure of pricing data export | Cloud Billing](https://cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/pricing-data)
- [Structure of Detailed data export | Cloud Billing](https://cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage)

### Microsoft

- [Understand usage details fields - Microsoft Cost Management](https://learn.microsoft.com/en-us/azure/cost-management-billing/automate/understand-usage-details-fields)
- [Azure Retail Prices REST API overview | Microsoft Learn](https://learn.microsoft.com/en-us/rest/api/cost-management/retail-prices/azure-retail-prices)

### OCI

- [Cost and Usage Reports Overview](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/usagereportsoverview.htm)
- [Estimate Your Monthly Cost (List Pricing REST API)](https://docs.oracle.com/en-us/iaas/Content/GSG/Tasks/signingup_topic-Estimating_Costs.htm#accessing_list_pricing)

## Discussion / Scratch space

### Current data sources

- While Microsoft and AWS offer billing data, relying on pricing data for all providers is advisable due to mentioned discrepancies and volume/tier-based pricing concerns. Filtering pricing data based on resolved billing data to identify that specific list unit price is possible but often presents a challenge, particularly with volume/tier-based prices.
- MSFT lists the Retail Price as well as the Unit Price.

### Prices and Currencies

- If our plan includes specifying both BillingCurrency and PricingCurrency, and we permit use cases where BillingCurrency differs from PricingCurrency (rather than enforcing a single Currency per cost record), it becomes imperative to emphasize and clarify the currency that is applicable to a Unit Price dimension (should be part of the definition of the dimension). For the time being all unit price dimensions must be denominated in PricingCurrency.

### Naming challenges

Two naming challenges were resolved through polls, giving signed members the chance to voice their preferences.

- POLL 1: Please select the term you prefer to use when referring to the published rate and corresponding cost without any discounts:
  - Retail - 3 votes
  - List - 13 votes
  - Market - 1 vote
  - PAYG - 1 vote
  - Public - 5 votes

- POLL 2: Please select the term you prefer to use when referring to the price for a single unit of measure:
  - Rate - 2 votes
  - Unit Price - 13 votes
  - Price - 2 votes

The following dimensions and metrics names were influenced by these decisions:

- List Cost
- Billed Unit Price
- Amortized Unit Price
- List Unit Price

### Use Case Scenarios

See [Pricing Support – UCs and Data samples Spreadsheet](https://docs.google.com/spreadsheets/d/1AZ-vtkKeKwYc8rqhxP1zMTnAVAS-svmWQQmr8cpv-IM/edit#gid=117987709) for various UC scenarios.
