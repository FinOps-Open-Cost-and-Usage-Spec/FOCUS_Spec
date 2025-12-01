# RegionId

## Normative Text v1.2
The RegionId column adheres to the following requirements:

* RegionId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports deploying resources or services within a region.
* RegionId MUST be of type String.
* RegionId MUST conform to [StringHandling](#stringhandling) requirements.
* RegionId nullability is defined as follows:
  * RegionId MUST NOT be null when a *resource* or *service* is operated in or managed from a distinct region.
  * RegionId MAY be null when a *resource* or *service* is not operated in or managed from a distinct region.

## Normative Text v1.3-cr
## Requirements

RegionId adheres to the following requirements:

* RegionId MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the host provider supports deploying resources or services within a region.
* RegionId MUST be of type String.
* RegionId MUST conform to [StringHandling](#stringhandling) requirements.
* RegionId nullability is defined as follows:
  * RegionId MUST NOT be null when a *resource* or *service* is operated in or managed from a distinct region.
  * RegionId MAY be null when a *resource* or *service* is not operated in or managed from a distinct region.

## Diff
-The RegionId column adheres to the following requirements:
+## Requirements
 
-* RegionId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports deploying resources or services within a region.
+RegionId adheres to the following requirements:
+
+* RegionId MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the host provider supports deploying resources or services within a region.
 * RegionId MUST be of type String.
 * RegionId MUST conform to [StringHandling](#stringhandling) requirements.
 * RegionId nullability is defined as follows: