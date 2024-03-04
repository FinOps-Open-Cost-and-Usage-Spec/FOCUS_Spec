# List Unit Price

The List Unit Price represents the suggested provider-published unit price for a single [Pricing Unit](#pricingunit) of the associated SKU, exclusive of any discounts. This price is denominated in the [Billing Currency](#billingcurrency). The List Unit Price is commonly used for calculating savings based on various rate optimization activities.

The ListUnitPrice column MUST be present in the billing data when the provider publishes unit prices exclusive of discounts. This column MUST be a Decimal within the range of non-negative decimal values, MUST conform to [Numeric Format](#numericformat), and be denominated in the BillingCurrency. ListUnitPrice MUST NOT be null if [SkuPriceId](#skupriceid) is not null and MUST be null if SkuPriceId is null. When ListUnitPrice is not null, multiplying ListUnitPrice by [PricingQuantity](#pricingquantity) MUST equal [ListCost](#listcost).

## Column ID

ListUnitPrice

## Display name

List Unit Price

## Description

The suggested provider-published unit price for a single Pricing Unit of the associated SKU, exclusive of any discounts.

## Content Constraints

| Constraint      | Value                                |
|:----------------|:-------------------------------------|
| Column type     | Metric                               |
| FOCUS Essential | False                                |
| Allows nulls    | True                                 |
| Data type       | Decimal                              |
| Value format    | [Numeric Format](#numericformat)     |
| Number range    | Any valid non-negative decimal value |

## Introduced (version)

1.0
