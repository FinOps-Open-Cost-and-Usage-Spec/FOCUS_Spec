# Contracted Unit Price

The Contracted Unit Price represents the agreed-upon unit price for a single [Pricing Unit](#datamodel.skuprice.pricingunit) of the associated [*SKU Price*](#glossary:sku-price), inclusive of [*negotiated discounts*](#glossary:negotiated-discount), if present, while excluding negotiated [*commitment discounts*](#glossary:commitment-discount) or any other discounts. This price is denominated in the [Pricing Currency](#datamodel.skuprice.pricingcurrency), and applies to the [*contract*](#glossary:contract) identified by [Contract ID](#datamodel.skuprice.contractid) on the same record. On a record with a null Contract ID, which carries a public list price available to any customer, the Contracted Unit Price equals the [List Unit Price](#datamodel.skuprice.listunitprice), so every record carries a rate under this column whether or not a negotiation produced it.

Contracted Unit Price and List Unit Price are two properties of the same *SKU Price* rather than two separate records, so the negotiated rate and the public rate for a given [SKU Price ID](#datamodel.skuprice.skupriceid) can be read from one row without a self-join.

## Requirements

ContractedUnitPrice MUST adhere to the following requirements:

* ContractedUnitPrice MUST be of type Decimal.
* ContractedUnitPrice MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* ContractedUnitPrice MUST NOT be null.
* ContractedUnitPrice MUST be a non-negative decimal value.
* ContractedUnitPrice MUST be denominated in the [PricingCurrency](#datamodel.skuprice.pricingcurrency).
* ContractedUnitPrice MUST equal [ListUnitPrice](#datamodel.skuprice.listunitprice) when [ContractId](#datamodel.skuprice.contractid) is null.

## Usability Constraints

**Aggregation:** Column values should only be viewed in the context of their row and not aggregated to produce a total.

## Column ID

ContractedUnitPrice

## Display Name

Contracted Unit Price

## Description

The agreed-upon unit price for a single Pricing Unit of the associated SKU Price, inclusive of negotiated discounts, if present, while excluding negotiated commitment discounts or any other discounts.

## Content Constraints

| Constraint      | Value                                                                                      |
| :-------------- | :----------------------------------------------------------------------------------------- |
| Dataset         | [SKU Price](#datamodel.skuprice)                                                            |
| Conditions      | Not applicable                                                                              |
| Column type     | Metric                                                                                     |
| Feature level   | Mandatory                                                                                  |
| Allows nulls    | False                                                                                      |
| Data type       | Decimal                                                                                    |
| Value format    | [Numeric Format](#attributes.numericformat)                                                |
| Number range    | Any valid non-negative decimal value                                                       |

## Version Introduced

1.5
