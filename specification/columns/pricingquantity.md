# Pricing Quantity

The Pricing Quantity represents the volume of a given SKU associated with a [*resource*](#glossary:resource) or [*service*](#glossary:service) used or purchased, based on the [Pricing Unit](#pricingunit). Distinct from [Usage Quantity](#usagequantity) (complementary to [Usage Unit](#usageunit)), it focuses on pricing and cost, not *resource* and *service* consumption.

The PricingQuantity column MUST be present in the billing data. This column MUST be of type Decimal and MUST conform to [Numeric Format](#numericformat) requirements. The value MAY be negative in cases where [ChargeSubcategory](#chargesubcategory) is "Refund". This column MUST NOT be null if [ChargeCategory](#chargecategory) is "Usage" or "Purchase" and MAY be null for other ChargeCategory values. When unit prices are not null, multiplying PricingQuantity by a unit price MUST produce a result equal to the corresponding cost metric.

## Column ID

PricingQuantity

## Display Name

Pricing Quantity

## Description

The volume of a given SKU associated with a *resource* or *service* used or purchased, based on the Pricing Unit.

## Content constraints

|    Constraint   |      Value                |
|:----------------|:--------------------------|
| Column type     | Metric                    |
| Allows nulls    | True                      |
| Data type       | Decimal                   |
| Value format    | [Numeric Format](#numericformat) |
| Number Range    | Any valid decimal value   |

## Introduced (version)

1.0
