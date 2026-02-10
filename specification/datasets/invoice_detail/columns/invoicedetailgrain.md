# Invoice Detail Grain

Invoice Detail Grain represents the set of key-value pairs that defines the granularity of the invoice line item. This data is represented as key-value pairs instead of separate columns because the grain may vary from one record to the next, both on a single invoice and across invoice issuers; this enables FinOps practitioners to have a single point of reference for the known universe of [Invoice Detail](#datasets.invoicedetail) granularities for use in any necessary downstream data transformations. This information helps FinOps practitioners understand the specific grouping or aggregation level of a given [Invoice Detail](#datasets.invoicedetail) record, such as whether it represents a summary by service, resource, or another dimensional attribute.

## Requirements

InvoiceDetailGrain adheres to the following requirements:

* InvoiceDetailGrain MUST be of type JSON.
* InvoiceDetailGrain MUST conform to [KeyValueFormat](#attributes.key-valueformat) requirements.
* InvoiceDetailGrain property keys SHOULD conform to PascalCase format.
* InvoiceDetailGrain MUST NOT be null when one or more properties uniquely define the granularity of the invoice line item.
* InvoiceDetailGrain MUST contain the set of all properties that uniquely define the granularity of the invoice line item.
* InvoiceDetailGrain SHOULD use the applicable FOCUS-defined Invoice Detail Grain properties listed below to represent the granularity of the invoice line item.
* InvoiceDetailGrain MUST include all custom Invoice Detail Grain properties that are applicable to the granularity of the invoice line item when there is no equivalent FOCUS-defined property.
* InvoiceDetailGrain property keys SHOULD conform to [PascalCase](#glossary:pascalcase) format.
* InvoiceDetailGrain property keys MUST begin with the string "x_" unless it is a FOCUS-defined property.
* FOCUS-defined InvoiceDetailGrain properties adhere to the following additional requirements:
  * Property key MUST match the spelling and casing specified for the FOCUS-defined property.
  * Property value MUST be of the type specified for that property.

## Examples

```json
{
    "ServiceName": "Elastic Cloud Server",
    "ResourceType": "Cloud Host",
    "x_BillingMode": "Pay-per-Use"
}
```

## Column ID

InvoiceDetailGrain

## Display Name

Invoice Detail Grain

## Description

The set of key-value pairs that defines the granularity of the invoice line item.

## Content constraints

|    Constraint    |              Value             |
|:----------------|:--------------------------------|
| Column type     | Dimension                       |
| Feature level   | Mandatory                       |
| Allows nulls    | True                            |
| Data type       | JSON                            |
| Value format    | [Key-Value Format](#attributes.key-valueformat) |

### FOCUS-Defined Properties

The following keys should be used when applicable when a relevant concept is represented on an invoice. For more information, see the relevant [Cost and Usage](#datasets.costandusage) column entry.

* Contract ID (element of [ContractApplied](#datasets.costandusage.contractapplied))
* [Region ID](#datasets.costandusage.regionid)
* [Resource ID](#datasets.costandusage.resourceid)
* [Resource Type](#datasets.costandusage.resourcetype)
* [Service Name](#datasets.costandusage.servicename)
* [SKU ID](#datasets.costandusage.skuid)
* [SKU Meter](#datasets.costandusage.skumeter)
* [SKU Price ID](#datasets.costandusage.skupriceid)
* [Sub Account ID](#datasets.costandusage.subaccountid)

## Introduced (version)

1.4