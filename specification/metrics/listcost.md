# List Cost

List Cost represents the cost calculated by multiplying [List Unit Price](#listunitprice) and the corresponding [Pricing Quantity](#pricingquantity). List cost is denominated in the [Billing Currency](#billingcurrency) and is used for calculating savings based on various rate optimization activities, by comparing it with [Effective Cost](#effectivecost).

The ListCost column MUST be present in the billing data. This column MUST be a valid numeric value of type Decimal, denominated in the BillingCurrency, and MUST NOT contain null values. When a ListUnitPrice is not null, multiplying the ListUnitPrice by PricingQuantity MUST produce the ListCost.

In cases where the ListUnitPrice is null, the following applies:

* The ListCost MUST be calculated based on the ListCost of the related charges if the charge is calculated based on other charges (e.g. [ChargeType](#chargetype) is 'Tax').
* The ListCost MUST match the BilledCost if the charge is unrelated to other charges (e.g. [AdjustmentType](#adjustmenttype) is 'Credit').

## Column ID

ListCost

## Display name

List Cost

## Description

Cost calculated by multiplyingn List Unit Price and the corresponding Pricing Quantity.

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
