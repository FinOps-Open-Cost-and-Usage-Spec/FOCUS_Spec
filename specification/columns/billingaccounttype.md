# Billing Account Type

Billing Account Type is the label the provider uses to describe the kind of the billing account. Billing Account Type is a readable display name and not a code. Billing Account Type is commonly used for scenarios like mapping FOCUS constructs to provider constructs and summarizing costs across providers.

The BillingAccountType column MUST be present and MUST NOT be null or empty. This column MUST be of type String and MUST NOT be null when BillingAccountId is not null. When BillingAccountId is null, BillingAccountType MUST also be null. Providers MUST use a consistent value-format and a set of values for BillingAccountType values within their cost and usage datasets.

## Column ID

BillingAccountType

## Display Name

Billing Account Type

## Description

Label the provider uses to describe the kind of billing account.

## Content Constraints

| Constraint      | Value            |
| :-------------- | :--------------- |
| Column required | True             |
| Data type       | String           |
| Allows nulls    | False            |
| Value format    | \<not specified> |

## Introduced (version)

1.0
