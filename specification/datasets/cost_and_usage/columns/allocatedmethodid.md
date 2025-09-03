# Allocated Method ID

Allocated Method ID is the identifier for the method defined by the provider which was used for the provider-calculated split cost allocation.

The AllocatedMethodId column adheres to the following requirements:

* AllocatedMethodId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports provider-calculated split cost allocation.
* AllocatedMethodId MUST be of type String.
* AllocatedMethodId MUST conform to [StringHandling](#stringhandling) requirements.
* AllocatedMethodId nullability is defined as follows:
  * AllocatedResourceId MUST be null when a *charge* is not related to a provider-calculated split cost allocation.
  * AllocatedResourceId MUST be null when a *charge* represents the unallocated portion of the origin *charge* after split cost allocation.
  * AllocatedResourceId MUST NOT be null when a *charge* represents the allocated portion of the origin *charge*.
* AllocatedMethodId MUST uniquely identify the method used to calculate the split cost allocation in the provider's documentation.

## Column ID

AllocatedMethodId

## Display Name

Allocated Method ID

## Description

Allocated Method ID is the identifier for the method defined by the provider which was used for the provider-calculated split cost allocation.

## Content constraints

|    Constraint   |      Value       |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Feature level   | Conditional      |
| Allows nulls    | True             |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

1.3
