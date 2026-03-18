# Tag Details

The Tag Details column is a superset of [Tags](#tags) which includes additional properties describing tag eligibility and tag provenance from all [*tag sources*](#glossary:tag-source). Tag Details can be used to determine whether a [*charge*](#glossary:charge) was eligible to be tagged, improving the accuracy of tag coverage calculations. Tag Details can also be used to determine the origin of the [*finalized tag*](#glossary:finalized-tag) as well as find tag values present on ancestor sources which do not appear in the Tags column.

## Requirements

### Column Requirements

The TagDetails column adheres to the following requirements:

* TagDetails MUST be of type String.
* TagDetails MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* TagDetails MUST conform to [JsonObjectFormat](#attributes.jsonobjectformat) requirements.
* TagDetails nullability is defined as follows:
  * TagDetails MUST NOT be null unless all of the following are true:
    * Tags column is null.
    * Tags are not present in any other *tag sources*.
    * No *tag sources* are supported for any user-defined [*tag scheme*](glossary:tag-scheme).

### Object Schema Requirements

Tag Details consists of a valid JSON object which contains objects for one or more *tag schemes* which each contain an object describing the tags as well as an array of eligible *tag sources* which do not contain tags.

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
  * Each tag key object MUST contain an object with the key "AncestorTaggedSources".
    * The value of AncestorTaggedSources MUST be null when the tag key from the corresponding tag key object within the tag scheme is not present in any *tag source* other than the *tag source* which results in the *finalized tag*.
    * When the value of AncestorTaggedSources is not null, each object in AncestorTaggedSources MUST have a key denoting the *tag source*.
      * Each tag source object MUST contain FOCUS-defined tag properties.
    * AncestorTaggedSources SHOULD contain objects for *tag sources* which did not result in the *finalized tag*.
* Each tag scheme object MUST contain an array with the key "UntaggedSources".
  * UntaggedSources array MUST contain all *tag sources* for the corresponding tag scheme which are eligible to be tagged for the *charge* but have no tags applied.
  * The value of UntaggedSources MUST be null when there are no eligible *tag sources* which contain no tags.

### Content Requirements

The following keys are used for tag properties to facilitate standardized extraction of data across providers. FOCUS-defined keys will appear in the list below and data generator-defined keys will be prefixed with "x_" to make them easy to identify as well as prevent collisions.

<b>TagValue</b>

"TagValue" represents the tag value associated with the tag key for the corresponding tag scheme and *tag source*.

The "TagValue" property adheres to the following requirements:

* TagValue MUST be present in each tag key object in the Tags object.
* When TagValue is directly contained in the tag key object, TagValue MUST represent the *finalized tag*.
* TagValue MUST be present in each tag source object in the AncestorTaggedSources object.
* TagValue MUST have the value of true (boolean) when the TagScheme does not support values.
* Data generator MUST NOT alter tag values unless applying true (boolean) to valueless tags.
* TagValue MAY be null when the data generator supports setting a null value for a key-value pair type tag.

<b>TagSource</b>

"TagSource" denotes the type of *tag source* where the tag key is present.

The "TagSource" property adheres to the following requirements:

* TagSource MUST be present in each tag key object in the Tags object.
* TagSource MUST contain the type of *tag source* where the tag key is present.
* TagSource SHOULD NOT be present in each tag source object in the AncestorTaggedSources object.

<b>TagSourceId</b>

"TagSourceId" denotes the identifier of the specific *tag source* where the tag key is present.

The "TagSourceId" property adheres to the following requirements:

* TagSourceId MUST be present in each tag key object in the Tags object.
* TagSourceId MUST be present in each tag source object in the AncestorTaggedSources object.
* TagSourceId MUST contain the identifier of the TagSource.

## Overview

### Object Schema

The object contains an object for each tag scheme present in the Tags column.

| Key | Parent | ValueType | Required | Description |
| ----- | ---- | ---- | ---------- | ----------- |
| Default | _root object_ | Object | TRUE | The object containing information about the unprefixed tag scheme in the Tags column. |
| _TagScheme_ | _root object_ | Object | TRUE | One or more objects containing information about a prefixed tag scheme in the Tags column. |
| Tags | _tag scheme object_ | Object | TRUE | An object containing all tag keys present in the Tags column. |
| UntaggedSources | _tag scheme object_ | Array | TRUE | A list of sources which support this tag scheme (i.e. are taggable) that had no tags applied. |
| _TagKey_ | Tags | Object | TRUE | An object containing the properties of the *finalized tag* as well as other *tag sources* where this key was present. |
| AncestorTaggedSources | _TagKey_ | Object | TRUE | An object containing all *tag sources* where the corresponding tag key was present which did not result in the *finalized tag*. |
| _AncestorTaggedSource_ | AncestorTaggedSources | Object | Conditional | An object containing the properties of the tag present in the *tag source*. |

### Object Entries

The tag key object and tag source objects contain the following properties:

| Key | ValueType | Required | Description |
| ----- | ---- | ---------- | ----------- |
| TagSource | String | Conditional | The type of *tag source* where the tag key is present. |
| TagSourceId | String | TRUE | The identifier of the *tag source* where the tag key is present. |
| TagValue | String, Boolean, or Number | TRUE |  The value associated with the tag key. |

### Example

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
            "TagSourceId": "/subs/#",
            "TagValue": "foo"
          },
          "Resource Group": {
            "TagSourceId": "/subs/#/rgs/x",
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
        "TagSource": "Resource",
        "TagSourceId": "my-resource-11",
        "TagValue": "bar",
        "AncestorTaggedSources": null
      }
    },
    "UntaggedSources": null
  },
  "userDefinedTagScheme3": {
    "Tags": {
      "foo": {
        "TagSource": "Resource",
        "TagSourceId": "my-resource-11",
        "TagValue": "bar",
        "AncestorTaggedSources": null
      }
    },
    "UntaggedSources": null
  },
  "providerDefinedTagScheme1": {
    "Tags": {
      "foo": {
        "TagSource": "Resource",
        "TagSourceId": "my-resource-11",
        "TagValue": "bar",
        "AncestorTaggedSources": null
      }
    },
    "UntaggedSources": null
  },
  "providerDefinedTagScheme2": {
    "Tags": {
      "foo": {
        "TagSource": "Resource",
        "TagSourceId": "my-resource-11",
        "TagValue": "bar",
        "AncestorTaggedSources": null
      }
    },
    "UntaggedSources": null
  }
}
```

The corresponding Tags column would be:

```json
{
  "foo":"baz",
  "userDefinedTagScheme2/foo":"bar",
  "userDefinedTagScheme3/foo":"bar",
  "providerDefinedTagScheme1/foo":"bar",
  "providerDefinedTagScheme2/foo":"bar"
}
```

### JSON Schema Definition

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://focus.finops.org/schemas/tagdetails.json",
  "title": "TagDetails",
  "description": "A superset of Tags which includes additional properties describing tag eligibility and tag provenance from all tag sources.",
  "type": "object",
  "patternProperties": {
    "^[a-zA-Z0-9_]+$": {
      "$ref": "#/$defs/tagScheme"
    }
  },
  "additionalProperties": false,
  "$defs": {
    "tagScheme": {
      "type": "object",
      "properties": {
        "Tags": {
          "type": "object",
          "patternProperties": {
            "^[a-zA-Z0-9_]+$": {
              "$ref": "#/$defs/tagKeyObject"
            }
          },
          "additionalProperties": false
        },
        "UntaggedSources": {
          "type": [
            "array",
            "null"
          ],
          "items": {
            "type": "string"
          }
        }
      },
      "required": [
        "Tags",
        "UntaggedSources"
      ]
    },
    "tagKeyObject": {
      "type": "object",
      "properties": {
        "TagSource": {
          "type": [
            "string",
            "null"
          ],
          "description": "The source of the finalized tag. Can be null if the tag is only present on an ancestor."
        },
        "TagSourceId": {
          "type": [
            "string",
            "null"
          ],
          "description": "The ID of the finalized tag's source. Can be null if the tag is only present on an ancestor."
        },
        "TagValue": {
          "description": "The finalized tag value. Can be null, indicating it doesn't appear in the Tags column.",
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "boolean"
            },
            {
              "type": "number"
            },
            {
              "type": "null"
            }
          ]
        },
        "AncestorTaggedSources": {
          "type": [
            "object",
            "null"
          ],
          "patternProperties": {
            "^[a-zA-Z0-9_ ]+$": {
              "$ref": "#/$defs/ancestorTag"
            }
          },
          "additionalProperties": false
        }
      },
      "required": [
        "TagSource",
        "TagSourceId",
        "TagValue",
        "AncestorTaggedSources"
      ]
    },
    "ancestorTag": {
      "type": "object",
      "properties": {
        "TagSourceId": {
          "type": "string"
        },
        "TagValue": {
          "description": "The tag value from an ancestor source.",
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "boolean"
            },
            {
              "type": "number"
            },
            {
              "type": "null"
            }
          ]
        }
      },
      "required": [
        "TagSourceId",
        "TagValue"
      ]
    }
  }
}
```

