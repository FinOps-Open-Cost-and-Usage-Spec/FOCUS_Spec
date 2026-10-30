# Allocated Tags

The [Allocated Tags](#col) column represents the set of [tags](#term) assigned to [tag sources](#term) which are specifically applicable to [allocated charges](#term) resulting from a data generator-calculated split cost allocation.

## Requirements

[AllocatedTags](#col) MUST adhere to the following requirements:

* [AllocatedTags](#col) MUST be of type JSON Object (serialized as a String where necessary).
* [AllocatedTags](#col) MUST conform to [StringHandling](#attr) requirements.
* [AllocatedTags](#col) MUST conform to [KeyValueFormat](#attr) requirements.
* [AllocatedTags](#col) MUST adhere to the following nullability requirements:
  * [AllocatedTags](#col) MUST be null when a [charge](#term) is not related to a data generator-calculated split cost allocation.
  * [AllocatedTags](#col) MAY be null in all other cases.
* When [AllocatedTags](#col) is not null, [AllocatedTags](#col) MUST adhere to the following requirements:
  * [AllocatedTags](#col) MUST NOT include resource tags already present in [Tags](#col).
  * [AllocatedTags](#col) MUST include all applicable user-defined and data generator-defined tags for the [AllocatedResourceId](#col).
  * Tag keys that do not support corresponding values MUST have a corresponding true (boolean) value set.
  * Tag values MUST match the provided values unless true (boolean) is applied to valueless tags.
* Data generator-defined tags MUST adhere to the following requirements:
  * Data generator-defined tag keys MUST be prefixed with a predetermined, data generator-specified tag key prefix that is unique to each corresponding provider-specified [tag scheme](#term).
  * Data generator-specified tag key prefixes SHOULD be publicly documented.
* User-defined tags MUST adhere to the following requirements:
  * User-defined tag keys MUST match the tag keys assigned to the [tag source](#term) when no [tag scheme](#term)-specific prefix is prepended.
  * User-defined tag keys MUST match the [tag scheme](#term)-specific prefix followed by the tag key assigned to the [tag source](#term) when a [tag scheme](#term)-specific prefix is prepended.
  * User-defined tag keys in all user-defined [tag schemes](#term) MUST include a predetermined, data generator-specified tag key prefix that is unique to each corresponding user-defined [tag scheme](#term) when the data generator has more than one user-defined [tag scheme](#term).

## Data Generator-Defined vs. User-Defined Tags

This example illustrates various tags produced from multiple user-defined and data generator-defined [tag schemes](#term). The first two tags illustrate examples from two different, user-defined [tag schemes](#term). The second tag is produced from a valueless, user-defined [tag scheme](#term), so the data generator also applies `true` as its default value.

The last two tags illustrate examples from two different, data generator-defined [tag schemes](#term).

```json
    {
        "userDefinedTagScheme1/foo": "bar",
        "userDefinedTagScheme2/foo": true,
        "providerDefinedTagScheme1/foo": "bar",
        "providerDefinedTagScheme2/foo": "bar"
    }
```

## Column ID

AllocatedTags

## Display Name

Allocated Tags

## Description

A set of tags assigned to tag sources that are applicable to [allocated charges](#term) in data generator-calculated split cost allocation.

## Content Constraints

| Constraint                 | Value                                           |
| :------------------------- | :---------------------------------------------- |
| Dataset                    | [Cost and Usage](#ds)                           |
| Operating model conditions | [Includes Split Cost Allocation](#omc)                                                  |
| Column type                | Dimension                                       |
| Feature level              | Conditional                                     |
| Allows nulls               | True                                            |
| Data type                  | JSON                                            |
| Value format               | [Key-Value Format](#attr)                       |

## Version Introduced

1.3
