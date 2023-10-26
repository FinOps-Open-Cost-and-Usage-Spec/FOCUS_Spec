# List Unit Price

The List Unit Price represents a suggested provider-published unit price for a single pricing measurement unit (identified by a [Sku Price Id](#skupriceid)), which incorporates volume/tier-based rates while excluding any negotiated or commitment-based discounts. This price is denominated in the [Billing Currency](#billingcurrency). It is used to calculate List Cost and savings based on rate optimization activities.

The ListUnitPrice column MUST be present in the billing data. This column MUST be a numeric value of type Decimal within the range of non-negative decimal values. It MUST NOT contain null if SkuPriceId is not null and it MUST be null if SkuPriceId is null. When ListUnitPrice is not null, multiplying ListUnitPrice by [QuantityInPricingUnit](#quantityinpricingunit) MUST equal [ListCost](#listcost).

## Column ID

ListUnitPrice

## Display name

List Unit Price

## Description

A suggested provider-published unit price for a single pricing measurement unit (identified by a [Sku Price Id](#skupriceid)), which incorporates volume/tier-based rates while excluding any negotiated or commitment-based discounts.

## Content Constraints

| Constraint      | Value                                |
|:----------------|:-------------------------------------|
| Column required | True                                 |
| Data type       | Decimal                              |
| Allows nulls    | True                                 |
| Value format    | Numeric value                        |
| Number range    | Any valid non-negative decimal value |

## Introduced (version)

1.0
