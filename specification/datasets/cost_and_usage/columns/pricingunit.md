# Pricing Unit

The [Pricing Unit](#col) represents a service-provider-specified measurement unit for determining unit prices, indicating how the service provider rates measured usage and purchase quantities after applying pricing rules like [block pricing](#term). Common examples include the number of hours for compute appliance runtime (e.g., `Hours`), gigabyte-hours for a storage appliance (e.g., `GB-Hours`), or an accumulated count of requests for a network appliance or API service (e.g., `1000 Requests`). [Pricing Unit](#col) complements the [Pricing Quantity](#col) metric. Distinct from the [Consumed Unit](#col), it focuses on pricing and cost, not [resource](#term) and [service](#term) consumption, often at a coarser granularity.

## Requirements

[PricingUnit](#col) MUST adhere to the following requirements:

* [PricingUnit](#col) MUST be of type String.
* [PricingUnit](#col) MUST conform to [StringHandling](#attr) requirements.
* [PricingUnit](#col) SHOULD conform to [UnitFormat](#attr) requirements.
* [PricingUnit](#col) MUST adhere to the following nullability requirements:
  * [PricingUnit](#col) MUST be null when [PricingQuantity](#col) is null.
  * [PricingUnit](#col) MUST NOT be null when [PricingQuantity](#col) is not null.
* When [PricingUnit](#col) is not null, [PricingUnit](#col) MUST adhere to the following requirements:
  * [PricingUnit](#col) MUST be semantically equal to the corresponding pricing measurement unit provided in service-provider-published [price list](#term).
  * [PricingUnit](#col) MUST be semantically equal to the corresponding pricing measurement unit provided in invoice, when the invoice includes a pricing measurement unit.

## Column ID

PricingUnit

## Display Name

Pricing Unit

## Description

Service-provider-specified measurement unit for determining unit prices, indicating how the service provider rates measured usage and purchase quantities after applying pricing rules like [block pricing](#term).

## Content Constraints

| Constraint                 | Value                                     |
| :------------------------- | :---------------------------------------- |
| Dataset                    | [Cost and Usage](#ds)                     |
| Operating model conditions | Not applicable                            |
| Column type                | Dimension                                 |
| Feature level              | Mandatory                                 |
| Allows nulls               | True                                      |
| Data type                  | String                                    |
| Value format               | [Unit Format](#attr)                      |

## Version Introduced

1.0-preview
