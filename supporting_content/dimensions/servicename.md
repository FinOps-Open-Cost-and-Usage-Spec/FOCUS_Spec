# Column: ServiceName

## Example provider mappings

Current column mappings found in available data sets:

| Provider  | Data set                 | Column                                                    |
|-----------|--------------------------|-----------------------------------------------------------|
| AWS       | CUR                      | line_item_product_code                                    |
| GCP       | Big Query Billing Export | service.description                                       |
| Microsoft | Cost details             | ServiceName (EA only)<br>MeterCategory (EA and MCA)<br>(Both are functionally the same. ServiceName has “cleaner” values for EA only.)<br>Related:<br>ConsumedService (represents the ARM resource provider, which is not a 1:1 relationship to the actual service)<br>Description: Name of the classification category for the meter. Same as the service in the Microsoft Customer Agreement Price Sheet. Exact string values differ. |
| Microsoft | Price sheet              | serviceName                                               |                                                                                                                                                                 |

## Example usage scenarios

Current values observed in billing data for various scenarios:

| Provider  | Data set                 | Example Value                                      |
|-----------|--------------------------|----------------------------------------------------|
| AWS       | CUR                      | AmazonS3, AmazonRDS                                |
| GCP       | Big Query Billing Export | Networking, Cloud SQL, BigQuery                    |
| Microsoft | Cost details             | Virtual Machines, Azure App Service, Azure Monitor |

- Microsoft: [understand-usage-details-fields](https://learn.microsoft.com/en-us/azure/cost-management-billing/automate/understand-usage-details-fields)
- AWS: The code of the product measured
- GCP: The service.description column contains the name of the service.

## Discussion / Scratch space

- Definition for ‘Service’ to come from the glossary
