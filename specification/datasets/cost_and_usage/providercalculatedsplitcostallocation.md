# Provider-Calculated Split Cost Allocation

The provider-calculated split cost allocation for provider-defined services is a capability that can be offered by providers which allocates (or in some cases provides more granular detail about) a charge to a more granular level. This is accomplished by taking a charge record present in a FOCUS dataset (origin charge) and splitting it into multiple charge records (allocated charges) to reflect the more granular detail, while ensuring the origin charge can be derived from the combination of allocated charges. This feature is used by practitioners to conduct chargebacks and better understand the usage of resources.

If a provider supports provider-calculated split cost allocation for provider-defined services, a FOCUS dataset MUST adhere to the following requirements:

- The following columns MUST be included in a FOCUS dataset when the provider supports provider-calculated split cost allocation:
  - [AllocatedResourceDetails](#allocatedresourcedetails)
  - [AllocatedResourceId](#allocatedresourceid)
- The combination of allocated charge records MUST match the origin charge record.
  - The sum of all allocated charges MUST have the same value as to origin charge for all metric columns.
    - Dimension columns which describe the unit for metric columns MUST have the same value as the origin charge for all allocated charges.
  - Allocated charges MUST include the tags from the origin charge in the [Tags](#tags) column.
    - If tags are supported for the AllocatedResourceId, these tags SHOULD be included in the Tags column as a user-defined tag scheme.
    - The provier MAY include properties of the AllocatedResourceId in the Tags column as a provider-defined tag scheme.
- The normative requirements for all columns MUST be satisfied for all allocated charges.
- The method used for allocating origin charges to create allocated charges MUST be documented by the provider and accessible to practitioners.
- The provider MAY create allocated charges for concepts related to their documented split cost allocation method.
  - Unused or unallocated usage of the ResourceId MAY be included as separate allocated charges OR MAY be apportioned to the remaining allocated charges, aligning to the provider's documented allocation method.
- Split-cost allocation SHOULD be offered on an opt-in basis.

## Description

Provider-calculated split cost allocation for provider-defined services allows providers to offer more detailed cost and usage information based on a method defined and documented by the provider, including support for allocating costs in cases where the usage of a resrouce might not match the units the resource is measured in.
