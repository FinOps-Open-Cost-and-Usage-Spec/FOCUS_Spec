# Product Family

Product Family is a collection of related product lines that share common characteristics within a Product Group. Product Family is third-level of classification of a product just below Product Group. Each product should have one and only one family that categorizes products into a set with specific attributes and characteristics applicable to a family of products. As an example, a Product Family "Memory Optimized" may be used to identify products in the "Compute" category and "Linux VM" group as being virtual machine products running the Linux operating system that have optimized for high-memory workloads. Product Family is commonly used to group related products together to analyze usage patterns and costs specific to a subset of products within a group.

The ProductFamily column MUST be present and MUST NOT be null when a lower-level breakdown of the product details is available within the Product Group. This column is of type String and MAY be null when not applicable. ProductFamily contains provider-specific values and is not restricted to a set of allowed values.

## Column ID

ProductFamily

## Display Name

Product Family

## Description

A collection of related product lines that share common characteristics within a Product Group.

## Content Constraints

| Constraint      | Value            |
| :-------------- | :--------------- |
| Column required | True             |
| Data type       | String           |
| Allows nulls    | True             |
| Value format    | \<not specified> |

## Introduced (version)

1.0
