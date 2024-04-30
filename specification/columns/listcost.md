# List Cost

List Cost represents the cost calculated by multiplying the [*list unit price*](#glossary:list-unit-price) and the corresponding [Pricing Quantity](#pricingquantity). List Cost is denominated in the [Billing Currency](#billingcurrency) and is commonly used for calculating savings based on various rate optimization activities, by comparing it with [Contracted Cost](#contractedcost), [Billed Cost](#billedcost) and [Effective Cost](#effectivecost).

When aggregating for savings calculations, it's important to exclude one-time or recurring charges that are paid to cover future eligible charges or the covered charges themselves. This exclusion helps prevent double counting of these charges in the aggregation. For instance, charges categorized as [ChargeCategory](#chargecategory) "Purchase" and their related [ChargeCategory](#chargecategory) "Tax" charges for a [Commitment-Based Discount](#glossary:commitment-based-discount) might be excluded from an accrual-basis cost aggregation of List Cost. This is because the "Usage" and "Tax" charge records provided during the term of the commitment discount already specify the List Cost.

The ListCost column MUST be present in the billing data and MUST NOT be null. This column MUST be of type Decimal, MUST conform to [Numeric Format](#numericformat) requirements, and be denominated in the BillingCurrency. When [ListUnitPrice](#listunitprice) is present and not null, multiplying the ListUnitPrice by PricingQuantity MUST produce the ListCost, except in cases of [ChargeClass](#chargeclass) "Correction", which may address PricingQuantity or any cost discrepancies independently.

In cases where the ListUnitPrice is present and is null, the following applies:

* The ListCost of a charge calculated based on other charges (e.g., when the [ChargeCategory](#chargecategory) is "Tax") MUST be calculated based on the ListCost of those related charges.
* The ListCost of a charge unrelated to other charges (e.g., when the [ChargeCategory](#chargecategory) is "Credit") MUST match the [BilledCost](#billedcost).

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

1.0-preview
