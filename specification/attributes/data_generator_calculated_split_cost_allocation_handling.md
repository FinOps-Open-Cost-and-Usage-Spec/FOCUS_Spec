# Data Generator-Calculated Split Cost Allocation Handling

The data generator-calculated split cost allocation for data generator-defined services is a capability that can be offered by data generators which allocates (or in some cases provides more granular detail about) a charge to a more granular level. This is accomplished by taking a charge record present in a FOCUS dataset ([*origin charge*](#glossary:origin-charge)) and splitting it into multiple charge records ([*allocated charges](#glossary:allocated-charge)) to reflect the more granular detail, while ensuring the origin charge can be derived from the combination of *allocated charges*. This feature is used by practitioners to conduct chargebacks and better understand the usage of resources.

## Attribute ID

DataGeneratorCalculatedSplitCostAllocationHandling

## Attribute Name

Data Generator-Calculated Split Cost Allocation Handling

## Description

An attribute that allows data generators to offer more detailed cost and usage information based on a method defined and documented by the data generator, including support for allocating costs in cases where the usage of a resource might not match the units the resource is measured in.

## Requirements

DataGeneratorCalculatedSplitCostAllocationHandling MUST adhere to the following requirements:

* CostAndUsage FOCUS dataset MUST include [AllocatedMethodId](#datasets.costandusage.allocatedmethodid), [AllocatedResourceId](#datasets.costandusage.allocatedresourceid), [AllocatedResourceName](#datasets.costandusage.allocatedresourcename), and [AllocatedResourceTags](#datasets.costandusage.allocatedtags) when the data generator supports data generator-calculated split cost allocation.
* CostAndUsage FOCUS dataset SHOULD include [AllocatedMethodDetails](#datasets.costandusage.allocatedmethoddetails) when the data generator supports data generator-calculated split cost allocation.
* When the data generator supports data generator-calculated split cost allocation, CostAndUsage FOCUS dataset MUST adhere to the following requirements:
  * CostAndUsage FOCUS dataset MUST have its split cost allocation method documented and accessible to practitioners.
  * CostAndUsage FOCUS dataset SHOULD offer split cost allocation on an opt-in basis.
  * CostAndUsage FOCUS dataset MAY contain records for concepts not related to resource usage, if it aligns with the documented split cost allocation method.
  * CostAndUsage FOCUS dataset MAY contain records for unused or unallocated usage from the *origin charge* as separate *allocated charges*, if it aligns with the documented split cost allocation method.
  * CostAndUsage FOCUS dataset MAY contain *allocated charges* with apportioned costs for unused or unallocated usage, if it aligns with the documented split cost allocation method.
  * CostAndUsage FOCUS dataset MUST conform to normative requirements for all columns in *allocated charges*.
* When the data generator supports data generator-calculated split cost allocation, FOCUS column MUST adhere to the following requirements:
  * FOCUS column containing summable [*metric*](#glossary:metric) values (e.g., costs and quantities) in *allocated charges* MUST sum up to the corresponding value in the *origin charge*.
  * FOCUS column containing non-summable *metric* values (e.g., unit prices) in *allocated charges* MUST match the corresponding value in the *origin charge*.
  * FOCUS column containing dimension values in *allocated charges* MUST match the corresponding value in the *origin charge*.
  * FOCUS column containing tag values in *allocated charges* MUST include the same keys and values present in the [CostAndUsage.Tags](#datasets.costandusage.tags) column in the *origin charge*.

## Introduced (version)

1.3
