# SKU Details

The **SKU Details** column represents a list of relevant properties shared by all resources having the same [**SKU ID**](#skuid) which are not captured in another FOCUS column. These properties enable a practitioner to more easily calculate metrics such as total units of a service when it is not directly billed in those units (e.g. cores) and thus enables FinOps capabilities such as unit economics.


The _SkuDetails_ column adheres to the following requirements:

* The properties (both key and value) contained in the _SkuDetails_ column MUST be shared across all resources having the same _SkuId_.
* The _SkuDetails_ column MUST be in [_KeyValueFormat_](#key-valueformat).
* The _SkuDetails_ column SHOULD NOT contain properties which are not applicable to the corresponding _SkuId_.
* Where _SkuDetails_ contains a property with a value which is a numerical, the value provided MUST represent the value for a [_ConsumedQuantity_](#consumedquantity) of 1.
* The key for a property SHOULD remain consistent across comparable SKUs having that property and the values for this key SHOULD remain in a consistent format.
* The key for a property SHOULD be formatted in PascalCase.
* Properties included in _SkuDetails_ SHOULD be immutable once included for a _SkuId_.

## Examples

```json
    {
        "Cores": 4,
        "EphemeralDiskGB": 100,
        "NestedVirtualization": true,
    }
```

## Column ID

SkuDetails

## Display Name

SKU Details

## Description

A set of properties of a **SKU ID** which are meaningful but not common across all **SKU ID**s.

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
