# Contracted Cost

Contracted Cost represents the cost calculated by multiplying [*contracted unit price*](#glossary:contracted-unit-price) and the corresponding [Pricing Quantity](#pricingquantity). Contracted Cost is denominated in the [Billing Currency](#billingcurrency) and is commonly used for calculating savings based on negotiation activities, by comparing it with [List Cost](#listcost). If negotiated discounts are not applicable, the Contracted Cost defaults to the List Cost.

The ContractedCost column MUST be present in the billing data and MUST NOT be null. This column MUST be of type Decimal, MUST conform to [Numeric Format](#numericformat) requirements, and be denominated in the BillingCurrency. When ContractedUnitPrice is present and is not null, multiplying the ContractedUnitPrice by PricingQuantity MUST produce the ContractedCost.

In cases where the ContractedUnitPrice is present and null, the following applies:

* The ContractedCost of a charge calculated based on other charges MUST be calculated based on the ContractedCost of the other related charges (e.g. [ChargeCategory](#chargecategory) is "Tax").
* The ContractedCost MUST match the [BilledCost](#billedcost) if the charge is unrelated to other charges (e.g. [ChargeSubcategory](#chargesubcategory) is "Credit").

## Column ID

ContractedCost

## Display name

Contracted Cost

## Description

Cost calculated by multiplying [*contracted unit price*](#glossary:contracted-unit-price) and the corresponding Pricing Quantity.

## Content Constraints

| Constraint      | Value                   |
|:----------------|:------------------------|
| Column type     | Metric                  |
| FOCUS Essential | True                   |
| Allows nulls    | False                   |
| Data type       | Decimal                 |
| Value format    | [Numeric Format](#numericformat) |
| Number range    | Any valid decimal value |

## Introduced (version)

1.0
