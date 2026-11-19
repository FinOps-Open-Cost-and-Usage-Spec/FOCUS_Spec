# Consumed Unit

The [Consumed Unit](#col) represents a service-provider-specified measurement unit indicating how a service provider measures usage of a metered SKU associated with a [resource](#term) or [service](#term). [Consumed Unit](#col) complements the [Consumed Quantity](#col) metric. It is often listed at a finer granularity or over a different time interval when compared to [Pricing Unit](#col) (complementary to [Pricing Quantity](#col)), and focuses on [resource](#term) and [service](#term) consumption, not pricing and cost.

## Requirements

[ConsumedUnit](#col) MUST adhere to the following requirements:

* [ConsumedUnit](#col) MUST be of type String.
* [ConsumedUnit](#col) MUST conform to [StringHandling](#attr) requirements.
* [ConsumedUnit](#col) SHOULD conform to [UnitFormat](#attr) requirements.
* [ConsumedUnit](#col) MUST adhere to the following nullability requirements:
  * [ConsumedUnit](#col) MUST be null when [ConsumedQuantity](#col) is null.
  * [ConsumedUnit](#col) MUST NOT be null when [ConsumedQuantity](#col) is not null.

## Column ID

ConsumedUnit

## Display Name

Consumed Unit

## Description

Service-provider-specified measurement unit indicating how a service provider measures usage of a metered SKU associated with a [resource](#term) or [service](#term).

## Content Constraints

| Constraint                 | Value                                             |
| :------------------------- | :------------------------------------------------ |
| Dataset                    | [Cost and Usage](#ds)                             |
| Operating model conditions | [Includes Usage Measurement](#omc)                                               |
| Column type                | Dimension                                         |
| Feature level              | Conditional                                       |
| Allows nulls               | True                                              |
| Data type                  | String                                            |
| Value format               | [Unit Format](#attr) recommended                  |

## Version Introduced

1.0
