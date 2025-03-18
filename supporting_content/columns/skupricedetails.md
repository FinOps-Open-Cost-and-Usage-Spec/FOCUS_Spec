# Column: SkuPriceDetails

## Example provider mappings

AWS
| F_InstanceType  | Family            | Generation | Additional Scope | F_SizeClass| F_Series                |
|---------------  |-------------------|------------|------------------|---------   |-------------------------|
| r4.xlarge       | Memory Optimized  | 4          |                  | xlarge     | r4                      |
| r5.xlarge       | Memory Optimized  | 5          |                  | xlarge     | r5                      |
| r5.2xlarge      | Memory Optimized  | 5          |                  | 2xlarge    | r5                      |
| r6g.8xlarge     | Memory Optimized  | 6          | local disk       | 8xlarge    | r6g                     |
| r6gd.8xlarge    | Memory Optimized  | 6          | local disk       | 8xlarge    | r6gd                    |
| c6g.8xlarge     | Compute Optimized | 6          |                  | 8xlarge    | c6g                     |

GCP
| sku.id         | sku.name                                        | F_Series | F_CoreCount | F_MemorySize |
| -------------- |-------------------------------------------------| -------- | ----------- | ------------ |
| 2E27-4F75-95CD | N1 Predefined Instance Core running in Americas | N1       | 1           |              |
| 07C7-3B6C-C92A | N2D AMD Custom Instance Ram running in Zurich   | N2D      |             | 1            |

- GCP would not include F_InstanceType nor F_SizeClass because these are properties of a resource since their SKUs aren't specific to an instance size/shape
- The CoreCount and MemorySize are both equal to 1 becuase the pricing unit is 1 core / hour and the RAM is 1 GB (2<sup>10</sup> which is referred to as GiB outside of the context of memory)

Azure
| F_InstanceType | F_Series | F_CoreCount | F_MemorySize | F_GpuCount | F_OperatingSystem |
| -------------- | -------- | ----------- | ------------ | ---------- | ----------------- |
| E16_v4         | Ev4      | 16          | 128          |            | Windows           |
| NC12s_v3       | NCsv3    | 12          | 224          | 2          | Linux             |


| F_InstanceType | F_DiskSpace   | F_Redundancy | F_DiskType | F_StorageClass |
| -------------- | ------------- | ------------ | ---------- | -------------- |
| P50            | 4096          | Zonal        | SSD        | Premium SSD    |

## Example Usecases

- Capcity Planning: 
  - Quantify how many cores of a VM Series you have provisioned in a region on average.
    - Uses: SkuPriceDetails {F_CoreCount, F_Series}, PricingUnit (e.g. in case PricingUnit is 10 Hours), PricingQuantity, ChargePeriodStart, ChargePeriodEnd, RegionName
  - Determine how much disk storage you have provisioned
- Unit Economics
  - Calculate the average cost per core of a VM Series

## Clarifications

## Reference

- https://cloud.google.com/skus

## Discussion / Scratch space
