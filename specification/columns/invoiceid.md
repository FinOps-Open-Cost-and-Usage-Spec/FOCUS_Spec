# Invoice ID

An Invoice ID is a provider-assigned identifier for an invoice encapsulating some or all charges in the corresponding [*billing period*](#glossary:billing-period) for a given [*billing account*](#glossary:billing-account). Invoices are commonly used for scenarios like tracking billing transactions, facilitating payment processes and for performing invoice reconciliation between charges and billing periods.

The InvoiceId column adheres to the following requirements:

* InvoiceId is RECOMMENDED to be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* InvoiceId MUST be of type String.
* InvoiceId MUST conform to [StringHandling](#stringhandling) requirements.
* InvoiceId nullability is defined as follows:
  * InvoiceId MUST be null when the [*charge*](#glossary:charge) is not associated either with an invoice or with a pre-generated provisional invoice.
  * InvoiceId MUST NOT be null when the *charge* is associated with either an issued invoice or a pre-generated provisional invoice.
* InvoiceId MAY be generated prior to an invoice being issued.
* InvoiceId MUST be associated with the related *charge* and BillingAccountId when a pre-generated invoice or provisional invoice exists.

See [Appendix: Grouping constructs for resources or services](#groupingconstructsforresourcesorservices) for details and examples of the different grouping constructs supported by FOCUS.

## Column ID

InvoiceId

## Display Name

Invoice ID

## Description

The provider-assigned identifier for an invoice encapsulating some or all charges in the corresponding billing period for a given billing account.

## Content constraints

|    Constraint   |      Value       |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Feature level   | Recommended        |
| Allows nulls    | True            |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

1.2
