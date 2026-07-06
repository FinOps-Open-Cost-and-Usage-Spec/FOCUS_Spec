# Unit Price Category

Unit Price Category describes the type of unit price represented by the [*SKU Price*](#glossary:sku-price) record. This column is useful for distinguishing between standard public catalog rates and custom negotiated rates specific to a billing account.

## Requirements

UnitPriceCategory MUST adhere to the following requirements:

* UnitPriceCategory MUST be of type String.
* UnitPriceCategory MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* UnitPriceCategory MUST NOT be null.
* UnitPriceCategory MUST be one of the allowed values.
* UnitPriceCategory MUST be "List" when the unit price is the standard, current public rate offered by the service provider.
* UnitPriceCategory MUST be "Contracted" when the unit price is a negotiated or custom rate specific to a billing account or agreement.
* UnitPriceCategory MUST be "List" when [ContractId](#datasets.skuprice.contractid) is null.

## Allowed Values

| Value      | Description                                                                                                                                                             |
| :--------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| List       | The standard, publicly available unit price published by the service provider.                                                                                          |
| Contracted | A custom or negotiated unit price specifically established for a given billing account or agreement.                                                                    |

## Column ID

UnitPriceCategory

## Display Name

Unit Price Category

## Description

Describes the type of unit price represented by the SKU Price record.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [SKU Price](#datasets.skuprice)                      |
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | False                                                |
| Data type       | String                                               |
| Value format    | Allowed values                                       |

## Version Introduced

1.5
