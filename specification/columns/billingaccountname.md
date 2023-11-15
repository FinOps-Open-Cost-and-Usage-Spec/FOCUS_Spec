# Billing Account Name

A Billing Account Name is a display name assigned to a [*billing account*](#glossary:billing-account). *Billing accounts* are commonly used for scenarios like grouping based on organizational constructs, invoice reconciliation and cost allocation strategies.

The BillingAccountName column MUST be present in the billing data. This column MUST be of type String. The BillingAccountName MUST NOT be null if a display name can be assigned to a *billing account*. BillingAccountName MUST be unique within a customer when a customer has more than one *billing account*.

See [Appendix: Grouping constructs for resources or services](#groupingconstructsforresourcesorservices) for details and examples of the different grouping constructs supported by FOCUS.

## Column ID

BillingAccountName

## Display name

Billing Account Name

## Description

The display name assigned to a *billing account*.

## Content constraints

|    Constraint   |      Value       |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Column required | True             |
| Allows nulls    | True             |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

0.5
