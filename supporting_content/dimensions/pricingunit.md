# Column: PricingUnit

## Example provider mappings

Current column mappings found in available data sets:

| Provider  | Data set                     | Column                   |
|:----------|:-----------------------------|:-------------------------|
| AWS       | CUR                          | pricing/unit             |
| GCP       | BigQuery Billing Export      | usage.pricing_unit       |
| Microsoft | Cost details                 | UnitOfMeasure            |
| OCI       | Cost and Usage Report        | cost/billingUnitReadable |

## Example usage scenarios

Current values observed in billing data for various scenarios:

| Provider  | Scenario                                          | Pattern                                                                                                                                    |
|-----------|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| AWS       | CUR                                               | hours; Hrs; Queries; GB; Secrets; vCPU-Hours; API Requests; Keys; Alarms etc.                                                              |
| GCP       | BigQuery Billing Export                           | tebibyte; count; gibibyte; tebibyte; hour; gibibyte hour; gibibyte month; gibibyte hour; gibibyte; hour; count; gibibyte month; etc.       |
| Microsoft | Cost details                                      | 1 Hour; 10 Hours; 1/Month; 1 GB; 10K; 1 GB-Month; etc.                                                                                     |
| OCI       | Cost and Usage Report                             | TBC                                                                                                                                        |

## References and Resources

### AWS

- [Pricing details - AWS Cost and Usage Reports](https://docs.aws.amazon.com/cur/latest/userguide/pricing-columns.html)

### GCP

- [Structure of Detailed data export | Cloud Billing](https://cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage)

### Microsoft

- [Understand usage details fields - Microsoft Cost Management](https://learn.microsoft.com/en-us/azure/cost-management-billing/automate/understand-usage-details-fields)

### OCI

- [Cost and Usage Reports Overview](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/usagereportsoverview.htm)

## Discussion / Scratch space

### Add into an appendix that describes pricing units, tiers, strategies
The most basic math for calculating costs of cloud or SaaS services is Unit Price * Quantity = Cost.  Because different services require measuring different fundamental usage units while using a common billing format, the quantity column’s meaning or scale is unclear without specifying the unit of measure.
