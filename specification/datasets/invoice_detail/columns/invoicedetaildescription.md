# Invoice Detail Description

An Invoice Detail Description is the invoice-issuer-provided description of an invoice line item. This description provides context for the charge as it appears on the invoice, often summarizing the service, resource, or period covered by that specific line item to assist in human-readable reconciliation.

## Requirements

InvoiceDetailDescription adheres to the following requirements:

* InvoiceDetailDescription MUST be present in an Invoice Detail [*FOCUS dataset*](#glossary:FOCUS-dataset).
* InvoiceDetailDescription MUST be of type String.
* InvoiceDetailDescription MUST be the description of the cost represented by the [InvoiceDetailId](#datasets.invoicedetail.invoicedetailid).

## Column ID

InvoiceDetailDescription

## Display Name

Invoice Detail Description

## Description

The invoice-issuer-provided description of an invoice line item.

## Content constraints

|    Constraint    |              Value             |
|:----------------|:--------------------------------|
| Column type     | Dimension                       |
| Feature level   | Mandatory                       |
| Allows nulls    | False                           |
| Data type       | String                          |
| Value format    | <unspecified>                   |

## Introduced (version)

1.4