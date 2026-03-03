# Contracted Cost

Contracted Cost represents the cost calculated by multiplying [*contracted unit price*](#glossary:contracted-unit-price) and the corresponding [Pricing Quantity](#datasets.costandusage.pricingquantity). Contracted Cost is denominated in the [Billing Currency](#datasets.costandusage.billingcurrency) and is commonly used for calculating savings based on negotiation activities, by comparing it with [List Cost](#datasets.costandusage.listcost). If [*negotiated discounts*](#glossary:negotiated-discount) are not applicable, the Contracted Cost defaults to the List Cost.

## Requirements

ContractedCost MUST adhere to the following requirements:

* ContractedCost MUST be of type Decimal.
* ContractedCost MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* ContractedCost MUST NOT be null.
* ContractedCost MUST be a valid decimal value.
* ContractedCost MUST be denominated in the BillingCurrency.
* When [ContractedUnitPrice](#datasets.costandusage.contractedunitprice) is null, ContractedCost MUST adhere to the following requirements:
  * ContractedCost of a [*charge*](#glossary:charge) calculated based on other *charges* (e.g., when the [ChargeCategory](#datasets.costandusage.chargecategory) is "Tax") MUST be calculated based on the ContractedCost of those related *charges*.
  * ContractedCost of a *charge* unrelated to other *charges* (e.g., when the ChargeCategory is "Credit") MUST match the [BilledCost](#datasets.costandusage.billedcost).
* ContractedCost MUST equal the product of ContractedUnitPrice and PricingQuantity when ContractedUnitPrice is not null and PricingQuantity is not null.

## Column ID

ContractedCost

## Display Name

Contracted Cost

## Description

Cost calculated by multiplying *contracted unit price* and the corresponding Pricing Quantity.

## Usability Constraints

**Aggregation:** When aggregating Contracted Cost for savings calculations, it's important to exclude either [Charge Category](#datasets.costandusage.chargecategory) "Purchase" *charges* (one-time and recurring) that are paid to cover future eligible *charges* (e.g., [commitment discount](#glossary:commitment-discount)) or the covered [Charge Category](#datasets.costandusage.chargecategory) "Usage" *charges* themselves. This exclusion helps prevent double counting of these *charges* in the aggregation. Which set of *charges* to exclude depends on whether cost are aggregated on a billed basis (exclude covered *charges*) or accrual basis (exclude Purchases for future *charges*). For instance, *charges* categorized as [Charge Category](#datasets.costandusage.chargecategory) "Purchase" and their related [Charge Category](#datasets.costandusage.chargecategory) "Tax" *charges* for a Commitment Discount might be excluded from an accrual basis cost aggregation of Contracted Cost. This is because the "Usage" and "Tax" charge records provided during the commitment [*period*](#glossary:period) already specify the Contracted Cost. Purchase *charges* that cover future eligible *charges* can be identified by filtering for [Charge Category](#datasets.costandusage.chargecategory) "Purchase" records with a [Billed Cost](#datasets.costandusage.billedcost) greater than 0 and an [Effective Cost](#datasets.costandusage.effectivecost) equal to 0.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [Cost and Usage](#datasets.costandusage)             |
| Column type     | Metric                                               |
| Feature level   | Mandatory                                            |
| Allows nulls    | False                                                |
| Data type       | Decimal                                              |
| Value format    | [Numeric Format](#attributes.numericformat)          |
| Number range    | Any valid decimal value                              |

## Introduced (version)

1.0
