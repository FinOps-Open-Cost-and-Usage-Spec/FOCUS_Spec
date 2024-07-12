# Capacity Reservation ID

A Capacity Reservation ID is the identifier assigned to a [*capacity reservation*](#glossary:capacity-reservation) by the provider. Capacity Reservation ID is commonly used for scenarios like chargeback for capacity reservation usage.

The CapacityReservationId column MUST be present in the billing data when the provider supports capacity reservations. This column MUST be of type String and MUST NOT contain null values when a charge is related to a capacity reservation. When a charge is not associated with a capacity reservation, the column MUST be null. CapacityReservationId MUST be unique within the provider.

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