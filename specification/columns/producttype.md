# Product Type

Product Type is a specific model of the product being charged for. Product Type should be the most precise identifier, name, or code that represents the characteristics of the product that was used or purchased. Some common terms used to describe product types by different providers and publishers are instance type, size, shape, tier, and edition, among others. Product Type indicates **what** was used or purchased. Each product should have one and only one product type to identify the exact product being purchased. As an example, the Product Type "Mv6 32-Core" may be used to identify products in the "Compute" category, "Virtual Machines" group, "Linux" family, "Memory Optimized" class, in the "Xv6" class would refer to a 32-core virtual machine in the 6th generation of the memory optimized Linux VM product family.

Product Type is commonly used to quantify usage and/or purchases for a specific product and plan for or calculate utilization and coverage metrics for commitment-based discounts.

The ProductType column MUST be present and MUST NOT be null when a specific type identifier is available for the product. This column is of type String and MAY be null when not applicable. ProductType contains provider-specific values and is not restricted to a set of allowed values.

## Column ID

ProductType

## Display Name

Product Type

## Description

Specific model of the product being charged for.

## Content Constraints

| Constraint      | Value            |
| :-------------- | :--------------- |
| Column required | True             |
| Data type       | String           |
| Allows nulls    | True             |
| Value format    | \<not specified> |

## Introduced (version)

1.0
