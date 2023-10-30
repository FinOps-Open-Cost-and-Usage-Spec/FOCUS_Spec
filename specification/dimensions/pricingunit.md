# Pricing Unit

The Pricing Unit is the provider-specified measurement unit for determining the unit prices associated with the use or purchase of a specific resource and/or service. The Pricing Unit indicates how a provider rates the measured usage and purchase quantities after pricing rules, such as block pricing, are applied. Common examples include the number of hours for compute appliance runtime, gigabyte-hours for a storage appliance, or an accumulated count of requests for a network appliance or API service. In some cases, providers may opt for block pricing, such as using a million requests as the Pricing Unit instead of pricing individual requests. The Pricing Unit complements and describes how the measurement of [Quantity In Pricing Unit](#quantityinpricingunit) is conducted. The Pricing Unit pertains to pricing and cost determination and should not be confused with the [Usage Unit](#usageunit), which tracks resource and service consumption, typically at a finer granularity than the Pricing Unit.

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
