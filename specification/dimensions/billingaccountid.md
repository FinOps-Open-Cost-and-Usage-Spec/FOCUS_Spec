# Billing Account ID

A billing account is a container for resources and/or services that are billed together in an invoice. Billing accounts are commonly used for scenarios like grouping based on organizational constructs, invoice reconciliation and cost allocation strategies.

A billing account ID is a provider assigned identifier for a billing account.

The BillingAccountId column MUST be present in the billing data. This column must be of type String and MUST NOT contain null values. BillingAccountId MUST be a globally unique identifier within a provider.

## Column ID

BillingAccountId

## Display name

Billing Account ID

## Description

The identifier assigned to a billing account by the provider.

## Content constraints

|    Constraint   |      Value      |
|:----------------|:----------------|
| Column required | True            |
| Data type       | String          |
| Allows nulls    | False            |
| Value format    | \<not specified> |

## Introduced (version)

0.5
