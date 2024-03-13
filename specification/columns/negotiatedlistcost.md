# Negotiated List Cost

Negotiated List Cost represents the cost calculated by multiplying [Negotiated List Unit Price](#negotiatedlistunitprice) and the corresponding [Pricing Quantity](#pricingquantity). Negotiated List Cost is denominated in the [Billing Currency](#billingcurrency) and is commonly used for calculating savings based on negotiation activities, by comparing it with [List Cost](#listcost). If negotiated discounts are not applicable, the Negotiated List Cost defaults to the List Cost.

The NegotiatedListCost column MUST be present in the billing data and MUST NOT be null. This column MUST be of type Decimal, MUST conform to [Numeric Format](#numericformat), and be denominated in the BillingCurrency. When a NegotiatedListUnitPrice is not null, multiplying the NegotiatedListUnitPrice by PricingQuantity MUST produce the NegotiatedListCost.

In cases where the NegotiatedListUnitPrice is null, the following applies:

* The NegotiatedListCost MUST be calculated based on the NegotiatedListCost of the related charges if the charge is calculated based on other charges (e.g. [ChargeCategory](#chargecategory) is "Tax").
* The NegotiatedListCost MUST match the [BilledCost](#billedcost) if the charge is unrelated to other charges (e.g. [ChargeSubcategory](#chargesubcategory) is "Credit").

## Column ID

NegotiatedListCost

## Display name

Negotiated List Cost

## Description

Cost calculated by multiplying Negotiated List Unit Price and the corresponding Pricing Quantity.

## Content Constraints

| Constraint      | Value                   |
|:----------------|:------------------------|
| Column type     | Metric                  |
| Column required | True                    |
| Allows nulls    | False                   |
| Data type       | Decimal                 |
| Value format    | [Numeric Format](#numericformat) |
| Number range    | Any valid decimal value |

## Introduced (version)

1.0
