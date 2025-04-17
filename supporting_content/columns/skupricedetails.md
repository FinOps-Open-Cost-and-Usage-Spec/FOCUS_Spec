# Column: SkuPriceDetails

## Example provider mappings

### AWS
| InstanceType    | Family            | Generation | Additional Scope | SizeClass  | InstanceSeries          |
|---------------  |-------------------|------------|------------------|---------   |-------------------------|
| r4.xlarge       | Memory Optimized  | 4          |                  | xlarge     | r4                      |
| r5.xlarge       | Memory Optimized  | 5          |                  | xlarge     | r5                      |
| r5.2xlarge      | Memory Optimized  | 5          |                  | 2xlarge    | r5                      |
| r6g.8xlarge     | Memory Optimized  | 6          | local disk       | 8xlarge    | r6g                     |
| r6gd.8xlarge    | Memory Optimized  | 6          | local disk       | 8xlarge    | r6gd                    |
| c6g.8xlarge     | Compute Optimized | 6          |                  | 8xlarge    | c6g                     |

- Per [AWS EC2 User Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) InstanceSeries would refer to the entire Instance Family, including all of the Series, Generation, and Options components.

### GCP
| sku.id         | sku.name                                        | InstanceSeries   | CoreCount   | MemorySize   |
| -------------- |-------------------------------------------------| ---------------- | ----------- | ------------ |
| 2E27-4F75-95CD | N1 Predefined Instance Core running in Americas | N1               | 1           |              |
| 07C7-3B6C-C92A | N2D AMD Custom Instance Ram running in Zurich   | N2D              |             | 1            |

- InstanceSeries refers to the "machine series" as defined in [Compute Engine Terminology](https://cloud.google.com/compute/docs/machine-resource#vm_terminology).
- GCP would not include InstanceType nor SizeClass because these are properties of a resource since their SKUs aren't specific to an instance size/shape.
- The CoreCount and MemorySize are both equal to 1 becuase the pricing unit is 1 core / hour and the RAM is 1 GB (2<sup>10</sup> which is referred to as GiB outside of the context of memory).

### Azure
| InstanceType   | InstanceSeries   | CoreCount   | MemorySize   | GpuCount   | OperatingSystem   |
| -------------- | ---------------- | ----------- | ------------ | ---------- | ----------------- |
| E16_v4         | Ev4              | 16          | 128          |            | Windows           |
| NC12s_v3       | NCsv3            | 12          | 224          | 2          | Linux             |


| InstanceType   | DiskSpace     | Redundancy   | DiskType   | StorageClass   |
| -------------- | ------------- | ------------ | ---------- | -------------- |
| P50            | 4096          | Zonal        | SSD        | Premium SSD    |

- Azure refers to multiple groupings of Virtual Machine SKUs as series. [This page](https://azure.microsoft.com/en-us/pricing/details/virtual-machines/series/#d-series) refers to "D-series," "Dplds VM series," and "Dpdsv5 VM series" whereas [this page](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/general-purpose/d-family) calls these the D-family.
  - To remove ambiguity, the InstanceSeries Focus-defined property value will refer to the subset of [Azure Virtual Machine naming convention](https://learn.microsoft.com/en-us/azure/virtual-machines/vm-naming-conventions) excluding the "# of vCPUs" and "*Constrained vCPUs" components, as shown in the [Virtual Machine name breakdowns structure](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/overview#name-structure-breakdown)
  - Referencing the above examples, this approach aligns to how Azure lists the series which are part of the D-family, would match the "Dpdsv5 VM series" example, and generally aligns the information in the Instance Series dropdown of the [Azure Pricing Calculator](https://azure.microsoft.com/en-us/pricing/calculator/) when Virtual Machines are selected (without the appended "-series" and without using whitespace characters).

## Example Usecases

- Capacity Planning: 
  - Quantify how many cores of a VM Series you have provisioned in a region on average.
    - Uses: SkuPriceDetails {CoreCount, Series}, PricingQuantity, ChargePeriodStart, ChargePeriodEnd, RegionName
  - Determine how much disk storage you have provisioned.
- Unit Economics
  - Calculate the average cost per core of a VM Series.

## Clarifications

- The intent of the clause `Property value MUST represent the value for a single PricingUnit when the property holds a numeric value.` is to handle for a situation where the pricing unit is not equal to a single unit and varies across similar SKUs.
  - If all of my VM SKUs have a pricing unit of 1 hour, then a practitioner doesn't need to factor in the pricing unit (beyond the denominator of hour vs day) to determine how many cores are running using the Core Count property. It's as simple as Core Count * Pricing Quantity.
  - However, if a SKU has a pricing unit of 100 hours, today a practitioner needs to take the number of cores on the VM and then parse the pricing unit to determine how many VMs 1 pricing quantity represents.
    - In the case of a SKU for a virtual machine which has 2 cores and a pricing unit of 100 hours, the desire is to have a Core Count value of 200 communicating that a pricing quantity of 1 represents 100 VMs running for 1 hour. This once again makes the math as simple as Core Count * Pricing Quantity.
- The clause `SkuPriceDetails MUST be associated with a given SkuPriceId.` was previously written `SkuPriceDetails properties (both keys and values) MUST be shared across all charges having the same SkuPriceId, subject to the below provisions.` with the below provisions stating that properties could be added over time but not modified or removed.
  - The intent of this clause is still the same: All occurances of a SkuPriceId should have the same SkuPriceDetails, but we recognize that adoption of this column by providers can and should result in additional properties being added over time. There were concerns with the original phrasing as being internally contradictory, so when the normative requirements were refined, this needed to be rephrased.
- In the case of "burstable" SKUs, the value chosen for a numeric property should be the baseline value for that SKU. 


## Reference

- https://cloud.google.com/skus

## Discussion / Scratch space
