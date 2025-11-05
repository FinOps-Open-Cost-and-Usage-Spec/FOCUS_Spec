# Allocated Resource ID

An Allocated Resource ID is an identifier assigned by the data generator which cost is being allocated to in a [Data Generator-Calculated Split Cost Allocation](#datagenerator-calculatedsplitcostallocationhandling). The Allocated Resource ID is used to understand what the cost is being allocated to in [*charges*](#glossary:charge) where the data generator is allocating costs to something other than the *charge's* [ResourceID](#ResourceId), as is the case for [allocated charges](#glossary:allocated-charge).

## Requirements

AllocatedResourceId adheres to the following requirements:

* AllocatedResourceId MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports data generator-calculated split cost allocation.
* AllocatedResourceId MUST be of type String.
* AllocatedResourceId MUST conform to [StringHandling](#stringhandling) requirements.
* AllocatedResourceId nullability is defined as follows:
  * AllocatedResourceId MUST be null when a *charge* is not related to a data generator-calculated split cost allocation.
  * AllocatedResourceId MUST be null when a *charge* represents the unallocated portion of the origin *charge* after split cost allocation.
  * AllocatedResourceId MUST NOT be null when a *charge* represents the allocated portion of the origin *charge*.
* When AllocatedResourceId is not null, AllocatedResourceId adheres to the following additional requirements:
  * AllocatedResourceId SHOULD be a locally unique identifier within the associated ResourceId and ChargePeriod.
  * AllocatedResourceId MAY NOT be unique across ResourceId or ChargePeriod values.

## Column ID

AllocatedResourceId

## Display Name

Allocated Resource ID

## Description

The identifier of the object to which cost is allocated in data generator-calculated split cost allocation.

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
