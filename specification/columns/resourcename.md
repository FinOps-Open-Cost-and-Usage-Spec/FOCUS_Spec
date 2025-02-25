# Resource Name

The Resource Name is a display name assigned to a [*resource*](#glossary:resource). It is commonly used for cost analysis, reporting, and allocation scenarios.

The ResourceName column adheres to the following requirements:

* ResourceName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports billing based on provisioned resources.
* ResourceName MUST be of type String.
* ResourceName MUST conform to [String Handling](#stringhandling) requirements.
* ResourceName nullability is defined as follows:
  * ResourceName MUST be null when [ResourceId](#resourceid) is null or when the *resource* only has a system-generated ResourceId without an assigned display name.
  * ResourceName MUST NOT be null when ResourceId is not null and the *resource* has an assigned display name.
* ResourceName MUST NOT duplicate ResourceId when the *resources* is not provisioned interactively or only has a system-generated [ResourceId](#resourceid).

## Column ID

ResourceName

## Display Name

Resource Name

## Description

Display name assigned to a *resource*.

## Content Constraints

|    Constraint   |      Value      |
|:----------------|:----------------|
| Column type     | Dimension       |
| Feature level   | Conditional     |
| Allows nulls    | True            |
| Data type       | String          |
| Value format    | \<not specified> |

## Introduced (version)

0.5
