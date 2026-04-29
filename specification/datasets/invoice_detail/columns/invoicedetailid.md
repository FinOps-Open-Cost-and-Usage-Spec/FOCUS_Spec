# Invoice Detail ID

Invoice Detail ID is the invoice-issuer-assigned identifier for an [Invoice Detail](#datasets.invoicedetail) record encapsulating charges in the corresponding billing period for a given billing account. This identifier allows FinOps practitioners to map specific line items from an invoice to the granular charge data, facilitating detailed reconciliation and auditability.

## Requirements

InvoiceDetailId MUST adhere to the following requirements:

* InvoiceDetailId MUST be of type String.
* InvoiceDetailId MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* InvoiceDetailId MUST NOT be null.
* InvoiceDetailId MUST uniquely identify a record within a given [InvoiceId](#datasets.invoicedetail.invoiceid).

## Column ID

InvoiceDetailId

## Display Name

Invoice Detail ID

## Description

The invoice-issuer-assigned identifier for an Invoice Detail record encapsulating charges in the corresponding billing period for a given billing account.

## Content Constraints

|    Constraint    |              Value             |
|:----------------|:--------------------------------|
| Column type     | Dimension                       |
| Feature level   | Mandatory                       |
| Allows nulls    | False                           |
| Data type       | String                          |
| Value format    | \<not specified>                |

## Version Introduced

1.4
