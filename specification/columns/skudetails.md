# SKU Details

The SKU Details column represents a list of relevant properties shared by all resources having the same [SKU ID](#skuid) which are not captured in another FOCUS column. These properties enable a practitioner to more easily calculate metrics such as total units of a service when it is not directly billed in those units (e.g. cores) and thus enables FinOps capabilities such as unit economics.


The SkuDetails column adheres to the following requirements:

* The properties (both key and value) contained in the SkuDetails column MUST be shared across all resources having the same SkuId.
* The SkuDetails column MUST be in [Key-Value Format](#key-valueformat).
* The SkuDetails column SHOULD NOT contain properties which are not applicable to the corresponding SkuId.
* Where SkuDetails contains a property with a value which is a numerical, the value provided MUST represent the value for a [ConsumedUnit](#consumedunit) of 1.
* The key for a property SHOULD remain consistent across comparable SKUs having that property and the values for this key SHOULD remain in a consistent format.

## Examples

```json
    {
        "cores": 4,
        "ephemeral_disk_gb": 100,
        "nested_virtualization": true,
    }
```

## Column ID

SkuDetails

## Display Name

SKU Details

## Description

A set of properties of a SKU ID which are meaningful but not common across all SKU IDs.

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
