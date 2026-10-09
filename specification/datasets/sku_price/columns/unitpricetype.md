# Unit Price Type

Unit Price Type categorizes the monetary value in [Unit Price](#datamodel.skuprice.unitprice) by indicating the nature of the rate. This categorization delineates between a standard public price, a baseline price tied to a specific [*contract*](#glossary:contract), a price made available as part of a custom negotiated agreement, or other price types specific to a given [*service provider*](#glossary:service-provider).

## Requirements

UnitPriceType MUST adhere to the following requirements:

* UnitPriceType MUST be of type String.
* UnitPriceType MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* UnitPriceType MUST NOT be null.
* UnitPriceType MUST NOT be "Base" when the SkuPrice record does not represent the [*list unit price*](#glossary:list-unit-price) at a point in time, fixed for a given [ContractId](#datamodel.skuprice.contractid).
* UnitPriceType MUST NOT be "Contracted" when the SkuPrice record does not represent a [*contracted unit price*](#glossary:contracted-unit-price) for a given ContractId.
* UnitPriceType SHOULD use one of the recommended values when the price model aligns with a defined concept.
* UnitPriceType SHOULD be "List" when the SkuPrice record does not represent a price specific to a contract.
* UnitPriceType SHOULD be "Base" when the SkuPrice record represents a price specific to a contract and that price is a list price fixed for the contract at a point in time.
* UnitPriceType SHOULD be "Contracted" when the SkuPrice record represents a price specific to a contract and that price is not a list price fixed for the contract at a point in time.
* UnitPriceType MAY contain provider-specific values when the price model does not align with a recommended value.

## Recommended Values

| Value        | Description                                                                 |
|:-------------|:----------------------------------------------------------------------------|
| List         | A *list unit price* not specific to a *contract*. |
| Base         | A *list unit price* at a point in time, fixed for a given *contract*, typically at the beginning of the *contract*. |
| Contracted   | A *contracted unit price* for a given *contract*. |

## Column ID

UnitPriceType

## Display Name

Unit Price Type

## Description

Categorizes the monetary value in *Unit Price*.

## Content Constraints

| Constraint                 | Value                                     |
| :------------------------- | :---------------------------------------- |
| Dataset                    | [SKU Price](#datamodel.skuprice)          |
| Operating Model Conditions | Not applicable                            |
| Column type                | Dimension                                 |
| Feature level              | Mandatory                                 |
| Allows nulls               | False                                     |
| Data type                  | String                                    |
| Value format               | Recommended values                        |

## Version Introduced

1.5
