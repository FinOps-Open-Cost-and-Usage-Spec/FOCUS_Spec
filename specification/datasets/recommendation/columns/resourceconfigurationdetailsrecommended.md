# Resource Configuration Details Recommended

Resource Configuration Details Recommended represents the configuration of the [*resource*](#glossary:resource) that a recommendation proposes to change to (for example, a smaller instance size or a newer storage tier). Resource Configuration Details Recommended is commonly used alongside [Resource Configuration Details Current](#datasets.recommendation.resourceconfigurationdetailscurrent) to show the target state of a configuration-change recommendation.

## Requirements

ResourceConfigurationDetailsRecommended MUST adhere to the following requirements:

* ResourceConfigurationDetailsRecommended MUST be of type JSON Object (serialized as a String where necessary).
* ResourceConfigurationDetailsRecommended MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* ResourceConfigurationDetailsRecommended MUST conform to [KeyValueFormat](#attributes.key-valueformat) requirements.
* ResourceConfigurationDetailsRecommended property keys SHOULD conform to [PascalCase](#glossary:pascalcase) format.
* ResourceConfigurationDetailsRecommended MUST adhere to the following nullability requirements:
  * ResourceConfigurationDetailsRecommended MUST NOT be null when a recommendation proposes a change to the configuration of a *resource*, except when the recommended change is the removal of the *resource*.
  * ResourceConfigurationDetailsRecommended MUST be null when the recommended change is the removal of the *resource*.
  * ResourceConfigurationDetailsRecommended MUST be null when a recommendation does not propose a change to the configuration of a *resource*.
* When ResourceConfigurationDetailsRecommended is not null, ResourceConfigurationDetailsRecommended MUST adhere to the following requirements:
  * Property key MUST begin with the string "x_".
  * Property key SHOULD remain consistent across comparable *resources* having that property, and the values for this key SHOULD remain in a consistent format.
  * ResourceConfigurationDetailsRecommended SHOULD convey the same properties as ResourceConfigurationDetailsCurrent when ResourceConfigurationDetailsCurrent is not null.

## FOCUS-Defined Properties

FOCUS does not define resource configuration property names in this release. All properties are defined by the [data generator](#metadata.datagenerator) and prefixed with "x_" to prevent collisions with FOCUS-defined properties introduced in a future release.

## Examples

```json
{
  "x_InstanceType": "m5.large",
  "x_VCpuCount": 2,
  "x_MemoryGiB": 8
}
```

## Column ID

ResourceConfigurationDetailsRecommended

## Display Name

Resource Configuration Details Recommended

## Description

The configuration of the *resource* that a recommendation proposes to change to.

## Content Constraints

| Constraint      | Value                                          |
| :-------------- | :--------------------------------------------- |
| Dataset         | [Recommendation](#datasets.recommendation)     |
| Column type     | Dimension                                      |
| Feature level   | Conditional                                    |
| Allows nulls    | True                                           |
| Data type       | JSON                                           |
| Value format    | [Key-Value Format](#attributes.key-valueformat) |

## Version Introduced

1.5
