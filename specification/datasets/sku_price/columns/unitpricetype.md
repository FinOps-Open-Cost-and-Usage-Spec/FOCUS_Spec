# Unit Price Type

Unit Price Type categorizes the monetary value in [Unit Price](#datamodel.skuprice.unitprice) by indicating the nature of the rate. This categorization delineates between a standard public price, a baseline price tied to a specific [*contract*](#glossary:contract), a price made available as part of a custom negotiated agreement, or other price types specific to a given [*service provider*](#glossary:service-provider).

## Requirements

UnitPriceType MUST adhere to the following requirements:

* UnitPriceType MUST be of type String.
* UnitPriceType MUST NOT be null.
* UnitPriceType SHOULD use one of the recommended values when the price model aligns with a defined concept.
* UnitPriceType MAY contain provider-specific values when the price model does not align with a recommended value.

## Recommended Values

| Value        | Description                                                                 |
|:-------------|:----------------------------------------------------------------------------|
| List         | A price not specific to a *contract*, such as a published catalog price or a temporary promotional price. |
| Base         | A list price fixed for a *contract* at a point in time, typically at the beginning of the *contract*. |
| Contracted   | A price specific to a *contract*, other than a "Base" price. |

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
