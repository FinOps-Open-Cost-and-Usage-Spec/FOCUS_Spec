# Recommendation Details

Recommendation Details represents additional properties of a recommendation that are not expressed in other columns, capturing supporting detail a [*practitioner*](#glossary:practitioner) needs to evaluate a recommendation. Details vary by [*service provider*](#glossary:service-provider), [*service*](#glossary:service), and recommendation type, so properties are conveyed as key-value pairs rather than as a fixed set of columns. Recommendation Details complements [Resource Configuration Details Current](#datasets.recommendation.resourceconfigurationdetailscurrent) and [Resource Configuration Details Recommended](#datasets.recommendation.resourceconfigurationdetailsrecommended), which convey resource configuration specifically, by carrying detail that is not resource configuration, such as pricing properties of a proposed [*SKU*](#glossary:sku) or the metrics a recommendation is derived from.

FOCUS-defined property keys appear in the list below and custom (e.g., service-provider-defined) keys are prefixed with "x_" to make them easy to identify as well as prevent collisions with FOCUS-defined properties introduced in a future release.

## Requirements

RecommendationDetails MUST adhere to the following requirements:

* RecommendationDetails MUST be of type JSON Object (serialized as a String where necessary).
* RecommendationDetails MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* RecommendationDetails MUST conform to [KeyValueFormat](#attributes.key-valueformat) requirements.
* RecommendationDetails property keys SHOULD conform to [PascalCase](#glossary:pascalcase) format.
* RecommendationDetails MUST be null when a recommendation has no additional properties.
* When RecommendationDetails is not null, RecommendationDetails MUST adhere to the following requirements:
  * RecommendationDetails MUST NOT include a property that duplicates the value of another [*FOCUS column*](#glossary:FOCUS-column) in the same [*row*](#glossary:row).
  * Property key MUST begin with the string "x_" unless it is a FOCUS-defined property.
  * Property key SHOULD remain consistent across comparable recommendations having that property, and the values for this key SHOULD remain in a consistent format.
  * RecommendationDetails MUST include the FOCUS-defined recommendation property when an equivalent property is included as a custom property.
  * RecommendationDetails SHOULD include all FOCUS-defined recommendation properties listed below that are applicable to the recommendation.
  * Property key SHOULD remain consistent across comparable recommendations having that property, and the values for this key SHOULD remain in a consistent format.
  * Property key MUST begin with the string "x_" unless it is a FOCUS-defined property.
* FOCUS-defined recommendation properties MUST adhere to the following requirements:
  * Property key MUST match the spelling and casing specified for the FOCUS-defined property.
  * Property value MUST be of the type specified for that property.

## FOCUS-Defined Properties

The following keys should be used when applicable to facilitate cross-service-provider queries for the same conceptual property. Custom (e.g., service-provider-defined) keys are prefixed with "x_".

| Key                        | Description                                                                                | Data Type | Unit of Measure (numeric) or example values (string) |
| :------------------------- | :----------------------------------------------------------------------------------------- | :-------- | :--------------------------------------------------- |
| CommitmentDiscountQuantity | Amount of the [*commitment discount*](#glossary:commitment-discount) proposed for purchase | Numeric   | Measure: Commitment Discount Unit                    |
| CommitmentDiscountUnit     | Unit of measurement for the proposed Commitment Discount Quantity                          | String    | Examples: "Hours", "USD", "DPUs"                     |
| ObservedMetricName         | Name of the metric a recommendation was derived from                                       | String    | Examples: "CpuUtilization", "MemoryUtilization"      |
| ObservedMetricUnit         | Unit of measurement for the Observed Metric Value                                          | String    | Examples: "Percent", "GiB", "Requests"               |
| ObservedMetricValue        | Value of the metric a recommendation was derived from                                      | Numeric   | Measure: Observed Metric Unit                        |
| SkuId                      | [SKU](#datasets.costandusage.skuid) proposed by a recommendation                           | String    | Examples: "m5d.2xlarge", "NC24rs_v3"                 |
| SkuPriceId                 | [SKU Price](#datasets.costandusage.skupriceid) proposed by a recommendation                | String    | Examples: "AB12CD34EF56"                             |

## Examples

```json
{
    "SkuId": "m5d.2xlarge",
    "ObservedMetricName": "CpuUtilization",
    "ObservedMetricValue": 4.2,
    "ObservedMetricUnit": "Percent",
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

| Constraint      | Value                                           |
| :-------------- | :---------------------------------------------- |
| Dataset         | [Recommendation](#datasets.recommendation)      |
| Column type     | Dimension                                       |
| Feature level   | Mandatory                                       |
| Allows nulls    | True                                            |
| Data type       | JSON                                            |
| Value format    | [Key-Value Format](#attributes.key-valueformat) |

## Version Introduced

1.5
