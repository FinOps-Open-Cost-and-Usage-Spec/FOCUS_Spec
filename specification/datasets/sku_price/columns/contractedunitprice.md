# Contracted Unit Price

The Contracted Unit Price represents the agreed-upon unit price for a single [Pricing Unit](#datasets.skuprice.pricingunit) of the associated [*SKU Price*](#glossary:sku-price), inclusive of [*negotiated discounts*](#glossary:negotiated-discount), if present, while excluding negotiated [*commitment discounts*](#glossary:commitment-discount) or any other discounts. This price is denominated in the [Pricing Currency](#datasets.skuprice.pricingcurrency), and applies to the [*contract*](#glossary:contract) identified by [Contract ID](#datasets.skuprice.contractid) on the same record.

Contracted Unit Price and [List Unit Price](#datasets.skuprice.listunitprice) are two properties of the same *SKU Price* rather than two separate records, so the negotiated rate and the public rate for a given [SKU Price ID](#datasets.skuprice.skupriceid) can be read from one row without a self-join.

## Requirements

ContractedUnitPrice MUST adhere to the following requirements:

* ContractedUnitPrice MUST be of type Decimal.
* ContractedUnitPrice MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* ContractedUnitPrice MUST adhere to the following nullability requirements:
  * ContractedUnitPrice MUST be null when [ContractId](#datasets.skuprice.contractid) is null.
  * ContractedUnitPrice MUST NOT be null when ContractId is not null.
* When ContractedUnitPrice is not null, ContractedUnitPrice MUST adhere to the following requirements:
  * ContractedUnitPrice MUST be a non-negative decimal value.
  * ContractedUnitPrice MUST be denominated in the [PricingCurrency](#datasets.skuprice.pricingcurrency).

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
| Dataset         | [SKU Price](#datasets.skuprice)                                                            |
| Column type     | Metric                                                                                     |
| Feature level   | Conditional                                                                                |
| Condition       | [Includes contract commitments](#conditions.includescontractcommitments)                   |
| Allows nulls    | True                                                                                       |
| Data type       | Decimal                                                                                    |
| Value format    | [Numeric Format](#attributes.numericformat)                                                |
| Number range    | Any valid non-negative decimal value                                                       |

## Version Introduced

1.5
