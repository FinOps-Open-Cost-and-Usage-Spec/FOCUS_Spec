# Examples: Tag Details

The JSON samples in the scenarios below each represent the `TagDetails` object for a single charge. They detail the provenance and eligibility of tags across various tag sources and schemes, illustrating how the finalized tags were derived.

## Scenario 1: Standard resource and ancestor tags

A common scenario where tags are applied directly to the resource but are also inherited from ancestor sources. In this case, the tag `env` is finalized from the resource, but was also present on an ancestor. The tag `owner` is only finalized from an ancestor source.

```json
{
  "Default": {
    "Tags": {
      "env": {
        "TagSource": "Resource",
        "TagSourceId": "i-1234567890abcdef0",
        "TagValue": "prod",
        "AncestorTaggedSources": {
          "Resource Group": {
            "TagSourceId": "rg-frontend-01",
            "TagValue": "dev"
          }
        }
      },
      "owner": {
        "TagSource": "Subscription",
        "TagSourceId": "sub-987654321",
        "TagValue": "team-alpha",
        "AncestorTaggedSources": null
      }
    },
    "UntaggedSources": null
  }
}
```

## Scenario 2: Ancestor tags only

The charge has no tags finalized directly at the primary source level (e.g., an API request or a resource that wasn't directly tagged), but tags are inherited from an ancestor level. The finalized `TagSource`, `TagSourceId`, and `TagValue` are null, and the value is only found within the `AncestorTaggedSources` object.

```json
{
  "Default": {
    "Tags": {
      "project": {
        "TagSource": null,
        "TagSourceId": null,
        "TagValue": null,
        "AncestorTaggedSources": {
          "Project": {
            "TagSourceId": "gcp-project-8675309",
            "TagValue": "backend-api"
          }
        }
      }
    },
    "UntaggedSources": [
      "Resource"
    ]
  }
}
```

## Scenario 3: Eligible sources with no tags applied

The charge originates from sources that support tagging for the specified scheme, but no tags were applied. This is critical for calculating accurate tag coverage. The `Tags` object is empty, and the eligible sources are listed in `UntaggedSources`.

```json
{
  "Default": {
    "Tags": {},
    "UntaggedSources": [
      "Resource",
      "Resource Group",
      "Subscription"
    ]
  }
}
```

## Scenario 4: Multiple schemes with valueless and provider-defined tags

The data generator supports multiple tag schemes. One scheme uses a valueless label (represented as a boolean `true`), while a provider-defined scheme includes non-string values like numbers and booleans.

```json
{
  "Default": {
    "Tags": {
      "department": {
        "TagSource": "Resource",
        "TagSourceId": "my-resource-11",
        "TagValue": "finance",
        "AncestorTaggedSources": null
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
      "Resource Group"
    ]
  },
  "providerDefinedTagScheme": {
    "Tags": {
      "is_spot_instance": {
        "TagSource": "Resource",
        "TagSourceId": "my-resource-11",
        "TagValue": false,
        "AncestorTaggedSources": null
      },
      "k8s_version": {
        "TagSource": "Resource",
        "TagSourceId": "my-resource-11",
        "TagValue": 1.29,
        "AncestorTaggedSources": null
      }
    },
    "UntaggedSources": null
  }
}
```

## Scenario 5: Additional non-FOCUS specified properties

A data generator can add custom properties if they feel more context is helpful or necessary to the practitioner. Custom keys must be prefixed with `x_` followed by PascalCase. In this scenario, the data generator is supplying an internal metadata ID and a policy enforcement status alongside the standard tag data.

```json
{
  "Default": {
    "x_InternalTaggingSystemId": "sys-998877",
    "Tags": {
      "costcenter": {
        "TagSource": "Resource",
        "TagSourceId": "i-1234567890abcdef0",
        "TagValue": "cc-404",
        "AncestorTaggedSources": null,
        "x_EnforcementPolicy": "Strict",
        "x_AppliedBy": "terraform-svc-account"
      }
    },
    "UntaggedSources": null
  }
}
```
