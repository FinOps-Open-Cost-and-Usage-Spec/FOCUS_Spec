# Allocated Resource ID

An [Allocated Resource ID](#col) is an identifier assigned by the data generator which cost is being allocated to in a [Data Generator-Calculated Split Cost Allocation](#attr:DataGeneratorCalculatedSplitCostAllocationHandling). The [Allocated Resource ID](#col) is used to understand what the cost is being allocated to in [charges](#term) where the data generator is allocating costs to something other than the *charge's* [Resource ID](#col), as is the case for [allocated charges](#term).

## Requirements

[AllocatedResourceId](#col) MUST adhere to the following requirements:

* [AllocatedResourceId](#col) MUST be of type String.
* [AllocatedResourceId](#col) MUST conform to [StringHandling](#attr) requirements.
* [AllocatedResourceId](#col) MUST adhere to the following nullability requirements:
  * [AllocatedResourceId](#col) MUST be null when a [charge](#term) is not related to a data generator-calculated split cost allocation.
  * [AllocatedResourceId](#col) MUST be null when a [charge](#term) represents the unallocated portion of the origin [charge](#term) after split cost allocation.
  * [AllocatedResourceId](#col) MUST NOT be null when a [charge](#term) represents the allocated portion of the origin [charge](#term).
* When [AllocatedResourceId](#col) is not null, [AllocatedResourceId](#col) MUST adhere to the following requirements:
  * [AllocatedResourceId](#col) SHOULD be a locally unique identifier within the associated [ResourceId](#col) and ChargePeriod.
  * [AllocatedResourceId](#col) MAY NOT be unique across [ResourceId](#col) or ChargePeriod values.

## Column ID

AllocatedResourceId

## Display Name

Allocated Resource ID

## Description

The identifier of the object to which cost is allocated in data generator-calculated split cost allocation.

## Content Constraints

| Constraint                 | Value                                     |
| :------------------------- | :---------------------------------------- |
| Dataset                    | [Cost and Usage](#ds)                     |
| Operating model conditions | [Includes Split Cost Allocation](#omc)                                                  |
| Column type                | Dimension                                 |
| Feature level              | Conditional                               |
| Allows nulls               | True                                      |
| Data type                  | String                                    |
| Value format               | \<not specified>                          |

## Version Introduced

1.3
