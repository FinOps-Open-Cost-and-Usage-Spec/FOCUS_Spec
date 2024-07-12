# Consumed Quantity

The Consumed Quantity represents the volume of a given SKU associated with a [*resource*](#glossary:resource) or [*service*](#glossary:service) used, based on the [Consumed Unit](#consumedunit). Consumed Quantity is often derived at a finer granularity or over a different time interval when compared to the [Pricing Quantity](#pricingquantity) (complementary to [Pricing Unit](#pricingunit)) and focuses on *resource* and *service* consumption, not pricing and cost.

The ConsumedQuantity column adheres to the following requirements:

* ConsumedQuantity MUST be present in the billing data when the provider supports the measurement of usage.
* ConsumedQuantity MUST be of type Decimal and MUST conform to [Numeric Format](#numericformat) requirements.
* ConsumedQuantity MUST NOT be null if [ChargeCategory](#chargecategory) is "Usage", unless [ChargeClass](#chargeclass) is "Correction" or [CommitmentDiscountStatus](#commitmentdiscountstatus) is "Unused".
* ConsumedQuantity MAY be null if ChargeCategory is "Usage" and ChargeClass is "Correction"
* ConsumedQuantity MUST be null if CommitmentDiscountStatus is "Unused" or for other ChargeCategory values.
* ConsumedQuantity value MAY be negative in cases where ChargeClass is "Correction".

The ConsumedQuantity column MUST NOT be used to determine values related to any pricing or cost metrics.

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
