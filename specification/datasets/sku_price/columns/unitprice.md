# Unit Price

The Unit Price represents the service-provider-published unit price for a single [Pricing Unit](#datamodel.skuprice.pricingunit) of the associated [*SKU Price*](#glossary:sku-price). This price is denominated in the [Pricing Currency](#datamodel.skuprice.pricingcurrency).

When [Contract ID](#datamodel.skuprice.contractid) is null, the Unit Price represents the standard public price. When Contract ID is populated, the Unit Price represents a price specific to that contract, and [Unit Price Type](#datamodel.skuprice.unitpricetype) indicates which kind (e.g., a "Base" list price fixed for the contract, or a "Contracted" rate).

## Requirements

UnitPrice MUST adhere to the following requirements:

* UnitPrice MUST be of type Decimal.
* UnitPrice MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* UnitPrice MUST NOT be null.
* UnitPrice MUST be a non-negative decimal value.
* UnitPrice MUST be denominated in the [PricingCurrency](#datamodel.skuprice.pricingcurrency).

## Usability Constraints

**Aggregation:** Column values should only be viewed in the context of their row and not aggregated to produce a total.

## Column ID

UnitPrice

## Display Name

Unit Price

## Description

The service-provider-published unit price for a single *Pricing Unit* of the associated *SKU Price*.

## Content Constraints

| Constraint                 | Value                                                |
| :------------------------- | :--------------------------------------------------- |
| Dataset                    | [SKU Price](#datamodel.skuprice)                     |
| Operating Model Conditions | Not applicable                                       |
| Column type                | Metric                                               |
| Feature level              | Mandatory                                            |
| Allows nulls               | False                                                |
| Data type                  | Decimal                                              |
| Value format               | [Numeric Format](#attributes.numericformat)          |
| Number range               | Any valid non-negative decimal value                 |

## Version Introduced

1.5
