# List Unit Price

The List Unit Price represents the suggested service-provider-published unit price for a single [Pricing Unit](#datamodel.skuprice.pricingunit) of the associated [*SKU Price*](#glossary:sku-price), exclusive of any discounts. This price is denominated in the [Pricing Currency](#datamodel.skuprice.pricingcurrency). The List Unit Price provides the base catalog rate for an offering and is used for estimating expected costs, comparing catalog rates, and calculating savings based on rate optimization activities.

## Requirements

ListUnitPrice MUST adhere to the following requirements:

* ListUnitPrice MUST be of type Decimal.
* ListUnitPrice MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* ListUnitPrice MUST adhere to the following nullability requirements:
  * ListUnitPrice MUST NOT be null when the *SKU Price* is offered at a publicly published rate.
  * ListUnitPrice MUST be null when the *SKU Price* is offered only under a [*contract*](#glossary:contract).
* When ListUnitPrice is not null, ListUnitPrice MUST adhere to the following requirements:
  * ListUnitPrice MUST be a non-negative decimal value.
  * ListUnitPrice MUST be denominated in the [PricingCurrency](#datamodel.skuprice.pricingcurrency).

## Usability Constraints

**Aggregation:** Column values should only be viewed in the context of their row and not aggregated to produce a total.

## Column ID

ListUnitPrice

## Display Name

List Unit Price

## Description

The suggested service-provider-published unit price for a single Pricing Unit of the associated SKU Price, exclusive of any discounts.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [SKU Price](#datamodel.skuprice)                      |
| Column type     | Metric                                               |
| Feature level   | Mandatory                                            |
| Allows nulls    | True                                                 |
| Data type       | Decimal                                              |
| Value format    | [Numeric Format](#attributes.numericformat)          |
| Number range    | Any valid non-negative decimal value                 |

## Version Introduced

1.5
