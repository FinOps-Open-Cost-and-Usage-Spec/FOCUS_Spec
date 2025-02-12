# SKU Family

The SKU Family column represents the common name for the family or version of the [*SKU*](#glossary:SKU).

It is oftentimes the case that within a [Service Subcategory](#servicesubcategory) a Provider(#provider) offers multiple different families of versions of SKUs. The SKU Family column provides this information to group and aggregate cost and usage data across SKUs of the same family or version.

The SkuFamily column adheres to the following requirements:

* The SkuFamily column is RECOMMENDED be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* This column MUST be of type String and MAY contain null values.
* SkuFamily values SHOULD follow a common convention used by the provider and SHOULD be consistent across SkuId and SkuPriceId records.
* SkuFamily MUST contain null values when SkuId is null or is not associated with a family or version.

## Column ID

SkuFamily

## Display Name

SKU Family

## Description

A common name for the family or version of the SKU, where applicable.

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
