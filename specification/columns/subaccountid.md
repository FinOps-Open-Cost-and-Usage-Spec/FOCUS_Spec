# Sub Account ID

A Sub Account ID is a provider-assigned identifier assigned to a [*sub account*](#glossary:sub-account). Sub Account ID is commonly used for scenarios like grouping based on organizational constructs, access management needs, and cost allocation strategies.

The SubAccountId column adheres to the following requirements:

* SubAccountId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports a *sub account* construct.
* SubAccountId MUST be of type String.
* SubAccountId MUST conform to [StringHandling](#stringhandling) requirements.
* SubAccountId nullability is defined as follows:
  * SubAccountId MUST be null when a charge is not related to a *sub account*.
  * SubAccountId MUST NOT be null when a charge is related to a *sub account*.

See [Appendix: Grouping constructs for resources or services](#groupingconstructsforresourcesorservices) for details and examples of the different grouping constructs supported by FOCUS.

## Column ID

SubAccountId

## Display Name

Sub Account ID

## Description

An ID assigned to a grouping of [*resources*](#glossary:resource) or [*services*](#glossary:service), often used to manage access and/or cost.

## Content constraints

|    Constraint   |      Value      |
|:----------------|:----------------|
| Column type     | Dimension       |
| Feature level   | Conditional     |
| Allows nulls    | True            |
| Data type       | String          |
| Value format    | \<not specified> |

## Introduced (version)

0.5
