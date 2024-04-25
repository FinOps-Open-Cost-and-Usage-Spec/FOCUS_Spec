# List Unit Price

The List Unit Price represents the suggested provider-published unit price for a single [Pricing Unit](#pricingunit) of the associated SKU, exclusive of any discounts. This price is denominated in the [Billing Currency](#billingcurrency). The List Unit Price is commonly used for calculating savings based on various rate optimization activities.

The ListUnitPrice column MUST be present in the billing data when the provider publishes unit prices exclusive of discounts. This column MUST be a Decimal within the range of non-negative decimal values, MUST conform to [Numeric Format](#numericformat) requirements, and be denominated in the BillingCurrency. It MUST NOT be null when [ChargeClass](#chargeclass) is "Standard" and [ChargeCategory](#chargecategory) is "Usage" or "Purchase", MUST be null when ChargeCategory is "Tax", and MAY be null for all other combinations of ChargeClass and ChargeCategory. When ListUnitPrice is present and is not null, multiplying ListUnitPrice by [PricingQuantity](#pricingquantity) MUST equal [ListCost](#listcost), except in cases of ChargeClass "Correction", which MAY address PricingQuantity or any cost discrepancies independently.

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
| Feature level   | Conditional                          |
| Allows nulls    | True                                 |
| Data type       | Decimal                              |
| Value format    | [Numeric Format](#numericformat)     |
| Number range    | Any valid non-negative decimal value |

## Introduced (version)

1.0-preview
