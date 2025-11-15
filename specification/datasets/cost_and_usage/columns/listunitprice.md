# List Unit Price

The List Unit Price represents the suggested service-provider-published unit price for a single [Pricing Unit](#pricingunit) of the associated SKU, exclusive of any discounts. This price is denominated in the [Billing Currency](#billingcurrency). The List Unit Price is commonly used for calculating savings based on various rate optimization activities.

## Requirements

ListUnitPrice adheres to the following requirements:

* ListUnitPrice MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider publishes unit prices exclusive of discounts.
* ListUnitPrice MUST be of type Decimal.
* ListUnitPrice MUST conform to [NumericFormat](#numericformat) requirements.
* ListUnitPrice nullability is defined as follows:
  * ListUnitPrice MUST be null when [SkuPriceId](#skupriceid) is null.
  * ListUnitPrice MUST be null when [ChargeCategory](#chargecategory) is "Tax".
  * ListUnitPrice MUST NOT be null when [SkuPriceId](#skupriceid) is not null.
  * ListUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
  * ListUnitPrice MAY be null in all other cases.
* When ListUnitPrice is not null, ListUnitPrice adheres to the following additional requirements:
  * ListUnitPrice MUST be a non-negative decimal value.
  * ListUnitPrice MUST be denominated in the BillingCurrency.
* [ListCost](#listcost) MUST equal the product of ListUnitPrice and [PricingQuantity](#pricingquantity) when ListUnitPrice is not null and PricingQuantity is not null.

## Column ID

ListUnitPrice

## Display Name

List Unit Price

## Description

The suggested service-provider-published unit price for a single Pricing Unit of the associated SKU, exclusive of any discounts.

## Usability Constraints

**Aggregation:** Column values should only be viewed in the context of their row and not aggregated to produce a total.

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
