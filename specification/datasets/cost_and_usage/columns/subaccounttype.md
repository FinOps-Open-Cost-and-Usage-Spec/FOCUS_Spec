# Sub Account Type

Sub Account Type is a service-provider-assigned name to identify the type of [*sub account*](#glossary:sub-account). Sub Account Type is a readable display name and not a code. Sub Account Type is commonly used for scenarios like mapping FOCUS and service provider constructs, summarizing costs across service providers, or invoicing and chargeback.

## Requirements

SubAccountType adheres to the following requirements:

* SubAccountType MUST be of type String.
* SubAccountType MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* SubAccountType nullability is defined as follows:
  * SubAccountType MUST be null when [SubAccountId](#datasets.costandusage.subaccountid) is null.
  * SubAccountType MUST NOT be null when SubAccountId is not null.
* SubAccountType MUST be a consistent, readable display value.

## Column ID

SubAccountType

## Display Name

Sub Account Type

## Description

A service-provider-assigned name to identify the type of *sub account*.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [Cost and Usage](#datasets.costandusage)             |
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Introduced (version)

1.2
