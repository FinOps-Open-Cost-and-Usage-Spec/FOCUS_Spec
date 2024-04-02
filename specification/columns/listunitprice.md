# List Unit Price

The List Unit Price represents the suggested provider-published unit price for a single [Pricing Unit](#pricingunit) of the associated SKU, exclusive of any discounts. This price is denominated in the [Billing Currency](#billingcurrency). The List Unit Price is commonly used for calculating savings based on various rate optimization activities.

The ListUnitPrice column SHOULD be present in the billing data when the provider publishes unit prices exclusive of discounts. This column MUST be a Decimal within the range of non-negative decimal values, MUST conform to [Numeric Format](#numericformat) requirements, and be denominated in the BillingCurrency. When ListUnitPrice is present, it MUST NOT be null if [ChargeCategory](#chargecategory) is "Usage" or "Purchase" and MAY be null for other ChargeCategory values. When ListUnitPrice is not null, multiplying ListUnitPrice by [PricingQuantity](#pricingquantity) MUST equal [ListCost](#listcost).

## Column ID

ListUnitPrice

## Display Name

List Unit Price

## Description

The suggested provider-published unit price for a single Pricing Unit of the associated SKU, exclusive of any discounts.

## Content Constraints

| Constraint      | Value                                |
|:----------------|:-------------------------------------|
| Column type     | Metric                               |
| Feature Level   | Conditional                          |
| Allows nulls    | True                                 |
| Data type       | Decimal                              |
| Value format    | [Numeric Format](#numericformat)     |
| Number range    | Any valid non-negative decimal value |

## Introduced (version)

1.0
