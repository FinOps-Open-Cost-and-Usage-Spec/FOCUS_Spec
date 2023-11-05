# List Unit Price

The List Unit Price represents a suggested provider-published unit price for a single pricing measurement unit (identified by a [Sku Price Id](#skupriceid)), which incorporates free-tier, volume/tier-based, BYOL-based and dynamically priced SKU rates, while excluding any other discounts or the amortization of upfront charges (one-time or recurring). This price is denominated in the [Billing Currency](#billingcurrency). The List Unit Price can be used for calculating savings based on rate optimization activities. In this context, activities such as increased consumption leading to lower volume/tier-based rates, the use of pre-owned software licenses (BYOL - Bring Your Own License), leveraging interruptible resources and/or services, or optimizing usage to take advantage of dynamic pricing models are not considered rate optimization activities.

The ListUnitPrice column MUST be present in the billing data. This column MUST be a numeric value of type Decimal within the range of non-negative decimal values. It MUST NOT contain null if SkuPriceId is not null and it MUST be null if SkuPriceId is null. When ListUnitPrice is not null, multiplying ListUnitPrice by [QuantityInPricingUnit](#quantityinpricingunit) MUST equal [ListCost](#listcost).

## Column ID

ListUnitPrice

## Display name

List Unit Price

## Description

A suggested provider-published unit price for a single pricing measurement unit (identified by a [Sku Price Id](#skupriceid)), which incorporates free-tier, volume/tier-based, BYOL-based and dynamically priced SKU rates, while excluding any other discounts or the amortization of upfront charges (one-time or recurring).

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
