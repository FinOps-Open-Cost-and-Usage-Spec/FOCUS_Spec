# Unit Price Type

Unit Price Type categorizes the monetary value in [Unit Price](#datamodel.skuprice.unitprice) by indicating the nature of the rate. This categorization delineates between a standard public price, a baseline for tiered calculations, a custom contractual agreement, or other price types specific to a given [*service provider*](#glossary:service-provider).

## Requirements

UnitPriceType MUST adhere to the following requirements:

* UnitPriceType MUST be of type String.
* UnitPriceType MUST NOT be null.
* UnitPriceType MUST use one of the allowed values defined in this specification when the price model aligns with a defined concept.
* UnitPriceType MAY contain provider-specific values when the price model does not align with a standard value.

## Allowed Values

| Value        | Description                                                                 |
|:-------------|:----------------------------------------------------------------------------|
| List         | The standard public catalog price offered to all consumers before discounts.|
| Contracted   | A custom price established through a contractual agreement.                   |
| Base         | A list price for a given contract as it existed at a specific point in time, typically at the beginning of the contract. |

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
| Operating Model Conditions | None                                      |
| Column type                | Dimension                                 |
| Feature level              | Mandatory                                 |
| Allows nulls               | False                                     |
| Data type                  | String                                    |
| Value format               | Open                                      |

## Version Introduced

1.5
