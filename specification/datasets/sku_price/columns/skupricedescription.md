# SKU Price Description

A [SKU Price Description](#col) provides a high-level context of a [SKU Price](#term) without requiring additional discovery. This column is a self-contained summary of the catalog offering's purpose and unit price. It typically covers a select group of corresponding details across a [SKU Price](#ds) dataset or provides information not otherwise available.

## Requirements

[SkuPriceDescription](#col) MUST adhere to the following requirements:

* [SkuPriceDescription](#col) MUST be of type String.
* [SkuPriceDescription](#col) MUST conform to [StringHandling](#attr) requirements.
* [SkuPriceDescription](#col) MUST NOT be null.
* [SkuPriceDescription](#col) maximum length SHOULD be provided in the corresponding FOCUS Metadata Schema.

## Column ID

SkuPriceDescription

## Display Name

SKU Price Description

## Description

Self-contained summary of the [SKU Price's](#term:sku-price) purpose and offering.

## Content Constraints

| Constraint                 | Value                                                |
| :------------------------- | :--------------------------------------------------- |
| Dataset                    | [SKU Price](#ds)                                     |
| Operating Model Conditions | Not applicable                                       |
| Column type                | Dimension                                            |
| Feature level              | Mandatory                                            |
| Allows nulls               | False                                                |
| Data type                  | String                                               |
| Value format               | \<not specified>                                     |

## Version Introduced

Preview: 1.5
