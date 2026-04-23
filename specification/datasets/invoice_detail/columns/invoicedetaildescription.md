# Invoice Detail Description

Invoice Detail Description is the invoice-issuer-provided description of an invoice line item. This description provides context for the charge as it appears on the invoice, often summarizing the service, resource, or period covered by that specific line item to assist in human-readable reconciliation.

## Requirements

InvoiceDetailDescription MUST adhere to the following requirements:

* InvoiceDetailDescription MUST be of type String.
* InvoiceDetailDescription MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* InvoiceDetailDescription SHOULD NOT be null.
* InvoiceDetailDescription maximum length SHOULD be provided in the corresponding FOCUS Metadata Schema.
* InvoiceDetailDescription MUST describe the [*charges*](#glossary:charge) represented by the [InvoiceDetailId](#datasets.invoicedetail.invoicedetailid).

## Column ID

InvoiceDetailDescription

## Display Name

Invoice Detail Description

## Description

The invoice-issuer-provided description of an invoice line item.

## Content Constraints

|    Constraint    |              Value             |
|:----------------|:--------------------------------|
| Column type     | Dimension                       |
| Feature level   | Mandatory                       |
| Allows nulls    | True                            |
| Data type       | String                          |
| Value format    | \<unspecified>                   |

## Introduced (Version)

1.4
