## Diff

ResourceType [-adheres-]{+MUST adhere+} to the following requirements:

[-* ResourceType MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports billing based on provisioned *resources* and supports assigning types to *resources*.-]
* ResourceType MUST be of type String.
* ResourceType MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* ResourceType {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * ResourceType MUST be null when [-[ResourceId](#resourceid)-]{+[ResourceId](#datasets.costandusage.resourceid)+} is null.
  * ResourceType MUST NOT be null when ResourceId is not null.

