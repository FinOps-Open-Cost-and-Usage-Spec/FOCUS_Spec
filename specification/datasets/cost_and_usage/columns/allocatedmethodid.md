# Allocated Method ID

Allocated Method ID is the unique identifier for the [allocated method](#glossary:allocated-method) defined by the service provider which was used for the [Service-Provider-Calculated Split Cost Allocation](#serviceprovidercalculatedsplitcosthandling). This unique identifier can be used to find how the [allocated charge](#glossary:allocated-charge) was calculated in the provider's documentation.

The AllocatedMethodId column adheres to the following requirements:

* AllocatedMethodId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the servie provider supports service-provider-calculated split cost allocation.
* AllocatedMethodId MUST be of type String.
* AllocatedMethodId MUST conform to [StringHandling](#stringhandling) requirements.
* AllocatedMethodId nullability is defined as follows:
  * AllocatedMethodId MUST be null when a [*charge*](#glossary:charge) is not related to a service-provider-calculated split cost allocation.
  * AllocatedMethodId MUST NOT be null when a *charge* is related to a service-provider-calculated split cost allocation.
* Service provider documentation of a split cost allocation method MUST make reference to a single AllocatedMethodId value.

## Column ID

AllocatedMethodId

## Display Name

Allocated Method ID

## Description

A unique identifier defining the method of service-provider-calculated split cost allocation.

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
