# Sub Account Type

Sub Account Type is the label the provider uses to describe the kind of the sub account. Sub Account Type is a readable display name and not a code. Sub Account Type is commonly used for scenarios like mapping FOCUS constructs to provider constructs and summarizing costs across providers.

The SubAccountType column MUST be present and MUST NOT be null or empty. This column MUST be of type String and MUST NOT be null when SubAccountId is not null. When SubAccountId is null, SubAccountType MUST also be null. Providers MUST use a consistent value-format and a set of values for SubAccountType values within their cost and usage datasets.

## Column ID

SubAccountType

## Display Name

Sub Account Type

## Description

Label the provider uses to describe the kind of sub account.

## Content Constraints

| Constraint      | Value            |
| :-------------- | :--------------- |
| Column required | True             |
| Data type       | String           |
| Allows nulls    | False            |
| Value format    | \<not specified> |

## Introduced (version)

1.0
