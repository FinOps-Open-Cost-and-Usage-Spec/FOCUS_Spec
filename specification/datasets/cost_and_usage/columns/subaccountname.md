# Sub Account Name

A [Sub Account Name](#col) is a display name assigned to a [sub account](#term). [Sub Account Name](#col) is commonly used for scenarios like grouping based on organizational constructs, access management needs, and cost allocation strategies.

## Requirements

[SubAccountName](#col) MUST adhere to the following requirements:

* [SubAccountName](#col) MUST be of type String.
* [SubAccountName](#col) MUST conform to [StringHandling](#attr) requirements.
* [SubAccountName](#col) MUST adhere to the following nullability requirements:
  * [SubAccountName](#col) MUST be null when [SubAccountId](#col) is null.
  * [SubAccountName](#col) MUST NOT be null when [SubAccountId](#col) is not null.

See [Appendix: Grouping constructs for resources or services](#appendix.groupingconstructsforresourcesorservices) for details and examples of the different grouping constructs supported by FOCUS.

## Column ID

SubAccountName

## Display Name

Sub Account Name

## Description

A name assigned to a grouping of [resources](#term) or [services](#term), often used to manage access and/or cost.

## Content Constraints

| Constraint                 | Value                                     |
| :------------------------- | :---------------------------------------- |
| Dataset                    | [Cost and Usage](#ds)                     |
| Operating model conditions | [Includes Sub Accounts](#omc)                                          |
| Column type                | Dimension                                 |
| Feature level              | Conditional                               |
| Allows nulls               | True                                      |
| Data type                  | String                                    |
| Value format               | \<not specified>                          |

## Version Introduced

0.5
