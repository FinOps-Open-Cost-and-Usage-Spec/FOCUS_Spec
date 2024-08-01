# SKU Price Details

The **SKU Price Details** column represents a list of relevant properties shared by all resources having the same [**SKU Price ID**](#skupriceid) which are not captured in another FOCUS column. These properties enable a practitioner to more easily understand the differences that make up the multiple **SKU Price ID**s under a given [**SKU ID**](#skuid).


The _SkuPriceDetails_ column adheres to the following requirements:

* The properties (both key and value) contained in the _SkuPriceDetails_ column MUST be shared across all resources having the same _SkuPriceId_.
* The _SkuPriceDetails_ column MUST be in [_KeyValueFormat_](#key-valueformat).
* The _SkuPriceDetails_ column SHOULD NOT contain properties which are not applicable to the corresponding _SkuPriceId_.
* The _SkuPriceDetails_ column SHOULD NOT contain properties which are already captured in the [_SkuDetails_](#skudetails) column.
* The _SkuPriceDetails_ column MAY contain properties which are already captured in other dedicated columns.
* Where _SkuPriceDetails_ contains a property with a value which is a numerical, the value provided MUST represent the value for a [_ConsumedQuantity_](#consumedquantity) of 1.
* The key for a property SHOULD remain consistent across comparable SKUs having that property and the values for this key SHOULD remain in a consistent format.
* The key for a property SHOULD be formatted in [PascalCase](#glossary:pascalcase).
* Properties included in _SkuPriceDetails_ SHOULD be immutable once included for a _SkuPriceId_.

## Examples

```json
    {
        "OperationClass": "A",
        "PricingTier": 2,
        "PreimumProcessing": true,
    }
```

## Column ID

SkuPriceDetails

## Display Name

SKU Price Details

## Description

A set of properties of a **SKU Price ID** which allow differentiation between different **SKU Price ID**s within the same **SKU ID**.

## Content Constraints

|    Constraint   |      Value       |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Feature level   | Conditional      |
| Allows nulls    | True             |
| Data type       | JSON             |
| Value format    | [Key-Value Format](#key-valueformat) |

## Introduced (version)

1.1
