# Billing Account ID

A billing account is a container for resources and/or services that are billed together in an invoice. Common scenarios for using billing accounts include grouping based on organizational constructs and hierarchy-based cost allocation approach.

A billing account ID is an provider assigned identifier for a billing account. It is commonly used for cost reporting, invoice reconciliation and cost allocation scenarios.

The BillingAccountId column MUST be present in the billing data. This column must be of type String and MUST NOT contain null values. BillingAccountId SHOULD be a globally unique identifier within a provider. BillingAccountId MUST be unique when a customer has more than one billing account.

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