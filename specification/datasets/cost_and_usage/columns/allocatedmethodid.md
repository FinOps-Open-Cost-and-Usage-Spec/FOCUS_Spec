# Allocated Method ID

Allocated Method ID is the identifier for the method defined by the provider which was used for the provider-calculated split cost allocation.

The AllocatedMethodId column adheres to the following requirements:

* AllocatedMethodId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports provider-calculated split cost allocation.
* AllocatedMethodId MUST be of type String.
* AllocatedMethodId MUST conform to [StringHandling](#stringhandling) requirements.
* AllocatedMethodId nullability is defined as follows:
  * AllocatedMethodId MUST be null when a charge does not qualify for provider-calculated split cost allocation.
  * AllocatedMethodId MUST NOT be null when a charge qualifies for provider-calculated split cost allocation.
* When a charge qualifies for for provider-calculated split cost allocation, AllocatedMethodId adheres to the following additional requirements:
  * AllocatedMethodId MUST uniquely identify the method used to calculate the split cost allocation in the provider's documentation when the charge is the result of provider-calculated split cost allocation.
  * AllocatedMethodId MUST be "Unallocated" when the charge qualifies for provider-calculated split cost allocation but no split cost allocation was applied.

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
