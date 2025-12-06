## ResourceId

### Normative Text v1.2

The ResourceId column adheres to the following requirements:

* ResourceId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports billing based on provisioned *resources*.
* ResourceId MUST be of type String.
* ResourceId MUST conform to [StringHandling](#stringhandling) requirements.
* ResourceId nullability is defined as follows:
  * ResourceId MUST be null when a [*charge*](#glossary:charge) is not related to a *resource*.
  * ResourceId MUST NOT be null when a *charge* is related to a *resource*.
* When ResourceId is not null, ResourceId adheres to the following additional requirements:
  * ResourceId MUST be a unique identifier within the provider.
  * ResourceId SHOULD be a fully-qualified identifier.

### Normative Text v.13

ResourceId adheres to the following requirements:

* ResourceId MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports billing based on provisioned *resources*.
* ResourceId MUST be of type String.
* ResourceId MUST conform to [StringHandling](#stringhandling) requirements.
* ResourceId nullability is defined as follows:
  * ResourceId MUST be null when a [*charge*](#glossary:charge) is not related to a *resource*.
  * ResourceId MUST NOT be null when a *charge* is related to a *resource*.
* When ResourceId is not null, ResourceId adheres to the following additional requirements:
  * ResourceId MUST be a unique identifier within the s

### Diff

-A Resource ID is an identifier assigned to a [*resource*](#glossary:resource) by the provider. The Resource ID is commonly used for cost reporting, analysis, and allocation scenarios.
+A Resource ID is an identifier assigned to a [*resource*](#glossary:resource) by the service provider. The Resource ID is commonly used for cost reporting, analysis, and allocation scenarios.
 
-The ResourceId column adheres to the following requirements:
+## Requirements
 
-* ResourceId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports billing based on provisioned *resources*.
+ResourceId adheres to the following requirements:
+
+* ResourceId MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports billing based on provisioned *resources*.
 * ResourceId MUST be of type String.
 * ResourceId MUST conform to [StringHandling](#stringhandling) requirements.
 * ResourceId nullability is defined as follows:
   * ResourceId MUST be null when a [*charge*](#glossary:charge) is not related to a *resource*.
   * ResourceId MUST NOT be null when a *charge* is related to a *resource*.
 * When ResourceId is not null, ResourceId adheres to the following additional requirements:
-  * ResourceId MUST be a unique identifier within the provider.
+  * ResourceId MUST be a unique identifier within the service provider.
   * ResourceId SHOULD be a fully-qualified identifier.
