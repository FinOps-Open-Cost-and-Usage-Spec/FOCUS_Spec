# SKU Size

The SKU Size column represents the common name for the size and shape of the [*SKU*](#glossary:SKU), where applicable.

It is oftentimes the case that a SKU has a common name to refer to its size and shape. This size may be common across multiple [SKU IDs](#skuid) and [SKU Price IDs](#skupriceid), which are differentiated based on properties other than their size (e.g. [Region Name](#regionname), [Pricing Category](#pricingcategory), etc.). The SKU Size column provides a way to group and aggregate cost and usage data across like sizes.

The SkuSize column adheres to the following requirements:

* The SkuSize column is RECOMMENDED be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* This column MUST be of type String and MAY contain null values.
* SkuSize values SHOULD follow a common convention used by the provider and SHOULD be consistent across SkuId and SkuPriceId records of the same size and shape.
* SkuSize MUST contain null values when SkuId is null or is not associated with a named size.

## Column ID

SkuSize

## Display Name

SKU Size

## Description

A common name for the size and shape of the SKU, where applicable.

## Content Constraints

| Constraint      | Value            |
| :-------------- | :--------------- |
| Column type     | Dimension        |
| Feature level   | Recommended      |
| Allows nulls    | True             |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

1.2
