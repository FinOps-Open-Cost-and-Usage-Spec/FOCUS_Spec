# Sub Account Type

Sub Account Type is the label the provider uses to describe the kind of [*sub account*](#glossary:sub-account). Sub Account Type is a readable display name and not a code. Sub Account Type is commonly used for scenarios like mapping FOCUS constructs to provider constructs and summarizing costs across providers.

The SubAccountType column MUST be present in the billing data. This column MUST be of type String, MUST be null when [SubAccountId](#subaccountid) is null, and MUST NOT be null when SubAccountId is not null. SubAccountType MUST be a consistent, readable display value within the billing data.

## Column ID

SubAccountType

## Display Name

Sub Account Type

## Description

Label the provider uses to describe the kind of sub account.

## Content Constraints

| Constraint      | Value            |
| :-------------- | :--------------- |
| Column type     | Dimension        |
| Column required | True             |
| Allows nulls    | True             |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

1.0
