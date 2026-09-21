# Unit Price

The Unit Price represents the service-provider-published unit price for a single [Pricing Unit](#datamodel.skuprice.pricingunit) of the associated [*SKU Price*](#glossary:sku-price). This price is denominated in the [Pricing Currency](#datamodel.skuprice.pricingcurrency).

When [Contract ID](#datamodel.skuprice.contractid) is null, the Unit Price represents the standard public list price. When Contract ID is populated, the Unit Price represents a contractually agreed rate, typically lower than the public rate.

## Requirements

UnitPrice MUST adhere to the following requirements:

* UnitPrice MUST be of type Decimal.
* UnitPrice MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* UnitPrice MUST NOT be null.
* UnitPrice MUST be a non-negative decimal value.
* UnitPrice MUST be denominated in the [PricingCurrency](#datamodel.skuprice.pricingcurrency).
* UnitPrice MUST represent a contracted unit price when *ContractId* is not null.
* UnitPrice MUST represent a list unit price when *ContractId* is null.

## Usability Constraints

**Aggregation:** Column values should only be viewed in the context of their row and not aggregated to produce a total.

## Column ID

UnitPrice

## Display Name

Unit Price

## Description

The service-provider-published unit price for a single *Pricing Unit* of the associated *SKU Price*.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [SKU Price](#datamodel.skuprice)                      |
| Conditions      | Not applicable                                        |
| Column type     | Metric                                               |
| Feature level   | Mandatory                                            |
| Allows nulls    | False                                                |
| Data type       | Decimal                                              |
| Value format    | [Numeric Format](#attributes.numericformat)          |
| Number range    | Any valid non-negative decimal value                 |

## Version Introduced

1.5
