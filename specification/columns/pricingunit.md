# Pricing Unit

The Pricing Unit represents a provider-specified measurement unit for determining unit prices, indicating how the provider rates measured usage and purchase quantities after applying pricing rules like [*block pricing*](#glossary:block-pricing). Common examples include the number of hours for compute appliance runtime (e.g. `Hours`), gigabyte-hours for a storage appliance (e.g., `GB-Hours`), or an accumulated count of requests for a network appliance or API service (e.g., `1000 Requests`). Pricing Unit complements the [Pricing Quantity](#pricingquantity) metric. Distinct from the [Usage Unit](#usageunit), it focuses on pricing and cost, not [*resource*](#glossary:resource) and [*service*](#glossary:service) consumption, often at a coarser granularity.

The PricingUnit column MUST be present in the billing data. This column MUST be of type String. This column MUST NOT be null if [ChargeCategory](#chargecategory) is "Usage" or "Purchase" and MAY be null for other ChargeCategory values. Units of measure used in PricingUnit SHOULD adhere to the values and format requirements specified in the [UnitFormat](#unitformat) attribute.

The PricingUnit value MUST be semantically equal to the corresponding pricing measurement unit value provided in:

* The provider-published [*price list*](#glossary:price-list)
* The invoice, when the invoice includes a pricing measurement unit

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
| Compliance level| Basic                   |
| Allows nulls    | True                    |
| Data type       | String                  |
| Value format    | [Unit Format](#unitformat) |

## Introduced (version)

1.0
