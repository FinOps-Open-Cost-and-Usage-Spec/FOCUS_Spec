# Allocated Resource ID

An Allocated Resource ID is an identifier assigned by the provider which cost is being allocated to in a provider-calculated split cost allocation. The Allocated Resource ID is used to understand what the cost is being allocated to in [*charges*](#glossary:charge) where the provider is allocating costs to something other than the *charge's* [ResourceID](#ResourceId).

The AllocatedResourceId column adheres to the following requirements:

* AllocatedResourceId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports provider-calculated split cost allocation.
* AllocatedResourceId MUST be of type String.
* AllocatedResourceId MUST conform to [StringHandling](#stringhandling) requirements.
* AllocatedResourceId nullability is defined as follows:
  * AllocatedResourceId MUST be null when a charge is not related to a provider-calculated split cost allocation.
  * AllocatedResourceId MUST NOT be null when a charge is related to a provider-calculated split cost allocation.
* When AllocatedResourceId is not null, AllocatedResourceId adheres to the following additional requirements:
  * AllocatedResourceId SHOULD be a locally unique identifier within the associated ResourceId and ChargePeriod.
  * AllocatedResourceId MAY NOT be unique across ResourceId or time periods.

## Column ID

AllocatedResourceId

## Display Name

Allocated Resource ID

## Description

Identifier assigned by the provider which cost will be allocated to in a provider-calculated split cost allocation.

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
