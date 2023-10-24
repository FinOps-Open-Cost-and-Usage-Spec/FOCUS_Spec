# Column: ChargeDescription

## Example provider mappings

Current resource types found or extracted from available data sets:

| Provider  | Data set                | Column                                            	|
| :-------- | :---------------------- | :-------------------------------------------------------|
| AWS       | CUR                     | lineItem/LineItemDescription 				|
| GCP       | BigQuery Billing Export | sku.description                                         |
| Microsoft | Cost details            | Not available      			                |

## Example usage scenarios

| Provider  | Data set                | Scenario                           | Value                    |
|:----------|:------------------------|:-----------------------------------|:-------------------------|
| AWS       | CUR                     | Not available                      | $0.00 per GB - US West (Oregon) data transfer from US West (Northern California) |
| GCP       | BigQuery Billing Export | Not available                      | Not Available            |
| Microsoft | Cost details            | via Cost export file		   | Not Available            |

## Discussion Topics

### Minimum Information Requirements vs Open-Ended

We deliberated if we should be more specific and define the minimum required information for this column?

- A list of FOCUS columns which we believe provide this high-level context without the need for additional discovery and thus must be included (concatenated) as part of the Charge description? (Irena)
- Are these enough? Region/location? Qty? (Larry)
  - What: lineItem/LineItemDescription
  - Where: Region
  - How (many): Qty

Considering a variable landscape across cloud, SaaS, etc. we decided to keep it open-ended.
