# Pricing Measure

The Pricing Measure is a provider-specified measurement unit for determining unit prices, indicating how a provider rates measured usage and purchase quantities after applying pricing rules like block pricing. Common examples include the number of hours for compute appliance runtime, gigabyte-hours for a storage appliance, or an accumulated count of requests for a network appliance or API service. Pricing Measure complements the [Pricing Quantity](#pricingquantity) measurement. Distinct from the [Usage Unit](#usageunit), it focuses on pricing and cost, not resource and service consumption, often at a coarser granularity.

The PricingMeasure column MUST be present in the billing data. This column MUST be of type String. It MUST NOT contain null if PricingQuantity is not null. The PricingMeasure value MUST be aligned with the corresponding pricing measure value provided in:

* The provider-published price list
* The invoice, when the invoice includes a pricing measure

## Column ID

PricingMeasure

## Display name

Pricing Measure

## Description

A provider-specified measurement unit for determining unit prices, indicating how a provider rates measured usage and purchase quantities after applying pricing rules like block pricing

## Content constraints

| Constraint      | Value           |
|-----------------|-----------------|
| Column required | True            |
| Data type       | String          |
| Allows nulls    | True            |
| Value format    | \<not specified> |

## Introduced (version)

1.0
