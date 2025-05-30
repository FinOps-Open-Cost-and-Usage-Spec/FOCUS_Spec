# Capacity Reservation Status

Capacity Reservation Status indicates whether the [*charge*](#glossary:charge) represents either the consumption of the [*capacity reservation*](#glossary:capacity-reservation) identified in the CapacityReservationId column or when the *capacity reservation* is unused.

The CapacityReservationStatus column adheres to the following requirements:

* CapacityReservationStatus MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *capacity reservations*.
* CapacityReservationStatus MUST be of type String.
* CapacityReservationStatus nullability is defined as follows:
  * CapacityReservationStatus MUST be null when CapacityReservationId is null.
  * CapacityReservationStatus MUST NOT be null when CapacityReservationId is not null and [ChargeCategory](#chargecategory) is "Usage".
* When CapacityReservationStatus is not null, CapacityReservationStatus adheres to the following additional requirements:
  * CapacityReservationStatus MUST be one of the allowed values.
  * CapacityReservationStatus MUST be "Unused" when the *charge* represents the unused portion of a *capacity reservation*.
  * CapacityReservationStatus MUST be "Used" when the *charge* represents the used portion of a *capacity reservation*.

## Column ID

CapacityReservationStatus

## Display Name

Capacity Reservation Status

## Description

Indicates whether the *charge* represents either the consumption of a *capacity reservation* or when a *capacity reservation* is unused.

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
| Used   | *Charges* that utilized a specific amount of a *capacity reservation*.      |
| Unused | *Charges* that represent the unused portion of a *capacity reservation*.    |

## Introduced (version)

1.1
