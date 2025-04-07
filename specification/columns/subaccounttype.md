# Sub Account Type

Sub Account Type is a provider-assigned name to identify the type of [*sub account*](#glossary:sub-account). Sub Account Type is a readable display name and not a code. Sub Account Type is commonly used for scenarios like mapping FOCUS and provider constructs, summarizing costs across providers, or invoicing and chargeback.

The SubAccountType column adheres to the following requirements:

* SubAccountType MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports more than one possible SubAccountType value.
* SubAccountType MUST be of type String.
* SubAccountType MUST conform to [StringHandling](#stringhandling) requirements.
* SubAccountType nullability is defined as follows:
  * SubAccountType MUST be null when [SubAccountId](#subaccountid) is null.
  * SubAccountType MUST NOT be null when SubAccountId is not null.
* SubAccountType MUST be a consistent, readable display value.

## Column ID

SubAccountType

## Display Name

Sub Account Type

## Description

A provider-assigned identifier for the type of *sub account* applied to the charge.

## Content Constraints

| Constraint      | Value            |
| :-------------- | :--------------- |
| Column type     | Dimension        |
| Feature level   | Conditional      |
| Column required | True             |
| Allows nulls    | True             |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

1.2
