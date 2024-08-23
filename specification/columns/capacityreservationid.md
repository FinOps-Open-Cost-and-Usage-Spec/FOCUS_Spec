# Capacity Reservation ID

A Capacity Reservation ID is the identifier assigned to a [*capacity reservation*](#glossary:capacity-reservation) by the provider. Capacity Reservation ID is commonly used for scenarios to allocate charges for capacity reservation usage.

The CapacityReservationId column SHOULD be present in the billing data when the provider supports capacity reservations. This column MUST be of type String and MUST NOT contain null values when a charge is related to a capacity reservation. When a charge is not associated with a capacity reservation, the column MUST be null. CapacityReservationID SHOULD be a fully-qualified identifier that ensures global uniqueness within the provider. The value MAY be negative in cases where ChargeClass is `Correction`.

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
