# SKU Price Effective End

[SKU Price Effective End](#col) represents the exclusive date and time when the specified [SKU Price](#ds) record is no longer active or applicable for a given [SKU Price ID](#col).

When combined with [SKU Price Effective Start](#col), this column defines the precise validity window of a rate card entry. When a SKU Price record has no scheduled expiration or deprecation date, this value remains null, including for a price published ahead of taking effect. A null therefore states that the price has no upper boundary, not that the price is the one currently in effect. A [charge](#term) in [Cost and Usage](#ds) falls under this price when its [Charge Period Start](#col:CostAndUsage.ChargePeriodStart) is before [SKU Price Effective End](#col), or when this value is null.

## Requirements

[SkuPriceEffectiveEnd](#col) MUST adhere to the following requirements:

* [SkuPriceEffectiveEnd](#col) MUST be of type Date/Time.
* [SkuPriceEffectiveEnd](#col) MUST conform to [DateTimeFormat](#attr) requirements (e.g., UTC).
* [SkuPriceEffectiveEnd](#col) MUST adhere to the following nullability requirements:
  * [SkuPriceEffectiveEnd](#col) MUST be null when the [SkuPrice](#ds) record is applicable without an upper time boundary.
  * [SkuPriceEffectiveEnd](#col) MUST NOT be null when the [SkuPrice](#ds) record has a designated timestamp from which it is no longer applicable.
* [SkuPriceEffectiveEnd](#col) MUST be the [exclusive end bound](#term) of the effective [period](#term) of the [SkuPrice](#ds) record when [SkuPriceEffectiveEnd](#col) is not null.
* [SkuPriceEffectiveEnd](#col) MUST be greater than [SkuPriceEffectiveStart](#col) when [SkuPriceEffectiveStart](#col) is not null and [SkuPriceEffectiveEnd](#col) is not null.

## Column ID

SkuPriceEffectiveEnd

## Display Name

SKU Price Effective End

## Description

The exclusive date and time when the specified SKU Price record is no longer active or applicable.

## Content Constraints

| Constraint                 | Value                                                |
| :------------------------- | :--------------------------------------------------- |
| Dataset                    | [SKU Price](#ds)                                     |
| Operating Model Conditions | Not applicable                                       |
| Column type                | Dimension                                            |
| Feature level              | Mandatory                                            |
| Allows nulls               | True                                                 |
| Data type                  | Date/Time                                            |
| Value format               | [Date/Time Format](#attr)                            |

## Version Introduced

Preview: 1.5
