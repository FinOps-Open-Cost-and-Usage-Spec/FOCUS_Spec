# Allocated Resource Name

The Allocated Resource Name is a display name which cost is being allocated to in a [Provider-Calculated Split Cost Allocation](#providercalculatedsplitcosthandling). The Allocated Resource Name is used to understand what the cost is being allocated to in [*charges*](#glossary:charge) where the provider is allocating costs to something other than the charge's [ResourceID](#ResourceId), as is the case for [allocated charges](#glossary:allocated-charge).

The AllocatedResourceName column adheres to the following requirements:

* AllocatedResourceName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports provider-calculated split cost allocation.
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

The display name of the object to which cost is allocated in provider-calculated split cost allocation.

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
