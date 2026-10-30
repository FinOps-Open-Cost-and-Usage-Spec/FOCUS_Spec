# Sub Account Type

[Sub Account Type](#col) is a service-provider-assigned name to identify the type of [sub account](#term). [Sub Account Type](#col) is a readable display name and not a code. [Sub Account Type](#col) is commonly used for scenarios like mapping FOCUS and service provider constructs, summarizing costs across service providers, or invoicing and chargeback.

## Requirements

[SubAccountType](#col) MUST adhere to the following requirements:

* [SubAccountType](#col) MUST be of type String.
* [SubAccountType](#col) MUST conform to [StringHandling](#attr) requirements.
* [SubAccountType](#col) MUST adhere to the following nullability requirements:
  * [SubAccountType](#col) MUST be null when [SubAccountId](#col) is null.
  * [SubAccountType](#col) MUST NOT be null when [SubAccountId](#col) is not null.
* [SubAccountType](#col) MUST be a consistent, readable display value.

## Column ID

SubAccountType

## Display Name

Sub Account Type

## Description

A service-provider-assigned name to identify the type of [sub account](#term).

## Content Constraints

| Constraint                 | Value                                     |
| :------------------------- | :---------------------------------------- |
| Dataset                    | [Cost and Usage](#ds)                     |
| Operating model conditions | [Includes Multiple Sub Account Types](#omc)                                                      |
| Column type                | Dimension                                 |
| Feature level              | Conditional                               |
| Allows nulls               | True                                      |
| Data type                  | String                                    |
| Value format               | \<not specified>                          |

## Version Introduced

1.2
