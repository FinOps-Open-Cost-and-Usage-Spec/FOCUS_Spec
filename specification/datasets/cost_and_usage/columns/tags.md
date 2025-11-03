# Tags

The Tags column represents the set of [*tags*](#glossary:tag) assigned to [*tag sources*](#glossary:tag-source) that also account for potential provider-defined or user-defined tag evaluations. Tags are commonly used for scenarios like adding business context to cost and usage data to identify and accurately allocate [*charges*](#glossary:charge). Tags may also be referred to by service providers using other terms such as labels.

A tag becomes [*finalized*](#glossary:finalized-tag) when a single value is selected from a set of possible tag values assigned to the tag key.  When supported by a service provider, this can occur when a tag value is set by provider-defined or user-defined rules.

## Requirements

Tags adheres to the following requirements:

* Tags MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports setting user or provider-defined tags.
* Tags MUST conform to [KeyValueFormat](#key-valueformat) requirements.
* Tags MAY be null.
* When Tags is not null, Tags adheres to the following additional requirements:
  * Tags MUST include all user-defined and provider-defined tags.
  * Tags MUST only include finalized tags.
  * Tags SHOULD include tag keys with corresponding non-null values for a given [*resource*](#glossary:resource).
  * Tags MAY include tag keys with a null value for a given *resource* depending on the service provider's tag finalization process.
  * Tag keys that do not support corresponding values, MUST have a corresponding true (boolean) value set.
  * Service provider SHOULD publish tag finalization methods and semantics within their respective documentation.
  * Service provider MUST NOT alter tag values unless applying true (boolean) to valueless tags.
* Provider-defined tags adhere to the following additional requirements:
  * Provider-defined tag keys MUST be prefixed with a predetermined, provider-specified tag key prefix that is unique to each corresponding provider-specified tag scheme.
  * Service provider SHOULD publish all provider-specified tag key prefixes within their respective documentation.
* User-defined tags adhere to the following additional requirements:
  * Service provider MUST prefix all but one user-defined tag scheme with a predetermined, provider-specified tag key prefix that is unique to each corresponding user-defined tag scheme when the service provider has more than one user-defined tag scheme.
  * Service provider MUST NOT prefix tag keys when the service provider has only one user-defined tag scheme.
  * Service provider MUST NOT allow reserved tag key prefixes to be used as prefixes for any user-defined tag keys within a prefixless user-defined tag scheme.

## Provider-Defined vs. User-Defined Tags

This example illustrates various tags produced from multiple user-defined and provider-defined tag schemes.  The first three tags illustrate examples from three different, user-defined tag schemes. The service provider predetermined that 1 user-defined tag scheme (i.e., `"foo": "bar"`) does not have a prepended prefix, but the remaining two user-defined tag schemes (i.e., `"userDefinedTagScheme2/foo": "bar"`, `"userDefinedTagScheme3/foo": true`) do have service-provider-defined and reserved prefixes.  Additionally, the third tag is produced from a valueless, user-defined tag scheme, so the service provider also applies `true` as its default value.

The last two tags illustrate examples from two different, provider-defined tag schemes. Since all provider-defined tag schemes require a prefix, the service provider has prepended predefined and reserved prefixes (`providerDefinedTagScheme1/`, `providerDefinedTagScheme2/`) to each tag.

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

Within a service provider, tag keys may be associated with multiple values, and potentially defined at different levels within the service provider, such as accounts, folders, [*resource*](#glossary:resource) and other *resource* grouping constructs. When finalizing, *service providers* must reduce these multiple levels of definition to a single value where each key is associated with exactly one value. The method by which this is done and the semantics are up to each service provider but must be documented within their respective documentation.

As an example, let's assume 1 [*sub account*](#glossary:sub-account) exists with 1 virtual machine with the following details, and tag inheritance favors Resources over *Sub Accounts*.

* Sub Account
  * id: *my-sub-account*
  * user-defined tags: *team:ops*, *env:prod*
* Virtual Machine
  * id: *my-vm*
  * user-defined tags: *team:web*

The table below represents a finalized dataset with these *resources*.  It also shows the finalized state after all resource-oriented, tag inheritance rules are processed.

| ResourceType    | ResourceId     | Tags                                        |
| :---------------| :--------------| :-------------------------------------------|
| Sub Account     | my-sub-account | { "team": "ops", "env": "prod" }            |
| Virtual Machine | my-vm          | { "team": "web", *"env": "prod"* }          |

Because the Virtual Machine Resource did not have an `env` tag, it inherited tag, `env:prod` (italicized), from its parent *sub account*.  Conversely, because the Virtual Machine Resource already has a `team` tag (`team:web`), it did not inherit `team:ops` from its parent *sub account*.

## Column ID

Tags

## Display Name

Tags

## Description

The set of tags assigned to *tag sources* that account for potential provider-defined or user-defined tag evaluations.

## Content Constraints

|    Constraint   |      Value       |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Feature level   | Conditional      |
| Allows nulls    | True             |
| Data type       | JSON             |
| Value format    | [Key-Value Format](#key-valueformat) |

## Introduced (version)

1.0-preview
