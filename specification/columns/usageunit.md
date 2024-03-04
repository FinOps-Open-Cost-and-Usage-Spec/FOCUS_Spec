# Usage Unit

The Usage Unit represents a provider-specified measurement unit indicating how a provider measures usage or purchase of a given SKU associated with a [*resource*](#glossary:resource) or [*service*](#glossary:service). Usage Unit complements the [Usage Quantity](#usagequantity) metric. It is often listed at a finer granularity or over a different time interval when compared to the [Pricing Unit](#pricingunit) (complementary to [Pricing Quantity](#pricingquantity)), and focuses on *resource* and *service* consumption, not pricing and cost.

The UsageUnit column MUST be present in the billing data when the provider supports the measurement of usage. This column MUST be of type String. UsageUnit MUST NOT be null if [SkuPriceId](#skupriceid) is not null and MUST be null if SkuPriceId is null. Units of measure used in UsageUnit SHOULD adhere to the values and format requirements specified in the [UnitFormat](#unitformat) attribute. The UsageUnit column MUST NOT be used to determine values related to any pricing or cost metrics.

## Column ID

UsageUnit

## Display name

Usage Unit

## Description

Provider-specified measurement unit indicating how a provider measures usage or purchase of a given SKU associated with a *resource* or *service*.

## Content constraints

|    Constraint   |      Value      |
|:----------------|:----------------|
| Column type     | Metric          |
| FOCUS Essential | False           |
| Allows nulls    | True            |
| Data type       | String          |
| Value format    | [Unit Format](#unitformat) recommended |

## Introduced (version)

1.0
