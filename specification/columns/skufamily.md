# SKU Family

A [*SKU*](#glossary:sku) Family describes...

The SkuFamily column adheres to the following requirements:

* SkuFamily MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports multiple SKU families for any SKU.
* SkuFamily MUST be of type String.
* SkuFamily MUST NOT contain null values when the SkuId has an associated SKU family.
* SkuFamily MUST contain null values when SkuId is null or is not associated with a SKU family.

## Column ID

SkuFamily

## Display Name

SKU Family

## Description

TODO

## Content constraints

| Constraint    | Value            |
| :------------ | :--------------- |
| Column type   | Dimension        |
| Feature level | Conditional      |
| Allows nulls  | True             |
| Data type     | String           |
| Value format  | \<not specified> |

## Introduced (version)

1.2
