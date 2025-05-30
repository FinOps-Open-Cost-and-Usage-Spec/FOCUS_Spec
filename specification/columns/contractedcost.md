# Contracted Cost

Contracted Cost represents the cost calculated by multiplying [*contracted unit price*](#glossary:contracted-unit-price) and the corresponding [Pricing Quantity](#pricingquantity). Contracted Cost is denominated in the [Billing Currency](#billingcurrency) and is commonly used for calculating savings based on negotiation activities, by comparing it with [List Cost](#listcost). If [*negotiated discounts*](#glossary:negotiated-discount) are not applicable, the Contracted Cost defaults to the List Cost.

The ContractedCost column adheres to the following requirements:

* ContractedCost MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ContractedCost MUST be of type Decimal.
* ContractedCost MUST conform to [NumericFormat](#numericformat) requirements.
* ContractedCost MUST NOT be null.
* ContractedCost MUST be a valid decimal value.
* ContractedCost MUST be denominated in the BillingCurrency.
* When [ContractedUnitPrice](#contractedunitprice) is null, ContractedCost adheres to the following additional requirements:
  * ContractedCost of a [*charge*](#glossary:charge) calculated based on other *charges* (e.g., when the [ChargeCategory](#chargecategory) is "Tax") MUST be calculated based on the ContractedCost of those related *charges*.
  * ContractedCost of a *charge* unrelated to other *charges* (e.g., when the ChargeCategory is "Credit") MUST match the [BilledCost](#billedcost).
* The product of ContractedUnitPrice and PricingQuantity MUST match the ContractedCost when ContractedUnitPrice is not null, PricingQuantity is not null, and [ChargeClass](#chargeclass) is not "Correction".
* Discrepancies in ContractedCost, ContractedUnitPrice, or PricingQuantity MAY exist when ChargeClass is "Correction".

## Column ID

ContractedCost

## Display Name

Contracted Cost

## Description

Cost calculated by multiplying *contracted unit price* and the corresponding Pricing Quantity.

## Usability Constraints

**Aggregation:** When aggregating Contracted Cost for savings calculations, it's important to exclude either [Charge Category](#chargecategory) "Purchase" *charges* (one-time and recurring) that are paid to cover future eligible *charges* (e.g., [commitment discount](#glossary:commitment-discount)) or the covered [Charge Category](#chargecategory) "Usage" *charges* themselves. This exclusion helps prevent double counting of these *charges* in the aggregation. Which set of *charges* to exclude depends on whether cost are aggregated on a billed basis (exclude covered *charges*) or accrual basis (exclude Purchases for future *charges*). For instance, *charges* categorized as [Charge Category](#chargecategory) "Purchase" and their related [Charge Category](#chargecategory) "Tax" *charges* for a Commitment Discount might be excluded from an accrual basis cost aggregation of Contracted Cost. This is because the "Usage" and "Tax" charge records provided during the term of the commitment discount already specify the Contracted Cost. Purchase *charges* that cover future eligible *charges* can be identified by filtering for [Charge Category](#chargecategory) "Purchase" records with a [Billed Cost](#billedcost) greater than 0 and an [Effective Cost](#effectivecost) equal to 0.

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
