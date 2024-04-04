# List Cost

List Cost represents the cost calculated by multiplying the [*list unit price*](#glossary:list-unit-price) and the corresponding [Pricing Quantity](#pricingquantity). List Cost is denominated in the [Billing Currency](#billingcurrency) and is commonly used for calculating savings based on various rate optimization activities, by comparing it with [Billed Cost](#billedcost) and [Effective Cost](#effectivecost).

The ListCost column MUST be present in the billing data and MUST NOT be null. This column MUST be of type Decimal, MUST conform to [Numeric Format](#numericformat) requirements, and be denominated in the BillingCurrency. Multiplying the *list unit price* by PricingQuantity MUST produce the ListCost.

In cases where the ListUnitPrice is present and is null, the following applies:

* The ListCost MUST be calculated based on the ListCost of the related charges if the charge is calculated based on other charges (e.g. [ChargeCategory](#chargecategory) is "Tax").
* The ListCost MUST match the [BilledCost](#billedcost) if the charge is unrelated to other charges (e.g. [ChargeSubcategory](#chargesubcategory) is "Credit").

## Column ID

ListCost

## Display Name

List Cost

## Description

Cost calculated by multiplying List Unit Price and the corresponding Pricing Quantity.

## Content Constraints

| Constraint      | Value                   |
|:----------------|:------------------------|
| Column type     | Metric                  |
| Feature level   | Mandatory               |
| Allows nulls    | False                   |
| Data type       | Decimal                 |
| Value format    | [Numeric Format](#numericformat) |
| Number range    | Any valid decimal value |

## Introduced (version)

1.0
