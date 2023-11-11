# List Unit Price

The List Unit Price represents the suggested provider-published unit price for a single [Pricing Unit](#pricingunit) of the associated SKU, exclusive of any discounts. This price is denominated in the [Billing Currency](#billingcurrency). The List Unit Price can be used for calculating savings based on various rate optimization activities.

The ListUnitPrice column MUST be present in the billing data. This column MUST be a numeric value of type Decimal within the range of non-negative decimal values and denominated in the BillingCurrency. ListUnitPrice MUST NOT be null or empty if [SkuPriceId](#skupriceid) is not null and MUST be null if SkuPriceId is null. When ListUnitPrice is not null, multiplying ListUnitPrice by [PricingQuantity](#pricingquantity) MUST equal [ListCost](#listcost).

## Column ID

ListUnitPrice

## Display name

List Unit Price

## Description

The suggested provider-published unit price for a single [Pricing Unit](#pricingunit) of the associated SKU, exclusive of any discounts.

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
