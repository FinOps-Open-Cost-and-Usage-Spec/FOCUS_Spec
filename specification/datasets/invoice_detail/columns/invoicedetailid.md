# Invoice Detail ID

[Invoice Detail ID](#col) is the invoice-issuer-assigned identifier for an [Invoice Detail](#ds) record encapsulating charges in the corresponding billing period for a given billing account. This identifier allows FinOps practitioners to map specific line items from an invoice to the granular charge data, facilitating detailed reconciliation and auditability.

## Requirements

[InvoiceDetailId](#col) MUST adhere to the following requirements:

* [InvoiceDetailId](#col) MUST be of type String.
* [InvoiceDetailId](#col) MUST conform to [StringHandling](#attr) requirements.
* [InvoiceDetailId](#col) MUST NOT be null.
* [InvoiceDetailId](#col) MUST uniquely identify a record within a given [InvoiceId](#col).

## Column ID

InvoiceDetailId

## Display Name

Invoice Detail ID

## Description

The invoice-issuer-assigned identifier for an [Invoice Detail](#ds) record encapsulating charges in the corresponding billing period for a given billing account.

## Content Constraints

| Constraint                 | Value                                      |
| :------------------------- | :----------------------------------------- |
| Dataset                    | [Invoice Detail](#ds)                      |
| Operating model conditions | Not applicable                             |
| Column type                | Dimension                                  |
| Feature level              | Mandatory                                  |
| Allows nulls               | False                                      |
| Data type                  | String                                     |
| Value format               | \<not specified>                           |

## Version Introduced

1.4
