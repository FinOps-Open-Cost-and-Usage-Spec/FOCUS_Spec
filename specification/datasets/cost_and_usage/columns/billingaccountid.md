# Billing Account ID

A [Billing Account ID](#col) is an invoice-issuer-assigned identifier for a [billing account](#term). [Billing accounts](#term) are commonly used for scenarios like grouping based on organizational constructs, invoice reconciliation and cost allocation strategies.

## Requirements

[BillingAccountId](#col) MUST adhere to the following requirements:

* [BillingAccountId](#col) MUST be of type String.
* [BillingAccountId](#col) MUST conform to [StringHandling](#attr) requirements.
* [BillingAccountId](#col) MUST NOT be null.
* [BillingAccountId](#col) MUST be a unique identifier within an [invoice issuer](#term).
* [BillingAccountId](#col) SHOULD be a fully-qualified identifier.

See [Appendix: Grouping constructs for resources or services](#appendix.groupingconstructsforresourcesorservices) for details and examples of the different grouping constructs supported by FOCUS.

## Column ID

BillingAccountId

## Display Name

Billing Account ID

## Description

The identifier assigned to a [billing account](#term) by the invoice issuer.

## Content Constraints

| Constraint                 | Value                                     |
| :------------------------- | :---------------------------------------- |
| Dataset                    | [Cost and Usage](#ds)                     |
| Operating model conditions | Not applicable                            |
| Column type                | Dimension                                 |
| Feature level              | Mandatory                                 |
| Allows nulls               | False                                     |
| Data type                  | String                                    |
| Value format               | \<not specified>                          |

## Version Introduced

0.5
