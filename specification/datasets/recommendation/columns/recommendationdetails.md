# Recommendation Details

Recommendation Details represents additional properties of a recommendation that are not expressed in other columns, capturing supporting detail a [*practitioner*](#glossary:practitioner) needs to evaluate a recommendation. Details vary by [*service provider*](#glossary:service-provider), [*service*](#glossary:service), and recommendation type, so properties are conveyed as key-value pairs rather than as a fixed set of columns. Recommendation Details complements [Resource Configuration Details Current](#datasets.recommendation.resourceconfigurationdetailscurrent) and [Resource Configuration Details Recommended](#datasets.recommendation.resourceconfigurationdetailsrecommended), which convey resource configuration specifically, by carrying detail that is not resource configuration, such as pricing properties of a proposed [*SKU*](#glossary:sku) or the metrics a recommendation is derived from.

FOCUS-defined property keys appear in the list below and custom (e.g., service-provider-defined) keys are prefixed with "x_" to make them easy to identify as well as prevent collisions with FOCUS-defined properties introduced in a future release.

## Requirements

RecommendationDetails MUST adhere to the following requirements:

* RecommendationDetails MUST be of type JSON Object (serialized as a String where necessary).
* RecommendationDetails MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* RecommendationDetails MUST conform to [KeyValueFormat](#attributes.key-valueformat) requirements.
* RecommendationDetails property keys SHOULD conform to [PascalCase](#glossary:pascalcase) format.
* RecommendationDetails MUST adhere to the following nullability requirements:
  * RecommendationDetails MUST NOT be null when a recommendation has supporting detail that is not expressed in other columns.
  * RecommendationDetails MUST be null when a recommendation has no supporting detail that is not expressed in other columns.
* When RecommendationDetails is not null, RecommendationDetails MUST adhere to the following requirements:
  * RecommendationDetails MUST NOT include a property that duplicates the value of another [*FOCUS column*](#glossary:FOCUS-column) in the same [*row*](#glossary:row).
  * Property key MUST begin with the string "x_" unless it is a FOCUS-defined property.
  * Property key SHOULD remain consistent across comparable recommendations having that property, and the values for this key SHOULD remain in a consistent format.
  * RecommendationDetails MUST include the FOCUS-defined recommendation property when an equivalent property is included as a custom property.
  * RecommendationDetails SHOULD include all FOCUS-defined recommendation properties that are applicable to the recommendation.
  * RecommendationDetails MAY include FOCUS-defined [SkuPriceDetails](#datasets.costandusage.skupricedetails) properties describing the *SKU* a recommendation proposes.
* FOCUS-defined recommendation properties MUST adhere to the following requirements:
  * Property key MUST match the spelling and casing specified for the FOCUS-defined property.
  * Property value MUST be of the type specified for that property.
  * Property value MUST be denominated in the unit of measure specified for that property when the property holds a numeric value.
* Observed metric properties MUST adhere to the following requirements:
  * Property key MUST combine a metric name and a calculation in the `<MetricName><Calculation>` format.
  * Property key SHOULD use one of the recommended metric names listed below.
  * Property key SHOULD use one of the recommended calculations listed below.
  * Property key MUST express a metric name that is not listed as one of the recommended metric names in PascalCase format.
  * Property key MUST express a calculation that is not listed as one of the recommended calculations in PascalCase format.
  * Property value MUST be of type Numeric.
  * Property value MUST be denominated in the unit of measure specified for that metric name.

## FOCUS-Defined Properties

The following keys should be used when applicable to facilitate cross-service-provider queries for the same conceptual property. Custom (e.g., service-provider-defined) keys are prefixed with "x_".

| Key                        | Description                                                                                | Data Type | Unit of Measure (numeric) or example values (string) |
| :------------------------- | :----------------------------------------------------------------------------------------- | :-------- | :--------------------------------------------------- |
| CommitmentDiscountQuantity | Amount of the [*commitment discount*](#glossary:commitment-discount) proposed for purchase | Numeric   | Measure: Commitment Discount Unit                    |
| CommitmentDiscountUnit     | Unit of measurement for the proposed Commitment Discount Quantity                          | String    | Examples: "Hours", "USD", "DPUs"                     |
| SkuId                      | [SKU](#datasets.costandusage.skuid) proposed by a recommendation                           | String    | Examples: "m5d.2xlarge", "NC24rs_v3"                 |
| SkuPriceId                 | [SKU Price](#datasets.costandusage.skupriceid) proposed by a recommendation                | String    | Examples: "AB12CD34EF56"                             |

In addition to the keys above, any FOCUS-defined [SKU Price](#datasets.costandusage.skupricedetails) property MAY be included to describe the *SKU* a recommendation proposes (e.g., CoreCount, MemorySize, InstanceType).

### Observed Metric Properties

A recommendation is commonly derived from one or more metrics observed over the [evaluation period](#datasets.recommendation.evaluationperiodstart). Observed metric property keys combine a metric name and a calculation in the `<MetricName><Calculation>` format (e.g., `CpuUtilizationAverage`, `MemoryUtilizationP95`), so a recommendation derived from several metrics can convey each one, and each is directly queryable.

The table below lists recommended metric names. A metric name that is not listed can be used as long as it is expressed in [PascalCase](#glossary:pascalcase) format.

| Metric Name       | Description                                | Unit of Measure                    |
| :---------------- | :----------------------------------------- | :--------------------------------- |
| CpuUtilization    | Processor utilization                      | Percent                            |
| DiskUtilization   | Storage capacity utilization               | Percent                            |
| DiskIops          | Storage input/output operations per second | Input/Output Operations per Second |
| MemoryUtilization | Memory utilization                         | Percent                            |
| NetworkThroughput | Network throughput for data transfer       | Megabits per second (Mbps)         |
| RequestCount      | Requests processed                         | Requests                           |

The table below lists recommended calculations. A calculation that is not listed can be used as long as it is expressed in PascalCase format.

| Calculation | Description                                                                                                                                              |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Average     | Arithmetic mean of the values observed over the evaluation period.                                                                                       |
| Count       | Number of observations recorded over the evaluation period.                                                                                              |
| Max         | Largest value observed over the evaluation period.                                                                                                       |
| Median      | Middle value of the observations recorded over the evaluation period.                                                                                    |
| Min         | Smallest value observed over the evaluation period.                                                                                                      |
| P*p*        | Value at the *p*th percentile of the observations recorded over the evaluation period, where *p* is an integer from 1 to 99 (e.g., `P50`, `P95`, `P99`). |
| Total       | Sum of the values observed over the evaluation period.                                                                                                   |

## Examples

```json
{
    "SkuId": "m5d.large",
    "CoreCount": 2,
    "MemorySize": 8,
    "CpuUtilizationAverage": 4.2,
    "CpuUtilizationP95": 11.5,
    "MemoryUtilizationAverage": 18.3,
    "MemoryUtilizationMax": 31.7,
    "x_ConfidenceScore": 0.87
}
```

## Column ID

RecommendationDetails

## Display Name

Recommendation Details

## Description

Additional properties of a recommendation that are not expressed in other columns.

## Content Constraints

| Constraint    | Value                                           |
| :------------ | :---------------------------------------------- |
| Dataset       | [Recommendation](#datasets.recommendation)      |
| Column type   | Dimension                                       |
| Feature level | Mandatory                                       |
| Allows nulls  | True                                            |
| Data type     | JSON                                            |
| Value format  | [Key-Value Format](#attributes.key-valueformat) |

## Version Introduced

1.5
