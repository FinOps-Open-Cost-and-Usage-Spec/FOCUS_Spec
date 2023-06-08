# Sub Account Name

A sub account is an optional provider-supported construct for organizing resources and services connected to a billing account. Sub accounts are commonly used for scenarios like grouping based on organizational constructs, access management needs and cost allocation strategies. Sub accounts must be associated with a billing account as they do not receive invoices.

A sub account name is a display name assigned to a sub account.

The SubAccountName column MUST be present in the billing data. This column MUST be of type String and SHOULD NOT contain null values. If a provider doesn't support a sub account construct (only has a billing account), BillingAccountName value SHOULD BE used. If a provider does support a sub account construct, but the charge does not apply to a sub account, the SubAccountName column MAY be null.

## Column ID

SubAccountName

## Display name

Sub Account Name

## Description

A name assigned to a grouping of resources, often used to manage access and/or cost.

## Content constraints

| Constraint      | Value           |
|-----------------|-----------------|
| Column required | True            |
| Data type       | String          |
| Allows nulls    | False*          |
| Value format    | \<not specified> |

* Where a provider doesn't support a sub account construct, use the BillingAccountName value

## Introduced (version)

0.5
