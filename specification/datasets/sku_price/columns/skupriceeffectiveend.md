# SKU Price Effective End

SKU Price Effective End represents the exclusive date and time when the specified unit price and its associated pricing properties are no longer active or applicable for a given [*SKU Price ID*](#datasets.skuprice.skupriceid).

When combined with [SKU Price Effective Start](#datasets.skuprice.skupriceeffectivestart), this column defines the precise validity window of a rate card entry. If a unit price is currently active and has no scheduled expiration or deprecation date, this value remains null.

## Requirements

SkuPriceEffectiveEnd MUST adhere to the following requirements:

* SkuPriceEffectiveEnd MUST be of type DateTime.
* SkuPriceEffectiveEnd MUST conform to [DateTimeFormat](#attributes.datetimeformat) requirements (e.g., UTC).
* SkuPriceEffectiveEnd MUST adhere to the following nullability requirements:
  * SkuPriceEffectiveEnd MUST be null when the unit price is currently active and does not have a defined expiration or deprecation timestamp.
  * SkuPriceEffectiveEnd MUST NOT be null when the unit price has expired, been superseded, or has a scheduled termination timestamp.
* When SkuPriceEffectiveEnd is not null, SkuPriceEffectiveEnd MUST adhere to the following requirements:
  * SkuPriceEffectiveEnd MUST be chronologically greater than [SkuPriceEffectiveStart](#datasets.skuprice.skupriceeffectivestart).

## Column ID

SkuPriceEffectiveEnd

## Display Name

SKU Price Effective End

## Description

The exclusive date and time when the specified unit price and associated pricing properties are no longer active or applicable.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [SKU Price](#datasets.skuprice)                      |
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | True                                                 |
| Data type       | DateTime                                             |
| Value format    | [DateTime Format](#attributes.datetimeformat)        |

## Version Introduced

1.5
