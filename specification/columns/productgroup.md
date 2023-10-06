# Product Group

Product Group is second highest-level of classification of a product just below Product Category. Each product should have one and only one group that categorizes products into sets with common attributes and characteristics. As an example, a Product Group may be used to identify products in the "Compute" category as being products associated with particular operating system or processor architectures.

The Product Group is commonly used to group related products together to analyze usage patterns and costs specific to a subset of products within a category.

The ProductGroup column MUST be present and MUST NOT be null. This column is of type String and contains provider-specific values and is not restricted to a set of allowed values.

## Column ID

ProductGroup

## Display Name

Product Group

## Description

Product Group is the second highest-level classification of a product that can be used or purchased within a Product Category.

## Content Constraints

| Constraint      | Value            |
| :-------------- | :--------------- |
| Column required | True             |
| Data type       | String           |
| Allows nulls    | False            |
| Value format    | \<not specified> |

## Introduced (version)

1.0
