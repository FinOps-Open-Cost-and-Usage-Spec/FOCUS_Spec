# SKU Family

SKU Family is a collection of related SKU lines that share common characteristics within a SKU Group. SKU Family is third-level of classification of a SKU just below SKU Group. Each SKU should have one and only one family that categorizes SKUs into a set with specific attributes and characteristics applicable to a family of SKUs. As an example, a SKU Family "Memory Optimized" may be used to identify SKUs in the "Compute" category and "Linux VM" group as being virtual machine SKUs running the Linux operating system that have optimized for high-memory workloads. SKU Family is commonly used to group related SKUs together to analyze usage patterns and costs specific to a subset of SKUs within a group.

The SkuFamily column MUST be present and MUST NOT be null when a lower-level breakdown of the SKU details is available within the SKU Group. This column is of type String and MAY be null when not applicable. SkuFamily contains provider-specific values and is not restricted to a set of allowed values.

## Column ID

SkuFamily

## Display Name

SKU Family

## Description

A collection of related SKU lines that share common characteristics within a SKU Group.

## Content Constraints

| Constraint      | Value            |
| :-------------- | :--------------- |
| Column required | True             |
| Data type       | String           |
| Allows nulls    | True             |
| Value format    | \<not specified> |

## Introduced (version)

1.0
