# SKU Price Details

SKU Price Details represent a list of [*SKU Price*](#glossary:sku-price) properties (key-value pairs) associated with a specific [SKU Price ID](#skupriceid). These properties include qualitative and quantitative properties of a [*SKUs*](#glossary:sku) (e.g., functionality and technical specifications), along with core stable pricing properties (e.g., pricing terms, tiers, etc.), excluding dynamic or negotiable pricing elements such as unit price amounts, currency (and related exchange rates), temporal validity (e.g., effective dates), and contract- or negotiation-specific factors (e.g., contract or account identifiers, and negotiable discounts).

The composition of properties associated with a specific *SKU Price* may differ across providers and across *SKUs* within the same provider. However, the exclusion of dynamic or negotiable pricing properties should ensure that all charges with the same SKU Price ID share the same SKU Price Details, i.e., that SKU Price Details remains consistent across different billing periods and billing accounts within a provider.

SKU Price Details helps practitioners understand and distinguish *SKU Prices*, each identified by a SKU Price ID and associated with a used or purchased [*resource*](#glossary:resource) or [*service*](#glossary:service). It can also enable practitioners to calculate metrics such as total units of a SKU when it is not directly priced in those units (e.g. cores) and thus enables FinOps capabilities such as unit economics. Additionally, the SKU Price Details may be used to analyze costs based on pricing properties such as terms and tiers.

The SkuPriceDetails column adheres to the following requirements:

* SkuPriceDetails MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports unit pricing concepts and publishes [*price lists*](#glossary:price-list), publicly or as part of contracting.
* SkuPriceDetails MUST conform to [KeyValueFormat](#key-valueformat) requirements.
* SkuPriceDetails property keys SHOULD conform to [PascalCase](#glossary:pascalcase) format.
* SkuPriceDetails nullability is defined as follows:
  * SkuPriceDetails MUST be null when SkuPriceId is null.
  * SkuPriceDetails MAY be null when SkuPriceId is not null.
* When SkuPriceDetails is not null, SkuPriceDetails adheres to the following additional requirements:
  * SkuPriceDetails MUST be associated with a given SkuPriceId.
  * SkuPriceDetails MUST NOT include properties that are not applicable to the corresponding SkuPriceId.
  * SkuPriceDetails SHOULD include all FOCUS-defined SKU Price properties listed below that are applicable to the corresponding SkuPriceId.
  * SkuPriceDetails MUST include the FOCUS-defined SKU Price property when an equivalent property is included as a Provider-defined property.
  * SkuPriceDetails MAY include properties that are already captured in other dedicated columns.
  * SkuPriceDetails properties for a given SkuPriceId adhere to the following additional requirements:
    * Existing SkuPriceDetails properties SHOULD remain consistent over time.
    * Existing SkuPriceDetails properties SHOULD NOT be removed.
    * Additional SkuPriceDetails properties MAY be added over time.
  * Property key SHOULD remain consistent across comparable SKUs having that property, and the values for this key SHOULD remain in a consistent format.
  * Property key MUST begin with the string "x_" unless it is a FOCUS-defined property.
  * Property value MUST represent the value for a single [PricingUnit](#pricingunit) when the property holds a numeric value.
* FOCUS-defined SKU Price properties adhere to the following additional requirements:
  * Property key MUST match the spelling and casing specified for the FOCUS-defined property.
  * Property value MUST be of the type specified for that property.
  * Property value MUST represent the value for a single PricingUnit, denominated in the unit of measure specified for that property when the property holds a numeric value.

## Examples

```json
{
    "StorageClass": "Archive",
    "CoreCount": 4,
    "x_PremiumProcessing": true,
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
| Data type     | JSON                               |
| Value format  | [KeyValueFormat](#key-valueformat) |

### FOCUS-Defined Properties

The following keys should be used when applicable to facilitate cross-SKU and cross-provider queries for the same conceptual property. Focus-defined keys will appear in the list below and Provider-defined keys will be prefixed with "x_" to make them easy to identify as well as prevent collisions.

| Key                      | Description                                                     | Data Type        | Unit of Measure (numeric) or example values (string)  |
| :----------------------- | :-------------------------------------------------------------- | :--------------- | :---------------------------------------------------- |
| CoreCount                | Number of physical or virtual CPUs available<sup>1</sup>        | Numeric          | Measure: Quantity of Cores                            |
| DiskIops                 | Storage input/output operations per second<sup>1</sup>          | Numeric          | Measure: Input/Output Operations per Second (IOPS)    |
| DiskSpace                | Storage capacity available                                      | Numeric          | Measure: Gibibytes (GiB)                              |
| DiskType                 | Kind of disk used                                               | String           | Examples: "SSD", "HDD", "NVMe"                        |
| GpuCount                 | Number of GPUs available                                        | Numeric          | Measure: Quantity of GPUs                             |
| InstanceType             | Common name of the instance including size, shape, series, etc. | String           | Examples: "m5d.2xlarge", "NC24rs_v3", "P50"           |
| InstanceSeries           | Common name for the series and/or generation of the instance    | String           | Examples: "M5", "Dadv5", "N2D"                        |
| MemorySize               | RAM allocated for processing                                    | Numeric          | Measure: Gibibytes (GiB<sup>2</sup>)                  |
| NetworkBandwidth         | Network capacity for data transfer<br><sup>1</sup>              | Numeric          | Measure: Megabits per second (Mbps)                   |
| NetworkIops              | Network input/output operations per second<br><sup>1</sup>      | Numeric          | Measure: Input/Output Operations per Second (IOPS)    |
| OperatingSystem          | Operating system family<sup>3</sup>                             | String           | Examples: "Linux", "MacOS", "Windows"                 |
| Redundancy               | Level of redundancy offered by the SKU                          | String           | Examples: "Local", "Zonal", "Global"                  |
| StorageClass             | Class or tier of storage provided                               | String           | Examples: "Hot", "Archive", "Nearline"                |

Notes
<br><sup>1</sup> In the case of "burstable" SKUs offering variable levels of performance, the baseline or guaranteed value should be used.
<br><sup>2</sup> Memory manufacturers still commonly uses "GB" to refer to 2<sup>30</sup> bytes, which is known as GiB in other contexts.
<br><sup>3</sup> This is the operating system family of the SKU, if it's included with the SKU or the SKU only supports one type of operating system.

## Introduced (version)

1.1
