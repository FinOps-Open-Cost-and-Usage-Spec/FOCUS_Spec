# SKU Price Effective End

SKU Price Effective End represents the exclusive date and time when the specified unit price and its associated pricing properties are no longer active or applicable for a given [*SKU Price ID*](#datamodel.skuprice.skupriceid).

When combined with [SKU Price Effective Start](#datamodel.skuprice.skupriceeffectivestart), this column defines the precise validity window of a rate card entry. When a unit price has no scheduled expiration or deprecation date, this value remains null, including for a price published ahead of taking effect. A null therefore states that the price has no upper boundary, not that the price is the one currently in effect. A charge in Cost and Usage falls under this price when its charge period start is before SKU Price Effective End, or when this value is null.

## Requirements

SkuPriceEffectiveEnd MUST adhere to the following requirements:

* SkuPriceEffectiveEnd MUST be of type Date/Time.
* SkuPriceEffectiveEnd MUST conform to [DateTimeFormat](#attributes.date/timeformat) requirements (e.g., UTC).
* SkuPriceEffectiveEnd MUST adhere to the following nullability requirements:
  * SkuPriceEffectiveEnd MUST be null when the unit price is applicable without an upper time boundary.
  * SkuPriceEffectiveEnd MUST NOT be null when the unit price has a designated timestamp beyond which it is no longer applicable.
* When SkuPriceEffectiveStart and SkuPriceEffectiveEnd are both not null, SkuPriceEffectiveEnd MUST be chronologically greater than [SkuPriceEffectiveStart](#datamodel.skuprice.skupriceeffectivestart).

## Column ID

SkuPriceEffectiveEnd

## Display Name

SKU Price Effective End

## Description

The exclusive date and time when the specified unit price and associated pricing properties are no longer active or applicable.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [SKU Price](#datamodel.skuprice)                      |
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | True                                                 |
| Data type       | Date/Time                                            |
| Value format    | [Date/Time Format](#attributes.date/timeformat)      |

## Version Introduced

1.5
