# Negotiated List Unit Price

The Negotiated List Unit Price represents the agreed-upon unit price for a single [Pricing Unit](#pricingunit) of the associated SKU, inclusive of negotiated discounts, if present, while excluding negotiated commitment-based discounts or any other discounts. This price is denominated in the [Billing Currency](#billingcurrency). The Negotiated List Unit Price is commonly used for calculating savings based on negotiation activities. If negotiated discounts are not applicable, the Negotiated List Unit Price defaults to the [List Unit Price](#listunitprice).

The NegotiatedListUnitPrice column MUST be present in the billing data when the provider supports negotiated pricing concept. This column MUST be a Decimal within the range of non-negative decimal values, MUST conform to [Numeric Format](#numericformat), and be denominated in the BillingCurrency. NegotiatedListUnitPrice MUST NOT be null if [SkuPriceId](#skupriceid) is not null and MUST be null if SkuPriceId is null. When NegotiatedListUnitPrice is not null, multiplying NegotiatedListUnitPrice by [PricingQuantity](#pricingquantity) MUST equal [NegotiatedListCost](#negotiatedlistcost).

## Column ID

NegotiatedListUnitPrice

## Display name

Negotiated List Unit Price

## Description

The agreed-upon unit price for a single Pricing Unit of the associated SKU, inclusive of negotiated discounts, if present, and exclusive of any other discounts.

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
