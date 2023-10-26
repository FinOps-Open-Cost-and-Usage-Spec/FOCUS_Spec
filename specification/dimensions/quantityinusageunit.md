# Quantity In Usage Unit

Quantity In Usage Unit is the number of units of a resource or service that was used or consumed. The Quantity In Usage Unit is measured in units specified by the [UsageUnit](#usageunit). Quantity In Usage Unit is used in conjunction with Usage Unit to gain understanding of usage or consumption of a given product/service in an environment.

The Quantity In Usage Unit for a particular line item may differ from Quantity In Pricing Unit when providers use different quantity, quantity increments, or columns to determine cost. The values in UsageUnit and QuantityInUsageUnit are often listed at a finer granularity or over a different time interval than the [PricingUnit](#pricingunit) and [QuantityInPricingUnit](#quantityinpricingunit). While QuantityInUsageUnit may appear to relate to pricing and cost, QuantityInUsageUnit is focused on resource or service consumption. It is essential not to confuse QuantityInUsageUnit with QuantityInPricingUnit which is the basis for determining cost. The QuantityInUsageUnit column MUST NOT be used as the basis for determining values related to any pricing or cost metric.

Quantity In Usage Unit MUST exist in billing data. The column MUST be a numeric value and when the [ChargeType](#chargetyep) is "Usage" Quantity In Usage Unit SHOULD NOT contain nulls. Negative values are only permissable when providers are adjusting for usage corrections.

## Column ID

QuantityInUsageUnit

## Display name

Quantity In Usage Unit

## Description

The number of units of a resource or service that was used or consumed based on the [UsageUnit](#usageunit)

## Content constraints

| Constraint      | Value        |
|-----------------|--------------|
| Column required | True         |
| Data type       | Numeric      |
| Allows nulls    | False        |
| Value format    | Numeric value |

## Introduced (version)

1.0
