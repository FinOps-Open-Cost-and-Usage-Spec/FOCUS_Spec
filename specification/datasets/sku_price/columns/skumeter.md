# SKU Meter

SKU Meter describes the functionality being metered or measured by a particular [*SKU*](#glossary:sku) in the [*price list*](#glossary:price-list).

Service providers often have billing models in which multiple *SKUs* exist for a given [*service*](#glossary:service) to describe and bill for different functionalities for that service. For example, an object storage service may have separate *SKUs* for functionalities such as object storage, API requests, data transfer, encryption, and object management. This field provides the specific native meter identifier, allowing [*practitioners*](#glossary:practitioner) to seamlessly join or filter rate card data against the exact consumption meters that appear in a [Cost and Usage](#datamodel.costandusage) dataset.

## Requirements

SkuMeter MUST adhere to the following requirements:

* SkuMeter MUST be of type String.
* SkuMeter MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* SkuMeter SHOULD NOT be null.
* SkuMeter SHOULD remain consistent over time for a given [SkuId](#datamodel.skuprice.skuid).

## Examples

Compute Usage, Block Volume Usage, Data Transfer, API Requests

## Column ID

SkuMeter

## Display Name

SKU Meter

## Description

Describes the functionality being metered or measured by a particular *SKU* in the *price list*.

## Content Constraints

| Constraint                 | Value                                                |
| :------------------------- | :--------------------------------------------------- |
| Dataset                    | [SKU Price](#datamodel.skuprice)                     |
| Operating Model Conditions | Not applicable                                       |
| Column type                | Dimension                                            |
| Feature level              | Mandatory                                            |
| Allows nulls               | True                                                 |
| Data type                  | String                                               |
| Value format               | \<not specified>                                     |

## Version Introduced

1.5
