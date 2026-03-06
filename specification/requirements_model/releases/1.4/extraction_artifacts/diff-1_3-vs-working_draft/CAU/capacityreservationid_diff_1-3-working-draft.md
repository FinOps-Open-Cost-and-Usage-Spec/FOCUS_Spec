## Diff

CapacityReservationId [-adheres-]{+MUST adhere+} to the following requirements:

[-* CapacityReservationId MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *capacity reservations*.-]
* CapacityReservationId MUST be of type String.
* CapacityReservationId MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* CapacityReservationId {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * CapacityReservationId MUST be null when a *charge* is not related to a *capacity reservation*.
  * CapacityReservationId MUST NOT be null when a *charge* represents the unused portion of a *capacity reservation*.
  * CapacityReservationId SHOULD NOT be null when a *charge* is related to a capacity reservation.
* When CapacityReservationId is not null, CapacityReservationId [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * CapacityReservationId MUST be a unique identifier within the service provider.
  * CapacityReservationId SHOULD be a fully-qualified identifier.

