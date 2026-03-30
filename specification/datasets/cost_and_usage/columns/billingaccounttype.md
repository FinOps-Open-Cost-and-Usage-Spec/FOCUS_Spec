# Billing Account Type

Billing Account Type is an invoice-issuer-assigned name to identify the type of [*billing account*](#glossary:billing-account). Billing Account Type is a readable display name and not a code. Billing Account Type is commonly used for scenarios like mapping FOCUS and provider constructs, summarizing costs across providers, or invoicing and chargeback.

## Requirements

BillingAccountType MUST adhere to the following requirements:

* BillingAccountType MUST be of type String.
* BillingAccountType MUST adhere to the following nullability requirements:
  * BillingAccountType MUST be null when [BillingAccountId](#datasets.costandusage.billingaccountid) is null.
  * BillingAccountType MUST NOT be null when BillingAccountId is not null.
* BillingAccountType MUST be a consistent, readable display value.

## Column ID

BillingAccountType

## Display Name

Billing Account Type

## Description

An invoice-issuer-assigned name to identify the type of *billing account*.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [Cost and Usage](#datasets.costandusage)             |
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | False                                                |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Introduced (version)

1.2
