# SKU Price Details

The **SKU Price Details** column represents a list of relevant properties shared by all charges with the same [**SKU Price ID**](#skupriceid). These properties enable practitioners to calculate metrics such as total units of a service when it is not directly billed in those units (e.g. cores) and thus enables FinOps capabilities such as unit economics. They also help a practitioner understand the specifics of a **SKU Price ID**.


The _SkuPriceDetails_ column adheres to the following requirements:

* The _SkuPriceDetails_ column MUST be in [_KeyValueFormat_](#key-valueformat).
* The key for a property SHOULD be formatted in [PascalCase](#glossary:pascalcase).
* The properties (both keys and values) contained in the _SkuPriceDetails_ column MUST be shared across all charges having the same _SkuPriceId_.
  * Additional properties (key-value pairs) MAY be added to _SkuPriceDetails_ for a _SkuPriceId_.
  * Properties SHOULD NOT be removed from _SkuPriceDetails_ for a _SkuPriceId_, once they have been included.
  * Individual properties (key-value pairs) SHOULD NOT be modified for a _SkuPriceId_.
* The key for a property SHOULD remain consistent across comparable SKUs having that property and the values for this key SHOULD remain in a consistent format.
* The _SkuPriceDetails_ column SHOULD NOT contain properties which are not applicable to the corresponding _SkuPriceId_.
* The _SkuPriceDetails_ column MAY contain properties which are already captured in other dedicated columns.
* Properties in _SkuPriceDetails_ which have a numerical value MUST represent the value for a the individual [_ConsumedUnit_](#consumedunit) i.e. a [_ConsumedQuantity_](#consumedquantity) of 1.
* Additional properties (key-value pairs) MAY be added to _SkuPriceDetails_ for a _SkuPriceId_.
  * Properties SHOULD NOT be removed from _SkuPriceDetails_ for a _SkuPriceId_, once they have been included.
  * Individual properties (key-value pairs) SHOULD NOT be modified for a _SkuPriceId_.
 * The _SkuPriceDetils_ column MUST be present in the billing data when the provider includes a _SkuPriceID_.

## Examples

```json
{
    "OperationClass": "A",
    "PricingTier": 2,
    "CoreHours": 4,
    "PreimumProcessing": true,
}
```

## Column ID

SkuPriceDetails

## Display Name

SKU Price Details

## Description

A set of properties of a **SKU Price ID** which are meaningful and common to all instances of that **SKU Price ID**

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
