# Pricing Quantity

The Pricing Quantity represents the volume of a given resource and/or service used or purchased based on the [Pricing Unit](#pricingunit). Distinct from [Usage Quantity](#usagequantity) (complementary to [Usage Unit](#usageunit)), it focuses on pricing and cost, not resource and service consumption.

PricingQuantity MUST be present in the billing data. This column MUST be a numeric value of type Decimal. The value MAY be negative in cases where [AdjustmentType](#chargesubcategory) is 'Refund'. This column MUST NOT be null where unit prices are not null and MUST be null if unit prices are null. When unit prices are not null, multiplying PricingQuantity by a unit price MUST produce a result equal to the corresponding cost metric.

## Column ID

PricingQuantity

## Display name

Pricing Quantity

## Description

The volume of a given resource and/or service used or purchased based on the Pricing Unit.

## Content constraints

|    Constraint   |      Value                |
|:----------------|:--------------------------|
| Column required | True                      |
| Data type       | Decimal                   |
| Allows nulls    | True                      |
| Value format    | Numeric value             |
| Number Range    | Any valid decimal value   |

## Introduced (version)

1.0
