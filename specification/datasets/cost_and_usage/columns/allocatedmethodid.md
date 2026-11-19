# Allocated Method ID

[Allocated Method ID](#col) is the unique identifier for the [allocated method](#term) defined by the service provider which was used for the [Data Generator-Calculated Split Cost Allocation](#attr:DataGeneratorCalculatedSplitCostAllocationHandling). This unique identifier can be used to find how the [allocated charge](#term) was calculated in the provider's documentation.

## Requirements

[AllocatedMethodId](#col) MUST adhere to the following requirements:

* [AllocatedMethodId](#col) MUST be of type String.
* [AllocatedMethodId](#col) MUST conform to [StringHandling](#attr) requirements.
* [AllocatedMethodId](#col) MUST adhere to the following nullability requirements:
  * [AllocatedMethodId](#col) MUST be null when a [charge](#term) is not related to a data generator-calculated split cost allocation.
  * [AllocatedMethodId](#col) MUST NOT be null when a [charge](#term) is related to a data generator-calculated split cost allocation.
* Data generator-calculated split cost allocation method documentation MUST reference a single [AllocatedMethodId](#col) value.

## Column ID

AllocatedMethodId

## Display Name

Allocated Method ID

## Description

A unique identifier defining the method of data generator-calculated split cost allocation.

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
