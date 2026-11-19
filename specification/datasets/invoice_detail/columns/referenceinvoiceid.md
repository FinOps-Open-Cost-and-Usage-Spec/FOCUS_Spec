# Reference Invoice ID

[Reference Invoice ID](#col) is an invoice-issuer-assigned identifier for an invoice that affects charges as stated on a previous invoice. This occurs typically in the context of credits, refunds, or corrections where an adjustment is applied to a specific previously-issued billing document. This ID allows for direct lineage between adjustments and the original billing records.

## Requirements

[ReferenceInvoiceId](#col) MUST adhere to the following requirements:

* [ReferenceInvoiceId](#col) MUST be of type String.
* [ReferenceInvoiceId](#col) MUST conform to [StringHandling](#attr) requirements.
* [ReferenceInvoiceId](#col) MUST NOT be null.
* [ReferenceInvoiceId](#col) MUST match the [InvoiceId](#col) of the original [invoice](#term) when it adjusts another invoice.
* [ReferenceInvoiceId](#col) MUST match the [InvoiceId](#col) of the current invoice when it does not adjust another invoice.

## Column ID

ReferenceInvoiceId

## Display Name

Reference Invoice ID

## Description

The invoice-issuer-assigned identifier for an invoice that affects charges as stated on a previous invoice.

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
