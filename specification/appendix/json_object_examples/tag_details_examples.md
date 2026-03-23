# Examples: Tag Details

The scenarios below illustrate the relationship between the [TagDetails](#datasets.costandusage.tagdetails) and [Tags](#datasets.costandusage.tags) columns for a single charge.

For each scenario, two JSON samples are provided:
1. **`TagDetails`:** Details the provenance and eligibility of tags across various tag sources and schemes, showing how the finalized tags were derived.
2. **`Tags`:** The resulting finalized key-value pairs as they would appear in the `Tags` column for that exact same charge.

## Scenario 1: Standard resource and ancestor tags

A common scenario where tags are applied directly to the resource but are also inherited from ancestor sources. In this case, the tag `env` is finalized from the resource, but was also present on an ancestor. The tag `owner` is only finalized from an ancestor source.

### `TagDetails` Column

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

### `Tags` Column

```json
{
  "env": "prod",
  "owner": "team-alpha"
}
```

## Scenario 2: Ancestor tags only

The charge has no tags finalized directly at the primary source level (e.g., an API request or a resource that wasn't directly tagged), but tags are inherited from an ancestor level. The finalized `TagSource`, `TagSourceId`, and `TagValue` are null, and the value is only found within the `AncestorTaggedSources` object.

### `TagDetails` Column

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

### `Tags` Column

(The column would be null or contain an empty object, as no tags were finalized.)

```json
{}
```

## Scenario 3: Eligible sources with no tags applied

The charge originates from sources that support tagging for the specified scheme, but no tags were applied. This is critical for calculating accurate tag coverage. The `Tags` object is empty, and the eligible sources are listed in `UntaggedSources`.

### `TagDetails` Column

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

### `Tags` Column

```json
{}
```

## Scenario 4: Multiple schemes with valueless and provider-defined tags

The data generator supports multiple tag schemes. One scheme uses a valueless label (represented as a boolean `true`), while a provider-defined scheme includes non-string values like numbers and booleans.

### `TagDetails` Column

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

### `Tags` Column

```json
{
  "department": "finance",
  "userDefinedValuelessLabelScheme/project_foci": true,
  "providerDefinedTagScheme/is_spot_instance": false,
  "providerDefinedTagScheme/k8s_version": 1.29
}
```

## Scenario 5: Additional non-FOCUS specified properties

A data generator can add custom properties if they feel more context is helpful or necessary to the practitioner. Custom keys must be prefixed with `x_` followed by PascalCase. In this scenario, the data generator is supplying an internal metadata ID and a policy enforcement status alongside the standard tag data.

### `TagDetails` Column

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

### `Tags` Column

```json
{
  "costcenter": "cc-404"
}
```
