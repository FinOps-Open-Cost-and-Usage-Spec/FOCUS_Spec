# Invoice ID

An Invoice ID is an invoice-issuer-assigned identifier for an invoice encapsulating [*charges*](#glossary:charge) in the corresponding [*billing period*](#glossary:billing-period) for a given [*billing account*](#glossary:billing-account). Invoices are commonly used for scenarios like tracking billing transactions, facilitating payment processes and for performing invoice reconciliation between *charges* and billing periods.

## Requirements

InvoiceId MUST adhere to the following requirements:

* InvoiceId MUST be of type String.
* InvoiceId MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* InvoiceId MUST adhere to the following nullability requirements:
  * InvoiceId MUST be null when the *charge* is not associated either with an invoice or with a pre-generated provisional invoice.
  * InvoiceId MUST NOT be null when the *charge* is associated with either an issued invoice or a pre-generated provisional invoice.
* InvoiceId MAY be generated prior to an invoice being issued.
* InvoiceId MUST be associated with the related *charge* and BillingAccountId when a pre-generated invoice or provisional invoice exists.

See [Appendix: Grouping constructs for resources or services](#appendix.groupingconstructsforresourcesorservices) for details and examples of the different grouping constructs supported by FOCUS.

## Column ID

InvoiceId

## Display Name

Invoice ID

## Description

The invoice-issuer-assigned identifier for an invoice encapsulating *charges* in the corresponding billing period for a given billing account.

## Content constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [Cost and Usage](#datasets.costandusage)             |
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Introduced (version)

1.2
