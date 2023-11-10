# List Cost

List Cost represents the cost calculated based on [List Unit Price](#listunitprice) and the corresponding [Pricing Quantity](#pricingquantity). List cost is denominated in the [Billing Currency](#billingcurrency) and is used for calculating savings based on various rate optimization activities, by comparing it with [Effective Cost](#effectivecost).

The ListCost column MUST be present in the billing data. This column MUST be a valid numeric value of type Decimal, denominated in the BillingCurrency, and MUST NOT contain null values. When a ListUnitPrice is not null, multiplying the ListUnitPrice by PricingQuantity MUST produce the ListCost.

In cases where the ListUnitPrice is null, the following applies:
* If the charge is calculated based on other charges (e.g. [ChargeCategory](#chargecategory) is 'Tax'), the ListCost MUST be calculated based on the ListCost of the related charges.
* If the charge is unrelated to other charges (e.g. [ChargeSubcategory](#chargesubcategory) is 'Credit'), the ListCost MUST match the BilledCost.

## Column ID

ListCost

## Display name

List Cost

## Description

Cost calculated based on List Unit Price and the corresponding Pricing Quantity.

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
