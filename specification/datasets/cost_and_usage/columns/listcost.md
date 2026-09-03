# List Cost

List Cost represents the cost of a [*charge*](#glossary:charge) based on the service-provider-suggested pricing.

When [List Unit Price](#datamodel.costandusage.listunitprice) and [Pricing Quantity](#datamodel.costandusage.pricingquantity) are provided for the *charge*, List Cost is calculated by multiplying the List Unit Price by the corresponding Pricing Quantity.

List Cost does not reflect negotiated unit price adjustments for the associated [*SKU Price*](#glossary:sku-price) or any cost impact conditional on a discount-bearing [*commitment program*](#glossary:commitment-program) (e.g., [*commitment discount*](#glossary:commitment-discount)) being applied to the *charge*.

List Cost is denominated in the [Billing Currency](#datamodel.costandusage.billingcurrency). List Cost is commonly used to calculate savings from various negotiated and rate optimization activities by comparing it with [Contracted Cost](#datamodel.costandusage.contractedcost), [Billed Cost](#datamodel.costandusage.billedcost), and [Effective Cost](#datamodel.costandusage.effectivecost).

## Requirements

ListCost MUST adhere to the following requirements:

* ListCost MUST be of type Decimal.
* ListCost MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* ListCost MUST NOT be null.
* ListCost MUST be denominated in the BillingCurrency.
* ListCost MUST NOT reflect negotiated unit price adjustments for the associated *SKU Price*.
* ListCost MUST NOT reflect any cost impact conditional on a discount-bearing *commitment program* being applied to the *charge*.
* ListCost MUST equal BilledCost when [ChargeCategory](#datamodel.costandusage.chargecategory) is "Credit".
* ListCost MUST be calculated based on the ListCost of the related *charges* when ChargeCategory is "Tax".
* ListCost MAY differ from BilledCost when ChargeCategory is "Adjustment".
* ListCost MUST equal the product of ListUnitPrice and PricingQuantity when ListUnitPrice is not null and PricingQuantity is not null.

## Usability Constraints

**Aggregation:** When aggregating List Cost for savings calculations, exclude either the [*covering charges*](#glossary:covering-charge) (e.g., [*commitment discount*](#glossary:commitment-discount) purchases) or the [*covered charges*](#glossary:covered-charge) (e.g., usage charges applied against *commitment discount*) to avoid double counting. Including both would result in the same costs being counted more than once in the aggregation. The appropriate set to exclude depends on the cost basis: exclude *covered charges* when aggregating on a billed basis, or exclude *covering charges* when aggregating on an accrual basis.

## Column ID

ListCost

## Display Name

List Cost

## Description

Cost of a *charge* based on the service-provider-suggested pricing.

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

1.0-preview
