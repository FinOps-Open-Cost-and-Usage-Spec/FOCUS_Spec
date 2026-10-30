# SKU Price Effective Start

[SKU Price Effective Start](#col) represents the inclusive date and time when the specified [SKU Price](#ds) record becomes applicable for a given [SKU Price ID](#col). It reflects when the price becomes contractually or publicly applicable, not when a [practitioner](#term) first uses the [SKU](#term). A [charge](#term) in [Cost and Usage](#ds) falls under this price when its [Charge Period Start](#col:CostAndUsage.ChargePeriodStart) is on or after [SKU Price Effective Start](#col). When [SKU Price Effective Start](#col) is null, the SKU Price record has no lower boundary and applies to every [charge](#term) that precedes [SKU Price Effective End](#col), or to every [charge](#term) when [SKU Price Effective End](#col) is also null. A null states that the price is unbounded in that direction, not that its origin date is unknown.

When combined with [SKU Price Effective End](#col), this column defines the precise validity window of a rate card entry. This column allows [practitioners](#term) to correctly map historical or future usage to the exact SKU Price record that was valid at the time the consumption occurred, enabling accurate cost rating and temporal price variation analysis.

## Requirements

[SkuPriceEffectiveStart](#col) MUST adhere to the following requirements:

* [SkuPriceEffectiveStart](#col) MUST be of type Date/Time.
* [SkuPriceEffectiveStart](#col) MUST conform to [DateTimeFormat](#attr) requirements (e.g., UTC).
* [SkuPriceEffectiveStart](#col) MUST adhere to the following nullability requirements:
  * [SkuPriceEffectiveStart](#col) MUST be null when the SkuPrice record is applicable without a lower time boundary.
  * [SkuPriceEffectiveStart](#col) MUST NOT be null when the SkuPrice record has a designated timestamp from which it becomes applicable.
* [SkuPriceEffectiveStart](#col) MUST be the [inclusive start bound](#term) of the effective [period](#term) of the SkuPrice record when [SkuPriceEffectiveStart](#col) is not null.

## Column ID

SkuPriceEffectiveStart

## Display Name

SKU Price Effective Start

## Description

The inclusive date and time when the specified SKU Price record becomes active and applicable.

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
