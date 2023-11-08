# Column: PricingMeasure

## Example provider mappings

Current column mappings found in available data sets:

| Provider  | Data set                                        | Column                   |
|:----------|:------------------------------------------------|:-------------------------|
| AWS       | CUR                                             | pricing/unit             |
| GCP       | BigQuery Billing Export                         | usage.pricing_unit       |
| Microsoft | Cost details                                    | UnitOfMeasure            |
| OCI       | Cost and Usage Report;<br>List Pricing REST API | cost/billingUnitReadable is closest match<br>*Note: The values in this column are similar but not identical to those in the List Pricing REST API; therefore, it may be preferable to rely on the List Pricing REST API, which we already plan to use for ListUnitPrice.* |

## Example usage scenarios

Current values observed in billing data for various scenarios:

| Provider  | Scenario                | Pattern                                                                                                                              |
|-----------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| AWS       | CUR                     | hours; Hrs; Queries; GB; Secrets; vCPU-Hours; API Requests; Keys; Alarms etc.                                                        |
| GCP       | BigQuery Billing Export | tebibyte; count; gibibyte; tebibyte; hour; gibibyte hour; gibibyte month; gibibyte hour; gibibyte; hour; count; gibibyte month; etc. |
| Microsoft | Cost details            | 1 Hour; 10 Hours; 1/Month; 1 GB; 10K; 1 GB-Month; etc.                                                                               |
| OCI       | Cost and Usage Report   | ONE GiB HOURS STORAGE_SIZE; ONE GiB HOURS MEMORY; etc.                                                                               |
| OCI       | List Pricing REST API   | Gigabyte Per Hour; etc.<br>*Note: Gigabyte Per Hour corresponds to both ONE GiB HOURS STORAGE_SIZE and ONE GiB HOURS MEMORY*         |

## References and Resources

### AWS

* [Pricing details - AWS Cost and Usage Reports](https://docs.aws.amazon.com/cur/latest/userguide/pricing-columns.html)

### GCP

* [Structure of Detailed data export | Cloud Billing](https://cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage)

### Microsoft

* [Understand usage details fields - Microsoft Cost Management](https://learn.microsoft.com/en-us/azure/cost-management-billing/automate/understand-usage-details-fields)

### OCI

* [Cost and Usage Reports Overview](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/usagereportsoverview.htm)

## Discussion / Scratch space

### PricingMeasure - non-normalized vs normalized

* After several discussions the team has decided to use **PricingMeasure (non-normalized)** instead of earlier proposed PricingUnit (semi-normalized).
* Distinction between non-normalized, semi-normalized/normalized columns is clear and it is in line with UsageUnit (semi-normalized) name.

* PricingMeasure is commonly used for scenarios like validating unit prices against the price sheet and thus must match (or at least align) with the corresponding value published in the price list. Since price sheets fall outside the scope of FOCUS, PricingMeasure remains non-normalized, retaining as-is values provided by the service providers, which are typically already present in current billing data and merely mapped. Consequently, in certain cases, PricingMeasure may even encompass both quantifiers and actual measurement units.

* To facilite improved comparability of quantities (in pricing units) across different entities being measured, priced, and charged, both within a single provider's offerings and across various providers, in the future (post 1.0) we plan to differentiate quantifiers from measurement units by introducing:
  * An additional metric for pricing unit quantifiers.
  * An additional 'semi-normalized' dimension for pricing measurement units, with established guidelines and recommended values, encompassing both base units and combined/derived values, similar to the Usage Unit (see [Usage Unit - Specification](../../specification/dimensions/usageunit.md) and [Usage Unit - Supporting content](.usageunit.md) for details).

* Note: In preparation for establishing guidelines and recommended values for the semi-normalized pricing measurement unit, it would be extremely helpful to have insight into as many current PricingMeasure distinct values as possible.
  * List of all distinct Microsoft/Azure EA unit of measure values is available at this [link](https://github.com/microsoft/finops-toolkit/pull/348).

### Add into an appendix that describes pricing units, tiers, strategies

The most basic math for calculating costs of cloud or SaaS services is Unit Price * Quantity = Cost.  Because different services require measuring different fundamental usage units while using a common billing format, the quantity column’s meaning or scale is unclear without specifying the unit of measure.
