# Availability Zone

An [Availability Zone](#term) is a host-provider-assigned identifier for a physically separated and isolated area within a Region that provides high availability and fault tolerance. Availability Zone is commonly used for scenarios like analyzing cross-zone data transfer usage and the corresponding cost based on where [resources](#term) are deployed.

## Requirements

[AvailabilityZone](#col) MUST adhere to the following requirements:

* [AvailabilityZone](#col) MUST be of type String.
* [AvailabilityZone](#col) MUST conform to [StringHandling](#attr) requirements.
* [AvailabilityZone](#col) MUST be null when a [charge](#term) is not specific to an [availability zone](#term).

## Column ID

AvailabilityZone

## Display Name

Availability Zone

## Description

A host-provider-assigned identifier for a physically separated and isolated area within a Region that provides high availability and fault tolerance.

## Content Constraints

| Constraint                 | Value                                     |
| :------------------------- | :---------------------------------------- |
| Dataset                    | [Cost and Usage](#ds)                     |
| Operating model conditions | [Includes Availability Zones](#omc)                                                |
| Column type                | Dimension                                 |
| Feature level              | Recommended                               |
| Allows nulls               | True                                      |
| Data type                  | String                                    |
| Value format               | \<not specified>                          |

## Version Introduced

0.5
