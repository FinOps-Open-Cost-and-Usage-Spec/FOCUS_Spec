# CapacityReservationId

## Normative Text v1.2

The CapacityReservationId column adheres to the following requirements:

* CapacityReservationId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *capacity reservations*.
* CapacityReservationId MUST be of type String.
* CapacityReservationId MUST conform to [StringHandling](#stringhandling) requirements.
* CapacityReservationId nullability is defined as follows:
  * CapacityReservationId MUST be null when a *charge* is not related to a *capacity reservation*.
  * CapacityReservationId MUST NOT be null when a *charge* represents the unused portion of a *capacity reservation*.
  * CapacityReservationId SHOULD NOT be null when a *charge* is related to a capacity reservation.
* When CapacityReservationId is not null, CapacityReservationId adheres to the following additional requirements:
  * CapacityReservationId MUST be a unique identifier within the provider.
  * CapacityReservationId SHOULD be a fully-qualified identifier.

## Normative Text v1.3

## Requirements

CapacityReservationId adheres to the following requirements:

* CapacityReservationId MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *capacity reservations*.
* CapacityReservationId MUST be of type String.
* CapacityReservationId MUST conform to [StringHandling](#stringhandling) requirements.
* CapacityReservationId nullability is defined as follows:
  * CapacityReservationId MUST be null when a *charge* is not related to a *capacity reservation*.
  * CapacityReservationId MUST NOT be null when a *charge* represents the unused portion of a *capacity reservation*.
  * CapacityReservationId SHOULD NOT be null when a *charge* is related to a capacity reservation.
* When CapacityReservationId is not null, CapacityReservationId adheres to the following additional requirements:
  * CapacityReservationId MUST be a unique identifier within the service provider.
  * CapacityReservationId SHOULD be a fully-qualified identifier.

## Diff

-The CapacityReservationId column adheres to the following requirements:
+## Requirements
 
-* CapacityReservationId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *capacity reservations*.
+CapacityReservationId adheres to the following requirements:
+
+* CapacityReservationId MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *capacity reservations*.
 * CapacityReservationId MUST be of type String.
 * CapacityReservationId MUST conform to [StringHandling](#stringhandling) requirements.
 * CapacityReservationId nullability is defined as follows:
@@ -12,7 +14,7 @@ The CapacityReservationId column adheres to the following requirements:
   * CapacityReservationId MUST NOT be null when a *charge* represents the unused portion of a *capacity reservation*.
   * CapacityReservationId SHOULD NOT be null when a *charge* is related to a capacity reservation.
 * When CapacityReservationId is not null, CapacityReservationId adheres to the following additional requirements:
-  * CapacityReservationId MUST be a unique identifier within the provider.
+  * CapacityReservationId MUST be a unique identifier within the service provider.
   * CapacityReservationId SHOULD be a fully-qualified identifier.