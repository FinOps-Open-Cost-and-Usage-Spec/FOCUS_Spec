# Billing Account Name

A [Billing Account Name](#col) is a display name assigned to a [billing account](#term). [Billing accounts](#term) are commonly used for scenarios like grouping based on organizational constructs, invoice reconciliation and cost allocation strategies.

## Requirements

[BillingAccountName](#col) MUST adhere to the following requirements:

* [BillingAccountName](#col) MUST be of type String.
* [BillingAccountName](#col) MUST conform to [StringHandling](#attr) requirements.
* [BillingAccountName](#col) MUST NOT be null when the [invoice issuer](#term) supports assigning a display name for the [billing account](#term).

See [Appendix: Grouping constructs for resources or services](#appendix.groupingconstructsforresourcesorservices) for details and examples of the different grouping constructs supported by FOCUS.

## Column ID

BillingAccountName

## Display Name

Billing Account Name

## Description

The display name assigned to a [billing account](#term).

## Content Constraints

| Constraint                 | Value                                     |
| :------------------------- | :---------------------------------------- |
| Dataset                    | [Cost and Usage](#ds)                     |
| Operating model conditions | Not applicable                            |
| Column type                | Dimension                                 |
| Feature level              | Mandatory                                 |
| Allows nulls               | True                                      |
| Data type                  | String                                    |
| Value format               | \<not specified>                          |

## Version Introduced

0.5
