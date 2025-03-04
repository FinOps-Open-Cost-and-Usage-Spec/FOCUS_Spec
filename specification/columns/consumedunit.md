# Consumed Unit

The Consumed Unit represents a provider-specified measurement unit indicating how a provider measures usage of a metered SKU associated with a [*resource*](#glossary:resource) or [*service*](#glossary:service). Consumed Unit complements the [Consumed Quantity](#consumedquantity) metric. It is often listed at a finer granularity or over a different time interval when compared to [Pricing Unit](#pricingunit) (complementary to [Pricing Quantity](#pricingquantity)), and focuses on *resource* and *service* consumption, not pricing and cost.

The ConsumedUnit column adheres to the following requirements:

* ConsumedUnit MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports the measurement of usage.
* ConsumedUnit MUST be of type String.
* ConsumedUnit MUST conform to [StringHandling](#stringhandling) requirements.
* ConsumedUnit SHOULD conform to [UnitFormat](#unitformat) requirements.
* ConsumedUnit nullability is defined as follows:
  * ConsumedUnit MUST be null when [ChargeCategory](#chargecategory) is not "Usage", or when ChargeCategory is "Usage" and [CommitmentDiscountStatus](#commitmentdiscountstatus) is "Unused".
  * When ChargeCategory is "Usage" and CommitmentDiscountStatus is not "Unused", ConsumedUnit adheres to the following additional requirements:
    * ConsumedUnit MUST NOT be null when [ChargeClass](#chargeclass) is not "Correction".
    * ConsumedUnit MAY be null when ChargeClass is "Correction".

## Column ID

ConsumedUnit

## Display Name

Consumed Unit

## Description

Provider-specified measurement unit indicating how a provider measures usage of a metered SKU associated with a *resource* or *service*.

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
