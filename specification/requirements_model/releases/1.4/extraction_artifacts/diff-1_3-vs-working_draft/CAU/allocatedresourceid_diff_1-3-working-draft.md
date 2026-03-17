## Diff

AllocatedResourceId [-adheres-]{+MUST adhere+} to the following requirements:

[-* AllocatedResourceId MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports data generator-calculated split cost allocation.-]
* AllocatedResourceId MUST be of type String.
* AllocatedResourceId MUST conform to StringHandling requirements.
* AllocatedResourceId {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * AllocatedResourceId MUST be null when a *charge* is not related to a data generator-calculated split cost allocation.
  * AllocatedResourceId MUST be null when a *charge* represents the unallocated portion of the origin *charge* after split cost allocation.
  * AllocatedResourceId MUST NOT be null when a *charge* represents the allocated portion of the origin *charge*.
* When AllocatedResourceId is not null, AllocatedResourceId [-adheres-]{+MUST adhere+} to the following[-additional-] requirements:
  * AllocatedResourceId SHOULD be a locally unique identifier within the associated ResourceId and ChargePeriod.
  * AllocatedResourceId MAY NOT be unique across ResourceId or ChargePeriod values.

