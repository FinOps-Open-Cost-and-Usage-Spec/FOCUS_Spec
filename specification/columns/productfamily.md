# Product Family

Product Family is third-level of classification of a product just below Product Group.  Each product should have one and only one family that categorizes products into a set with specific attributes and characteristics applicable to a family of products.  As an example, a Product Family "Memory Optimized" may be used to identify products in the "Compute" category and "Linux VM" group as being virtual machine products running the Linux operating system that have optimized for high-memory workloads.

The Product Family is commonly used to group related products together to analyze usage patterns and costs specific to a subset of products within a group.

The ProductFamily column MUST be present and MUST NOT be null or empty. This column is of type String.  ProductFamily may contain provider-specific values and is not restricted to a set of allowed values.

## Column ID

ProductFamily

## Display Name

Product Family

## Description

A Product Family is the third level of classification of a product that can be used or purchased within a Product Category and Product Group.

## Content Constraints

| Constraint      | Value            |
| :-------------- | :--------------- |
| Column required | True             |
| Data type       | String           |
| Allows nulls    | False             |
| Value format    | \<not specified> |

## Introduced (version)

1.0
