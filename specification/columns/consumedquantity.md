# Consumed Quantity

The Consumed Quantity represents the volume of a given SKU associated with a [*resource*](#glossary:resource) or [*service*](#glossary:service) used, based on the [Consumed Unit](#consumedunit). Consumed Quantity is often derived at a finer granularity or over a different time interval when compared to the [Pricing Quantity](#pricingquantity) (complementary to [Pricing Unit](#pricingunit)) and focuses on *resource* and *service* consumption, not pricing and cost.

The ConsumedQuantity column adheres to the following requirements:

* ConsumedQuantity MUST be present in a FOCUS dataset when the provider supports the measurement of usage.
* ConsumedQuantity MUST be of type Decimal and MUST conform to [Numeric Format](#numericformat) requirements.
* If [ChargeCategory](#chargecategory) is "Usage" and [CommitmentDiscountStatus](#commitmentdiscountstatus) is not "Unused", the following applies:
  * ConsumedQuantity MUST NOT be null and MUST be a valid positive decimal value if [ChargeClass](#chargeclass) is not "Correction".
  * ConsumedQuantity MAY be null or any valid decimal value if [ChargeClass](#chargeclass) is "Correction".
* ConsumedQuantity MUST be null in all other cases.

## Column ID

ConsumedQuantity

## Display Name

Consumed Quantity

## Description

The volume of a given SKU associated with a *resource* or *service* used, based on the Consumed Unit.

## Content constraints

| Constraint      | Value         |
|:----------------|:--------------|
| Column type     | Metric        |
| Feature level   | Conditional   |
| Allows nulls    | True          |
| Data type       | Decimal       |
| Value format    | [Numeric Format](#numericformat) |
| Number range    | Any valid decimal value |

## Introduced (version)

1.0
