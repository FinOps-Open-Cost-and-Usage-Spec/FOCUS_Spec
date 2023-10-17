# Quantity in Pricing Unit

The Quantity in Pricing Unit represents the volume of a given resource and/or service used or purchased based on the [PricingUnit](#pricingunit). This quantity value is used to calculate cost (List, Billed & Effective costs) when multiplied by the associated unit price metric. 

The QuantityInPricingUnit column MUST be present in the billing data. This column MUST be a numeric value of type Decimal. The value MAY be negative in case of adjustments. This column MUST NOT contain null values where unit prices are not null. When unit prices are not null, multiplying [QuantityInPricingUnit](#quantityinpricingunit) by a unit price’ MUST produce a result equal to the corresponding cost metric.

## Column ID

QuantityInPricingUnit

## Display name

Quantity In Pricing Unit

## Description

The volume of a given resource and/or service used or purchased based on the [PricingUnit](#pricingunit).

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
