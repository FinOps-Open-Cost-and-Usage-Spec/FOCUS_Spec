# SKU Price Details

The SKU Price Details column represents a list of relevant properties shared by all charges with the same [SKU Price ID](#skupriceid). These properties provide qualitative and quantitative details about the service represented by a SKU Price ID. This can enable practitioners to calculate metrics such as total units of a service when it is not directly billed in those units (e.g. cores) and thus enables FinOps capabilities such as unit economics. These properties can also help a practitioner understand the specifics of a SKU Price ID and differentiate it other SKU Price IDs.

The SkuPriceDetails column adheres to the following requirements:

* SkuPriceDetails MUST be in [ObjectFormat](#objectformat).
* SkuPriceDetails keys SHOULD be formatted in [PascalCase](#glossary:pascalcase).
* SkuPriceDetails properties (both keys and values) MUST be shared across all charges having the same SkuPriceId, subject to the below provisions.
  * Additional properties MAY be added to SkuPriceDetails going forward for a given SkuPriceId.
  * Properties SHOULD NOT be removed from SkuPriceDetails for a given SkuPriceId, once they have been included.
  * Individual properties SHOULD NOT be modified for a given SkuPriceId and SHOULD remain consistent over time.
* SkuPriceDetails keys and their values SHOULD remain consistent across comparable SKUs having that property.
* SkuPriceDetails MUST NOT contain properties which are not applicable to the corresponding SkuPriceId.
* SkuPriceDetails MAY contain properties which are already captured in other dedicated columns.
* SkuPriceDetails properties with a numeric value MUST represent the value for a single [PricingUnit](#pricingunit).
* SkuPriceDetails properties that represent common constructs listed in the Predefined Keys section below MUST use the predefined keys.
  * Values for predefined keys MUST be the specified data type for that key in the section below.
  * Values for predefined keys SHOULD be one of the Preferred Values, when applicable.
  * Values for predefined keys MAY be a custom value when the Preferred Values do not adequately represent the value.
* SkuPriceDetails properties that represent a unit-based, numeric measure MUST be represented as a nested key-value pair with `Quantity` and `Unit` keys.
  * Quantity MUST be a number.
  * Quantity MUST not be NULL.
  * Unit SHOULD adhere to the format requirements specified in the [UnitFormat](#unitformat) attribute.
  * Unit SHOULD be one of the Preferred Values, when applicable.
  * Unit MUST not be NULL.
  * Key-value pairs MAY include additional keys in addition to Quantity and Unit.
* SkuPriceDetails MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider includes a SkuPriceId.
  * SkuPriceDetails MAY be null when SkuPriceId is not null.
  * SkuPriceDetails MUST be null when SkuPriceId is null.

## Examples

```json
{
    "OperationClass": "A",
    "PricingTier": 2,
    "CoreHours": 4,
    "PreimumProcessing": true,
    "Processor": { "Quantity": 32, "Unit": "Cores" },
}
```

## Column ID

SkuPriceDetails

## Display Name

SKU Price Details

## Description

A set of properties of a SKU Price ID which are meaningful and common to all instances of that SKU Price ID.

## Content Constraints

| Constraint    | Value                          |
| :------------ | :----------------------------- |
| Column type   | Dimension                      |
| Feature level | Conditional                    |
| Allows nulls  | True                           |
| Data type     | JSON                           |
| Value format  | [Object Format](#objectformat) |

### Predefined Keys

The following keys should be used when applicable to facilitate cross-service and cross-provider queries for the same conceptual property.

| Key                      | Description                                    | Data Type        | Preferred Values                                   |
| :----------------------- | :--------------------------------------------- | :--------------- | :------------------------------------------------- |
| AccessTier               |                                                | String           | "Hot", "Cool", "Archive"                           |
| AutoScaling              | Options for web apps to handle varying demand. |                  |                                                    |
| Bandwidth                | Network capacity for data transfer.            |                  |                                                    |
| ComplianceCertifications |                                                | String array     |                                                    |
| Cores                    | Number of physical or virtual CPUs available.  | Count-based spec | "Cores" units                                      |
| DiskSpace                | Storage capacity available.                    | Data size spec   | "GB" units                                         |
| DiskType                 | Kind of disk used.                             | String           | "SSD", "HDD", "NVMe"                               |
| Encryption               |                                                |                  |                                                    |
| GPU                      | Number of GPUs available.                      | Count-based spec | "GPUs"                                             |
| InputOutput              | Input/output operations per second.            | Composite spec   | "Operations/Second"                                |
| Memory                   | RAM allocated for processing.                  | Data size spec   | "GB" units                                         |
| NetworkInterfaces        | Connections for VMs and web apps.              |                  |                                                    |
| OperatingSystem          |                                                | String           | "Linux", "MacOS", "Windows"                        |
| PerformanceTier          |                                                | String           |                                                    |
| Redundancy               |                                                | String           | "Local", "Geography", "Zone", "Geo-Zone", "Global" |

## Introduced (version)

1.1
