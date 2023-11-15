# Sub Account ID

A Sub Account ID is a provider assigned identifier assigned to a [*sub account*](#glossary:sub-account). Sub account ID is commonly used for scenarios like grouping based on organizational constructs, access management needs, and cost allocation strategies.

The SubAccountId column MUST be present in the billing data. This column MUST be of type String. If a provider supports a *sub account* construct, that value MUST appear in this column. If a provider does not support a *sub account* construct (only has a *billing account*](#glossary:billing-account)) or does support a *sub account* construct, but the charge does not apply to a *sub account*, the SubAccountId column MUST be null.

See [Appendix: Grouping constructs for resources or services](#groupingconstructsforresourcesorservices) for details and examples of the different grouping constructs supported by FOCUS.

## Column ID

SubAccountId

## Display name

Sub Account ID

## Description

An ID assigned to a grouping of *resources* or *services*, often used to manage access and/or cost.

## Content constraints

|    Constraint   |      Value      |
|:----------------|:----------------|
| Column type     | Dimension       |
| Column required | True            |
| Allows nulls    | True            |
| Data type       | String          |
| Value format    | \<not specified> |

## Introduced (version)

0.5
