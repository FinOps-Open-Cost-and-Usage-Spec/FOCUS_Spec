# Invoice ID

[Invoice ID](#col) is an invoice-issuer-assigned identifier for an invoice encapsulating [charges](#term) in the corresponding [billing period](#term) for a given [billing account](#term). Invoices are commonly used for scenarios like tracking billing transactions, facilitating payment processes and for performing invoice reconciliation between [charges](#term) and billing periods.

## Requirements

[InvoiceId](#col) MUST adhere to the following requirements:

* [InvoiceId](#col) MUST be of type String.
* [InvoiceId](#col) MUST conform to [StringHandling](#attr) requirements.
* [InvoiceId](#col) MUST NOT be null.
* [InvoiceId](#col) MAY be generated prior to an invoice being issued.
* [InvoiceId](#col) MUST uniquely identify the invoice as provided by the [invoice issuer](#term).

## Column ID

InvoiceId

## Display Name

Invoice ID

## Description

The invoice-issuer-assigned identifier for an invoice encapsulating [charges](#term) in the corresponding billing period for a given billing account.

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
