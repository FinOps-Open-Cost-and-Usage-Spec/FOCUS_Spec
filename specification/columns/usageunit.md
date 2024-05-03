# Usage Unit

The Usage Unit represents a provider-specified measurement unit indicating how a provider measures usage or purchase of a given SKU associated with a [*resource*](#glossary:resource) or [*service*](#glossary:service). Usage Unit complements the [Usage Quantity](#usagequantity) metric. It is often listed at a finer granularity or over a different time interval when compared to the [Pricing Unit](#pricingunit) (complementary to [Pricing Quantity](#pricingquantity)), and focuses on *resource* and *service* consumption, not pricing and cost.

The UsageUnit column MUST be present in the billing data when the provider supports the measurement of usage. This column MUST be of type String. It MUST NOT be null when [ChargeClass](#chargeclass) is "Original" and [ChargeCategory](#chargecategory) is "Usage" or "Purchase", MUST be null when ChargeCategory is "Tax", and MAY be null for all other combinations of ChargeClass and ChargeCategory. Units of measure used in UsageUnit SHOULD adhere to the values and format requirements specified in the [UnitFormat](#unitformat) attribute. The UsageUnit column MUST NOT be used to determine values related to any pricing or cost metrics.

## Column ID

UsageUnit

## Display Name

Usage Unit

## Description

Provider-specified measurement unit indicating how a provider measures usage or purchase of a given SKU associated with a *resource* or *service*.

## Content constraints

|    Constraint   |      Value      |
|:----------------|:----------------|
| Column type     | Metric          |
| Feature level   | Conditional     |
| Allows nulls    | True            |
| Data type       | String          |
| Value format    | [Unit Format](#unitformat) recommended |

## Introduced (version)

1.0-preview
