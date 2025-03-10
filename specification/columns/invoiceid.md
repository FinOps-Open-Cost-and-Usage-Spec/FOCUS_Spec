# Invoice ID

An Invoice ID is a provider-assigned identifier for an invoice encapsulating some or all charges in the corresponding [*billing period*](#glossary:billing-period) for a given [*billing account*](#glossary:billing-account). Invoices are commonly used for scenarios like tracking billing transactions, facilitating payment processes and for performing invoice reconciliation between charges and billing periods.

The Invoice ID column adheres to the following requirements:

* InvoiceId is RECOMMENDED to be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* InvoiceId MUST be of type String.
* InvoiceId MUST conform to [String Handling](#stringhandling) requirements.
* InvoiceId MUST be null when the [*charge*](#glossary:charge) is not associated either with an invoice or with a pre-generated provisional invoice.
* InvoiceId MUST NOT be null when the *charge* is associated with either an issued invoice or a pre-generated provisional invoice.
* InvoiceId MAY be generated prior to an invoice being issued.
* Where a pre-generated invoice or provisional invoice exists, it MUST be associated with the related *charge* and BillingAccountId.

For credit handling the Invoice ID column adheres to the following requirements:
* Credits related to current billing period:
  * InvoiceId MUST NOT be null and ChargeClass MUST be correction in the current *billing period*.
* Credits related to a previous billing period:
  * InvoiceId MUST contain the Invoice Id related to the previous *billing period* where a credit issued in the current billing period relates to a previous *billing period* and ChargeClass MUST be *correction*.

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
| Feature level   | Optional        |
| Allows nulls    | True            |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

1.2
