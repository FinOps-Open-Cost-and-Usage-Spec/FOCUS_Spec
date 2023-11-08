# List Cost

The List Cost represents a suggested provider-published cost inclusive of the impacts of free-tier, volume/tier-based, BYOL-based SKU rates, while excluding any other discounts or the amortization of upfront charges (one-time or recurring). List cost is denominated in the [Billing Currency](#billingcurrency) and is used for calculating savings based on various rate optimization activities, by comparing it with [Effective Cost](#effectivecost).

The ListCost column MUST be present in the billing data. This column MUST be a valid numeric value of type Decimal, denominated in the BillingCurrency,and MUST NOT contain null values. When a [ListUnitPrice](#listunitprice) is not null, multiplying the ListUnitPrice by [PricingQuantity](#pricingquantity) MUST produce the ListCost.

In cases where the ListUnitPrice is null, the following applies:

* If the line item is based on other charges (e.g. [ChargeCategory](#chargecategory) is 'Tax'), the ListCost MUST be calculated based on ListCost of the related charges
* If the line item is unrelated to other charges (e.g. [ChargeSubcategory](#chargesubcategory) is 'Credit'), the ListCost MUST match the BilledCost.

## Column ID

ListCost

## Display name

List Cost

## Description

A charge inclusive of the impacts of free-tier, volume/tier-based, BYOL-based and dynamically priced SKU rates, while excluding any other discounts or the amortization of upfront charges (one-time or recurring).

## Content Constraints

| Constraint      | Value                   |
|:----------------|:------------------------|
| Column required | True                    |
| Data type       | Decimal                 |
| Allows nulls    | False                   |
| Value format    | Numeric value           |
| Number range    | Any valid decimal value |

## Introduced (version)

1.0
