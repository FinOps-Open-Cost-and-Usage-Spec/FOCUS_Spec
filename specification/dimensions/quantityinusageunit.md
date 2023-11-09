# Usage Quantity

Usage Quantity represents the volume of a resource or service that was consumed, measured in units specified by the [UsageUnit](#usageunit). Distinct from [Pricing Quantity](#pricingquantity), Usage Quantity is used in conjunction with Usage Unit to measure the consumption of a product/service offering from a provider.

The Usage Quantity for a charge may differ from Pricing Quantity when providers use different quantity, quantity increments, or columns to determine cost. The values in UsageUnit and UsageQuantity are often listed at a finer granularity or over a different time interval than the [PricingMeasure](#pricingmeasure) and [PricingQuantity](#pricingquantity). While UsageQuantity may appear to relate to pricing and cost, UsageQuantity is focused on resource consumption. It is essential not to confuse the UsageQuantity column with the PricingQuantity column which is the basis for determining cost. The UsageQuantity column MUST NOT be used as the basis for determining values related to any pricing or cost metric.

UsageQuantity MUST exist in billing data. The column MUST be a numeric value. When [ChargeCategory](#chargecategory) is "Usage" or "Purchase", UsageQuantity MUST NOT be null or empty. When ChargeType is "Adjustment" and the adjustment applies to specific charges that had a common UsageUnit, UsageQuantity MUST NOT be null. 

## Column ID

UsageQuantity

## Display name

Usage Quantity

## Description

The number of units of a resource or service that was used or consumed based on the [UsageUnit](#usageunit)

## Content constraints

| Constraint      | Value        |
|-----------------|--------------|
| Column required | True         |
| Data type       | Numeric      |
| Allows nulls    | True         |
| Value format    | Numeric value |

## Introduced (version)

1.0
