# Allocated Tags

The Allocated Tags column represents the set of [*tags*](#glossary:tag) assigned to [*tag sources*](#glossary:tag-source) which are specifically applicable to [*allocated charges*](#glossary:allocated-charge) resulting from a provider-calculated split cost allocation.

The AllocatedTags column adheres to the following requirements:

* AllocatedTags MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports [Provider-Calculated Split Cost Allocation](#providercalculatedsplitcosthandling).
* AllocatedTags MUST conform to [KeyValueFormat](#key-valueformat) requirements.
* AllocatedTags nullability is defined as follows:
  * AllocatedTags MUST be null when a *charge* is not related to a provider-calculated split cost allocation.
  * AllocatedTags MAY be null in all other cases.
* When AllocatedTags is not null, AllocatedTags adheres to the following additional requirements:
  * AllocatedTags MUST NOT include resource tags already present in [Tags](#tags).
  * AllocatedTags MUST include all applicable user-defined and provider-defined tags for the [AllocatedResourceId](#AllocatedResourceId).
  * Tag keys that do not support corresponding values MUST have a corresponding true (boolean) value set.
  * Provider MUST NOT alter tag values unless applying true (boolean) to valueless tags.
* Provider-defined tags adhere to the following additional requirements:
  * Provider-defined tag keys MUST be prefixed with a predetermined, provider-specified tag key prefix that is unique to each corresponding provider-specified tag scheme.
  * Provider SHOULD publish all provider-specified tag key prefixes within their respective documentation.
* User-defined tags adhere to the following additional requirements:
  * Provider MUST prefix all user-defined tags scheme with a predetermined, provider-specified tag key prefix that is unique to each corresponding user-defined tag scheme when the provider has more than one user-defined tag scheme.

## Provider-Defined vs. User-Defined Tags

This example illustrates various tags produced from multiple user-defined and provider-defined tag schemes. The first two tags illustrate examples from two different, user-defined tag schemes. The second tag is produced from a valueless, user-defined tag scheme, so the provider also applies `true` as its default value.

The last two tags illustrate examples from two different, provider-defined tag schemes.

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

A set of tags assigned to tag sources that are applicable to *allocated charges* in provider-calculated split cost allocation.

## Content Constraints

|    Constraint   |      Value       |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Feature level   | Conditional      |
| Allows nulls    | True             |
| Data type       | JSON             |
| Value format    | [Key-Value Format](#key-valueformat) |

## Introduced (version)

1.3
