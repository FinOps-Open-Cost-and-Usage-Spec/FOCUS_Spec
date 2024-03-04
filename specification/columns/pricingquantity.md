# Pricing Quantity

The Pricing Quantity represents the volume of a given SKU associated with a [*resource*](#glossary:resource) or [*service*](#glossary:service) used or purchased, based on the [Pricing Unit](#pricingunit). Distinct from [Usage Quantity](#usagequantity) (complementary to [Usage Unit](#usageunit)), it focuses on pricing and cost, not *resource* and *service* consumption.

The PricingQuantity column MUST be present in the billing data. This column MUST be of type Decimal and MUST conform to [Numeric Format](#numericformat). The value MAY be negative in cases where [ChargeSubcategory](#chargesubcategory) is "Refund". This column MUST NOT be null if [SkuPriceId](#skupriceid) is not null and MUST be null if SkuPriceId is null. When unit prices are not null, multiplying PricingQuantity by a unit price MUST produce a result equal to the corresponding cost metric.

## Column ID

PricingQuantity

## Display name

Pricing Quantity

## Description

The volume of a given SKU associated with a *resource* or *service* used or purchased, based on the Pricing Unit.

## Content constraints

|    Constraint   |      Value                |
|:----------------|:--------------------------|
| Column type     | Metric                    |
| FOCUS Essential | True                      |
| Allows nulls    | True                      |
| Data type       | Decimal                   |
| Value format    | [Numeric Format](#numericformat) |
| Number Range    | Any valid decimal value   |

## Introduced (version)

1.0
