# Product Line

Product Line is a group of related product types that share common characteristics. Product Line is an optional, fifth-level of classification of a product just below Product Class used by providers to organize products. As an example, the Product Line "Xv6" may be used to identify products in the "Compute" category, "Virtual Machines" group, "Linux" family, and "Memory Optimized" class as being virtual machine products running the Linux operating system that have specifications optimized for high-memory workloads that are the sixth version of a compute product with a line identifier of "X". Product Line is commonly used to track usage patterns for specific subset of products within a family or to analyze costs in similar classes across multiple families and groups.

The ProductLine column SHOULD be present and SHOULD NOT be null when a lower-level breakdown of the product details is available within the Product Class. This column is of type String and MAY contain provider-specific values and is not restricted to a set of allowed values. ProductLine MAY be present when ProductClass is not present. In this case, ProductLine will provide the most granular level of product classification with a ProductCategory, ProductGroup, and ProductFamily.

## Column ID

ProductLine

## Display Name

Product Line

## Description

A group of related product types that share common characteristics.

## Content Constraints

| Constraint      | Value            |
| :-------------- | :--------------- |
| Column required | False             |
| Data type       | String           |
| Allows nulls    | True             |
| Value format    | \<not specified> |

## Introduced (version)

1.0
