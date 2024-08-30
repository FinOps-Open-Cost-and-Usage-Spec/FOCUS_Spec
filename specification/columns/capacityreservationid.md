# Capacity Reservation ID

A Capacity Reservation ID is the identifier assigned to a [*capacity reservation*](#glossary:capacity-reservation) by the provider. Capacity Reservation ID is commonly used for scenarios to allocate charges for capacity reservation usage.

The CapacityReservationId column adheres to the following requirements:

* CapacityReservationID MUST be present in the billing data when the provider supports *capacity reservations* and MUST be of type String.
* CapacityReservationID SHOULD NOT be null when a charge is related to a capacity reservation.
* CapacityReservationID MUST NOT be null when a charge represents the unused portion of a *capacity reservation*.
* CapacityReservationID MUST be null when a charge is not related to a *capacity reservation*.
* CapacityReservationID SHOULD be a fully-qualified identifier that ensures global uniqueness within the provider.

## Column ID

CapacityReservationId

## Display Name

Capacity Reservation ID

## Description

The identifier assigned to a *capacity reservation* by the provider.

## Content constraints

|    Constraint   |      Value       |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Feature level   | Conditional      |
| Allows nulls    | True             |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

1.1
