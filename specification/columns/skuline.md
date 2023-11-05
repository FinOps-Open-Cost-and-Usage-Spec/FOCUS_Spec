# SKU Line

SKU Line is a collection of related SKU types that share common characteristics within a SKU Class. SKU Line is an optional, fifth-level of classification of a SKU just below SKU Class used by providers to organize SKUs. As an example, the SKU Line "Xv6" may be used to identify SKUs in the "Compute" category, "Virtual Machines" group, "Linux" family, and "Memory Optimized" class as being virtual machine SKUs running the Linux operating system that have specifications optimized for high-memory workloads that are the sixth version of a compute SKU with a line identifier of "X". SKU Line is commonly used to track usage patterns for specific subset of SKUs within a family or to analyze costs in similar classes across multiple families and groups.

The SkuLine column SHOULD be present and SHOULD NOT be null when a lower-level breakdown of the SKU details is available within the SKU Class. This column is of type String and contains provider-specific values and is not restricted to a set of allowed values. SkuLine MAY be present when SkuClass is not present. In this case, SkuLine will provide the most granular level of SKU classification with a SkuCategory, SkuGroup, and SkuFamily.

## Column ID

SkuLine

## Display Name

SKU Line

## Description

A collection of related SKU types that share common characteristics.

## Content Constraints

| Constraint      | Value            |
| :-------------- | :--------------- |
| Column required | False            |
| Data type       | String           |
| Allows nulls    | True             |
| Value format    | \<not specified> |

## Introduced (version)

1.0
