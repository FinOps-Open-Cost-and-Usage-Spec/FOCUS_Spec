# Pricing Unit

Pricing Unit represents the service-provider-specified measurement unit used to define the unit price of an offering. Common examples include the number of hours for compute runtime (e.g., `Hours`), data volume for storage (e.g., `GB-Mo`), or an accumulated count of API requests or AI interactions (e.g., `1K Requests`, `1K Tokens`).

Distinct from the [Consumed Unit](#datasets.costandusage.consumedunit) in [Cost and Usage](#datasets.costandusage) data, Pricing Unit focuses strictly on the measurement standard dictated by the [*service provider*](#glossary:service-provider) in their rate card, which is often at a coarser granularity than the raw usage measurement.

## Requirements

PricingUnit MUST adhere to the following requirements:

* PricingUnit MUST be of type String.
* PricingUnit MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* PricingUnit SHOULD conform to [UnitFormat](#attributes.unitformat) requirements.
* PricingUnit MUST NOT be null.
* PricingUnit MUST be semantically equal to the corresponding pricing measurement unit provided in the service-provider-published [*price list*](#glossary:price-list).

## Implementation Guidance

Practitioners are encouraged to carefully distinguish between **Pricing Unit** from **Pricing Currency**.

* **Pricing Unit** defines the physical, volumetric, or logical measurement of the service itself (e.g., `Hours`, `GB`, `Tokens`).
* **Pricing Currency** defines the financial or consumable medium of exchange used to pay for that unit (e.g., `USD`, `Platform Credits`).

When a *service provider* abstracts billing into a proprietary [*consumption currency*](#glossary:consumption-currency) (e.g., "Normalized Billing Units"), Pricing Unit represents the volumetric measurement tied to the unit price rate, not the monetary instrument used to pay for it.

Notably, in the context of Artificial Intelligence and API services, a "Token" (e.g., LLM prompt or completion tokens) represents a volumetric unit of processing measurement (i.e., Pricing Unit), not a financial instrument to be exchanged (i.e., Pricing Currency).

## Column ID

PricingUnit

## Display Name

Pricing Unit

## Description

Service-provider-specified measurement unit used to define the unit price of an offering (e.g., `Hours`, `GB-Mo`, `1K Tokens`).

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [SKU Price](#datasets.skuprice)                      |
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | False                                                |
| Data type       | String                                               |
| Value format    | [Unit Format](#attributes.unitformat)                |

## Version Introduced

1.5
