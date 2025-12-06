## ResourceName

### Normative Text v1.2

The ResourceName column adheres to the following requirements:

* ResourceName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports billing based on provisioned resources.
* ResourceName MUST be of type String.
* ResourceName MUST conform to [StringHandling](#stringhandling) requirements.
* ResourceName nullability is defined as follows:
  * ResourceName MUST be null when [ResourceId](#resourceid) is null or when the *resource* does not have an assigned display name.
  * ResourceName MUST NOT be null when ResourceId is not null and the *resource* has an assigned display name.
* ResourceName MUST NOT duplicate ResourceId when the *resource* is not provisioned interactively or only has a system-generated ResourceId.

### Normative Text v1.3


ResourceName adheres to the following requirements:

* ResourceName MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports billing based on provisioned resources.
* ResourceName MUST be of type String.
* ResourceName MUST conform to [StringHandling](#stringhandling) requirements.
* ResourceName nullability is defined as follows:
  * ResourceName MUST be null when [ResourceId](#resourceid) is null or when the *resource* does not have an assigned display name.
  * ResourceName MUST NOT be null when ResourceId is not null and the *resource* has an assigned display name.
* ResourceName MUST NOT duplicate ResourceId when the *resource* is not provisioned interactively or only has a system-generated ResourceId.

### Diff

-The ResourceName column adheres to the following requirements:
+## Requirements
 
-* ResourceName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports billing based on provisioned resources.
+ResourceName adheres to the following requirements:
+
+* ResourceName MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports billing based on provisioned resources.
 * ResourceName MUST be of type String.
 * ResourceName MUST conform to [StringHandling](#stringhandling) requirements.
 * ResourceName nullability is defined as follows: