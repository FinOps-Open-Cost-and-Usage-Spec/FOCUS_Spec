# Pricing Unit

The Pricing Unit represents a service-provider-specified measurement unit for determining unit prices, indicating how the service provider rates measured usage and purchase quantities after applying pricing rules like [*block pricing*](#glossary:block-pricing). Common examples include the number of hours for compute appliance runtime (e.g., `Hours`), gigabyte-hours for a storage appliance (e.g., `GB-Hours`), or an accumulated count of requests for a network appliance or API service (e.g., `1000 Requests`). Pricing Unit complements the [Pricing Quantity](#datasets.costandusage.pricingquantity) metric. Distinct from the [Consumed Unit](#datasets.costandusage.consumedunit), it focuses on pricing and cost, not [*resource*](#glossary:resource) and [*service*](#glossary:service) consumption, often at a coarser granularity.

## Requirements

The PricingUnit column MUST adhere to the following requirements:

* PricingUnit MUST be of type String.
* PricingUnit MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* PricingUnit SHOULD conform to [UnitFormat](#attributes.unitformat) requirements.
* PricingUnit MUST adhere to the following nullability requirements:
  * PricingUnit MUST be null when PricingQuantity is null.
  * PricingUnit MUST NOT be null when PricingQuantity is not null.
* When PricingUnit is not null, PricingUnit MUST adhere to the following additional requirements:
  * PricingUnit MUST be semantically equal to the corresponding pricing measurement unit provided in service-provider-published [*price list*](#glossary:price-list).
  * PricingUnit MUST be semantically equal to the corresponding pricing measurement unit provided in invoice, when the invoice includes a pricing measurement unit.

## Column ID

PricingUnit

## Display Name

Pricing Unit

## Description

Service-provider-specified measurement unit for determining unit prices, indicating how the service provider rates measured usage and purchase quantities after applying pricing rules like *block pricing*.

## Content constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [Cost and Usage](#datasets.costandusage)             |
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | [Unit Format](#attributes.unitformat)                |

## Introduced (version)

1.0-preview
