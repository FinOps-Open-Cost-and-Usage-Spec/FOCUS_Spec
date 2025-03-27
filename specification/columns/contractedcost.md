# Contracted Cost

Contracted Cost represents the cost calculated by multiplying [*contracted unit price*](#glossary:contracted-unit-price) and the corresponding [Pricing Quantity](#pricingquantity). Contracted Cost is denominated in the [Billing Currency](#billingcurrency) and is commonly used for calculating savings based on negotiation activities, by comparing it with [List Cost](#listcost). If [*negotiated discounts*](#glossary:negotiated-discount) are not applicable, the Contracted Cost defaults to the List Cost.

The ContractedCost column adheres to the following requirements:

* The ContractedCost column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) and MUST NOT be null.
* This column MUST be of type Decimal, MUST conform to [Numeric Format](#numericformat) requirements, and be denominated in the BillingCurrency.
* When [ContractedUnitPrice](#contractedunitprice) is present and not null, multiplying the ContractedUnitPrice by PricingQuantity MUST produce the ContractedCost, except in cases of [ChargeClass](#chargeclass) "Correction", which may address PricingQuantity or any cost discrepancies independently.

In cases where the ContractedUnitPrice is present and null, the following applies:

* The ContractedCost of a charge calculated based on other charges (e.g., when the [ChargeCategory](#chargecategory) is "Tax") MUST be calculated based on the ContractedCost of those related charges.
* The ContractedCost of a charge unrelated to other charges (e.g., when the [ChargeCategory](#chargecategory) is "Credit") MUST match the [BilledCost](#billedcost).

## Column ID

ContractedCost

## Display Name

Contracted Cost

## Description

Cost calculated by multiplying *contracted unit price* and the corresponding Pricing Quantity.

## Usability Constraints

### Aggregation

When aggregating Contracted Cost for savings calculations, it's important to exclude certain types of charges to avoid double counting. Specifically, principal charges (defined as the original charge that is amortized over time across multiple other charges, with the [Amortization Class](#amortizationclass) set to "Principal") or amortized charges (representing the results of amortization from a previous charge, with the Amortization Class set to "Amortized Charge"). Both of these charges specify Contracted Cost, so including both would lead to double counting. Which Amortization Class to exclude depends on how costs are aggregated - for billed basis aggregation, exclude amortized charges (i.e., Amortization Class "Amortized Charge"), and for accrual basis aggregation, exclude principal charges (i.e., Amortization Class "Principal").

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

1.0
