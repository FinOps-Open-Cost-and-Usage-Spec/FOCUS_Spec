# Billing Account Type

Billing Account Type is the label the provider uses to describe the kind of [*billing account*](#glossary:billing-account). Billing Account Type is a readable display name and not a code. Billing Account Type is commonly used for scenarios like mapping FOCUS constructs to provider constructs and summarizing costs across providers.

The BillingAccountType column MUST be present in the billing data. This column MUST be of type String, MUST be null when [BillingAccountId](#billingaccountid) is null, and MUST NOT be null when BillingAccountId is not null. BillingAccountType MUST be a consistent, readable display value within the billing data.

## Column ID

BillingAccountType

## Display Name

Billing Account Type

## Description

Label the provider uses to describe the kind of billing account.

## Content Constraints

| Constraint      | Value            |
| :-------------- | :--------------- |
| Column type     | Dimension        |
| Column required | True             |
| Allows nulls    | False            |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

1.0
