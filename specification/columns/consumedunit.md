# Consumed Unit

The Consumed Unit represents a provider-specified measurement unit indicating how a provider measures usage of a given SKU associated with a metered [*resource*](#glossary:resource) or [*service*](#glossary:service). Consumed Unit complements the [Consumed Quantity](#consumedquantity) metric. It is often listed at a finer granularity or over a different time interval when compared to [Pricing Unit](#pricingunit) (complementary to [Pricing Quantity](#pricingquantity)), and focuses on metered *resource* and *service* consumption, not pricing and cost.

ConsumedUnit MUST be present in a FOCUS dataset when the provider supports the measurement of usage. This column MUST be null when [ChargeCategory](#chargecategory) is not "Usage", or *ChargeCategory* is "Usage" and [*CommitmentDiscountStatus*](#commitmentdiscountstatus) is "Unused". This column MUST NOT be null if *ChargeCategory* is "Usage" and [ChargeClass](#chargeclass) is not "Correction". This column MUST be of type String, units of measure used in ConsumedUnit SHOULD adhere to the values and format requirements specified in the [UnitFormat](#unitformat) attribute, and MUST NOT be used to determine values related to any pricing or cost metrics.

## Column ID

ConsumedUnit

## Display Name

Consumed Unit

## Description

Provider-specified measurement unit indicating how a provider measures usage of a given SKU associated with a metered *resource* or *service*.

## Content constraints

|    Constraint   |      Value      |
|:----------------|:----------------|
| Column type     | Dimension       |
| Feature level   | Conditional     |
| Allows nulls    | True            |
| Data type       | String          |
| Value format    | [Unit Format](#unitformat) recommended |

## Introduced (version)

1.0
