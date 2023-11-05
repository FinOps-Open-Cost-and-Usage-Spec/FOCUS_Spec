# SKU Group

SKU Group is second highest-level of classification of a SKU just below SKU Category. Each SKU should have one and only one group that categorizes SKUs into sets with common attributes and characteristics. As an example, a SKU Group may be used to identify SKUs in the "Compute" category as being SKUs associated with particular operating system or processor architectures.

The SKU Group is commonly used to group related SKUs together to analyze usage patterns and costs specific to a subset of SKUs within a category.

The SkuGroup column MUST be present and MUST NOT be null. This column is of type String and contains provider-specific values and is not restricted to a set of allowed values.

## Column ID

SkuGroup

## Display Name

SKU Group

## Description

SKU Group is the second highest-level classification of a SKU that can be used or purchased within a SKU Category.

## Content Constraints

| Constraint      | Value            |
| :-------------- | :--------------- |
| Column required | True             |
| Data type       | String           |
| Allows nulls    | False            |
| Value format    | \<not specified> |

## Introduced (version)

1.0
