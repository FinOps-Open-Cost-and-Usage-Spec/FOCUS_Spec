# Allocated Resource Name

The Allocated Resource Name is a display name which cost is being allocated to in a [Data Generator-Calculated Split Cost Allocation](#datagenerator-calculatedsplitcostallocationhandling). The Allocated Resource Name is used to understand what the cost is being allocated to in [*charges*](#glossary:charge) where the service provider is allocating costs to something other than the charge's [ResourceID](#ResourceId), as is the case for [allocated charges](#glossary:allocated-charge).

## Requirements

AllocatedResourceName adheres to the following requirements:

* AllocatedResourceName MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports data generator-calculated split cost allocation.
* AllocatedResourceName MUST be of type String.
* AllocatedResourceName MUST conform to [StringHandling](#stringhandling) requirements.
* AllocatedResourceName nullability is defined as follows:
  * AllocatedResourceName MUST be null when [AllocatedResourceId](#AllocatedResourceId) is null.
  * AllocatedResourceName MUST NOT be null when AllocatedResourceId is not null.
* AllocatedResourceName MAY duplicate AllocatedResourceId when a separate display name is not applicable.

## Column ID

AllocatedResourceName

## Display Name

Allocated Resource Name

## Description

The display name of the object to which cost is allocated in data generator-calculated split cost allocation.

## Content Constraints

| Constraint      | Value           |
|:----------------|:----------------|
| Column type     | Dimension       |
| Feature level   | Conditional     |
| Allows nulls    | True            |
| Data type       | String          |
| Value format    | \<not specified> |

## Introduced (version)

1.3
