# Quantity In Usage Unit

Quantity In Usage Unit is the amount of a resource or service that was used or purchased. The Quantity In Usage Unit is measured in units specified by the Usage Unit. Quantity In Usage Unit is used in conunction with Usage Unit to gain understanding of usage or consumption of a given product/service in an environment.

Quantity In Usage Unit MUST exist in billing data. The column MUST be a numeric value and MUST NOT contain nulls.

The Quantity In Usage Unit for a particular line item may differ from Quantity In Pricing Unit when providers use different quantity, quantity increments, or columns to determine cost. The values in UsageUnit and QuantityInUsageUnit are often listed at a finer granularity or over a different time interval than the PricingUnit and QuantityInPricingUnit. While QuantityInUsageUnit may appear to relate to pricing and cost, QuantityInUsageUnit is focused on resource or service consumption. It is essential not to confuse QuantityInUsageUnit with QuantityInPricingUnit which is the basis for determining cost. The QuantityInUsageUnit column MUST not be used as the basis for determining values related to any pricing or cost metric.

## Column ID

QuantityInUsageUnit

## Display name

Quantity In Usage Unit

## Description

## Content constraints

| Constraint      | Value        |
|-----------------|--------------|
| Column required | True         |
| Data type       | Numeric      |
| Allows nulls    | False        |
| Value format    | Numeric value |

## Introduced (version)

1.0
