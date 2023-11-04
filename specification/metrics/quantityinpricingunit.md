# Quantity in Pricing Unit

The Quantity in Pricing Unit represents the volume of a given resource and/or service used or purchased based on the [Pricing Unit](#pricingunit). It pertains to pricing and cost, and should not be confused with the [Quantity In Usage Unit](#quantityinusageunit), which is complementary to [Usage Unit](#usageunit) and intended for tracking resource and service consumption.

The QuantityInPricingUnit column MUST be present in the billing data. This column MUST be a numeric value of type Decimal. The value MAY be negative in cases where [ChargeType](#chargetype) is 'Adjustment'. This column MUST NOT contain null values where unit prices are not null. When unit prices are not null, multiplying QuantityInPricingUnit by a unit price MUST produce a result equal to the corresponding cost metric.

## Column ID

QuantityInPricingUnit

## Display name

Quantity In Pricing Unit

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
