# Billing Account ID

A Billing Account ID is an invoice-issuer-assigned identifier for a [*billing account*](#glossary:billing-account). *Billing accounts* are commonly used for scenarios like grouping based on organizational constructs, invoice reconciliation and cost allocation strategies.

## Requirements

BillingAccountId adheres to the following requirements:

* BillingAccountId MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).
* BillingAccountId MUST be of type String.
* BillingAccountId MUST conform to [StringHandling](#stringhandling) requirements.
* BillingAccountId MUST NOT be null.
* BillingAccountId MUST be a unique identifier within an invoice issuer.
* BillingAccountId SHOULD be a fully-qualified identifier.

See [Appendix: Grouping constructs for resources or services](#groupingconstructsforresourcesorservices) for details and examples of the different grouping constructs supported by FOCUS.

## Column ID

BillingAccountId

## Display Name

Billing Account ID

## Description

The identifier assigned to a *billing account* by the invoice issuer.

## Content constraints

|    Constraint   |      Value       |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Feature level   | Mandatory        |
| Allows nulls    | False            |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

0.5
