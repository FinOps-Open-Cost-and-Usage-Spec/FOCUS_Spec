# Allocated Service Name

The [Allocated Service Name](#col) is a display name for the [service](#term) to which cost is being allocated in a [Data Generator-Calculated Split Cost Allocation](#attr:DataGeneratorCalculatedSplitCostAllocationHandling). The [Allocated Service Name](#col) identifies the consuming [service](#term) on [allocated charges](#term) and complements the origin [Service Name](#col), which is preserved on those rows per the [Data Generator-Calculated Split Cost Allocation Handling](#attr) requirements. When a data generator complies with those requirements, the origin [Service Name](#col) on an [allocated charge](#term) reflects the [origin charge](#term) [service](#term), not the consuming [service](#term). [Allocated Service Name](#col) provides an explicit, queryable field for the consuming [service](#term) identity without overwriting the origin [Service Name](#col).

## Requirements

[AllocatedServiceName](#col) MUST adhere to the following requirements:

* [AllocatedServiceName](#col) MUST be of type String.
* [AllocatedServiceName](#col) MUST conform to [StringHandling](#attr) requirements.
* [AllocatedServiceName](#col) MUST adhere to the following nullability requirements:
  * [AllocatedServiceName](#col) MUST be null when [AllocatedMethodId](#col) is null.
  * [AllocatedServiceName](#col) MUST NOT be null when [AllocatedMethodId](#col) is not null.
* [AllocatedServiceName](#col) SHOULD match the [ServiceName](#col) used by the data generator for the equivalent [service](#term).

## Column ID

AllocatedServiceName

## Display Name

Allocated Service Name

## Description

The display name of the [service](#term) to which cost is allocated in data generator-calculated split cost allocation.

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

1.5
