# Invoice Detail ID

[Invoice Detail ID](#col) is the invoice-issuer-assigned identifier for an [Invoice Detail](#ds) record encapsulating charges in the corresponding billing period for a given billing account. This identifier allows FinOps practitioners to map specific line items from an invoice to the granular charge data, facilitating detailed reconciliation and auditability.

## Requirements

[InvoiceDetailId](#col) MUST adhere to the following requirements:

* [InvoiceDetailId](#col) MUST be of type String.
* [InvoiceDetailId](#col) MUST conform to [StringHandling](#attr) requirements.
* [InvoiceDetailId](#col) MUST adhere to the following nullability requirements:
  * [InvoiceDetailId](#col) MUST be null when the charge is not associated either with an invoice or with a pre-generated provisional invoice.
  * [InvoiceDetailId](#col) MUST NOT be null when the charge is associated with either an issued invoice or a pre-generated provisional invoice.
* [InvoiceDetailId](#col) MAY be generated prior to an invoice being issued.
* [InvoiceDetailId](#col) MUST uniquely identify a specific record within a given [InvoiceId](#col:InvoiceDetail.InvoiceId).

## Column ID

InvoiceDetailId

## Display Name

Invoice Detail ID

## Description

The invoice-issuer-assigned identifier for an [Invoice Detail](#ds) record encapsulating charges in the corresponding billing period for a given billing account.

## Content Constraints

| Constraint                 | Value                                     |
| :------------------------- | :---------------------------------------- |
| Dataset                    | [Cost and Usage](#ds)                     |
| Operating model conditions | [Includes Payable Invoices](#omc)                                              |
| Column type                | Dimension                                 |
| Feature level              | Conditional                               |
| Allows nulls               | True                                      |
| Data type                  | String                                    |
| Value format               | \<not specified>                          |

## Version Introduced

1.4
