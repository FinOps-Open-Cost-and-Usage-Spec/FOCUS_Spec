# Recommendation Details

Recommendation Details represents additional properties of a recommendation that are not expressed in other columns, capturing supporting detail a [*practitioner*](#glossary:practitioner) needs to evaluate a recommendation. Details vary by [*service provider*](#glossary:service-provider), [*service*](#glossary:service), and recommendation type, so properties are conveyed as key-value pairs rather than as a fixed set of columns. Recommendation Details complements [Resource Configuration Details Current](#datasets.recommendation.resourceconfigurationdetailscurrent) and [Resource Configuration Details Recommended](#datasets.recommendation.resourceconfigurationdetailsrecommended), which convey resource configuration specifically, by carrying detail that is not resource configuration, such as pricing properties of a proposed [*SKU*](#glossary:sku) or the observed metrics a recommendation is derived from.

## Requirements

RecommendationDetails MUST adhere to the following requirements:

* RecommendationDetails MUST be of type JSON Object (serialized as a String where necessary).
* RecommendationDetails MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* RecommendationDetails MUST conform to [KeyValueFormat](#attributes.key-valueformat) requirements.
* RecommendationDetails MUST be null when a recommendation has no additional properties.
* RecommendationDetails MUST NOT include a property that duplicates the value of another [*FOCUS column*](#glossary:FOCUS-column) in the same [*row*](#glossary:row).

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
