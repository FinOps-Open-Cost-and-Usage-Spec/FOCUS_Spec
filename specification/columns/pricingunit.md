# Pricing Unit

The Pricing Unit represents a provider-specified measurement unit for determining unit prices, indicating how the provider rates measured usage and purchase quantities after applying pricing rules like [*block pricing*](#glossary:block-pricing). Common examples include the number of hours for compute appliance runtime (e.g. `Hours`), gigabyte-hours for a storage appliance (e.g., `GB-Hours`), or an accumulated count of requests for a network appliance or API service (e.g., `1000 Requests`). Pricing Unit complements the [Pricing Quantity](#pricingquantity) metric. Distinct from the [Consumed Unit](#consumedunit), it focuses on pricing and cost, not [*resource*](#glossary:resource) and [*service*](#glossary:service) consumption, often at a coarser granularity.

The PricingUnit column adheres to the following requirements:

* PricingUnit MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* PricingUnit MUST be of type String.
* PricingUnit MUST conform to [String Handling](#stringhandling) requirements.
* PricingUnit SHOULD conform to [UnitFormat](#unitformat) requirements.
* PricingUnit nullability is defined as follows:
  * PricingUnit MUST be null when [ChargeCategory](#chargecategory) is "Tax".
  * PricingUnit MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
  * PricingUnit MAY be null in all other cases.
* When PricingUnit is not null, PricingUnit adheres to the following additional requirements:
  * PricingUnit MUST be semantically equal to the corresponding pricing measurement unit provided in provider-published [*price list*](#glossary:price-list).
  * PricingUnit MUST be semantically equal to the corresponding pricing measurement unit provided in invoice, when the invoice includes a pricing measurement unit.

## Column ID

PricingUnit

## Display Name

Pricing Unit

## Description

Provider-specified measurement unit for determining unit prices, indicating how the provider rates measured usage and purchase quantities after applying pricing rules like *block pricing*.

## Content constraints

| Constraint      | Value                   |
|-----------------|-------------------------|
| Column type     | Dimension               |
| Feature level   | Mandatory               |
| Allows nulls    | True                    |
| Data type       | String                  |
| Value format    | [Unit Format](#unitformat) |

## Introduced (version)

1.0-preview
