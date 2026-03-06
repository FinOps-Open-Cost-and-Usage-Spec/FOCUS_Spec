## Diff

AllocatedResourceName [-adheres-]{+MUST adhere+} to the following requirements:

[-* AllocatedResourceName MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports data generator-calculated split cost allocation.-]
* AllocatedResourceName MUST be of type String.
* AllocatedResourceName MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* AllocatedResourceName {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * AllocatedResourceName MUST be null when [-[AllocatedResourceId](#AllocatedResourceId)-]{+[AllocatedResourceId](#datasets.costandusage.allocatedresourceid)+} is null.
  * AllocatedResourceName MUST NOT be null when AllocatedResourceId is not null.
* AllocatedResourceName MAY duplicate AllocatedResourceId when a separate display name is not applicable.

