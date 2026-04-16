# Billing Account ID

Billing Account ID is an invoice-issuer-assigned identifier for a [*billing account*](#glossary:billing-account). *Billing accounts* are commonly used for scenarios like grouping based on organizational constructs, invoice reconciliation and cost allocation strategies.

## Requirements

BillingAccountId MUST adhere to the following requirements:

* BillingAccountId MUST be of type String.
* BillingAccountId MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* BillingAccountId MUST NOT be null.
* BillingAccountId MUST be a unique identifier within an [*invoice issuer*](#glossary:invoice issuer).
* BillingAccountId SHOULD be a fully-qualified identifier.

See [Appendix: Grouping constructs for resources or services](#appendix.groupingconstructsforresourcesorservices) for details and examples of the different grouping constructs supported by FOCUS.

## Column ID

BillingAccountId

## Display Name

Billing Account ID

## Description

The identifier assigned to a *billing account* by the [*invoice issuer*](#glossary:invoice issuer).

## Content constraints

|    Constraint   |      Value       |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Feature level   | Mandatory        |
| Allows nulls    | False            |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

1.4
