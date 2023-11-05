# SKU Class

SKU Class is an optional, fourth-level of classification of a SKU just below SKU Family. Each SKU MAY have one and only one class that categorizes SKUs into a subset with specific attributes and characteristics. As an example, the SKU Class "On-demand" may be used to identify SKUs in the "Compute" category, "Linux VM" group, and "Memory Optimized" family as being virtual machine SKUs running the Linux operating system that have specifications optimized for high-memory workloads that are being used on-demand as opposed to VMs that are reserved or purchased as an interruptible or spot instance.

SKU Class is commonly used to track usage patterns for specific subset of SKUs within a family or to analyze costs in similar classes across multiple families and groups.

The SkuClass column MAY be present and when present SHOULD NOT be null or empty. SkuClass may contain provider-specific values and is not restricted to a set of allowed values.

## Column ID

SkuClass

## Display Name

SKU Class

## Description

SKU Class is the fourth level of classification of a SKU just below SKU Family.

## Content Constraints

| Constraint      | Value            |
| :-------------- | :--------------- |
| Column required | False            |
| Data type       | String           |
| Allows nulls    | False            |
| Value format    | \<not specified> |

## Introduced (version)

1.0
