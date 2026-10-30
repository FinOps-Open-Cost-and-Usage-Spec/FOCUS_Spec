# Invoice Detail Grain

[Invoice Detail Grain](#col) represents the set of key-value pairs that defines the granularity of an invoice line item. The grain may vary from one record to the next, both within a single invoice and across [invoice issuers](#term), and key-value pairs are used instead of separate columns to accommodate this variability.

This gives FinOps practitioners a single point of reference for all possible [Invoice Detail](#ds) granularities (e.g., SKU, service, resource, custom dimension), supporting downstream data transformations such as reconciliation and cost allocation.

## Requirements

[InvoiceDetailGrain](#col) MUST adhere to the following requirements:

* [InvoiceDetailGrain](#col) MUST be of type JSON Object (serialized as a String where necessary).
* [InvoiceDetailGrain](#col) MUST conform to [StringHandling](#attr) requirements.
* [InvoiceDetailGrain](#col) MUST conform to [KeyValueFormat](#attr) requirements.
* [InvoiceDetailGrain](#col) MUST NOT be null when one or more properties uniquely define the granularity of the invoice line item.
* [InvoiceDetailGrain](#col) MUST contain the set of all properties that uniquely define the granularity of the invoice line item.
* [InvoiceDetailGrain](#col) SHOULD use the applicable FOCUS-defined [InvoiceDetailGrain](#col) properties listed below to represent the granularity of the invoice line item.
* [InvoiceDetailGrain](#col) MUST include all custom [InvoiceDetailGrain](#col) properties that are applicable to the granularity of the invoice line item when there is no equivalent FOCUS-defined property.
* [InvoiceDetailGrain](#col) property keys SHOULD conform to [PascalCase](#term) format.
* [InvoiceDetailGrain](#col) property keys MUST begin with the string "x_" unless it is a FOCUS-defined property.
* FOCUS-defined [InvoiceDetailGrain](#col) properties MUST adhere to the following requirements:
  * Property key MUST match the spelling and casing specified for the FOCUS-defined property.
  * Property value MUST be of the type specified for that property.

## FOCUS-Defined Properties

The following keys should be used when applicable when a relevant concept is represented on an invoice. For more information, see the relevant [Cost and Usage](#ds) column entry.

* Contract ID (element of [ContractApplied](#col:CostAndUsage.ContractApplied))
* [Region ID](#col:CostAndUsage.RegionId)
* [Resource ID](#col:CostAndUsage.ResourceId)
* [Resource Type](#col:CostAndUsage.ResourceType)
* [Service Name](#col:CostAndUsage.ServiceName)
* [SKU ID](#col:CostAndUsage.SkuId)
* [SKU Meter](#col:CostAndUsage.SkuMeter)
* [SKU Price ID](#col:CostAndUsage.SkuPriceId)
* [Sub Account ID](#col:CostAndUsage.SubAccountId)

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

## Content Constraints

| Constraint                 | Value                                           |
| :------------------------- | :---------------------------------------------- |
| Dataset                    | [Invoice Detail](#ds)                           |
| Operating model conditions | Not applicable                                  |
| Column type                | Dimension                                       |
| Feature level              | Mandatory                                       |
| Allows nulls               | True                                            |
| Data type                  | JSON                                            |
| Value format               | [Key-Value Format](#attr)                       |

## Version Introduced

1.4
