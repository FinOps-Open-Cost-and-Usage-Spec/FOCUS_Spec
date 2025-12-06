# Regionname

## Normative Text v1.2

The RegionName column adheres to the following requirements:

* RegionName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports deploying resources or services within a region.
* RegionName MUST be of type String.
* RegionName MUST conform to [StringHandling](#stringhandling) requirements.
* RegionName nullability is defined as follows:
  * RegionName MUST be null when [RegionId](#regionid) is null.
  * RegionName MUST NOT be null when RegionId is not null.

## Normative Text v1.3

## Requirements

RegionName adheres to the following requirements:

* RegionName MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the host provider supports deploying resources or services within a region.
* RegionName MUST be of type String.
* RegionName MUST conform to [StringHandling](#stringhandling) requirements.
* RegionName nullability is defined as follows:
  * RegionName MUST be null when [RegionId](#regionid) is null.
  * RegionName MUST NOT be null when RegionId is not null.


## Diff 

-The RegionName column adheres to the following requirements:
+## Requirements
 
-* RegionName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports deploying resources or services within a region.
+RegionName adheres to the following requirements:
+
+* RegionName MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the host provider supports deploying resources or services within a region.
 * RegionName MUST be of type String.
 * RegionName MUST conform to [StringHandling](#stringhandling) requirements.
 * RegionName nullability is defined as follows: