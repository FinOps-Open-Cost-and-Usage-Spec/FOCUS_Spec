# Resource Configuration Details Current

Resource Configuration Details Current represents the configuration of the [*resource*](#glossary:resource) targeted by a recommendation before the recommended change is applied (for example, an instance size or a storage tier). Resource Configuration Details Current is commonly used to show the starting point of a configuration-change recommendation.

## Requirements

ResourceConfigurationDetailsCurrent MUST adhere to the following requirements:

* ResourceConfigurationDetailsCurrent MUST be of type JSON Object (serialized as a String where necessary).
* ResourceConfigurationDetailsCurrent MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* ResourceConfigurationDetailsCurrent MUST conform to [KeyValueFormat](#attributes.key-valueformat) requirements.
* ResourceConfigurationDetailsCurrent property keys SHOULD conform to [PascalCase](#glossary:pascalcase) format.
* ResourceConfigurationDetailsCurrent MUST adhere to the following nullability requirements:
  * ResourceConfigurationDetailsCurrent MUST NOT be null when a recommendation proposes a change to the configuration of a *resource*.
  * ResourceConfigurationDetailsCurrent MUST be null when a recommendation does not propose a change to the configuration of a *resource*.
* When ResourceConfigurationDetailsCurrent is not null, ResourceConfigurationDetailsCurrent MUST adhere to the following requirements:
  * Property key MUST begin with the string "x_".
  * Property key SHOULD remain consistent across comparable *resources* having that property, and the values for this key SHOULD remain in a consistent format.
  * Existing properties SHOULD remain consistent over time.
  * Additional properties MAY be added over time.

## FOCUS-Defined Properties

FOCUS does not define resource configuration property names in this release. All properties are defined by the [data generator](#metadata.datagenerator) and prefixed with "x_" to prevent collisions with FOCUS-defined properties introduced in a future release.

## Examples

```json
{
  "x_InstanceType": "m5.xlarge",
  "x_VCpuCount": 4,
  "x_MemoryGiB": 16
}
```

## Column ID

ResourceConfigurationDetailsCurrent

## Display Name

Resource Configuration Details Current

## Description

The configuration of the *resource* targeted by a recommendation before the recommended change is applied.

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
