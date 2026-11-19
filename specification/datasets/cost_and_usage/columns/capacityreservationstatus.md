# Capacity Reservation Status

[Capacity Reservation Status](#col) indicates whether the [charge](#term) represents either the consumption of the [capacity reservation](#term) identified in the [Capacity Reservation ID](#col) column or when the [capacity reservation](#term) is unused.

## Requirements

[CapacityReservationStatus](#col) MUST adhere to the following requirements:

* [CapacityReservationStatus](#col) MUST be of type String.
* [CapacityReservationStatus](#col) MUST adhere to the following nullability requirements:
  * [CapacityReservationStatus](#col) MUST be null when [CapacityReservationId](#col) is null.
  * [CapacityReservationStatus](#col) MUST NOT be null when [CapacityReservationId](#col) is not null and [ChargeCategory](#col) is ["Usage"](#val:CostAndUsage.ChargeCategory).
* When [CapacityReservationStatus](#col) is not null, [CapacityReservationStatus](#col) MUST adhere to the following requirements:
  * [CapacityReservationStatus](#col) MUST be one of the allowed values.
  * [CapacityReservationStatus](#col) MUST be ["Unused"](#val:CapacityReservationStatus) when the [charge](#term) represents the unused portion of a [capacity reservation](#term).
  * [CapacityReservationStatus](#col) MUST be ["Used"](#val:CapacityReservationStatus) when the [charge](#term) represents the used portion of a [capacity reservation](#term).

## Allowed Values

| Value  | Description                                                                 |
| :----- | :-------------------------------------------------------------------------- |
| Used   | *Charges* that utilized a specific amount of a *capacity reservation*. |
| Unused | *Charges* that represent the unused portion of a *capacity reservation*. |

## Column ID

CapacityReservationStatus

## Display Name

Capacity Reservation Status

## Description

Indicates whether the [charge](#term) represents either the consumption of a [capacity reservation](#term) or when a [capacity reservation](#term) is unused.

## Content Constraints

| Constraint                 | Value                                     |
| :------------------------- | :---------------------------------------- |
| Dataset                    | [Cost and Usage](#ds)                     |
| Operating model conditions | [Includes Capacity Reservations](#omc)                                                   |
| Column type                | Dimension                                 |
| Feature level              | Conditional                               |
| Allows nulls               | True                                      |
| Data type                  | String                                    |
| Value format               | Allowed values                            |

## Version Introduced

1.1
