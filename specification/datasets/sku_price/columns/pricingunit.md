# Pricing Unit

[Pricing Unit](#col) represents the service-provider-specified measurement unit used to define the unit price of an offering. Common examples include the number of hours for compute runtime (e.g., `Hours`), data volume for storage (e.g., `GB-Months`), or an accumulated count of API requests or AI interactions (e.g., `1,000 Requests`, `1,000,000 Tokens`).

Distinct from the [Consumed Unit](#col:CostAndUsage.ConsumedUnit) in [Cost and Usage](#ds) data, [Pricing Unit](#col) focuses strictly on the measurement standard dictated by the [service provider](#term) in their rate card, which is often at a coarser granularity than the raw usage measurement.

## Requirements

[PricingUnit](#col) MUST adhere to the following requirements:

* [PricingUnit](#col) MUST be of type String.
* [PricingUnit](#col) MUST conform to [StringHandling](#attr) requirements.
* [PricingUnit](#col) SHOULD conform to [UnitFormat](#attr) requirements.
* [PricingUnit](#col) MUST NOT be null.
* [PricingUnit](#col) MUST match a [PricingCurrency](#col) value of records whose [PricingCurrencyCategory](#col) is ["Consumable"](#val:SkuPrice.PricingCurrencyCategory) when the [SkuPrice](#ds) record represents the price of that currency.

## Implementation Guidance

Practitioners are encouraged to carefully distinguish between **[Pricing Unit](#col)** and [Pricing Currency](#col).

* **[Pricing Unit](#col)** defines the physical, volumetric, or logical measurement of the service itself (e.g., `Hours`, `GB`, `Tokens`).
* **[Pricing Currency](#col)** defines the financial or consumable medium of exchange used to pay for that unit (e.g., `USD`, `Platform Credits`).

When a [service provider](#term) abstracts billing into a proprietary [consumption currency](#term) (e.g., "Normalized Billing Units"), [Pricing Unit](#col) represents the volumetric measurement tied to the unit price rate, not the monetary instrument used to pay for it.

Notably, in the context of Artificial Intelligence and API services, a "Token" (e.g., LLM prompt or completion tokens) represents a volumetric unit of processing measurement (i.e., [Pricing Unit](#col)), not a financial instrument to be exchanged (i.e., [Pricing Currency](#col)).

## Column ID

PricingUnit

## Display Name

Pricing Unit

## Description

Service-provider-specified measurement unit used to define the unit price of an offering (e.g., `Hours`, `GB-Months`, `1,000 Tokens`).

## Content Constraints

| Constraint                 | Value                                                |
| :------------------------- | :--------------------------------------------------- |
| Dataset                    | [SKU Price](#ds)                                     |
| Operating Model Conditions | Not applicable                                       |
| Column type                | Dimension                                            |
| Feature level              | Mandatory                                            |
| Allows nulls               | False                                                |
| Data type                  | String                                               |
| Value format               | [Unit Format](#attr)                                 |

## Version Introduced

Preview: 1.5
