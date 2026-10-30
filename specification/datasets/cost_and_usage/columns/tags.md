# Tags

The [Tags](#col) column represents the set of [tags](#term) assigned to [tag sources](#term) that also account for potential provider-defined or user-defined tag evaluations. [Tags](#col) are commonly used for scenarios like adding business context to cost and usage data to identify and accurately allocate [charges](#term). [Tags](#col) may also be referred to by data generators using other terms such as labels.

A tag becomes [finalized](#term:finalized-tag) when a single value is selected from a set of possible tag values assigned to the tag key. When supported by a data generator, this can occur when a tag value is set by provider-defined or user-defined rules.

## Requirements

[Tags](#col) MUST adhere to the following requirements:

* [Tags](#col) MUST be of type JSON Object (serialized as a String where necessary).
* [Tags](#col) MUST conform to [StringHandling](#attr) requirements.
* [Tags](#col) MUST conform to [KeyValueFormat](#attr) requirements.
* [Tags](#col) MAY be null.
* When [Tags](#col) is not null, [Tags](#col) MUST adhere to the following requirements:
  * [Tags](#col) MUST include all user-defined and provider-defined tags.
  * [Tags](#col) MUST only include finalized tags.
  * [Tags](#col) SHOULD include tag keys with corresponding non-null values for a given [resource](#term).
  * [Tags](#col) MAY include tag keys with a null value for a given [resource](#term) depending on the data generator's tag finalization process.
  * Tag keys that do not support corresponding values, MUST have a corresponding true (boolean) value set.
  * Tag values MUST match the provided values unless true (boolean) is applied to valueless tags.
* Provider-defined tags MUST adhere to the following requirements:
  * Provider-defined tag keys MUST be prefixed with a predetermined, provider-specified tag key prefix that is unique to each corresponding provider-specified [tag scheme](#term).
  * Provider-specified tag key prefixes SHOULD be publicly documented.
* User-defined tags MUST adhere to the following requirements:
  * User-defined tag keys MUST match the tag keys assigned to the [tag source](#term) when no [tag scheme](#term)-specific prefix is prepended.
  * User-defined tag keys MUST match the [tag scheme](#term)-specific prefix followed by the tag key assigned to the [tag source](#term) when a [tag scheme](#term)-specific prefix is prepended.
  * User-defined tag keys in all but one user-defined [tag scheme](#term) MUST include a predetermined, provider-specified tag key prefix that is unique to each corresponding user-defined [tag scheme](#term) when the data generator has more than one user-defined [tag scheme](#term).
  * User-defined tag keys MUST NOT include a [tag scheme](#term)-specific prefix when the data generator has only one user-defined [tag scheme](#term).
  * Reserved tag key prefixes MUST be prevented from being used as prefixes for any user-defined tag keys within a prefixless user-defined [tag scheme](#term).
* Tag finalization documentation MUST adhere to the following requirements:
  * Tag finalization documentation SHOULD include tag finalization methods and semantics.
  * Tag finalization documentation SHOULD be accessible to practitioners.

## Provider-Defined vs. User-Defined Tags

This example illustrates various tags produced from multiple user-defined and provider-defined [tag schemes](#term). The first three tags illustrate examples from three different, user-defined [tag schemes](#term). The data generator predetermined that one user-defined [tag scheme](#term) (i.e., `"foo": "bar"`) does not have a prepended prefix, but the remaining two user-defined [tag schemes](#term) (i.e., `"userDefinedTagScheme2/foo": "bar"`, `"userDefinedTagScheme3/foo": true`) do have provider-defined and reserved prefixes. Additionally, the third tag is produced from a valueless, user-defined [tag scheme](#term), so the data generator also applies `true` as its default value.

The last two tags illustrate examples from two different, provider-defined [tag schemes](#term). Since all provider-defined [tag schemes](#term) require a prefix, the data generator has prepended predefined and reserved prefixes (`providerDefinedTagScheme1/`, `providerDefinedTagScheme2/`) to each tag.

```json
    {
        "foo": "bar",
        "userDefinedTagScheme2/foo": "bar",
        "userDefinedTagScheme3/foo": true,
        "providerDefinedTagScheme1/foo": "bar",
        "providerDefinedTagScheme2/foo": "bar"
    }
```

## Finalized Tags

Within a data generator, tag keys may be associated with multiple values, and potentially defined at different levels within the data generator, such as accounts, folders, [resource](#term) and other [resource](#term) grouping constructs. When finalizing, the *data generator* reduces these multiple levels of definition to a single value where each key is associated with exactly one value. The method by which this is done and the semantics are up to each data generator and are documented within their respective documentation.

As an example, assume one [sub account](#term) exists with one virtual machine with the following details, and tag inheritance favors Resources over [Sub Accounts](#term).

* Sub Account
  * id: *my-sub-account*
  * user-defined tags: *team:ops*, *env:prod*
* Virtual Machine
  * id: *my-vm*
  * user-defined tags: *team:web*

The table below represents a finalized dataset with these [resources](#term). It also shows the finalized state after all resource-oriented, tag inheritance rules are processed.

| ResourceType    | ResourceId     | Tags                                        |
| :---------------| :--------------| :-------------------------------------------|
| Sub Account     | my-sub-account | { "team": "ops", "env": "prod" }            |
| Virtual Machine | my-vm          | { "team": "web", *"env": "prod"* }          |

Because the Virtual Machine Resource did not have an `env` tag, it inherited tag, `env:prod` (italicized), from its parent [sub account](#term). Conversely, because the Virtual Machine Resource already has a `team` tag (`team:web`), it did not inherit `team:ops` from its parent [sub account](#term).

## Column ID

Tags

## Display Name

Tags

## Description

The set of tags assigned to [tag sources](#term) that account for potential provider-defined or user-defined tag evaluations.

## Content Constraints

| Constraint                 | Value                                           |
| :------------------------- | :---------------------------------------------- |
| Dataset                    | [Cost and Usage](#ds)                           |
| Operating model conditions | [Includes Tags](#omc)                                   |
| Column type                | Dimension                                       |
| Feature level              | Conditional                                     |
| Allows nulls               | True                                            |
| Data type                  | JSON                                            |
| Value format               | [Key-Value Format](#attr)                       |

## Version Introduced

1.0-preview
