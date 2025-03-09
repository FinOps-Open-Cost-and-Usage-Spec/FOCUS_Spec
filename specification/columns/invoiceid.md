# Invoice ID

An Invoice ID is a invoice Issuer assigned identifier for an invoice encapsulating some or all charges in the corresponding [*billing period*](#glossary:billing-period) for a given [*billing account*](#glossary:billing-account). Invoices are commonly used for scenarios like tracking billing transactions, facilitating payment processes and for performing invoice reconciliation between charges and billing periods.

The Invoice ID column adheres to the following requirements:

* InvoiceId is RECOMMENDED to be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* InvoiceId MUST be of type String.
* InvoiceId MUST conform to [String Handling](#stringhandling) requirements.
* InvoiceId MUST be null when the [*charge*](#glossary:charge) is not associated either with an invoice or with a pre-generated provisional invoice.
* InvoiceId MUST NOT be null when the *charge* is associated with either an issued invoice or a pre-generated provisional invoice.
* InvoiceId MAY be generated prior to an invoice being issued.
* Where a pre-generated invoice or provisional invoice exists, it MUST be associated with the related charge and billingaccountId.

> Editor's Note: The group agrees the construct of the column is suitable to go for approval, however it requires some further definition to clarify credit handling. The group will determine if this should be in the column definition or supporting content.

See [Appendix: Grouping constructs for resources or services](#groupingconstructsforresourcesorservices) for details and examples of the different grouping constructs supported by FOCUS.

## Column ID

InvoiceId

## Display Name

Invoice Id

## Description

The service provider-assigned identifier for an invoice encapsulating some or all charges in the corresponding billing period for a given billing account.

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
