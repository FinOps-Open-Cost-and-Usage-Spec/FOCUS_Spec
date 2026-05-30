# SKU Price Description

A SKU Price Description provides a high-level context of a [*SKU Price*](#glossary:sku-price) without requiring additional discovery. This column is a self-contained summary of the catalog offering's purpose and unit price. It typically covers a select group of corresponding details across a rate card dataset or provides information not otherwise available.

## Requirements

SkuPriceDescription MUST adhere to the following requirements:

* SkuPriceDescription MUST be of type String.
* SkuPriceDescription MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* SkuPriceDescription MUST NOT be null.
* SkuPriceDescription maximum length SHOULD be provided in the corresponding FOCUS Metadata Schema.

## Column ID

SkuPriceDescription

## Display Name

SKU Price Description

## Description

Self-contained summary of the *SKU Price's* purpose and offering.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [SKU Price](#datasets.skuprice)                      |
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | False                                                |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Version Introduced

1.5
