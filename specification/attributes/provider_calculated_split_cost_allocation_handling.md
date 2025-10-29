# Provider-Calculated Split Cost Allocation Handling

The provider-calculated split cost allocation for provider-defined services is a capability that can be offered by providers which allocates (or in some cases provides more granular detail about) a charge to a more granular level. This is accomplished by taking a charge record present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) (origin charge) and splitting it into multiple charge records (allocated charges) to reflect the more granular detail, while ensuring the origin charge can be derived from the combination of allocated charges. This feature is used by practitioners to conduct chargebacks and better understand the usage of resources.

## Attribute ID

ProviderCalculatedSplitCostAllocationHandling

## Attribute Name

Provider-Calculated Split Cost Allocation Handling

## Description

An attribute that allows providers to offer more detailed cost and usage information based on a method defined and documented by the provider, including support for allocating costs in cases where the usage of a resource might not match the units the resource is measured in.

## Requirements

* A *FOCUS dataset* MUST include the following columns when the provider supports provider-calculated split cost allocation:
  * [AllocatedMethodId](#allocatedmethodid)
  * [AllocatedResourceId](#allocatedresourceid)
  * [AllocatedResourceName](#allocatedresourcename)
  * [AllocatedResourceTags](#allocatedresourcetags)
* A *FOCUS dataset* SHOULD include the following column when the provider supports provider-calculated split cost allocation:
  * [AllocatedMethodDetails](#allocatedmethoddetails)
* Allocated charge records in a *FOCUS dataset* MUST sum up to the origin charge record for all aggregatable metric columns.
* For each allocated charge record in a *FOCUS dataset*, all dimension columns and non-aggregatable metric columns MUST match the values of the origin charge record.
* Allocated charge records MUST include the same keys and values present in the [Tags](#tags) column for the origin charge.
* Allocated charge records MUST satisfy normative requirements for all columns.
* The method used for allocating origin charges to create allocated charges MUST be documented by the provider and accessible to practitioners.
* A FOCUS dataset MAY contain records for concepts not related to resource usage, if documented in the split cost allocation method.
* A FOCUS dataset MAY contain records for the unused or unallocated usage from the origin charge as separate allocated charges, if it aligns to the provider's documented allocation method.
* Allocated charge records MAY contain apportioned costs for the unused or unallocated usage from the origin charge, if it aligns to the provider's documented allocation method.
* Split-cost allocation is RECOMMENDED to be applied to charges on an opt-in basis.

## Exceptions

None

## Introduced (version)

1.3
