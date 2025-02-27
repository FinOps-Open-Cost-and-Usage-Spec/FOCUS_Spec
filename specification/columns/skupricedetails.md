# SKU Price Details

The SKU Price Details column represents a list of relevant properties (key-value pairs) shared by all charges with the same [SKU Price ID](#skupriceid). These properties provide qualitative and quantitative details about the service represented by a SKU Price ID. This can enable practitioners to calculate metrics such as total units of a service when it is not directly billed in those units (e.g. cores) and thus enables FinOps capabilities such as unit economics. These properties can also help a practitioner understand the specifics of a SKU Price ID and differentiate it other SKU Price IDs.

The SkuPriceDetails column adheres to the following requirements:

* SkuPriceDetails MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider publishes a SKU price list.
* SkuPriceDetails MUST conform to [KeyValueFormat](#key-valueformat) requirements.
* Property key SHOULD conform to [PascalCase](#glossary:pascalcase) format.
* SkuPriceDetails nullability is defined as follows:
  * SkuPriceDetails MUST be null when SkuPriceId is null.
  * SkuPriceDetails MAY be null when SkuPriceId is not null.
* When SkuPriceDetails is not null, SkuPriceDetails adheres to the following additional requirements:
  * SkuPriceDetails MUST NOT contain properties which are not applicable to the corresponding SkuPriceId.
  * SkuPriceDetails MAY contain properties which are already captured in other dedicated columns.
  * SkuPriceDetails SHOULD remain consistent over time for a given SkuPriceId.
  * SkuPriceDetails properties for a given SkuPriceId adhere to the following additional requirements:
    * Existing SkuPriceDetails properties SHOULD remain consistent over time.
    * Existing SkuPriceDetails properties SHOULD NOT be removed.
    * Additional SkuPriceDetails properties MAY be added over time.
  * Property key SHOULD remain consistent across comparable SKUs having that property, and the values for this key SHOULD remain in a consistent format.
  * Property value MUST represent the value for a single [PricingUnit](#pricingunit) when the property holds a numeric value.

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

A set of properties of a SKU Price ID which are meaningful and common to all instances of that SKU Price ID.

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
