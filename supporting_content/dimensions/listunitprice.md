# Column: ListUnitPrice

## Example provider mappings

Current column mappings found in available data sets:

| Provider  | Data set                     | Column                   |
|:----------|:-----------------------------|:-------------------------|
| AWS       | CUR;<br>AWS Price List API   | pricing/publicOnDemandRate: The public On-Demand Instance rate in this billing period for the specific line item of usage. If you have SKUs with multiple On-Demand public rates, the equivalent rate for the highest tier is displayed. For example, services offering free-tiers or tiered pricing.<br>*Note: Since currently only pricing/publicOnDemandRate definition includes note regarding highest tier, I'm not sure if volume-based pricing applies to all unit prices (rates) in CUR files. If it's not consistent, we might have to rely on the AWS Price List API.* |
| GCP       | BigQuery Pricing Data Export | Not available in BigQuery Billing Export, but can be resolved from the list_price Struct in the BigQuery Pricing Data Export |
| Microsoft | Cost details;<br>Azure Retail Prices REST API | pay-as-you-goPrice/PayGPrice: Retail price for the resource<br>*Note: Identified some discrepancy between the value in Cost details and the Retail Price obtained from the Azure Retail Prices REST API, particularly in the context of CSPs. Might be related to Partner Billing UC?* |
| OCI       | List Pricing REST API        | Not available in Cost and Usage Report but can be resolved from the List Pricing REST API |

## Example scenarios for current provider data

Current values observed in billing data for various scenarios:

| Provider  | Scenario                       | Pattern                              |
|:----------|:-------------------------------|:-------------------------------------|
| AWS       | Flat-rate based pricing        | pricing/publicOnDemandRate: 0.000005 |
| AWS       | Usage-dependent pricing        | pricing/publicOnDemandRate: ??? *TODO: look for a higher tier sample* |
| GCP       | Flat-rate based pricing        | Not available                        |
| GCP       | Usage-dependent pricing        | Not available                        |
| Microsoft | Flat-rate based pricing - PAYG | PayGPrice: 0.00036                   |
| Microsoft | Flat-rate based pricing - CSP  | PayGPrice: 0.0003707                 |
| Microsoft | Usage-dependent pricing - PAYG | PayGPrice: 0.087                     |
| Microsoft | Usage-dependent pricing - CSP  | PayGPrice: 0.087                     |
| OCI       | Flat-rate based pricing        | Not available                        |
| OCI       | Usage-dependent pricing        | Not available                        |

Alternative data sources:

| Provider  | Scenario                                    | Data source                  | Authentication required | Request/Query Sample |
|:----------|:--------------------------------------------|:-----------------------------|:------------------------|:---------------------|
| AWS       | Flat-rate based and usage-dependent pricing | AWS Price List API           | N | [GET request](https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonS3/current/index.csv) |
| GCP       | Flat-rate based pricing                     | BigQuery Pricing Data Export | Y | *TODO: include img or code* |
| GCP       | Usage-dependent pricing                     | BigQuery Pricing Data Export | Y | *TODO: include img or code* |
| Microsoft | Flat-rate based pricing                     | Azure Retail Prices REST API | N | [GET request](https://prices.azure.com/api/retail/prices?api-version=2023-01-01-preview&currencyCode=%27EUR%27&meterRegion=%27primary%27&$filter=meterId%20eq%20%27b9e5e77c-a0b3-4a2c-9b8b-57fa54f31c52%27%20and%20location%20eq%20%27EU%20West%27) |
| Microsoft | Usage-dependent pricing                     | Azure Retail Prices REST API | N | [GET request](https://prices.azure.com/api/retail/prices?api-version=2023-01-01-preview&currencyCode=%27USD%27&meterRegion=%27primary%27&$filter=meterId%20eq%20%279995d93a-7d35-4d3f-9c69-7a7fea447ef4%27%20%20and%20location%20eq%20%27EU%20West%27&$orderby=tierMinimumUnits%20asc) |
| OCI       | Flat-rate based pricing                     | OCI List Pricing REST API    | N | [GET request](https://apexapps.oracle.com/pls/apex/cetools/api/v1/products/?currencyCode=EUR&partNumber=B88513) |
| OCI       | Usage-dependent pricing                     | OCI List Pricing REST API    | N | [GET request](https://apexapps.oracle.com/pls/apex/cetools/api/v1/products/?currencyCode=EUR&partNumber=B90617) |

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

From a pricing quantity perspective, we distinguish two types of pricing mechanisms: flat-rate pricing and usage-dependent pricing (or pricing quantity-based pricing, to be more precise).

#### Flat-rate pricing

In case of **flat-rate pricing** each pricing unit is assigned a fixed price regardless of the pricing quantity.

#### Usage-dependent pricing

Usage-dependent pricing involves configuration of multiple price tiers. Each tier is characterized by a pricing quantity range and associated unit prices (such as ListUnitPrice, NegotiatedUnitPrice, BilledUnitPrice, etc.). Typically, higher pricing tiers feature lower unit prices, granting users the advantage of reduced unit costs as their usage expands. Furthermore, Usage-dependent pricing may also include free-tier, which is a special price tier applicable to minimal usage levels.

Within the realm of usage-dependent pricing we encounter two subtypes: volume-based pricing and tier-based pricing. The key difference between these two mechanisms lies in how charges are categorized into different price tiers. **Volume-based pricing** adjusts unit prices based on the total usage within a specific interval, affecting all charges within that interval. On the other hand, in **tier-based pricing**, unit prices change as the number of charged units increases, with specific charges moving into higher tiers as their usage crosses into those ranges.
In both sybtypes, the count of charged units resets at the beginning of each interval.

For better comprehension, please refer to the following sample price-tiers configuration and UC scenarios.

#### UC scenarios for different (sub-)types of pricing mechanisms

| Scenario | Description                                                                                                 |
|:---------|:------------------------------------------------------------------------------------------------------------|
| S-1      | Tier-based pricing: 12GB of usage falls into two different tiers, resulting in two separate charge records. |
| S-2      | Volume-based pricing: 12GB of usage falls into the highest tier, resulting in a single charge record.       |

#### Sample price-tiers configuration

|                            | Lower Tier | Higher Tier |
|:---------------------------|:-----------|:------------|
| List Unit Price            | 1          | 0.50        |
| Pricing currency           | USD        | USD         |
| Starting Range (inclusive) | 0          | 10GB        |
| Ending Range (exclusive)   | 10         | 100         |
| Pricing Unit               | 1GB        | 1GB         |
| Enterprise discount        | 10%        | 10%         |

#### Sample Billing data

| Scenario | Pricing/Billed Quantity | Pricing Unit | List Unit Price | Negotiated Unit Price | Billed Unit Price | Pricing currency | Billed Currency | List Cost | Billed Cost | Amortized Cost |
|:----|---:|:----|-----:|-----:|-----:|:----|:----|---:|----:|----:|
| S-1 | 10 | 1GB | 1    | 0.90 | 0.90 | USD | USD | 10 | 9   | 9   |
| S-1 | 2  | 1GB | 0.50 | 0.45 | 0.45 | USD | USD | 1  | 0.9 | 0.9 |
| S-2 | 12 | 1GB | 0.50 | 0.45 | 0.45 | USD | USD | 6  | 5.4 | 5.4 |


See [Pricing Support – UCs and Data samples Spreadsheet](https://docs.google.com/spreadsheets/d/1AZ-vtkKeKwYc8rqhxP1zMTnAVAS-svmWQQmr8cpv-IM/edit#gid=117987709) for various UC scenarios.
