## Diff

CapacityReservationStatus [-adheres-]{+MUST adhere+} to the following requirements:

[-* CapacityReservationStatus MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *capacity reservations*.-]
* CapacityReservationStatus MUST be of type String.
* CapacityReservationStatus {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * CapacityReservationStatus MUST be null when CapacityReservationId is null.
  * CapacityReservationStatus MUST NOT be null when CapacityReservationId is not null and ChargeCategory is "Usage".
* When CapacityReservationStatus is not null, CapacityReservationStatus [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * CapacityReservationStatus MUST be one of the allowed values.
  * CapacityReservationStatus MUST be "Unused" when the *charge* represents the unused portion of a *capacity reservation*.
  * CapacityReservationStatus MUST be "Used" when the *charge* represents the used portion of a *capacity reservation*.
