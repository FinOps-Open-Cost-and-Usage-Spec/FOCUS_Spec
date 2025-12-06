## ResourceType

### Normative Text v1.2

The ResourceType column adheres to the following requirements:

* ResourceType MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports billing based on provisioned *resources* and supports assigning types to *resources*.
* ResourceType MUST be of type String.
* ResourceType MUST conform to [StringHandling](#stringhandling) requirements.
* ResourceType nullability is defined as follows:
  * ResourceType MUST be null when [ResourceId](#resourceid) is null.
  * ResourceType MUST NOT be null when ResourceId is not null.

### Normative Text v1.3

## Requirements

ResourceType adheres to the following requirements:

* ResourceType MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports billing based on provisioned *resources* and supports assigning types to *resources*.
* ResourceType MUST be of type String.
* ResourceType MUST conform to [StringHandling](#stringhandling) requirements.
* ResourceType nullability is defined as follows:
  * ResourceType MUST be null when [ResourceId](#resourceid) is null.
  * ResourceType MUST NOT be null when ResourceId is not null.

### Diff

-The ResourceType column adheres to the following requirements:
+## Requirements
 
-* ResourceType MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports billing based on provisioned *resources* and supports assigning types to *resources*.
+ResourceType adheres to the following requirements:
+
+* ResourceType MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports billing based on provisioned *resources* and supports assigning types to *resources*.
 * ResourceType MUST be of type String.
 * ResourceType MUST conform to [StringHandling](#stringhandling) requirements.
 * ResourceType nullability is defined as follows:
