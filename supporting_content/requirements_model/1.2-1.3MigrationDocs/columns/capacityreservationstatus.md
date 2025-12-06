# CapacityReservationStatus

## Normative Text v1.2

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

## Normative Text v1.3

## Requirements

CapacityReservationStatus adheres to the following requirements:

* CapacityReservationStatus MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *capacity reservations*.
* CapacityReservationStatus MUST be of type String.
* CapacityReservationStatus nullability is defined as follows:
  * CapacityReservationStatus MUST be null when CapacityReservationId is null.
  * CapacityReservationStatus MUST NOT be null when CapacityReservationId is not null and [ChargeCategory](#chargecategory) is "Usage".
* When CapacityReservationStatus is not null, CapacityReservationStatus adheres to the following additional requirements:
  * CapacityReservationStatus MUST be one of the allowed values.
  * CapacityReservationStatus MUST be "Unused" when the *charge* represents the unused portion of a *capacity reservation*.
  * CapacityReservationStatus MUST be "Used" when the *charge* represents the used portion of a *capacity reservation*.

## Diff

-The CapacityReservationStatus column adheres to the following requirements:
+## Requirements
 
-* CapacityReservationStatus MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *capacity reservations*.
+CapacityReservationStatus adheres to the following requirements:
+
+* CapacityReservationStatus MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *capacity reservations*.
 * CapacityReservationStatus MUST be of type String.
 * CapacityReservationStatus nullability is defined as follows:
   * CapacityReservationStatus MUST be null when CapacityReservationId is null.
