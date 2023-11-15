# Usage Unit

Usage Unit represents the units of a given [*resource*](#glossary:resource) or [*service*](#glossary:service) used or purchased in combination with [Usage Quantity](#usagequantity). Usage Unit is often listed at a finer granularity or over a different time interval when compared to the [Pricing Unit](#pricingunit) (complementary to [Pricing Quantity](#pricingquantity)), and focuses on *resource* and *service* consumption, not pricing and cost.

The UsageUnit column MUST be present in the billing data. This column MUST be of type String and MUST NOT contain null values when the [ChargeCategory](#chargecategory) is "Usage". Units of measure used in UsageUnit SHOULD adhere to the values and format requirements specified in the [UnitFormat](#unitformat) attribute. The UsageUnit column MUST NOT be used as the basis for determining values related to any pricing or cost metric.

## Column ID

UsageUnit

## Display name

Usage Unit

## Description

Units of a given *resource* or *service* used or purchased in combination with [Usage Quantity](#usagequantity).

## Content constraints

|    Constraint   |      Value      |
|:----------------|:----------------|
| Column type     | Metric          |
| Column required | True            |
| Allows nulls    | True            |
| Data type       | String          |
| Value format    | [Unit Format](#unitformat) recommended |

## Introduced (version)

1.0
