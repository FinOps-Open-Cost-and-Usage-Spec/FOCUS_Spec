# Billing Account Type

[Billing Account Type](#col) is an invoice-issuer-assigned name to identify the type of [billing account](#term). [Billing Account Type](#col) is a readable display name and not a code. [Billing Account Type](#col) is commonly used for scenarios like mapping FOCUS and provider constructs, summarizing costs across providers, or invoicing and chargeback.

## Requirements

[BillingAccountType](#col) MUST adhere to the following requirements:

* [BillingAccountType](#col) MUST be of type String.
* [BillingAccountType](#col) MUST conform to [StringHandling](#attr) requirements.
* [BillingAccountType](#col) MUST adhere to the following nullability requirements:
  * [BillingAccountType](#col) MUST be null when [BillingAccountId](#col) is null.
  * [BillingAccountType](#col) MUST NOT be null when [BillingAccountId](#col) is not null.
* [BillingAccountType](#col) MUST be a consistent, readable display value.

## Column ID

BillingAccountType

## Display Name

Billing Account Type

## Description

An invoice-issuer-assigned name to identify the type of [billing account](#term).

## Content Constraints

| Constraint                 | Value                                     |
| :------------------------- | :---------------------------------------- |
| Dataset                    | [Cost and Usage](#ds)                     |
| Operating model conditions | [Includes Multiple Billing Account Types](#omc)                                                          |
| Column type                | Dimension                                 |
| Feature level              | Conditional                               |
| Allows nulls               | False                                     |
| Data type                  | String                                    |
| Value format               | \<not specified>                          |

## Version Introduced

1.2
