# Consumed Quantity

The Consumed Quantity represents the volume of a given SKU associated with a metered [*resource*](#glossary:resource) or [*service*](#glossary:service) used, based on the [Consumed Unit](#consumedunit). Consumed Quantity is often derived at a finer granularity or over a different time interval when compared to the [Pricing Quantity](#pricingquantity) (complementary to [Pricing Unit](#pricingunit)) and focuses on metered *resource* and *service* consumption, not pricing and cost.

ConsumedQuantity MUST be present in a FOCUS dataset when the provider supports the measurement of usage. This column MUST be null when [ChargeCategory](#chargecategory) is not "Usage", or [ChargeCategory](#chargecategory) is "Usage" and CommitmentDiscountStatus](#commitmentdiscountstatus) is "Unused". This column MUST NOT be null if [ChargeCategory](#chargecategory) is "Usage" and [ChargeClass](#chargeclass) is not "Correction". This column MUST be of type Decimal and MUST conform to [Numeric Format](#numericformat) requirements. The value MAY be negative in cases where [ChargeClass](#chargeclass) is "Correction".

## Column ID

ConsumedQuantity

## Display Name

Consumed Quantity

## Description

The volume of a given SKU associated with a metered *resource* or *service* used, based on the Consumed Unit.

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
