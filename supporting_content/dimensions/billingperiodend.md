# Column: BillingPeriodEnd

## Example provider mappings

Current column mappings found in available data sets:

| Provider  | Data set                 | Column                      |
|:----------|:-------------------------|:----------------------------|
| AWS       | CUR                      | bill/BillingPeriodEndDate |
| GCP       | BigQuery Billing Export  | invoice.month               |
| Microsoft | Cost details             | BillingPeriodEndDate      |
| OCI       | Cost reports             | lineItem/intervalUsageEnd |

## Example usage scenarios

| Provider  | Data set                | Scenario                           | Value                    |
|:----------|:------------------------|:-----------------------------------|:-------------------------|
| AWS       | CUR                     | Not available                      | 2023-05-01T00:00:00.000Z |
| GCP       | BigQuery Billing Export | Not available                      | 202304                   |
| Microsoft | Cost details            | via Consumption API (usageDetails) | 2022-10-11T00:00:00Z     |
| Microsoft | Cost details            | via Cost export file               | 02/13/2023               |
| OCI       | Cost reports            | via Cost report files              | 2022-08-19T02:00Z        |

## Discussion Topics

* See discussion topics from [Billing Period Start](../billingperiodstart.md)
