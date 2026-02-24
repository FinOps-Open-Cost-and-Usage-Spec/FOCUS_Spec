# List Cost

List Cost represents the cost calculated by multiplying the [*list unit price*](#glossary:list-unit-price) and the corresponding [Pricing Quantity](#datasets.costandusage.pricingquantity). List Cost is denominated in the [Billing Currency](#datasets.costandusage.billingcurrency) and is commonly used for calculating savings based on various rate optimization activities by comparing it with [Contracted Cost](#datasets.costandusage.contractedcost), [Billed Cost](#datasets.costandusage.billedcost) and [Effective Cost](#datasets.costandusage.effectivecost).

## Requirements

ListCost MUST adhere to the following requirements:

* ListCost MUST be of type Decimal.
* ListCost MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* ListCost MUST NOT be null.
* ListCost MUST be a valid decimal value.
* ListCost MUST be denominated in the BillingCurrency.
* When [ListUnitPrice](#datasets.costandusage.listunitprice) is null, ListCost MUST adhere to the following additional requirements:
  * ListCost of a [*charge*](#glossary:charge) calculated based on other *charges* (e.g., when the [ChargeCategory](#datasets.costandusage.chargecategory) is "Tax") MUST be calculated based on the ListCost of those related *charges*.
  * ListCost of a *charge* unrelated to other *charges* (e.g., when the ChargeCategory is "Credit") MUST match the [BilledCost](#datasets.costandusage.billedcost).
* ListCost MUST equal the product of ListUnitPrice and PricingQuantity when ListUnitPrice is not null and PricingQuantity is not null.

## Column ID

ListCost

## Display Name

List Cost

## Description

Cost calculated by multiplying List Unit Price and the corresponding Pricing Quantity.

## Usability Constraints

**Aggregation:** When aggregating List Cost for savings calculations, it's important to exclude either [Charge Category](#datasets.costandusage.chargecategory) "Purchase" *charges* (one-time and recurring) that are paid to cover future eligible *charges* (e.g., [commitment discount](#glossary:commitment-discount)) or the covered [Charge Category](#datasets.costandusage.chargecategory) "Usage" *charges* themselves. This exclusion helps prevent double counting of these *charges* in the aggregation. Which set of *charges* to exclude depends on whether cost are aggregated on a billed basis (exclude covered *charges*) or accrual basis (exclude Purchases for future *charges*). For instance, *charges* categorized as [Charge Category](#datasets.costandusage.chargecategory) "Purchase" and their related [Charge Category](#datasets.costandusage.chargecategory) "Tax" *charges* for a Commitment Discount might be excluded from an accrual basis cost aggregation of List Cost. This is because the "Usage" and "Tax" charge records provided during the term of the commitment discount already specify the List Cost. Purchase *charges* that cover future eligible *charges* can be identified by filtering for [Charge Category](#datasets.costandusage.chargecategory) "Purchase" records with a [Billed Cost](#datasets.costandusage.billedcost) greater than 0 and an [Effective Cost](#datasets.costandusage.effectivecost) equal to 0.

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

1.0-preview
