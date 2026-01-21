# Tags Details

The Tags Details column is a superset of [Tags](#tags) which includes additional properties describing tag eligibility and tag provenance from all [*tag sources*](#glossary:tag-source). Tags Details can be used to determine whether a [*charge*](#glossary:charge) was eligible to be tagged, improving the accuracy of tag coverage calculations. Tags Details can also be used to determine the origin of the [*finalized tag*](#glossary:finalized-tag) as well as find tag values present on ancestor sources.

## Requirements

### Column Requirements

The TagsDetails column adheres to the following requirements:

* TagDetails SHOULD be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the data generator supports setting user or provider-defined tags.
* TagDetails MUST be of type String.
* TagDetails MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* TagDetails MUST conform to [JsonObjectFormat](#attributes.jsonobjectformat) requirements.
* TagDetails nullability is defined as follows:
  * TagDetails MUST be null when Tags is null.
  * TagDetails SHOULD NOT be null when Tags is not null.

### Object Schema Requirements

Tag Details consists of a valid JSON object which contains objects for one or more Tags schemes which each contain an object describing the tags as well as an array of eligible *tag sources* which do not contain tags.

When TagDetails is not null, the JsonObjectFormat for TagDetails adheres to the following requirements:

* TagDetails root object MUST contain an object for each tag scheme present in Tags.
  * The key for each tag scheme object MUST align to the tag prefix (up to but not including the forward slash) used to define the tag scheme in Tags.
  * The key for the unprefixed user-defined tag scheme in Tags MUST be "Default".
* Each tag scheme object MUST contain an object for each tag key used in that tag scheme.
  * Each tag key object MUST contain FOCUS-defined tag properties.
  * FOCUS-defined tag properties are subject to the additional requirements:
    * Tag property key MUST match the spelling and casing specified for the FOCUS-defined property.
    * Tag property value MUST be of the type specified for that property.
    * Tag properties MUST adhere to additional normative requirements specific to that property.
  * Each tag key object MUST contain an object with they key "AncestorTaggedSources" which denotes the *tag sources* that did not result in the *finalized tag*.
    * AncestorTaggedSources MUST be null when the tag key from the corresponding tag key object within the tag scheme is not present in any *tag source* other than the *tag source* which results in the *finalized tag*.
    * When AncestorTaggedSources is not null, each object in AncestorTaggedSources MUST have a key denoting the *tag source*.
      * Each tag source object must contain FOCUS-defined tag properties.
* Each tag scheme object MUST contain an array with the key "UntaggedSources"
  * Untagged Sources array MUST contain all *tag sources* for the corresponding tag scheme which are eligible to be tagged for the *charge*.
  * Untagged Sources MUST be null when there are no eligible *tag sources* which contain no tags.

### Content Requirements

The following keys are used for tag properties to facilitate standardized extraction of data across providers. FOCUS-defined keys will appear in the list below and data generator-defined keys will be prefixed with "x_" to make them easy to identify as well as prevent collisions.

  * "TagsSource" denotes the type of [*tag source*] where the [*finalized tag*] value was set.
  * "TagsSourceId" denotes the specific [*tag source*] where the [*finalized tag*] value was set.
  * "TagValue" represents the *finalized tag* value associated with the tag key for the corresponding tag scheme and *tag source*

## Overview

### Object Entries

### Example

```json
{
  "Default": {
    "Tags": {
      "foo": {
        "FocusColumn": "ResourceId",
        "TagsSource": "Resource",
        "TagsSourceId": "my-resource-11",
        "TagValue": "baz",
        "AncestorTaggedSources": {
          "Subscription": {
            "FocusColumn": null,
            "TagsSourceId": "/subs/#",
            "TagValue": "foo"
          },
          "Resource Group": {
            "FocusColumn": null,
            "TagsSourceId": "/subs/#/rgs/x",
            "TagValue": "bar"
          }
        }
      }
    },
    "UntaggedSources": ["CustomSourceOne"]
  },
  "userDefinedTagScheme2": {
    "Tags": {
      "foo": {
        "FocusColumn": "ResourceId",
        "TagsSource": "Resource",
        "TagsSourceId": "my-resource-11",
        "TagValue": "bar",
        "AncestorTaggedSources": null
      }
    },
    "UntaggedSources": null
  },
  "userDefinedTagScheme3": {
    "Tags": {
      "foo": {
        "FocusColumn": "ResourceId",
        "TagsSource": "Resource",
        "TagsSourceId": "my-resource-11",
        "TagValue": "bar",
        "AncestorTaggedSources": null
      }
    },
    "UntaggedSources": null
  },
  "providerDefinedTagScheme1": {
    "Tags": {
      "foo": {
        "FocusColumn": "ResourceId",
        "TagsSource": "Resource",
        "TagsSourceId": "my-resource-11",
        "TagValue": "bar",
        "AncestorTaggedSources": null
      }
    },
    "UntaggedSources": null
  },
  "providerDefinedTagScheme2": {
    "Tags": {
      "foo": {
        "FocusColumn": "ResourceId",
        "TagsSource": "Resource",
        "TagsSourceId": "my-resource-11",
        "TagValue": "bar",
        "AncestorTaggedSources": null
      }
    },
    "UntaggedSources": null
  }
}

```

### JSON Type Definition

```json

```

## Example Scenarios



## Column ID

TagsDetails

## Display Name

Tags Details

## Description

The superset of Tags which includes additional properties describing tag eligibility and tag provenance from all *tag sources,* both provider-defined and user-defined.

## Content Constraints

| Constraint      | Value           |
|:----------------|:----------------|
| Column type     | Dimension       |
| Feature level   | Recommended     |
| Allows nulls    | True            |
| Data type       | JSON            |
| Value format    | [JSON Object Format](#attributes.jsonobjectformat) |

## Introduced (version)

1.4
