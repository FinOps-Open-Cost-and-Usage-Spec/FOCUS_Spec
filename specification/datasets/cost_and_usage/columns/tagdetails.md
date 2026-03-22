# Tag Details

The Tag Details column is a superset of [Tags](#tags) which includes additional properties describing tag eligibility and tag provenance from all [*tag sources*](#glossary:tag-source). Tag Details can be used to determine whether a [*charge*](#glossary:charge) was eligible to be tagged, improving the accuracy of tag coverage calculations. Tag Details can also be used to determine the origin of the [*finalized tag*](#glossary:finalized-tag) as well as find tag values present on ancestor sources which do not appear in the Tags column.

## Requirements

### Column Requirements

TagDetails MUST adhere to the following requirements:

* TagDetails MUST be of type JSON Object (serialized as a String where necessary).
* TagDetails MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* TagDetails MUST conform to [JsonObjectFormat](#attributes.jsonobjectformat) requirements.
* TagDetails MUST be null when [Tags](#datasets.costandusage.tags) is null, tags are not present in any other *tag sources*, and no *tag sources* are supported for any user-defined [*tag scheme*](#glossary:tag-scheme).
* TagDetails MUST conform to the [TagDetailsObjectSchema](#schemas.datasets.costandusage.tagdetailsobjectschema) JSON Schema.

## Tag Details Object

Tag Details consists of a valid JSON object which contains objects for one or more *tag schemes*, each of which contains an object describing the tags as well as an array of eligible *tag sources* which do not contain tags.

The following section details the normative requirements for the TagDetailsObject and its nested properties. For a logical overview of the expected content, see the [Schema Structure](#datasets.costandusage.tagdetails.schemastructure) and [Object Example](#datasets.costandusage.tagdetails.objectexample) sections.

### Object Requirements

The TagDetailsObject MUST adhere to the following requirements:

* TagDetailsObject.{\*} keys MUST align to the tag prefix (up to but not including the forward slash) used to define the tag scheme in Tags.
* TagDetailsObject.Default MUST be used to represent the unprefixed user-defined tag scheme in Tags.
* TagDetailsObject.{TagScheme}.UntaggedSources[\*] MUST contain all *tag sources* for the corresponding tag scheme which are eligible to be tagged for the *charge* but have no tags applied.
* TagDetailsObject.{TagScheme}.UntaggedSources MUST be null when there are no eligible *tag sources* which contain no tags.
* TagDetailsObject.{TagScheme}.Tags.{TagKey}.TagSource MUST contain the type of *tag source* where the tag key is present.
* TagDetailsObject.{TagScheme}.Tags.{TagKey}.TagSourceId MUST contain the identifier of the TagSource.
* TagDetailsObject.{TagScheme}.Tags.{TagKey}.TagValue MUST represent the *finalized tag*.
* When TagDetailsObject.{TagScheme}.Tags.{TagKey}.TagValue is not null, TagDetailsObject.{TagScheme}.Tags.{TagKey}.TagValue adheres to the following additional requirements:
  * TagDetailsObject.{TagScheme}.Tags.{TagKey}.TagValue MUST have the value of true (boolean) when the tag scheme does not support values.
  * TagDetailsObject.{TagScheme}.Tags.{TagKey}.TagValue MUST NOT be altered from the original tag value unless applying true (boolean) to valueless tags.
* TagDetailsObject.{TagScheme}.Tags.{TagKey}.TagValue MAY be null when setting a null value is supported for a key-value pair type tag.
* TagDetailsObject.{TagScheme}.Tags.{TagKey}.AncestorTaggedSources MUST be null when the tag key from the corresponding tag key object within the tag scheme is not present in any *tag source* other than the *tag source* which results in the *finalized tag*.
* When TagDetailsObject.{TagScheme}.Tags.{TagKey}.AncestorTaggedSources is not null, TagDetailsObject.{TagScheme}.Tags.{TagKey}.AncestorTaggedSources adheres to the following additional requirements:
  * TagDetailsObject.{TagScheme}.Tags.{TagKey}.AncestorTaggedSources.{TagSource} key MUST denote the *tag source*.
  * TagDetailsObject.{TagScheme}.Tags.{TagKey}.AncestorTaggedSources.{TagSource}.TagSourceId MUST contain the identifier of the TagSource.
  * TagDetailsObject.{TagScheme}.Tags.{TagKey}.AncestorTaggedSources.{TagSource}.TagValue MUST adhere to the same boolean/null conditional logic as the finalized TagValue.
  * TagDetailsObject.{TagScheme}.Tags.{TagKey}.AncestorTaggedSources SHOULD contain objects for *tag sources* which did not result in the *finalized tag*.

## Schema Structure

TagDetails contains a structured JSON object defining tag eligibility and provenance from all tag sources.

### Top-Level Properties

| Property | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `Default` | Object | True | The object containing information about the unprefixed tag scheme in the Tags column. |
| `*{TagScheme}*` | Object | True | One or more objects containing information about a prefixed tag scheme in the Tags column. |

### Tag Scheme Object

Each tag scheme object (including `Default`) contains the following entries:

| Key | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `Tags` | Object | True | An object containing all tag keys present in the Tags column for this scheme. |
| `UntaggedSources` | Array | True | A list of sources which support this tag scheme (i.e. are taggable) that had no tags applied. |

### Tags Object (Tag Key)

The tag key object contains the properties of the *finalized tag* as well as other *tag sources* where this key was present:

| Key | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `TagSource` | String or Null | True | The type of *tag source* where the tag key is present. |
| `TagSourceId` | String or Null | True | The identifier of the *tag source* where the tag key is present. |
| `TagValue` | String, Boolean, Number, or Null | True |  The value associated with the tag key. |
| `AncestorTaggedSources` | Object or Null | True | An object containing all *tag sources* where the corresponding tag key was present which did not result in the *finalized tag*. |

### Ancestor Tagged Sources Object

The ancestor tag source object contains the properties of the tag present in the *tag source*:

| Key | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `TagSourceId` | String | True | The identifier of the *tag source* where the tag key is present. |
| `TagValue` | String, Boolean, Number, or Null | True |  The value associated with the tag key. |

## Object Example

Here is a basic example of the object format containing multiple tag schemes and sources.

* For more detailed scenarios, including side-by-side comparisons with the corresponding `Tags` column, please see the [Tag Details Examples](#appendix.examples:jsonobject.examples:tagdetails) appendix.
* For the JSON schema, please see [Tag Details Object Schema](#schemas.datasets.costandusage.tagdetailsobjectschema).

```json
{
  "Default": {
    "Tags": {
      "foo": {
        "TagSource": "Resource",
        "TagSourceId": "my-resource-11",
        "TagValue": "baz",
        "AncestorTaggedSources": {
          "Subscription": {
            "TagSourceId": "1234-abcd-5678",
            "TagValue": "bar"
          },
          "Resource Group": {
            "TagSourceId": "/subscriptions/1234-abcd-5678/resourceGroups/myresourcegroup",
            "TagValue": "bang"
          }
        }
      },
      "lorem": {
        "TagSource": "Resource Group",
        "TagSourceId": "/subscriptions/1234-abcd-5678/resourceGroups/myresourcegroup",
        "TagValue": "ipsum",
        "AncestorTaggedSources": {
          "Subscription": {
            "TagSourceId": "1234-abcd-5678",
            "TagValue": "adest"
          }
        }
      }
    },
    "UntaggedSources": null
  },
  "userDefinedValuelessLabelScheme": {
    "Tags": {
      "project_foci": {
        "TagSource": "Resource",
        "TagSourceId": "my-resource-11",
        "TagValue": true,
        "AncestorTaggedSources": null
      }
    },
    "UntaggedSources": [
      "Resource Group",
      "Subscription"
    ]
  },
  "providerDefinedTagScheme": {
    "Tags": {
      "isfeatureenabled": {
        "TagSource": "Resource",
        "TagSourceId": "my-resource-11",
        "TagValue": false,
        "AncestorTaggedSources": null
      },
      "versionnumber": {
        "TagSource": "Resource",
        "TagSourceId": "my-resource-11",
        "TagValue": 12.2,
        "AncestorTaggedSources": null
      }
    },
    "UntaggedSources": null
  }
}
```

## Implementation Guidance

### Custom Properties

To facilitate querying data across tagging systems and data generators, a data generator may include one or more custom properties nested within the individual schema or element objects. Custom keys must be prefixed with "x_" followed by PascalCase format (e.g., `x_MyCustomKey`) to make them easy to identify as well as prevent collisions with FOCUS-defined keys.

### Object ID

TagDetailsObject

### Object Display Name

Tag Details Object

## Column ID

TagDetails

## Display Name

Tag Details

## Description

The superset of Tags which includes additional properties describing tag eligibility and tag provenance from all *tag sources*, both provider-defined and user-defined.

## Content Constraints

| Constraint | Value |
| :--- | :--- |
| Dataset | [Cost and Usage](#datasets.costandusage) |
| Column type | Dimension |
| Feature level | Recommended |
| Allows nulls | True |
| Data type | JSON |
| Value format | [JSON Object Format](#attributes.jsonobjectformat) |
| Object | [TagDetailsObject](#datasets.costandusage.tagdetails.tagdetailsobject) |

## Introduced (version)

1.4
