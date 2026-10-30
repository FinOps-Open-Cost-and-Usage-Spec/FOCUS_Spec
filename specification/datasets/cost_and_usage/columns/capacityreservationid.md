# Capacity Reservation ID

A [Capacity Reservation ID](#col) is the identifier assigned to a [capacity reservation](#term) by the service provider. [Capacity Reservation ID](#col) is commonly used for scenarios to allocate [charges](#term) for capacity reservation usage.

## Requirements

[CapacityReservationId](#col) MUST adhere to the following requirements:

* [CapacityReservationId](#col) MUST be of type String.
* [CapacityReservationId](#col) MUST conform to [StringHandling](#attr) requirements.
* [CapacityReservationId](#col) MUST adhere to the following nullability requirements:
  * [CapacityReservationId](#col) MUST be null when a [charge](#term) is not related to a [capacity reservation](#term).
  * [CapacityReservationId](#col) MUST NOT be null when a [charge](#term) represents the unused portion of a [capacity reservation](#term).
  * [CapacityReservationId](#col) SHOULD NOT be null when a [charge](#term) is related to a capacity reservation.
* When [CapacityReservationId](#col) is not null, [CapacityReservationId](#col) MUST adhere to the following requirements:
  * [CapacityReservationId](#col) MUST be a unique identifier within the service provider.
  * [CapacityReservationId](#col) SHOULD be a fully-qualified identifier.

## Column ID

CapacityReservationId

## Display Name

Capacity Reservation ID

## Description

The identifier assigned to a [capacity reservation](#term) by the service provider.

## Content Constraints

| Constraint                 | Value                                     |
| :------------------------- | :---------------------------------------- |
| Dataset                    | [Cost and Usage](#ds)                     |
| Operating model conditions | [Includes Capacity Reservations](#omc)                                                   |
| Column type                | Dimension                                 |
| Feature level              | Conditional                               |
| Allows nulls               | True                                      |
| Data type                  | String                                    |
| Value format               | \<not specified>                          |

## Version Introduced

1.1
