# Invoice ID

An [Invoice ID](#col) is an invoice-issuer-assigned identifier for an invoice encapsulating [charges](#term) in the corresponding [billing period](#term) for a given [billing account](#term). Invoices are commonly used for scenarios like tracking billing transactions, facilitating payment processes and for performing invoice reconciliation between [charges](#term) and billing periods.

## Requirements

[InvoiceId](#col) MUST adhere to the following requirements:

* [InvoiceId](#col) MUST be of type String.
* [InvoiceId](#col) MUST conform to [StringHandling](#attr) requirements.
* [InvoiceId](#col) MUST adhere to the following nullability requirements:
  * [InvoiceId](#col) MUST be null when the [charge](#term) is not associated either with an invoice or with a pre-generated provisional invoice.
  * [InvoiceId](#col) MUST NOT be null when the [charge](#term) is associated with either an issued invoice or a pre-generated provisional invoice.
* [InvoiceId](#col) MAY be generated prior to an invoice being issued.
* [InvoiceId](#col) MUST be associated with the related [charge](#term) and [BillingAccountId](#col) when a pre-generated invoice or provisional invoice exists.

See [Appendix: Grouping constructs for resources or services](#appendix.groupingconstructsforresourcesorservices) for details and examples of the different grouping constructs supported by FOCUS.

## Column ID

InvoiceId

## Display Name

Invoice ID

## Description

The invoice-issuer-assigned identifier for an invoice encapsulating [charges](#term) in the corresponding billing period for a given billing account.

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

1.2
