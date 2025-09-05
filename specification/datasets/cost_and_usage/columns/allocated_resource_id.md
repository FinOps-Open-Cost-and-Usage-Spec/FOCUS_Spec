# Allocated Resource ID

An Allocated Resource ID is an identifier assigned by the provider which cost is being allocated to in a provider-calculated split cost allocation. The Allocated Resource ID is used to understand what the cost is being allocated to in [*charges*](#glossary:charge) where the provider is allocating costs to something other than the *charge's* [ResourceID](#ResourceId).

The allocated_resource_id column adheres to the following requirements:

* allocated_resource_id MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports provider-calculated split cost allocation.
* allocated_resource_id MUST be of type String.
* allocated_resource_id MUST conform to [StringHandling](#stringhandling) requirements.
* allocated_resource_id nullability is defined as follows:
  * allocated_resource_id MUST be null when a *charge* is not related to a provider-calculated split cost allocation.
  * allocated_resource_id MUST be null when a *charge* represents the unallocated portion of the origin *charge* after split cost allocation.
  * allocated_resource_id MUST NOT be null when a *charge* represents the allocated portion of the origin *charge*.
* When allocated_resource_id is not null, allocated_resource_id adheres to the following additional requirements:
  * allocated_resource_id SHOULD be a locally unique identifier within the associated ResourceId and ChargePeriod.
  * allocated_resource_id MAY NOT be unique across ResourceId or ChargePeriod values.

## Column ID

allocated_resource_id

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
