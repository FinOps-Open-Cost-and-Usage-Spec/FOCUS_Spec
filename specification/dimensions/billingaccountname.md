# Billing Account Name

A billing account is a container for resources and/or services that are billed together in an invoice. Common scenarios for using billing accounts include grouping based on organizational constructs and hierarchy-based cost allocation approach.

A billing account name is a display name assigned to a billing account. It is commonly used for cost reporting, invoice reconciliation, and cost allocation scenarios.

The BillingAccountName column MUST be present in the billing data. This column MUST be of type String. The BillingAccountName MUST NOT be null if a display name can be assigned to a billing account. BillingAccountName MUST be unique when a customer has more than one billing account.

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
| Allows nulls    | False            |
| Value format    | \<not specified> |

## Introduced (version)

0.5