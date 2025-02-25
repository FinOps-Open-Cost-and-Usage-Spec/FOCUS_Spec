# Resource Type

Resource Type describes the kind of [*resource*](#glossary:resource) the charge applies to. A Resource Type is commonly used for scenarios like identifying cost changes in groups of similar *resources* and may include values like Virtual Machine, Data Warehouse, and Load Balancer.

The ResourceType column adheres to the following requirements:

* ResourceType MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports billing based on provisioned resources and supports assigning types to resources.
* ResourceType MUST be of type String.
* ResourceType MUST conform to [String Handling](#stringhandling) requirements.
* ResourceType nullability is defined as follows:
  * ResourceType MUST be null when [ResourceId](#resourceid) is null.
  * ResourceType MUST NOT be null when ResourceId is not null.

## Column ID

ResourceType

## Display Name

Resource Type

## Description

The kind of *resource* the charge applies to.

## Content Constraints

|    Constraint   |      Value      |
|:----------------|:----------------|
| Column type     | Dimension       |
| Feature level   | Conditional     |
| Allows nulls    | True            |
| Data type       | String          |
| Value format    | \<not specified> |

## Introduced (version)

1.0-preview
