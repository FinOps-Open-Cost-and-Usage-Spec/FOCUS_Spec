# Usage Quantity

The Usage Quantity represents the volume of a given SKU associated with a [*resource*](#glossary:resource) or [*service*](#glossary:service) used or purchased, based on the [Usage Unit](#usageunit). Usage Quantity is often derived at a finer granularity or over a different time interval when compared to the [Pricing Quantity](#pricingquantity) (complementary to [Pricing Unit](#pricingunit)) and focuses on *resource* and *service* consumption, not pricing and cost.

UsageQuantity column SHOULD be present in the billing data when the provider supports the measurement of usage. This column MUST be of type Decimal and MUST conform to [Numeric Format](#numericformat) requirements. The value MAY be negative in cases where [ChargeSubcategory](#chargesubcategory) is "Refund". This column MUST NOT be null if [ChargeCategory](#chargecategory) is "Usage" or "Purchase" and MAY be null for other ChargeCategory values.

## Column ID

UsageQuantity

## Display Name

Usage Quantity

## Description

The volume of a given SKU associated with a *resource* or *service* used or purchased, based on the Usage Unit.

## Content constraints

| Constraint      | Value         |
|:----------------|:--------------|
| Column type     | Metric        |
| Feature Level   | Conditional   |
| Allows nulls    | True          |
| Data type       | Decimal       |
| Value format    | [Numeric Format](#numericformat) |
| Number range    | Any valid decimal value |

## Introduced (version)

1.0
