# SKU Price Effective Start

SKU Price Effective Start represents the inclusive date and time when the specified unit price and its associated pricing properties become applicable for a given [*SKU Price ID*](#datamodel.skuprice.skupriceid). It reflects when the price becomes contractually or publicly applicable, not when a practitioner first uses the SKU. A charge in Cost and Usage falls under this price when its charge period start is on or after SKU Price Effective Start. When SKU Price Effective Start is null, the unit price is treated as applicable from the earliest available time.

When combined with [SKU Price Effective End](#datamodel.skuprice.skupriceeffectiveend), this column defines the precise validity window of a [*price list*](#glossary:price-list) entry. This column allows practitioners to correctly map historical or future usage to the exact unit price that was valid at the time the consumption occurred, enabling accurate cost rating and temporal price variation analysis.

## Requirements

SkuPriceEffectiveStart MUST adhere to the following requirements:

* SkuPriceEffectiveStart MUST be of type Date/Time.
* SkuPriceEffectiveStart MUST conform to [DateTimeFormat](#attributes.date/timeformat) requirements (e.g., UTC).
* SkuPriceEffectiveStart MAY be null when the *service provider* does not specify the date from which the unit price became applicable.
* When SkuPriceEffectiveStart is not null, SkuPriceEffectiveStart MUST represent the exact timestamp designated by the *service provider* from which the unit price is applicable.

## Column ID

SkuPriceEffectiveStart

## Display Name

SKU Price Effective Start

## Description

The inclusive date and time when the specified unit price and associated pricing properties become active and applicable.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [SKU Price](#datamodel.skuprice)                      |
| Conditions      | Not applicable                                        |
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | True                                                 |
| Data type       | Date/Time                                            |
| Value format    | [Date/Time Format](#attributes.date/timeformat)      |

## Version Introduced

1.5
