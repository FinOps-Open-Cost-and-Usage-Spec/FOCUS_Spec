# Column: BilledUnitPrice

## Example provider mappings

Current column mappings found in available data sets:

| Provider  | Data set                     | Column                   |
|:----------|:-----------------------------|:-------------------------|
| AWS       | CUR;                         | Use lineItem/NetUnblendedRate if available, otherwise ​​lineItem/UnblendedRate. |
| GCP       | BigQuery Billing Export;<br>BigQuery Pricing Data Export;<br>Cloud Billing API | Not available in BigQuery Billing Export<br>**price.effective_price** (present only in detail export and thus available only for a small subset of services/resources) is closest match<br>*see Discussion / Scratch space - GCP column mappings related issues for more details* |
| Microsoft | Cost details;<br>*TODO: Add reference to Custom Azure Prices REST API* | **unitPrice** is probably the best match, but according to  documentation it's available only for EA and PAYG. <br>*see Discussion / Scratch space - Microsoft column mappings related issues for more details* |
| OCI       | Cost and Usage Report        | Not available in Cost and Usage Report but can be resolved from the List Pricing REST API |

## References and Resources

### AWS

- [Line item details - AWS Cost and Usage Reports](https://docs.aws.amazon.com/cur/latest/userguide/Lineitem-columns.html)

### GCP

- [Structure of Detailed data export | Cloud Billing](https://cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage)
- [Structure of pricing data export | Cloud Billing](https://cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/pricing-data)
- [Get Google Cloud pricing information | Cloud Billing (GCP Cloud Billing API)](https://cloud.google.com/billing/docs/how-to/get-pricing-information-api)

### Microsoft

- [Understand usage details fields - Microsoft Cost Management](https://learn.microsoft.com/en-us/azure/cost-management-billing/automate/understand-usage-details-fields)
- [Azure Billing Enterprise APIs - PriceSheet | Microsoft Learn](https://learn.microsoft.com/en-us/rest/api/billing/enterprise/billing-enterprise-api-pricesheet)
  - Applies only to EA?
  - *TODO: Investigate the existence of a Microsoft Custom Prices REST API, which might provide custom prices for all account types*

### OCI

- [Cost and Usage Reports Overview](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/usagereportsoverview.htm)

## Example usage scenarios

- See [Appendix: Quantity-Driven Pricing strategies](../apendix/quantity_driven_pricing_strategies.md) for more information on
  - Quantity-Driven Pricing strategies (such as flat-rate, volume-based rates and tier-based rating)
  - related UC scenarios
  - Current values observed in billing data for various scenarios
  - Alternative data sources for various scenarios

- See [Pricing Support – UCs and Data samples Spreadsheet](https://docs.google.com/spreadsheets/d/1AZ-vtkKeKwYc8rqhxP1zMTnAVAS-svmWQQmr8cpv-IM/edit#gid=117987709) for additional UC scenarios and sample data.

## Discussion / Scratch space

### GCP column mappings related issues

- **price.effective_price** is present only in detail export and thus available only for small subset of services/resources. In order to resolve this information we should rely on **BigQuery Pricing Data Export** and/or **Cloud Billing API**, which provide price related structs (out-of-scope of this document). That being said, just like cost, regardless of the data source that we use the resolved price doesn't incorporate reductions provided in credits.

### Microsoft column mappings related issues

- According to  documentation **unitPrice** (The price per unit for the charge.) is the best match, but it's available only for EA and PAYG.
- Not sure if unitPrice is in Billing or Pricing currency. Noticed that for different accounts types different relations apply - in one case `unitPrice * quantity = costInBillingCurrency` and in another `unitPrice * quantity = costInUSD`.
- TODO: Investigate the existence of a Microsoft Custom Prices REST API, which might provide custom prices for all account types