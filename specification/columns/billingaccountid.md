# Billing Account ID

A [*billing account*](#glossary:billing-account) is a container for [*resources*](#glossary:resource) and/or services that are billed together in an invoice. *Billing accounts* are commonly used for scenarios like grouping based on organizational constructs, invoice reconciliation, and cost allocation strategies.

A Billing Account ID is a [*provider*](#glossary:provider) assigned identifier for a *billing account*.

The BillingAccountId column MUST be present in the billing data. This column MUST be of type String and MUST NOT contain null values. BillingAccountId MUST be a globally unique identifier within a *provider*.

See [Appendix: Grouping constructs for resources and/or services](#groupingconstructsforresourcesand/orservices) for details and examples of the different grouping constructs supported by [FOCUS](#glossary:finops-cost-and-usage-specification).

## Column ID

BillingAccountId

## Display name

Billing Account ID

## Description

The identifier assigned to a *billing account* by the *provider*.

## Content constraints

|    Constraint   |      Value      |
|:----------------|:----------------|
| Column required | True            |
| Data type       | String          |
| Allows nulls    | False            |
| Value format    | \<not specified> |

## Introduced (version)

0.5
