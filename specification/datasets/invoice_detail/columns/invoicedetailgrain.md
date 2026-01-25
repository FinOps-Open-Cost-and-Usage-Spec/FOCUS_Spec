# Invoice Detail Grain

An Invoice Detail Grain represents the set of key-value pairs that defines the granularity of the invoice line item. This metadata helps FinOps practitioners understand the specific grouping or aggregation level of a given invoice line, such as whether it represents a summary by service, resource, or another dimensional attribute.

## Requirements

InvoiceDetailGrain adheres to the following requirements:

* InvoiceDetailGrain MUST be present in an Invoice Detail [*FOCUS dataset*](#glossary:FOCUS-dataset).
* InvoiceDetailGrain MUST be of type JSON.
* InvoiceDetailGrain MUST conform to [Key-Value Pair](#attributes.keyvaluepair) requirements.
* InvoiceDetailGrain MUST contain the set of dimensions that uniquely define the level of aggregation for the line item as specified by the [InvoiceIssuerName](#datasets.invoicedetail.invoiceissuername).

## Column ID

InvoiceDetailGrain

## Display Name

Invoice Detail Grain

## Description

The set of key-value pairs that defines the granularity of the invoice line item.

## Content constraints

|    Constraint    |              Value              |
|:----------------|:--------------------------------|
| Column type     | Dimension                       |
| Feature level   | Mandatory                       |
| Allows nulls    | True                            |
| Data type       | JSON                            |
| Value format    | Key-Value                       |

## Introduced (version)

1.4