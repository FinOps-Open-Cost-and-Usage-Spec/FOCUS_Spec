# Allocated Resource Name

The [Allocated Resource Name](#col) is a display name which cost is being allocated to in a [Data Generator-Calculated Split Cost Allocation](#attr:DataGeneratorCalculatedSplitCostAllocationHandling). The [Allocated Resource Name](#col) is used to understand what the cost is being allocated to in [charges](#term) where the service provider is allocating costs to something other than the charge's [Resource ID](#col), as is the case for [allocated charges](#term).

## Requirements

[AllocatedResourceName](#col) MUST adhere to the following requirements:

* [AllocatedResourceName](#col) MUST be of type String.
* [AllocatedResourceName](#col) MUST conform to [StringHandling](#attr) requirements.
* [AllocatedResourceName](#col) MUST adhere to the following nullability requirements:
  * [AllocatedResourceName](#col) MUST be null when [AllocatedResourceId](#col) is null.
  * [AllocatedResourceName](#col) MUST NOT be null when [AllocatedResourceId](#col) is not null.
* [AllocatedResourceName](#col) MAY duplicate [AllocatedResourceId](#col) when a separate display name is not applicable.

## Column ID

AllocatedResourceName

## Display Name

Allocated Resource Name

## Description

The display name of the object to which cost is allocated in data generator-calculated split cost allocation.

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
