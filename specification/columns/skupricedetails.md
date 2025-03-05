# SKU Price Details

The SKU Price Details column represents a list of relevant properties shared by all charges with the same [SKU Price ID](#skupriceid). These properties provide qualitative and quantitative details about the service represented by a SKU Price ID. This can enable practitioners to calculate metrics such as total units of a service when it is not directly billed in those units (e.g. cores) and thus enables FinOps capabilities such as unit economics. These properties (key-value pairs) can also help a practitioner understand the specifics of a SKU Price ID and differentiate it other SKU Price IDs.

The SkuPriceDetails column adheres to the following requirements:

* SkuPriceDetails MUST be in [KeyValueFormat](#key-valueformat).
* SkuPriceDetails keys SHOULD be formatted in [PascalCase](#glossary:pascalcase).
* SkuPriceDetails properties (both keys and values) MUST be shared across all charges having the same SkuPriceId, subject to the below provisions.
  * Additional properties MAY be added to SkuPriceDetails going forward for a given SkuPriceId.
  * Properties SHOULD NOT be removed from SkuPriceDetails for a given SkuPriceId, once they have been included.
  * Individual properties SHOULD NOT be modified for a given SkuPriceId and SHOULD remain consistent over time.
* SkuPriceDetails keys and their values SHOULD remain consistent across comparable SKUs having that property.
* SkuPriceDetails MUST NOT contain properties which are not applicable to the corresponding SkuPriceId.
* SkuPriceDetails MAY contain properties which are already captured in other dedicated columns.
* SkuPriceDetails properties with a [numeric](#numeric-format) value MUST represent the value for a single [PricingUnit](#pricingunit).
* SkuPriceDetails properties that represent common constructs listed in the Predefined Keys section below SHOULD use the predefined keys.
  * Values for predefined keys SHOULD be the specified data type for that key in the section below.
  * Numeric values for predefined keys SHOULD be the specified unit of measure for that key in the section below.
* SkuPriceDetails MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider includes a SkuPriceId.
  * SkuPriceDetails MAY be null when SkuPriceId is not null.
  * SkuPriceDetails MUST be null when SkuPriceId is null.

## Examples

```json
{
    "AccessTier": "Archive",
    "CoreCount": 4,
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

| Constraint    | Value                              |
| :------------ | :--------------------------------- |
| Column type   | Dimension                          |
| Feature level | Conditional                        |
| Allows nulls  | True                               |
| Data type     | String                             |
| Value format  | [KeyValueFormat](#key-valueformat) |

### Predefined Keys

The following keys should be used when applicable to facilitate cross-service and cross-provider queries for the same conceptual property.

| Key                      | Description                                       | Data Type        | Unit of Measure (numeric) or example values (string)  |
| :----------------------- | :------------------------------------------------ | :--------------- | :---------------------------------------------------- |
| Bandwidth                | Network capacity for data transfer                | Numeric          | Measure: Megabits per second (Mbps)                   |
| CoreCount                | Number of physical or virtual CPUs available      | Numeric          | Measure: Quantity of Cores                            |
| DiskSpace                | Storage capacity available                        | Numeric          | Measure: Gibibytes (GiB)                              |
| DiskType                 | Kind of disk used                                 | String           | Examples: "SSD", "HDD", "NVMe"                        |
| GpuCount                 | Number of GPUs available                          | Numeric          | Measure: Quantity of GPUs                             |
| InputOutput              | Input/output operations per second                | Numeric          | Measure: Input/Output Operations per Second (IOPS)    |
| MemorySize               | RAM allocated for processing                      | Numeric          | Measure: Gibibytes (GiB<sup>1</sup>)                  |
| OperatingSystem          | Operating system family<sup>2</sup>               | String           | Examples: "Linux", "MacOS", "Windows"                 |
| PerformanceTier          |                                                   | String           |                                                       |
| PricingTier              | Category of pricing applicable to SkuPriceId      | String           | Examples: "Free", "Standard", "Preview"               |
| Redundancy               | Level of redundancy offered by the SKU            | String           | Examples: "Local", "Zonal", "Global"                  |
| StorageTier              | Tier or class of storage provided                 | String           | Examples: "Hot", "Archive", "Nearline"                |

Notes
<sup>1</sup> Memory manufacturers still commonly uses "GB" to refer to 2<sup>30</sup> bytes, which is known as GiB in other contexts.
<sup>2</sup> This is the operating system family of the SKU, if it's included with the SKU or the SKU only supports one type of operating system.

## Introduced (version)

1.1
