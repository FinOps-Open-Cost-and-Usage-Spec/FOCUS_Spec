# Sub Account Name

A sub account is an optional provider-supported construct for organizing resources and/or services connected to a [*billing account*](#glossary:billing-account). Sub accounts are commonly used for scenarios like grouping based on organizational constructs, access management needs, and cost allocation strategies. Sub accounts must be associated with a *billing account* as they do not receive invoices.

A sub account name is a display name assigned to a sub account.

The SubAccountName column MUST be present in the billing data. This column MUST be of type String. If a [*provider*](#glossary:provider) supports setting a display name for sub accounts, that value MUST appear in this column. If a *provider* does not support a sub account construct (only has a *billing account*) or does support a sub account construct, but the [*charge*](#glossary:charge) does not apply to a sub account, the SubAccountName column MUST be null.

See [Appendix: Grouping constructs for resources and/or services](#groupingconstructsforresourcesand/orservices) for details and examples of the different grouping constructs supported by FOCUS.

## Column ID

SubAccountName

## Display name

Sub Account Name

## Description

A name assigned to a grouping of resources and/or services, often used to manage access and/or cost.

## Content constraints

| Constraint      | Value           |
|-----------------|-----------------|
| Column required | True            |
| Data type       | String          |
| Allows nulls    | True          |
| Value format    | \<not specified> |

## Introduced (version)

0.5
