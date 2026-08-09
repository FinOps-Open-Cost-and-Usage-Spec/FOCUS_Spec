# Credential Details

Credential Details represents a set of properties describing the [*principal*](#glossary:principal) that initiated a request and the [*credential*](#glossary:credential) that credentialed the request to the [*service provider*](#glossary:service-provider). A *service provider* commonly records both: the *principal* to which access to a [*resource*](#glossary:resource) or [*service*](#glossary:service) is granted, and the *credential* that *principal* presented on the request that produced the [*charge*](#glossary:charge). Credential Details describes the *principal* identified by [Principal ID](#datamodel.costandusage.principalid) through its top-level properties, and describes the *credential* identified by [Credential ID](#datamodel.costandusage.credentialid) in a nested `Credential` property.

Where Principal ID and Credential ID provide opaque identifiers suited to grouping and joining, Credential Details carries the descriptive attributes a *service provider* publishes alongside those identifiers, such as a display name, an email address, and the kind of *principal* or *credential* the identifier represents. A request may be authenticated with an API key acting under a named user, or with a workload identity acting under a service account; in each case the named user or service account is the *principal*, and the API key or workload identity is the *credential*. Keeping the descriptive attributes of the *principal* at the top level means the most common analyses (e.g., grouping *charges* by principal name or email) read directly from those properties.

Credential Details helps practitioners attribute cost to a recognizable actor while preserving Principal ID and Credential ID as stable, opaque keys, and gives *service providers* a defined location for identity attributes that would otherwise appear as custom columns.

## Requirements

### Column Requirements

CredentialDetails MUST adhere to the following requirements:

* CredentialDetails MUST be of type JSON Object (serialized as a String where necessary).
* CredentialDetails MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* CredentialDetails MUST conform to [JsonObjectFormat](#attributes.jsonobjectformat) requirements.
* CredentialDetails MUST adhere to the following nullability requirements:
  * CredentialDetails MUST be null when the *service provider* cannot determine the *principal* or the *credential* associated with the *charge*.
  * CredentialDetails MAY be null when the *service provider* can determine the *principal* or the *credential* associated with the *charge*.
* CredentialDetails MUST conform to [CredentialDetailsObject](#datamodel.costandusage.credentialdetails.credentialdetailsobject) requirements when CredentialDetails is not null.

## Credential Details Object

Credential Details consists of a valid JSON object whose top-level properties describe the *principal* identified by PrincipalId. An optional `Credential` property describes the *credential* identified by CredentialId.

The following section details the normative requirements for the CredentialDetailsObject and its nested properties. For a logical overview of the expected content, see the [Schema Structure](#datamodel.costandusage.credentialdetails.credentialdetailsobject.objectschemastructure) and [Object Example](#datamodel.costandusage.credentialdetails.credentialdetailsobject.objectexample) sections.

### Object Requirements

CredentialDetailsObject MUST adhere to the following requirements:

* CredentialDetailsObject MUST conform to the [CredentialDetailsObjectSchema](#schemas.costandusage.credentialdetailsobjectschema) JSON Schema.
* CredentialDetailsObject MUST include at least one property.
* CredentialDetailsObject MUST NOT include properties that are not applicable to the corresponding PrincipalId or CredentialId.
* CredentialDetailsObject.Name MUST represent a readable display name for the *principal* identified by PrincipalId.
* CredentialDetailsObject.Email MUST represent an email address associated with the *principal* identified by PrincipalId.
* CredentialDetailsObject.Type MUST represent the kind of *principal* identified by PrincipalId.
* CredentialDetailsObject.Type MUST be a consistent, readable display value.
* CredentialDetailsObject SHOULD include Type when the *service provider* distinguishes kinds of *principals*.
* CredentialDetailsObject.Credential MUST represent the *credential* identified by CredentialId.
* CredentialDetailsObject.Credential.Id MUST equal CredentialId.
* CredentialDetailsObject.Credential.Type MUST represent the kind of *credential* identified by CredentialId.
* CredentialDetailsObject.Credential.Type MUST be a consistent, readable display value.
* CredentialDetailsObject.Credential.Name MUST represent a readable display name for the *credential* identified by CredentialId.

### Object Schema Structure

CredentialDetails contains a structured JSON object describing the *principal* identified by PrincipalId and the *credential* identified by CredentialId.

<div class="h7-nonindex">Top-Level Properties</div>

| Property | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `Name` | String | False | Readable display name for the *principal* identified by Principal ID. |
| `Email` | String | False | Email address associated with the *principal* identified by Principal ID. |
| `Type` | String | False | The kind of *principal* identified by Principal ID (e.g., "User", "Service Account", "Application"). |
| `Credential` | Object | False | The *credential* identified by Credential ID. |

<div class="h7-nonindex">Credential Object</div>

The `Credential` property contains an object with the following entries:

| Key | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `Id` | String | False | The value of Credential ID for the *credential* described by this object. |
| `Type` | String | True | The kind of *credential* identified by Credential ID (e.g., "API Key", "Session", "Delegated Role"). |
| `Name` | String | False | Readable display name for the *credential* identified by Credential ID. |

### Object Implementation Guidance

<div class="h7-nonindex">Custom Properties</div>

To facilitate querying data across *principals* and across *service providers*, a data generator may include one or more custom properties. These may be placed at the top level of the object (alongside `Name`) or nested within the `Credential` object. Custom keys must be prefixed with "x_" followed by PascalCase format (e.g., `x_MyCustomKey`) to make them easy to identify as well as prevent collisions with FOCUS-defined keys.

<div class="h7-nonindex">Property Placement</div>

Attributes describing the *principal* identified by PrincipalId belong at the top level of the object. Attributes describing the *credential* identified by CredentialId belong in the `Credential` object. Placing the descriptive attributes of the *principal* at the top level allows analyses that group or filter on those attributes to read them directly.

`Credential.Id` repeats the value carried in CredentialId. A *service provider* that publishes the *credential* identifier alongside its descriptive attributes has a FOCUS-defined key available for it rather than a custom property. Analyses that group or filter on the *credential* read CredentialId, which is available without parsing the object.

Where a *service provider* exposes only one level, PrincipalId and CredentialId carry the same value, and the attributes describing that identifier belong at the top level.

### Object Example

Here is a basic example of the object format.

* For more detailed examples, please see this column's entry in the JSON Object Examples appendix entry [here](#appendix.examples:jsonobject.examples:credentialdetails).
* For the JSON schema, please see [Credential Details Object Schema](#schemas.costandusage.credentialdetailsobjectschema).

```json
{
  "Name" : "Alex Rivera",
  "Email" : "alex.rivera@example.com",
  "Type" : "User",
  "Credential" : {
    "Type" : "API Key",
    "Name" : "prod-ingest-key"
  }
}
```

### Object ID

CredentialDetailsObject

### Object Display Name

Credential Details Object

## Column ID

CredentialDetails

## Display Name

Credential Details

## Description

A set of properties describing the *principal* that initiated a request and the *credential* that credentialed the request.

## Content Constraints

| Constraint | Value |
| :--- | :--- |
| Dataset | [Cost and Usage](#datamodel.costandusage) |
| Column type | Dimension |
| Feature level | Conditional |
| Allows nulls | True |
| Data type | JSON |
| Value format | [JSON Object Format](#attributes.jsonobjectformat) |
| Object | [CredentialDetailsObject](#datamodel.costandusage.credentialdetails.credentialdetailsobject) |

## Version Introduced

1.5
