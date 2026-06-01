# Unit Price

The Unit Price represents the service-provider-published unit price for a single [Pricing Unit](#datasets.skuprice.pricingunit) of the associated [*SKU Price*](#glossary:sku-price). This price is denominated in the [Pricing Currency](#datasets.skuprice.pricingcurrency). The Unit Price provides the exact base rate for a catalog offering and is used as the foundational metric for calculating expected costs, comparing catalog rates, and performing rate optimization analyses.

## Requirements

UnitPrice MUST adhere to the following requirements:

* UnitPrice MUST be of type Decimal.
* UnitPrice MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* UnitPrice MUST NOT be null.
* UnitPrice MUST be a non-negative decimal value.
* UnitPrice MUST be denominated in the [PricingCurrency](#datasets.skuprice.pricingcurrency).

## Column ID

UnitPrice

## Display Name

Unit Price

## Description

The service-provider-published unit price for a single Pricing Unit of the associated *SKU Price*.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [SKU Price](#datasets.skuprice)                      |
| Column type     | Metric                                               |
| Feature level   | Mandatory                                            |
| Allows nulls    | False                                                |
| Data type       | Decimal                                              |
| Value format    | [Numeric Format](#attributes.numericformat)          |
| Number range    | Any valid non-negative decimal value                 |

## Version Introduced

1.5
