# Allocated Method ID

Allocated Method ID is the unique identifier for the [allocated method](#glossary:allocated-method) defined by the provider which was used for the [Provider-Calculated Split Cost Allocation](#providercalculatedsplitcosthandling). This unique identifier can be used to find how the [allocated charge](#glossary:allocated-charge) was calculated in the provider's documentation.

The AllocatedMethodId column adheres to the following requirements:

* AllocatedMethodId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports provider-calculated split cost allocation.
* AllocatedMethodId MUST be of type String.
* AllocatedMethodId MUST conform to [StringHandling](#stringhandling) requirements.
* AllocatedMethodId nullability is defined as follows:
  * AllocatedMethodId MUST be null when a [*charge*](#glossary:charge) is not related to a provider-calculated split cost allocation.
  * AllocatedMethodId MUST NOT be null when a *charge* is related to a provider-calculated split cost allocation.
* Provider documentation of a split cost allocation method MUST make reference to a single AllocatedMethodId value.

## Column ID

AllocatedMethodId

## Display Name

Allocated Method ID

## Description

A unique identifier defining the method of provider-calculated split cost allocation.

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
