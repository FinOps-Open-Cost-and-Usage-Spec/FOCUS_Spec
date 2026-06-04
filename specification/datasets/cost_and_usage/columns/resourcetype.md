# Resource Type

Resource Type describes the kind of [*resource*](#glossary:resource) the [*charge*](#glossary:charge) applies to. A Resource Type is commonly used for scenarios like identifying cost changes in groups of similar *resources* and may include values like Virtual Machine, Data Warehouse, and Load Balancer.

## Requirements

ResourceType MUST adhere to the following requirements:

* ResourceType MUST be of type String.
* ResourceType MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* ResourceType MUST adhere to the following nullability requirements:
  * ResourceType MUST be null when [ResourceId](#datasets.costandusage.resourceid) is null.
  * ResourceType MUST NOT be null when ResourceId is not null.

## Column ID

ResourceType

## Display Name

Resource Type

## Description

The kind of *resource* the *charge* applies to.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [Cost and Usage](#datasets.costandusage)             |
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Version Introduced

1.0-preview
