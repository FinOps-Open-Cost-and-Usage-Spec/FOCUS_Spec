# Consumed Unit

The Consumed Unit represents a service-provider-specified measurement unit indicating how a service provider measures usage of a metered SKU associated with a [*resource*](#glossary:resource) or [*service*](#glossary:service). Consumed Unit complements the [Consumed Quantity](#datasets.costandusage.consumedquantity) metric. It is often listed at a finer granularity or over a different time interval when compared to [Pricing Unit](#datasets.costandusage.pricingunit) (complementary to [Pricing Quantity](#datasets.costandusage.pricingquantity)), and focuses on *resource* and *service* consumption, not pricing and cost.

## Requirements

ConsumedUnit MUST adhere to the following requirements:

* ConsumedUnit MUST be of type String.
* ConsumedUnit MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* ConsumedUnit SHOULD conform to [UnitFormat](#attributes.unitformat) requirements.
* ConsumedUnit MUST adhere to the following nullability requirements:
  * ConsumedUnit MUST be null when ConsumedQuantity is null.
  * ConsumedUnit MUST NOT be null when ConsumedQuantity is not null.

## Column ID

ConsumedUnit

## Display Name

Consumed Unit

## Description

Service-provider-specified measurement unit indicating how a service provider measures usage of a metered SKU associated with a *resource* or *service*.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [Cost and Usage](#datasets.costandusage)             |
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | [Unit Format](#attributes.unitformat) recommended    |

## Version Introduced

1.0
