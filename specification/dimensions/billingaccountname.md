# Billing Account Name

A billing account is a container for resources and/or services that are billed together in an invoice. Billing accounts are commonly used for scenarios like grouping based on organizational constructs, invoice reconciliation and cost allocation strategies.

A billing account name is a display name assigned to a billing account.

The BillingAccountName column MUST be present in the billing data. This column MUST be of type String. The BillingAccountName MUST NOT be null if a display name can be assigned to a billing account. BillingAccountName MUST be unique within a customer when a customer has more than one billing account.

## Column ID

BillingAccountName

## Display name

Billing Account Name

## Description

The display name assigned to a billing account.

## Content constraints

|    Constraint   |      Value      |
|:----------------|:----------------|
| Column required | True            |
| Data type       | String          |
| Allows nulls    | True            |
| Value format    | \<not specified> |

## Introduced (version)

0.5
