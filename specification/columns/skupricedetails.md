# SKU Price Details

The SKU Price Details column represents a list of relevant properties shared by all charges with the same [SKU Price ID](#skupriceid). These properties provide qualitative and quantitative details about the service represented by a SKU Price ID. This can enable practitioners to calculate metrics such as total units of a service when it is not directly billed in those units (e.g. cores) and thus enables FinOps capabilities such as unit economics. These properties (key-value pairs) can also help a practitioner understand the specifics of a SKU Price ID and differentiate it other SKU Price IDs.

The SkuPriceDetails column adheres to the following requirements:

* SkuPriceDetails MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports unit pricing concepts and publishes [*price lists*](#glossary:price-list), publicly or as part of contracting.
* SkuPriceDetails MUST be of type String.
* SkuPriceDetails MUST conform to [StringHandling](#stringhandling) requirements.
* SkuPriceDetails MUST conform to [KeyValueFormat](#key-valueformat) requirements.
* Property keys SHOULD conform to [PascalCase](#glossary:pascalcase) format.
* SkuPriceDetails nullability is defined as follows:
  * SkuPriceDetails MUST be null when SkuPriceId is null.
  * SkuPriceDetails MAY be null when SkuPriceId is not null.
* When SkuPriceDetails is not null, SkuPriceDetails adheres to the following additional requirements:
  * SkuPriceDetails MUST be associated with a given SkuPriceId.
  * SkuPriceDetails MUST NOT include properties that are not applicable to the corresponding SkuPriceId.
  * SkuPriceDetails SHOULD include all FOCUS-defined SKU Price properties listed below that are applicable to the corresponding SkuPriceId.
  * SkuPriceDetails MAY include properties that are already captured in other dedicated columns.
  * SkuPriceDetails properties for a given SkuPriceId adhere to the following additional requirements:
    * Existing SkuPriceDetails properties SHOULD remain consistent over time.
    * Existing SkuPriceDetails properties SHOULD NOT be removed.
    * Additional SkuPriceDetails properties MAY be added over time.
  * Property key SHOULD remain consistent across comparable SKUs having that property, and the values for this key SHOULD remain in a consistent format.
  * Property key MUST NOT begin with the string "F_" unless it is a FOCUS-defined property.
  * Property value MUST represent the value for a single [PricingUnit](#pricingunit) when the property holds a numeric value.
* FOCUS-defined SKU Price properties adhere to the following additional requirements:
  * Property key MUST equal the predefined key for that property.
  * Property value MUST be of the type specified for that property.
  * Property value MUST represent the value for a single PricingUnit, denominated in the unit of measure specified for that property when the property holds a numeric value.

## Examples

```json
{
    "F_StorageClass": "Archive",
    "F_CoreCount": 4,
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

### FOCUS-Defined Properties

The following keys should be used when applicable to facilitate cross-SKU and cross-provider queries for the same conceptual property. FOCUS-defined keys will be prefixed with "F_" to make them easy to identify and prevent collisions with other properties conveyed by a provider.

| Key                        | Description                                                     | Data Type        | Unit of Measure (numeric) or example values (string)  |
| :------------------------- | :-------------------------------------------------------------- | :--------------- | :---------------------------------------------------- |
| F_Bandwidth                | Network capacity for data transfer                              | Numeric          | Measure: Megabits per second (Mbps)                   |
| F_CoreCount                | Number of physical or virtual CPUs available                    | Numeric          | Measure: Quantity of Cores                            |
| F_DiskSpace                | Storage capacity available                                      | Numeric          | Measure: Gibibytes (GiB)                              |
| F_DiskType                 | Kind of disk used                                               | String           | Examples: "SSD", "HDD", "NVMe"                        |
| F_GpuCount                 | Number of GPUs available                                        | Numeric          | Measure: Quantity of GPUs                             |
| F_InputOutput              | Input/output operations per second                              | Numeric          | Measure: Input/Output Operations per Second (IOPS)    |
| F_InstanceType             | Common name of the instance including size, shape, series, etc. | String           | Examples: "m5d.2xlarge", "NC24rs_v3", "P50"           |
| F_MemorySize               | RAM allocated for processing                                    | Numeric          | Measure: Gibibytes (GiB<sup>1</sup>)                  |
| F_OperatingSystem          | Operating system family<sup>2</sup>                             | String           | Examples: "Linux", "MacOS", "Windows"                 |
| F_Redundancy               | Level of redundancy offered by the SKU                          | String           | Examples: "Local", "Zonal", "Global"                  |
| F_Series                   | Common name for the series and/or generation of the SKU         | String           | Examples: "M5", "Dadv5", "N2D"                        |
| F_SizeClass                | Logical grouping of size, which may be used for size fexibility | String           | Examples: "Large", "2xlarge", "Metal"                 |
| F_StorageClass             | Class or tier of storage provided                               | String           | Examples: "Hot", "Archive", "Nearline"                |

Notes
<br><sup>1</sup> Memory manufacturers still commonly uses "GB" to refer to 2<sup>30</sup> bytes, which is known as GiB in other contexts.
<br><sup>2</sup> This is the operating system family of the SKU, if it's included with the SKU or the SKU only supports one type of operating system.

## Introduced (version)

1.1
