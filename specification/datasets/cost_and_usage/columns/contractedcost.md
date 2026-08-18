# Contracted Cost

Contracted Cost represents the cost of a [*charge*](#glossary:charge) based on negotiated unit pricing.

When [Contracted Unit Price](#datamodel.costandusage.contractedunitprice) and [Pricing Quantity](#datamodel.costandusage.pricingquantity) are provided for the *charge*, Contracted Cost is calculated by multiplying the Contracted Unit Price by the corresponding Pricing Quantity.

Contracted Cost reflects negotiated unit price adjustments for the associated [*SKU Price*](#glossary:sku-price), independent of any discount-bearing [*commitment programs*](#glossary:commitment-program) (e.g., [*commitment discount*](#glossary:commitment-discount)) being applied to the charge. Contracted Cost does not reflect any cost impact conditional on a discount-bearing *commitment program* being applied to the *charge*.

When no negotiated unit price adjustments apply to the *charge*, Contracted Cost equals [List Cost](#datamodel.costandusage.listcost).

Contracted Cost is denominated in the [Billing Currency](#datamodel.costandusage.billingcurrency). Contracted Cost is commonly used for calculating savings based on negotiation activities by comparing it with List Cost.

## Requirements

ContractedCost MUST adhere to the following requirements:

* ContractedCost MUST be of type Decimal.
* ContractedCost MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* ContractedCost MUST NOT be null.
* ContractedCost MUST be denominated in the BillingCurrency.
* ContractedCost MUST reflect negotiated unit price adjustments for the *SKU Price* identified by the given [SkuPriceId](#datamodel.costandusage.skupriceid), independent of any discount-bearing *commitment programs* being applied to the *charge*.
* ContractedCost MUST NOT reflect any cost impact conditional on a discount-bearing *commitment program* being applied to the *charge*.
* ContractedCost MUST equal ListCost when no negotiated unit price adjustments apply to the *charge*.
* ContractedCost MUST equal [BilledCost](#datamodel.costandusage.billedcost) when [ChargeCategory](#datamodel.costandusage.chargecategory) is "Credit".
* ContractedCost MUST be calculated based on the ContractedCost of the related *charges* when ChargeCategory is "Tax".
* ContractedCost MAY differ from BilledCost when ChargeCategory is "Adjustment".
* ContractedCost MUST equal the product of ContractedUnitPrice and PricingQuantity when ContractedUnitPrice is not null and PricingQuantity is not null.

## Usability Constraints

**Aggregation:** When aggregating Contracted Cost for savings calculations, it's important to exclude either Charge Category "Purchase" *charges* (one-time and recurring) that are paid to cover future eligible *charges* (e.g., [commitment discount](#glossary:commitment-discount)) or the covered Charge Category "Usage" *charges* themselves. This exclusion helps prevent double counting of these *charges* in the aggregation. Which set of *charges* to exclude depends on whether costs are aggregated on a billed basis (exclude covered *charges*) or accrual basis (exclude Purchases for future *charges*). For instance, *charges* categorized as Charge Category "Purchase" and their related Charge Category "Tax" *charges* for a Commitment Discount might be excluded from an accrual basis cost aggregation of Contracted Cost. This is because the "Usage" and "Tax" charge records provided during the commitment [*period*](#glossary:period) already specify the Contracted Cost. Purchase *charges* that cover future eligible *charges* can be identified by filtering for Charge Category "Purchase" records with a Billed Cost greater than 0 and an [Effective Cost](#datamodel.costandusage.effectivecost) equal to 0.

## Column ID

ContractedCost

## Display Name

Contracted Cost

## Description

Cost of a *charge* based on negotiated unit pricing.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [Cost and Usage](#datamodel.costandusage)             |
| Column type     | Metric                                               |
| Feature level   | Mandatory                                            |
| Allows nulls    | False                                                |
| Data type       | Decimal                                              |
| Value format    | [Numeric Format](#attributes.numericformat)          |
| Number range    | Any valid decimal value                              |

## Version Introduced

1.0
