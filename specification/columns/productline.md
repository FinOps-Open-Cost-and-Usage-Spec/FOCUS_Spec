# Product Line

Product Line is an optional, fifth-level of classification of a product just below Product Class. Each product MAY have one and only one line that classifies products into a specific subset of products with the same product details and attributes. As an example, the Product Line "Xv6" may be used to identify products in the "Compute" category, "Linux VM" group, "Memory Optimized" family, and "On-demand" class as being virtual machine products running the Linux operating system that have specifications optimized for high-memory workloads that are being used on-demand that are the sixth version of a compute product with a line identifier of "X".

Product Line is commonly used to track usage patterns for specific subset of products within a family or to analyze costs in similar classes across multiple families and groups.

The ProductLine column MAY be present and when present SHOULD NOT be null or empty. ProductLine may contain provider-specific values and is not restricted to a set of allowed values.  ProductLine MAY be present when ProductClass is not present.  In this case, ProductLine will provide the most granular level of product classification with the required fields ProductCategory, ProductGroup, and ProductFamily.

## Column ID

ProductLine

## Display Name

Product Line

## Description

A Product Line is a specific set of items within a Product Family or Product Class that have the same attributes and product details.

## Content Constraints

| Constraint      | Value            |
| :-------------- | :--------------- |
| Column required | False             |
| Data type       | String           |
| Allows nulls    | False            |
| Value format    | \<not specified> |

## Introduced (version)

1.0
