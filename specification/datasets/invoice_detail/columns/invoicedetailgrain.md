# Invoice Detail Grain

Invoice Detail Grain represents the set of key-value pairs that defines the granularity of an invoice line item. The grain may vary from one record to the next, both within a single invoice and across [*invoice issuers*](#glossary:invoice-issuer), and key-value pairs are used instead of separate columns to accommodate this variability.

This gives FinOps practitioners a single point of reference for all possible [Invoice Detail](#datamodel.invoicedetail) granularities (e.g., SKU, service, resource, custom dimension), supporting downstream data transformations such as reconciliation and cost allocation.

## Requirements

InvoiceDetailGrain MUST adhere to the following requirements:

* InvoiceDetailGrain MUST be of type JSON Object (serialized as a String where necessary).
* InvoiceDetailGrain MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* InvoiceDetailGrain MUST conform to [KeyValueFormat](#attributes.key-valueformat) requirements.
* InvoiceDetailGrain MUST NOT be null when one or more properties uniquely define the granularity of the invoice line item.
* InvoiceDetailGrain MUST contain the set of all properties that uniquely define the granularity of the invoice line item.
* InvoiceDetailGrain SHOULD use the applicable FOCUS-defined Invoice Detail Grain properties listed below to represent the granularity of the invoice line item.
* InvoiceDetailGrain MUST include all custom Invoice Detail Grain properties that are applicable to the granularity of the invoice line item when there is no equivalent FOCUS-defined property.
* InvoiceDetailGrain property keys SHOULD conform to [PascalCase](#glossary:pascalcase) format.
* InvoiceDetailGrain property keys MUST begin with the string "x_" unless it is a FOCUS-defined property.
* FOCUS-defined InvoiceDetailGrain properties MUST adhere to the following requirements:
  * Property key MUST match the spelling and casing specified for the FOCUS-defined property.
  * Property value MUST be of the type specified for that property.

## FOCUS-Defined Properties

The following keys should be used when applicable when a relevant concept is represented on an invoice. For more information, see the relevant [Cost and Usage](#datamodel.costandusage) column entry.

* Contract ID (element of [ContractApplied](#datamodel.costandusage.contractapplied))
* [Region ID](#datamodel.costandusage.regionid)
* [Resource ID](#datamodel.costandusage.resourceid)
* [Resource Type](#datamodel.costandusage.resourcetype)
* [Service Name](#datamodel.costandusage.servicename)
* [SKU ID](#datamodel.costandusage.skuid)
* [SKU Meter](#datamodel.costandusage.skumeter)
* [SKU Price ID](#datamodel.costandusage.skupriceid)
* [Sub Account ID](#datamodel.costandusage.subaccountid)

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

|    Constraint    |              Value             |
|:----------------|:--------------------------------|
| Dataset         | [Invoice Detail](#datamodel.invoicedetail)             |
| Operating Model Conditions      | Not applicable                                         |
| Column type     | Dimension                       |
| Feature level   | Mandatory                       |
| Allows nulls    | True                            |
| Data type       | JSON                            |
| Value format    | [Key-Value Format](#attributes.key-valueformat) |

## Version Introduced

1.4
