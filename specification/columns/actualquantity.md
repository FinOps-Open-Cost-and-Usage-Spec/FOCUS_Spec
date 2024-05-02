# Actual Quantity

The Actual Quantity represents the volume of a given SKU associated with a [*resource*](#glossary:resource) or [*service*](#glossary:service) used or purchased, based on the [Actual Unit](#actualunit). Actual Quantity is often derived at a finer granularity or over a different time interval when compared to the [Pricing Quantity](#pricingquantity) (complementary to [Pricing Unit](#pricingunit)) and focuses on the actual amount of a *resource* or *service* used or purchased, not pricing and cost.

When [ChargeCategory](#chargecategory) is "Purchase":
    The value represents the volume of units purchased of a [*resource*](#glossary:resource) or [*service*](#glossary:service) which may be different from the quantity represented in the [PricingQuantity](#pricingquantity) column or measured in a different unit to that of [PricingUnit](#pricingunit). It should be relevant to any associated  [ChargeCategory](#chargecategory) "Usage" records.

When [ChargeCategory](#chargecategory) is "Usage":
    The measurement represents the actual quantity consumed which may be a different value to the quantity that is charged represented in the [PricingQuantity](#pricingquantity) column or measured in a different unit to that of [pricingunit](#pricingunit).

ActualQuantity column MUST be present in the billing data when the provider supports the measurement of usage or purchases. This column MUST be of type Decimal and MUST conform to [Numeric Format](#numericformat) requirements. The value MAY be negative in cases where [ChargeClass](#chargeclass) is "Correction". This column MUST NOT be null when [ChargeClass](#chargeclass) is "Standard" and [ChargeCategory](#chargecategory) is "Usage" or "Purchase", MUST be null when ChargeCategory is "Tax", and MAY be null for all other combinations of ChargeClass and ChargeCategory.

## Column ID

ActualQuantity

## Display Name

Actual Quantity

## Description

The volume of a given SKU associated with a *resource* or *service* used or purchased, based on the Actual Unit.

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

1.0-preview
