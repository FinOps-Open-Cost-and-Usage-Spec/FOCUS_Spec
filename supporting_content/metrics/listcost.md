# Column: ListCost

## Example provider mappings

Current column mappings found in available data sets:

| Provider  | Data set                     | Column                   |
|:----------|:-----------------------------|:-------------------------|
| AWS       | CUR                          | pricing/publicOnDemandCost  is a closest match;<br>Definition: The public On-Demand Cost for the billing period for the specific line item of usage and rate. For SKUs with multiple On-Demand public costs, the equivalent cost for the highest tier is displayed. (Example: Services offering free-tiers or tiered pricing).<br>Note: Currently, the note regarding the highest tier is found only in the pricing/publicOnDemandCost definition. Sample data records confirm that volume-based pricing applies to publicOnDemandCost, while tier-based pricing applies to other costs in CUR files. ListCost can be **computed by multiplying the pre-determined values in the FOCUS columns ListUnitPrice and QuantityInPricingUnit**. This approach is preferred over mapping pricing/publicOnDemandCost due to the previously mentioned inconsistency. |
| GCP       | BigQuery Billing Export      | **cost_at_list**<br>Definition: The list prices associated with all line items charged to your Cloud Billing account.<br>Disclaimer: **The first full day of data with this field is June 29, 2023**.<br>Notes: When/if not available can be **computed by multiplying the pre-determined values in the FOCUS columns ListUnitPrice and QuantityInPricingUnit**. GCP splits out each pricing tier into separate rows. The list price is shown as the current price at that point in time. All prices are shown in the currency of the selected billing account. |
| Microsoft | Cost details                 | paygCostInBillingCurrency (paygCostInUsd) is a closest match but it's no longer documented in [Understand usage details fields - Microsoft Cost Management](https://learn.microsoft.com/en-us/azure/cost-management-billing/automate/understand-usage-details-fields). When/if not available can be **computed by multiplying the pre-determined values in the FOCUS columns ListUnitPrice and QuantityInPricingUnit**. |
| OCI       | Cost and Usage Report        | **Not available** in Cost and Usage Report but can be **computed by multiplying the pre-determined values in the FOCUS columns ListUnitPrice and QuantityInPricingUnit**. |

## References and Resources

### AWS

* [Pricing details - AWS Cost and Usage Reports](https://docs.aws.amazon.com/cur/latest/userguide/pricing-columns.html)

### GCP

* [Structure of Standard data export | Cloud Billing](https://cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage)

### Microsoft

* [Understand usage details fields - Microsoft Cost Management](https://learn.microsoft.com/en-us/azure/cost-management-billing/automate/understand-usage-details-fields)

### OCI

* [Cost and Usage Reports Overview](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/usagereportsoverview.htm)

## Discussion / Scratch space

### ListCost is not-null even if ListUnitPrice is null

* In cases where ListUnitPrice and QuantityInPricingUnit are available (i.e., not null), the following applies: Cost = Price * Quantity. However, in cases where ListUnitPrice and QuantityInPricingUnit are not available (e.g., in the case of tax, ad-hoc credits, etc.), ListCost must be provided and must comply with the specified normative.

### Quantity-Driven Pricing strategies

* See [Appendix: Quantity-Driven Pricing strategies](../apendix/quantity_driven_pricing_strategies.md) section for more information on Quantity-Driven Pricing strategies (such as flat-rate, volume-based rates and tier-based rating) and related UC scenarios

### Current data sources

* Even though some major CSPs provide candidate columns for mapping to ListCost within their billing data, it is advisable to rely on multiplying the predetermined values in the FOCUS columns ListUnitPrice and QuantityInPricingUnit. This approach ensures more consistent and reliable results.
