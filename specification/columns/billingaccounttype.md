# Billing Account Type

Billing Account Type is a provider-assigned name to identify the type of [*billing account*](#glossary:billing-account). Billing Account Type is a readable display name and not a code. Billing Account Type is commonly used for scenarios like mapping FOCUS and provider constructs, summarizing costs across providers, or invoicing and chargeback.

The BillingAccountType column adheres to the following requirements:

* BillingAccountType MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports more than one possible BillingAccountType value.
* BillingAccountType MUST be of type String.
* BillingAccountType MUST conform to [StringHandling](#stringhandling) requirements.
* BillingAccountType nullability is defined as follows:
  * BillingAccountType MUST be null when [BillingAccountId](#billingaccountid) is null.
  * BillingAccountType MUST NOT be null when BillingAccountId is not null.
* BillingAccountType MUST be a consistent, readable display value.

## Column ID

BillingAccountType

## Display Name

Billing Account Type

## Description

A provider-assigned identifier for the type of *billing account* applied to the charge.

## Content Constraints

| Constraint      | Value            |
| :-------------- | :--------------- |
| Column type     | Dimension        |
| Feature level   | Conditional      |
| Column required | True             |
| Allows nulls    | False            |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

1.2
