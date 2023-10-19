# Pricing Unit

The Pricing Unit is a measurement unit specified by the provider for determining unit prices associated with the usage or the purchase of a specific resource and/or service. Common examples include the number of hours a compute appliance was running for a given period, the number of gigabytes * the number of hours (gigabyte-hours) for a storage appliance, or a cumulative count of requests for a network appliance or API service. For certain services providers can choose block pricing i.e., million requests as a base unit. Pricing Unit is complementary to and describes how [Quantity In Pricing Unit](#quantityinpricingunit) is measured. While Pricing Unit may appear to relate to resource and/or service consumption, Pricing Unit is primarily focused on pricing and cost. It is essential not to confuse Pricing Unit with [Usage Unit](#usageunit), which is dedicated to tracking resource and/or service consumption and is often at a lower granularity than the Pricing Unit.

The PricingUnit column MUST be present in the billing data. This column MUST be of type String. It MUST NOT contain null if [QuantityInPricingUnit](#quantityinpricingunit) is not null. The PricingUnit MUST match the corresponding value published in the price list. If the level of detail provided on invoice includes pricing units, PricingUnit values MUST be consistent in both the billing data and the invoice for the same billing period.

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
