# SKU Price Effective Start

SKU Price Effective Start represents the inclusive date and time when the specified unit price and its associated pricing properties become active and applicable for a given [*SKU Price ID*](#datasets.skuprice.skupriceid).

When combined with [SKU Price Effective End](#datasets.skuprice.skupriceeffectiveend), this column defines the precise validity window of a rate card entry. This column allows practitioners to correctly map historical or future usage to the exact unit price that was valid at the time the consumption occurred, enabling accurate cost rating and temporal price variation analysis.

## Requirements

SkuPriceEffectiveStart MUST adhere to the following requirements:

* SkuPriceEffectiveStart MUST be of type DateTime.
* SkuPriceEffectiveStart MUST conform to [DateTimeFormat](#attributes.datetimeformat) requirements (e.g., UTC).
* SkuPriceEffectiveStart MUST NOT be null.
* SkuPriceEffectiveStart MUST represent the exact timestamp designated by the *service provider* when the specific pricing rate card row is effective.

## Column ID

SkuPriceEffectiveStart

## Display Name

SKU Price Effective Start

## Description

The inclusive date and time when the specified unit price and associated pricing properties become active and applicable.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [SKU Price](#datasets.skuprice)                      |
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | False                                                |
| Data type       | DateTime                                             |
| Value format    | [DateTime Format](#attributes.datetimeformat)        |

## Version Introduced

1.5
