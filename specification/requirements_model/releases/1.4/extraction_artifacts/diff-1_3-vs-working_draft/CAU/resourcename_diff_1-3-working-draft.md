## Diff

ResourceName [-adheres-]{+MUST adhere+} to the following requirements:

[-* ResourceName MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports billing based on provisioned resources.-]
* ResourceName MUST be of type String.
* ResourceName MUST conform to [-[StringHandling](#stringhandling)-]{+[StringHandling](#attributes.stringhandling)+} requirements.
* ResourceName {+MUST adhere to the following+} nullability [-is defined as follows:-]{+requirements:+}
  * ResourceName MUST be null when [-[ResourceId](#resourceid)-]{+[ResourceId](#datasets.costandusage.resourceid)+} is null or when the *resource* does not have an assigned display name.
  * ResourceName MUST NOT be null when ResourceId is not null and the *resource* has an assigned display name.
* ResourceName MUST NOT duplicate ResourceId when the *resource* is not provisioned interactively or only has a system-generated ResourceId.

