# Pricing Unit

The Pricing Unit is the provider-specified measurement unit for determining unit prices, indicating how a provider rates measured usage and purchase quantities after applying pricing rules like block pricing. Common examples include the number of hours for compute appliance runtime, gigabyte-hours for a storage appliance, or an accumulated count of requests for a network appliance or API service. Pricing Unit complements the [Quantity In Pricing Unit](#quantityinpricingunit) measurement. Distinct from the [Usage Unit](#usageunit), it focuses on pricing and cost, not resource and service consumption, often at a coarser granularity.

The PricingUnit column MUST be present in the billing data. This column MUST be of type String. It MUST NOT contain null if [QuantityInPricingUnit](#quantityinpricingunit) is not null. The PricingUnit value MUST be aligned with the corresponding pricing unit value provided in:

* The provider-published price list
* The invoice, when the invoice includes a pricing unit

## Column ID

PricingUnit

## Display name

Pricing Unit

## Description

A measurement unit specified by the provider for determining unit prices associated with the usage or the purchase of a specific resource and/or service.

## Content constraints

| Constraint      | Value           |
|-----------------|-----------------|
| Column required | True            |
| Data type       | String          |
| Allows nulls    | True            |
| Value format    | \<not specified> |

## Introduced (version)

1.0
