# Billing Account Name

A Billing Account Name is a display name assigned to a [*billing account*](#glossary:billing-account). *Billing accounts* are commonly used for scenarios like grouping based on organizational constructs, invoice reconciliation and cost allocation strategies.

The BillingAccountName column adheres to the following requirements:

* BillingAccountName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* BillingAccountName MUST be of type String.
* BillingAccountName MUST conform to [StringHandling](#stringhandling) requirements.
* BillingAccountName MUST NOT be null when the provider supports assigning a display name for the *billing account*.

See [Appendix: Grouping constructs for resources or services](#groupingconstructsforresourcesorservices) for details and examples of the different grouping constructs supported by FOCUS.

## Column ID

BillingAccountName

## Display Name

Billing Account Name

## Description

The display name assigned to a *billing account*.

## Content constraints

|    Constraint   |      Value       |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Feature level   | Mandatory        |
| Allows nulls    | True             |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

0.5
