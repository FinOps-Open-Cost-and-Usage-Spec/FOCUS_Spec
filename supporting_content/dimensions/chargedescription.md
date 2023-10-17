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

- Should we explicitly define the minimum required information for this column? A list of FOCUS (Irena)
- Are these enough? Region/location? Qty? (Larry)
	- What: lineItem/LineItemDescription
	- Where: Region
	- How (many): Qty
