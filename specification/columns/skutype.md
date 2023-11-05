# SKU Type

SKU Type is a specific model of the SKU being charged for. SKU Type should be the most precise identifier, name, or code that represents the characteristics of the SKU that was used or purchased. Some common terms used to describe SKU types by different providers and publishers are instance type, size, shape, tier, and edition, among others. SKU Type indicates **what** was used or purchased. Each SKU should have one and only one SKU type to identify the exact SKU being purchased. As an example, the SKU Type "Mv6 32-Core" may be used to identify SKUs in the "Compute" category, "Virtual Machines" group, "Linux" family, "Memory Optimized" class, in the "Xv6" class would refer to a 32-core virtual machine in the 6th generation of the memory optimized Linux VM SKU family.

SKU Type is commonly used to quantify usage and/or purchases for a specific SKU and plan for or calculate utilization and coverage metrics for commitment-based discounts.

The SkuType column MUST be present and MUST NOT be null when a specific type identifier is available for the SKU. This column is of type String and MAY be null when not applicable. SkuType contains provider-specific values and is not restricted to a set of allowed values.

## Column ID

SkuType

## Display Name

SKU Type

## Description

Specific model of the SKU being charged for.

## Content Constraints

| Constraint      | Value            |
| :-------------- | :--------------- |
| Column required | True             |
| Data type       | String           |
| Allows nulls    | True             |
| Value format    | \<not specified> |

## Introduced (version)

1.0
