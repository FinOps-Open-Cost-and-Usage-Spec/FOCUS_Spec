# Quantity Tier Category

Quantity Tier Category indicates the mathematical methodology used to apply the [Unit Price](#datamodel.skuprice.unitprice) when consumption crosses quantity thresholds.

This column allows practitioners to correctly distinguish between a waterfall calculation model (where the rate applies only to the units inside the envelope) and a step-function model (where crossing the threshold changes the rate for all units consumed).

## Requirements

QuantityTierCategory MUST adhere to the following requirements:

* QuantityTierCategory MUST be of type String.
* QuantityTierCategory MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* QuantityTierCategory MUST adhere to the following nullability requirements:
  * QuantityTierCategory MUST be null when the SkuPrice record does not represent a rate associated with quantity-based pricing tiers.
  * QuantityTierCategory MUST NOT be null when the SkuPrice record represents a rate associated with quantity-based pricing tiers.
* QuantityTierCategory MUST be one of the allowed values.

## Allowed Values

| Value        | Description                                                                 |
|:-------------|:----------------------------------------------------------------------------|
| Graduated    | The unit price applies only to the quantity of consumption that falls within the tier's boundaries. |
| Retroactive  | The unit price applies to the total quantity of consumption once the tier's minimum threshold is crossed. |

## Column ID

QuantityTierCategory

## Display Name

Quantity Tier Category

## Description

Indicates the mathematical methodology used to apply the Unit Price when consumption crosses quantity thresholds.

## Content Constraints

| Constraint                 | Value                                                |
| :------------------------- | :--------------------------------------------------- |
| Dataset                    | [SKU Price](#datamodel.skuprice)                     |
| Operating Model Conditions | [Includes Quantity Tier Pricing](#operatingmodelconditions.includesquantitytierpricing) |
| Column type                | Dimension                                            |
| Feature level              | Conditional                                          |
| Allows nulls               | True                                                 |
| Data type                  | String                                               |
| Value format               | Allowed values                                       |

## Version Introduced

1.5
