# Sub Account ID

A [Sub Account ID](#col) is a service-provider-assigned identifier assigned to a [sub account](#term). [Sub Account ID](#col) is commonly used for scenarios like grouping based on organizational constructs, access management needs, and cost allocation strategies.

## Requirements

[SubAccountId](#col) MUST adhere to the following requirements:

* [SubAccountId](#col) MUST be of type String.
* [SubAccountId](#col) MUST conform to [StringHandling](#attr) requirements.
* [SubAccountId](#col) MUST adhere to the following nullability requirements:
  * [SubAccountId](#col) MUST be null when a [charge](#term) is not related to a [sub account](#term).
  * [SubAccountId](#col) MUST NOT be null when a [charge](#term) is related to a [sub account](#term).

See [Appendix: Grouping constructs for resources or services](#appendix.groupingconstructsforresourcesorservices) for details and examples of the different grouping constructs supported by FOCUS.

## Column ID

SubAccountId

## Display Name

Sub Account ID

## Description

An ID assigned to a grouping of [resources](#term) or [services](#term), often used to manage access and/or cost.

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
