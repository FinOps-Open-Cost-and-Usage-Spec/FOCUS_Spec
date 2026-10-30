# Charge Category

[Charge Category](#col) represents the highest-level classification of a [SKU Price](#term) based on the nature of what is being priced. In the [SKU Price](#ds) dataset, [Charge Category](#col) is used to quickly distinguish between published rates for consumption-based usage, published fees for upfront or recurring purchases, and published unit values for granted [credits](#term).

## Requirements

[ChargeCategory](#col) MUST adhere to the following requirements:

* [ChargeCategory](#col) MUST be of type String.
* [ChargeCategory](#col) MUST NOT be null.
* [ChargeCategory](#col) MUST be one of the allowed values.
* [ChargeCategory](#col) MUST be ["Usage"](#val:ChargeCategory) when the [SKU Price](#term) represents the rate for consumption of a [service](#term) or [resource](#term).
* [ChargeCategory](#col) MUST be ["Purchase"](#val:ChargeCategory) when the [SKU Price](#term) represents a fee for the acquisition of a [service](#term), [resource](#term), or [commitment](#term).
* [ChargeCategory](#col) MUST be ["Credit"](#val:ChargeCategory) when the [SKU Price](#term) represents the unit value of a [credit](#term) granted by the [service provider](#term).

## Allowed Values

| Value      | Description                                                                                                                                    |
| :--------- | :----------------------------------------------------------------------------------------------------------------------------------------------|
| Usage      | The published unit price for the quantity of a *service* or *resource* that is consumed over a given [*period*](#glossary:period) of time. |
| Purchase   | The published fee for the acquisition of a *service*, *resource*, or *commitment* bought upfront or on a recurring basis.          |
| Credit     | The published unit value of a *credit* granted by the *service provider* (e.g., a promotional *credit* carrying a defined unit value). |

## Implementation Guidance

While the [Charge Category](#col) column is shared between the [Cost and Usage](#ds) dataset and the SKU Price dataset, [practitioners](#term) should note that the allowed values differ by design.

The [Cost and Usage](#ds) dataset acts as a financial ledger that tracks post-facto financial events. Therefore, it requires values like "Tax" and "Adjustment" to accurately balance a final [invoice](#term).

Conversely, the SKU Price dataset acts as a pre-facto catalog of available unit rates. Because taxes are calculated dynamically based on jurisdiction and entity, and [adjustments](#term) are account-level ledger corrections, [service providers](#term) do not publish [SKU Prices](#term) for these events. Therefore, the allowed values for [Charge Category](#col) in the SKU Price dataset are limited to catalog pricing constructs: ["Usage"](#val:ChargeCategory) (the published rate to consume a [resource](#term)), ["Purchase"](#val:ChargeCategory) (the published fee to acquire a [commitment](#term) or [service](#term)), and ["Credit"](#val:ChargeCategory) (the published unit value of a granted [credit](#term)).

[Credits](#term) are catalog pricing constructs where a [service provider](#term) issues a distinct [SKU](#term) and [SKU Price](#term) for the [credit](#term), most commonly a promotional [credit](#term) carrying a defined unit value. Where a [service provider](#term) publishes no such [SKU Price](#term), the [credit](#term) appears only in [Cost and Usage](#ds) and has no SKU Price record.

## Column ID

ChargeCategory

## Display Name

Charge Category

## Description

Represents the highest-level classification of a [SKU Price](#term) based on whether it is a usage rate, a purchase fee, or a [credit](#term) value.

## Content Constraints

| Constraint                 | Value                                                |
| :------------------------- | :--------------------------------------------------- |
| Dataset                    | [SKU Price](#ds)                                     |
| Operating Model Conditions | Not applicable                                       |
| Column type                | Dimension                                            |
| Feature level              | Mandatory                                            |
| Allows nulls               | False                                                |
| Data type                  | String                                               |
| Value format               | Allowed values                                       |

## Version Introduced

Preview: 1.5
