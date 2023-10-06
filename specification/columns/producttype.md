# Product Type

Product Class is a mandatory field the specific product being charged for. Each product MUST have one and only product type to identify the exact product being purchased. As an example, the Product Type "Mv6 32-Core" may be used to identify products in the "Compute" category, "Linux VM" group, "Memory Optimized" family, "On-demand" class, in the "Xv6" class would refer to an on-demand, 32-core virtual machine in the 6th generation of the memory optimized Linux VM product group.

Product Type is commonly used to identify the specific product being purchase and to generate usage and cost data related to that specific product.

The ProductType column MUST be present and MUST NOT be null when a specific type identifier is available for the product. ProductType may contain provider-specific values and is not restricted to a set of allowed values.

## Column ID

ProductType

## Display Name

Product Type

## Description

Product Class is a mandatory field the specific product being charged for.

## Content Constraints

| Constraint      | Value            |
| :-------------- | :--------------- |
| Column required | True             |
| Data type       | String           |
| Allows nulls    | True             |
| Value format    | \<not specified> |

## Introduced (version)

1.0
