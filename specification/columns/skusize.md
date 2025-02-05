# SKU Size

A [*SKU*](#glossary:sku) Size describes the size, shape, or version of the SKU specified by the SKU ID...

The SkuSize column adheres to the following requirements:

* SkuSize MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* SkuSize MUST be of type String.
* SkuSize MUST NOT contain null values when the SkuId has an associated size.
* SkuSize MUST contain null values when SkuId is null or not associated with a size.
* ...

## Column ID

SkuSize

## Display Name

SKU Size

## Description

TODO

## Content constraints

| Constraint    | Value            |
| :------------ | :--------------- |
| Column type   | Dimension        |
| Feature level | Optional         |
| Allows nulls  | True             |
| Data type     | String           |
| Value format  | \<not specified> |

## Introduced (version)

1.2
