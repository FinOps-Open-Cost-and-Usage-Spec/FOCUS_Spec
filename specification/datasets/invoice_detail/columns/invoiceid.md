# Invoice ID

Invoice ID is an invoice-issuer-assigned identifier for an invoice encapsulating [*charges*](#glossary:charge) in the corresponding [*billing period*](#glossary:billing-period) for a given [*billing account*](#glossary:billing-account). Invoices are commonly used for scenarios like tracking billing transactions, facilitating payment processes and for performing invoice reconciliation between *charges* and billing periods.

## Requirements

InvoiceId MUST adhere to the following requirements:

* InvoiceId MUST be of type String.
* InvoiceId MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* InvoiceId MUST NOT be null.
* InvoiceId MAY be generated prior to an invoice being issued.
* InvoiceId MUST uniquely identify the invoice as provided by the invoice issuer.

## Column ID

InvoiceId

## Display Name

Invoice ID

## Description

The invoice-issuer-assigned identifier for an invoice encapsulating *charges* in the corresponding billing period for a given billing account.

## Content Constraints

|    Constraint   |      Value       |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Feature level   | Mandatory        |
| Allows nulls    | False            |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

1.4
