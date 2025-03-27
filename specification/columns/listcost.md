# List Cost

List Cost represents the cost calculated by multiplying the [*list unit price*](#glossary:list-unit-price) and the corresponding [Pricing Quantity](#pricingquantity). List Cost is denominated in the [Billing Currency](#billingcurrency) and is commonly used for calculating savings based on various rate optimization activities, by comparing it with [Contracted Cost](#contractedcost), [Billed Cost](#billedcost) and [Effective Cost](#effectivecost).

The ListCost column adheres to the following requirements:

* The ListCost column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) and MUST NOT be null.
* This column MUST be of type Decimal, MUST conform to [Numeric Format](#numericformat) requirements, and be denominated in the BillingCurrency.
* When [ListUnitPrice](#listunitprice) is present and not null, multiplying the ListUnitPrice by PricingQuantity MUST produce the ListCost, except in cases of [ChargeClass](#chargeclass) "Correction", which may address PricingQuantity or any cost discrepancies independently.

In cases where the ListUnitPrice is present and is null, the following applies:

* The ListCost of a charge calculated based on other charges (e.g., when the [ChargeCategory](#chargecategory) is "Tax") MUST be calculated based on the ListCost of those related charges.
* The ListCost of a charge unrelated to other charges (e.g., when the [ChargeCategory](#chargecategory) is "Credit") MUST match the [BilledCost](#billedcost).

## Column ID

ListCost

## Display Name

List Cost

## Description

Cost calculated by multiplying List Unit Price and the corresponding Pricing Quantity.

## Usability Constraints

### Aggregation

When aggregating List Cost for savings calculations, it's important to exclude certain types of charges to avoid double counting. Specifically, principal charges (defined as the original charge that is amortized over time across multiple other charges, with the [Amortization Class](#amortizationclass) set to "Principal") or amortized charges (representing the results of amortization from a previous charge, with the Amortization Class set to "Amortized Charge"). Both of these charges specify List Cost, so including both would lead to double counting. Which Amortization Class to exclude depends on how costs are aggregated - for billed basis aggregation, exclude amortized charges (i.e., Amortization Class "Amortized Charge"), and for accrual basis aggregation, exclude principal charges (i.e., Amortization Class "Principal").

In the case of a [commitment discount](#glossary:commitment-discount), principal charges typically refer to Charge Category "Purchase" charges (both one-time and recurring) that are paid to cover future eligible charges, along with their related Charge Category "Tax" charges. Amortized charges, on the other hand, correspond to Charge Category "Usage" records that are covered by these purchases.

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
