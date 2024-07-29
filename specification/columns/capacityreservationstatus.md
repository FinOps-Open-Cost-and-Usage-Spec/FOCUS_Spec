# Capacity Reservation Status

Capacity Reservation Status indicates whether the charge represents either the consumption of a [*capacity reservation*](#glossary:capacity-reservation) or when a *capacity reservation* is unused.

The CapacityReservationStatus column MUST be present in the billing data when the provider supports *capacity-reservations*. This column MUST be of type String, MUST be null when the charge is not related to a capacity reservation, and MUST NOT be null when the charge is related to a capacity reservation. The CapacityReservationStatus MUST be one of the allowed values. The CapacityReservationStatus MUST label all unused *capacity reservation* charges and SHOULD label used *capacity reservation* charges if the provider supports it.

## Column ID

CapacityReservationStatus

## Display Name

Capacity Reservation Status

## Description

Indicates whether the charge represents either the consumption of a *capacity reservation* or when a *capacity reservation* is unused.

## Content constraints

| Constraint      | Value          |
| :-------------- | :------------- |
| Column type     | Dimension      |
| Feature level   | Conditional    |
| Allows nulls    | True           |
| Data type       | String         |
| Value format    | Allowed Values |

Allowed values:

| Value  | Description                                                                 |
| :----- | :-------------------------------------------------------------------------- |
| Used   | Charges that utilized a specific amount of a capacity reservation.          |
| Unused | Charges that represent the unused portion of a capacity reservation.        |

## Introduced (version)

1.1