## Example Scenarios

### Ancestor tags only

Details:
* One Tag Scheme supported (default).
* Charge is for API usage which has no resource to tag, but this charge does support job tagging in the API request payload.
  * No tags were applied in the API request payload.
* One tag was applied at the ancestor level.

```json
{
  "Default": {
    "Tags": {
      "foo": {
        "TagSource": null,
        "TagSourceId": null,
        "TagValue": null,
        "AncestorTaggedSources": {
          "Project": {
            "TagSourceId": "gcp-project-8675309",
            "TagValue": "bar"
          }
        }
      }
    },
    "UntaggedSources": ["api-job-label"]
  }
}
```

The corresponding Tags column would either be null or contain an empty object:

```json
{}
```

### Tags from multiple sources and schemes with different value types

Details:
* 3 tag schemes are used:
  * User defined tags (default)
    * Provider supports tag finalization via inheritance.
    * First tag (foo) is set at the resource level as well as ancestor levels.
    * Second tag (lorem) is applied at ancestor levels.
      * One of the values from an ancestor is included in Tags column due to tag finalization process.
    * There are no other supported sources for tags to be applied for this charge.
  * userDefinedValuelessLabelScheme
    * Label scheme is valueless so boolean `true` is provided as value to represent the presence of the label.
    * User has set the label (project_foci) on the resource.
    * Label scheme is supported on ancestor levels, but no labels have been set on either.
  * providerDefinedTagScheme
    * Provider has tag scheme which is only applicable at the resource level.
    * First tag (isfeatureenabled) is boolean.
    * Second tag (versionnumber) is numeric.

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
    "UntaggedSources": ["Resource Group", "Subscription"]
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

The corresponding Tags column would contain:

```json
{
"foo": "baz",
"lorem": "ipsum",
"userDefinedValuelessLabelScheme/project_foci": true,
"providerDefinedTagScheme/isfeatureenabled": false,
"providerDefinedTagScheme/versionnumber": 12.2
}
```

## Column ID

TagDetails

## Display Name

Tag Details

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
