# Sub Account Name

A sub account name is a display name assigned to a *sub account*. Sub account Name is commonly used for scenarios like grouping based on organizational constructs, access management needs, and cost allocation strategies.

The SubAccountName column MUST be present in the billing data. This column MUST be of type String. If a provider supports setting a display name for *sub accounts*, that value MUST appear in this column. If a provider does not support a *sub account* construct (only has a [*billing account*](#glossary:billing-account)) or does support a *sub account* construct, but the charge does not apply to a *sub account*, the SubAccountName column MUST be null.

See [Appendix: Grouping constructs for resources or services](#groupingconstructsforresourcesorservices) for details and examples of the different grouping constructs supported by FOCUS.

## Column ID

SubAccountName

## Display name

Sub Account Name

## Description

A name assigned to a grouping of *resources* or *services*, often used to manage access and/or cost.

## Content constraints

| Constraint      | Value           |
|:----------------|:----------------|
| Column type     | Dimension       |
| Column required | True            |
| Allows nulls    | True            |
| Data type       | String          |
| Value format    | \<not specified> |

## Introduced (version)

0.5
