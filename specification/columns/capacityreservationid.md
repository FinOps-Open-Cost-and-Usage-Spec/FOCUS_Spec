# Capacity Reservation ID

A Capacity Reservation ID is the identifier assigned to a [*capacity reservation*](#glossary:capacity-reservation) by the provider. Capacity Reservation ID is commonly used for scenarios to allocate charges for capacity reservation usage.

The CapacityReservationId column adheres to the following requirements:

* CapacityReservationId column MUST be present in the billing data when the provider supports *capacity reservations* and MUST be of type String.
* CapacityReservationId MUST NOT contain null values when the [CapacityReservationStatus](#capacityreservationstatus) is `Unused` and SHOULD NOT contain null values when a charge is related to a capacity reservation.
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
