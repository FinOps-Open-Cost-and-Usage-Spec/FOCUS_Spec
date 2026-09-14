# List Cost

List Cost represents the cost of a [*charge*](#glossary:charge) based on the provider-suggested pricing. It is the cost before any negotiated unit price adjustments for the associated [*SKU Price*](#glossary:sku-price) or any discount-bearing [*commitment programs*](#glossary:commitment-program) (e.g., [*commitment discount*](#glossary:commitment-discount)) are applied to the *charge*.

When [List Unit Price](#datamodel.costandusage.listunitprice) and [Pricing Quantity](#datamodel.costandusage.pricingquantity) are provided for the *charge*, List Cost is calculated by multiplying the List Unit Price by the corresponding Pricing Quantity.

List Cost is denominated in the [Billing Currency](#datamodel.costandusage.billingcurrency). List Cost is commonly used to calculate savings from various negotiated and rate optimization activities by comparing it with [Contracted Cost](#datamodel.costandusage.contractedcost), [Billed Cost](#datamodel.costandusage.billedcost), and [Effective Cost](#datamodel.costandusage.effectivecost).

## Requirements

ListCost MUST adhere to the following requirements:

* ListCost MUST be of type Decimal.
* ListCost MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* ListCost MUST NOT be null.
* ListCost MUST be denominated in the BillingCurrency.
* ListCost MUST equal BilledCost when [ChargeCategory](#datamodel.costandusage.chargecategory) is "Credit".
* ListCost MUST be calculated based on the ListCost of the related *charges* when ChargeCategory is "Tax".
* ListCost MAY differ from BilledCost when ChargeCategory is "Adjustment".
* ListCost MUST equal the product of ListUnitPrice and PricingQuantity when ListUnitPrice is not null and PricingQuantity is not null.

## Usability Constraints

**Aggregation:** When aggregating List Cost for savings calculations, exclude either the [*covering charges*](#glossary:covering-charge) (e.g., [*commitment discount*](#glossary:commitment-discount) purchases) or the [*covered charges*](#glossary:covered-charge) (e.g., usage charges applied against *commitment discount*), based on the specific use case, to avoid double counting. The appropriate set to exclude depends on the relevant cost basis for the use case. Exclude *covered charges* when aggregating on a billed basis, or *covering charges* when aggregating on an accrual basis.

## Column ID

ListCost

## Display Name

List Cost

## Description

Cost of a *charge* based on the provider-suggested pricing.

## Content Constraints

| Constraint                 | Value                                       |
| :------------------------- | :------------------------------------------ |
| Dataset                    | [Cost and Usage](#datamodel.costandusage)   |
| Operating Model Conditions | Not applicable                              |
| Column type                | Metric                                      |
| Feature level              | Mandatory                                   |
| Allows nulls               | False                                       |
| Data type                  | Decimal                                     |
| Value format               | [Numeric Format](#attributes.numericformat) |
| Number range               | Any valid decimal value                     |

## Version Introduced

1.0-preview
