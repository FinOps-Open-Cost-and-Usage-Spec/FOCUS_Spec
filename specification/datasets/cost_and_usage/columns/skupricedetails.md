# SKU Price Details

[SKU Price Details](#col) represent a list of [SKU Price](#term) properties (key-value pairs) associated with a specific [SKU Price ID](#col). These properties include qualitative and quantitative properties of a [SKU](#term) (e.g., functionality and technical specifications), along with core stable pricing properties (e.g., pricing [periods](#term) and tiers).

[SKU Price Details](#col) exclude dynamic or negotiable pricing elements such as unit price amounts, currency, [foreign exchange](#term) rates, effective dates, contract or account identifiers, and negotiated discounts. However, modifications to the pricing structure itself (such as a negotiated tier configuration) are included.

The composition of properties associated with a specific [SKU Price](#term) may differ across service providers and across [SKUs](#term) within the same service provider. However, the exclusion of dynamic or negotiable pricing elements should ensure that all [charges](#term) with the same [SKU Price ID](#col) share the same [SKU Price Details](#col), i.e., that [SKU Price Details](#col) remains consistent across different [billing periods](#term) and [billing accounts](#term) within a service provider.

[SKU Price Details](#col) helps practitioners understand and distinguish [SKU Prices](#term), each identified by a [SKU Price ID](#col) and associated with a used or purchased [resource](#term) or [service](#term). It can also help determine the quantity of units for a property when it holds a numeric value (e.g., CoreCount), even when its unit differs from the one in which the [SKU](#term) is priced and charged, thus supporting FinOps capabilities such as unit economics. Additionally, the [SKU Price Details](#col) may be used to analyze costs based on pricing properties such as [periods](#term) and tiers.

## Requirements

[SkuPriceDetails](#col) MUST adhere to the following requirements:

* [SkuPriceDetails](#col) MUST be of type JSON Object (serialized as a String where necessary).
* [SkuPriceDetails](#col) MUST conform to [StringHandling](#attr) requirements.
* [SkuPriceDetails](#col) MUST conform to [KeyValueFormat](#attr) requirements.
* [SkuPriceDetails](#col) property keys SHOULD conform to [PascalCase](#term) format.
* [SkuPriceDetails](#col) MUST adhere to the following nullability requirements:
  * [SkuPriceDetails](#col) MUST be null when [SkuPriceId](#col) is null.
  * [SkuPriceDetails](#col) MAY be null when [SkuPriceId](#col) is not null.
* When [SkuPriceDetails](#col) is not null, [SkuPriceDetails](#col) MUST adhere to the following requirements:
  * [SkuPriceDetails](#col) MUST be associated with a given [SkuPriceId](#col).
  * [SkuPriceDetails](#col) MUST include the FOCUS-defined SKU Price property when an equivalent property is included as a custom property.
  * [SkuPriceDetails](#col) MUST NOT include properties that are not applicable to the corresponding [SkuPriceId](#col).
  * [SkuPriceDetails](#col) MUST NOT include TokenCacheAction when the [SKU Price](#term) does not meter [tokens](#term) consumed from a request (e.g., tokens generated in a response, or a charge for retaining cached content metered in token-hours).
  * [SkuPriceDetails](#col) MUST NOT include TokenCacheAction when the [SKU Price](#term) meters request tokens served from or placed into a [prompt cache](#term) together with request tokens that were not (e.g., request tokens billed on one meter whether or not they were placed into a [prompt cache](#term)).
  * [SkuPriceDetails](#col) MUST NOT include TokenDirection when the [SKU Price](#term) does not meter [tokens](#term) (e.g., a charge for retaining cached content metered in token-hours).
  * [SkuPriceDetails](#col) MUST NOT include TokenDirection when the [SKU Price](#term) meters both tokens consumed from a request and tokens generated in a response.
  * [SkuPriceDetails](#col) SHOULD include all FOCUS-defined SKU Price properties listed below that are applicable to the corresponding [SkuPriceId](#col).
  * [SkuPriceDetails](#col) SHOULD include TokenCacheAction when the [SKU Price](#term) meters only tokens consumed from a request, except when the [SKU Price](#term) meters request tokens served from or placed into a [prompt cache](#term) together with request tokens that were not.
  * [SkuPriceDetails](#col) SHOULD include TokenDirection when the [SKU Price](#term) meters only input or only output tokens.
  * [SkuPriceDetails](#col) SHOULD include all custom SKU Price properties that are applicable to the corresponding [SkuPriceId](#col) when there is no equivalent FOCUS-defined property.
  * [SkuPriceDetails](#col) MAY include properties that are already captured in other dedicated columns.
  * [SkuPriceDetails](#col) properties for a given [ServiceProviderName](#col) and [SkuPriceId](#col) MUST adhere to the following requirements:
    * Existing [SkuPriceDetails](#col) properties SHOULD remain consistent over time.
    * Existing [SkuPriceDetails](#col) properties SHOULD NOT be removed.
    * Additional [SkuPriceDetails](#col) properties MAY be added over time.
  * Property key SHOULD remain consistent across comparable [SKUs](#term) having that property, and the values for this key SHOULD remain in a consistent format.
  * Property key MUST begin with the string "x_" unless it is a FOCUS-defined property.
  * Property value MUST represent the value for a single [PricingUnit](#col) when the property holds a numeric value.
* FOCUS-defined SKU Price properties MUST adhere to the following requirements:
  * Property key MUST match the spelling and casing specified for the FOCUS-defined property.
  * Property value MUST be of the type specified for that property.
  * Property value MUST represent the value for a single [PricingUnit](#col), denominated in the unit of measure specified for that property when the property holds a numeric value.
  * Property value MUST be one of the allowed values specified for that property when allowed values are specified.
* When included, TokenCacheAction MUST adhere to the following requirements:
  * TokenCacheAction MUST be "Read" when the [SKU Price](#term) meters only tokens served from a [prompt cache](#term).
  * TokenCacheAction MUST be "Write" when the [SKU Price](#term) meters only tokens placed into a [prompt cache](#term) (e.g., a charge a service provider meters as cache creation).
  * TokenCacheAction MUST be "Uncached" when the [SKU Price](#term) meters only request tokens neither served from nor placed into a [prompt cache](#term) (e.g., input tokens that a service provider meters separately from its cache reads and cache writes).
  * TokenCacheAction MUST be "Other" when the [SKU Price](#term) meters a cache-related token charge to which none of the other allowed values apply.
* When included, TokenDirection MUST adhere to the following requirements:
  * TokenDirection MUST be "Input" when the [SKU Price](#term) meters tokens consumed from a request.
  * TokenDirection MUST be "Output" when the [SKU Price](#term) meters tokens generated in a response.

## FOCUS-Defined Properties

The following keys should be used when applicable to facilitate cross-SKU and cross-service-provider queries for the same conceptual property. FOCUS-defined keys will appear in the list below and custom (e.g., service-provider-defined) keys will be prefixed with "x_" to make them easy to identify as well as prevent collisions.

| Key                      | Description                                                              | Data Type        | Unit of Measure (numeric) or values (string)          |
| :----------------------- | :----------------------------------------------------------------------- | :--------------- | :---------------------------------------------------- |
| CoreCount                | Number of physical or virtual CPUs available<sup>1</sup>                 | Numeric          | Measure: Quantity of Cores                            |
| DiskMaxIops              | Storage maximum sustained input/output operations per second<sup>1</sup> | Numeric          | Measure: Input/Output Operations per Second (IOPS)    |
| DiskSpace                | Storage capacity available                                               | Numeric          | Measure: Gibibytes (GiB)                              |
| DiskType                 | Kind of disk used                                                        | String           | Examples: "SSD", "HDD", "NVMe"                        |
| GpuCount                 | Number of GPUs available                                                 | Numeric          | Measure: Quantity of GPUs                             |
| InstanceType             | Common name of the instance including size, shape, series, etc.          | String           | Examples: "m5d.2xlarge", "NC24rs_v3", "P50"           |
| InstanceSeries           | Common name for the series and/or generation of the instance             | String           | Examples: "M5", "Dadv5", "N2D"                        |
| MemorySize               | RAM allocated for processing                                             | Numeric          | Measure: Gibibytes (GiB<sup>2</sup>)                  |
| ModelDeveloper           | Name of the entity that created the model                                | String           | Examples: "Solora AI", "ModelMesh"                    |
| ModelFamily              | Grouping of related models as defined by the model developer             | String           | Examples: "Solora Reasoning", "ModelMesh General"     |
| ModelId                  | Identifier for the model as it appears in billing, which may be namespaced by the service provider and is not guaranteed to match across service providers | String           | Examples: "solora-reasoning-pro", "modelmesh-general-7b" |
| ModelVersion             | Version of the model within a given model family, as defined by the model developer | String           | Examples: "3.0", "2.5"                                |
| NetworkMaxIops           | Network maximum sustained input/output operations per second<sup>1</sup> | Numeric          | Measure: Input/Output Operations per Second (IOPS)    |
| NetworkMaxThroughput     | Network maximum sustained throughput for data transfer<sup>1</sup>       | Numeric          | Measure: Megabits per second (Mbps)                   |
| OperatingSystem          | Operating system family<sup>3</sup>                                      | String           | Examples: "Linux", "MacOS", "Windows"                 |
| Redundancy               | Level of redundancy offered by the SKU                                   | String           | Examples: "Local", "Zonal", "Global"                  |
| StorageClass             | Class or tier of storage provided                                        | String           | Examples: "Hot", "Archive", "Nearline"                |
| TokenCacheAction         | Interaction of the metered tokens with a cache<sup>4</sup>               | String           | Allowed values: "Uncached", "Read", "Write", "Other"  |
| TokenDirection           | Direction of the metered tokens, into or out of the model<sup>4</sup>    | String           | Allowed values: "Input", "Output"                     |

> **Notes:**
>
> 1. In the case of "burstable" SKUs offering variable levels of performance, the baseline or guaranteed value should be used.
> 2. Memory manufacturers still commonly use "GB" to refer to 2<sup>30</sup> bytes, which is known as GiB in other contexts.
> 3. This is the operating system family of the SKU, if it's included with the SKU or the SKU only supports one type of operating system.
> 4. TokenDirection applies to SKUs that meter tokens in one direction only, and TokenCacheAction to SKUs that meter only tokens consumed from a request. The requirements above state when each property applies and what each value identifies. A SKU that bills request tokens on one meter whether or not they were served from or placed into a cache carries no TokenCacheAction, because "Uncached" would misdescribe the tokens that interacted with the cache, and TokenDirection still identifies its tokens as input. Because null is not one of the allowed values, TokenCacheAction is omitted rather than set to null when the interaction of the metered tokens with a cache is not known. [Consumed Quantity](#col) requirements state that a token counted on a "Read" or "Write" row is not also counted on a row that carries neither value. The model developer defines which cache interactions and which token directions a model distinguishes. Which of those a service provider meters as its own charge, and the meter name it uses, vary across service providers and across model versions, so each property identifies one attribute of the metered tokens independently of how a given service provider names its meters. Reasoning tokens are generated in a response, so a SKU that meters them separately carries TokenDirection "Output". Dimensions that qualify a charge without describing the direction of its tokens or their interaction with a cache, such as token modality, reasoning effort, cache retention duration, and context window size, are not values of these properties. [Examples: AI Prompt Caching](#appendix.examples:aipromptcaching) shows both properties on two service providers that meter cache activity differently.

## Examples

```json
{
    "StorageClass": "Archive",
    "CoreCount": 4,
    "x_PremiumProcessing": true
}
```

## Column ID

SkuPriceDetails

## Display Name

SKU Price Details

## Description

A set of properties of a [SKU Price ID](#col) which are meaningful and common to all instances of that [SKU Price ID](#col).

## Content Constraints

| Constraint                 | Value                                           |
| :------------------------- | :---------------------------------------------- |
| Dataset                    | [Cost and Usage](#ds)                           |
| Operating model conditions | [Includes Unit Pricing](#omc)                                          |
| Column type                | Dimension                                       |
| Feature level              | Conditional                                     |
| Allows nulls               | True                                            |
| Data type                  | JSON                                            |
| Value format               | [Key-Value Format](#attr)                       |

## Version Introduced

1.1
