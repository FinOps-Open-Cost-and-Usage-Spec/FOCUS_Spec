# Invoice Detail ID

Invoice Detail ID is the invoice-issuer-assigned identifier for an [Invoice Detail](#datasets.invoicedetail) record encapsulating charges in the corresponding billing period for a given billing account. This identifier allows FinOps practitioners to map specific line items from an invoice to the granular charge data, facilitating detailed reconciliation and auditability.

## Requirements

InvoiceDetailId MUST adhere to the following requirements:

* InvoiceDetailId MUST be of type String.
* InvoiceDetailId MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* InvoiceDetailId MUST adhere to the following nullability requirements:
  * InvoiceDetailId MUST be null when the charge is not associated either with an invoice or with a pre-generated provisional invoice.
  * InvoiceDetailId MUST NOT be null when the charge is associated with either an issued invoice or a pre-generated provisional invoice.
* InvoiceDetailId MAY be generated prior to an invoice being issued. 
* InvoiceDetailId MUST uniquely identify a specific record within a given [InvoiceId](#datasets.invoicedetail.invoiceid).

## Column ID

InvoiceDetailId

## Display Name

Invoice Detail ID

## Description

The invoice-issuer-assigned identifier for an Invoice Detail record encapsulating charges in the corresponding billing period for a given billing account.

## Content constraints

|    Constraint    |              Value             |
|:----------------|:--------------------------------|
| Column type     | Dimension                       |
| Feature level   | Conditional                     |
| Allows nulls    | True                            |
| Data type       | String                          |
| Value format    | \<not specified>                |

## Introduced (version)

1.4