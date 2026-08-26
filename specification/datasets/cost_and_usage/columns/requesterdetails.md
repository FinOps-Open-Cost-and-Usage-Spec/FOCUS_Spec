# Requester Details

Requester Details represents a set of properties describing the [*requester*](#glossary:requester) on whose behalf a request that produced a [*charge*](#glossary:charge) was made. A [*service provider*](#glossary:service-provider) commonly represents a *requester* at more than one level: the [*principal*](#glossary:principal) to which access to a [*resource*](#glossary:resource) or [*service*](#glossary:service) is granted, and the [*credential*](#glossary:credential) that *principal* presented on the request. Requester Details describes the *principal* identified by [Principal ID](#datamodel.costandusage.principalid) through its top-level properties, and describes the *credential* identified by [Credential ID](#datamodel.costandusage.credentialid) in a nested `Credential` property.

Where Principal ID and Credential ID provide opaque identifiers suited to grouping and joining, Requester Details carries the descriptive attributes a *service provider* publishes alongside those identifiers, such as a display name, an email address, and the kind of *principal* or *credential* the identifier represents. A request may be authenticated with an API key acting under a named user, or with a workload identity acting under a service account; in each case the named user or service account is the *principal*, and the API key or workload identity is the *credential*. Keeping the descriptive attributes of the *principal* at the top level means the most common analyses (e.g., grouping *charges* by principal name or email) read directly from those properties.

Requester Details helps practitioners attribute cost to a recognizable *requester* while preserving Principal ID and Credential ID as stable, opaque keys, and gives *service providers* a defined location for identity attributes that would otherwise appear as custom columns. A *service provider* that represents a *requester* at levels beyond the *principal* and the *credential* describes each additional level in its own nested object, so the levels this specification defines and the levels a *service provider* defines share one shape.

## Requirements

### Column Requirements

RequesterDetails MUST adhere to the following requirements:

* RequesterDetails MUST be of type JSON Object (serialized as a String where necessary).
* RequesterDetails MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* RequesterDetails MUST conform to [JsonObjectFormat](#attributes.jsonobjectformat) requirements.
* RequesterDetails MUST adhere to the following nullability requirements:
  * RequesterDetails MAY be null when PrincipalId is null and CredentialId is null.
  * RequesterDetails MUST NOT be null when PrincipalId is not null or CredentialId is not null.
* RequesterDetails MUST conform to [RequesterDetailsObject](#datamodel.costandusage.requesterdetails.requesterdetailsobject) requirements when RequesterDetails is not null.

## Requester Details Object

Requester Details consists of a valid JSON object whose top-level properties describe the *principal* identified by PrincipalId. An optional `Credential` property describes the *credential* identified by CredentialId.

The following section details the normative requirements for the RequesterDetailsObject and its nested properties. For a logical overview of the expected content, see the [Schema Structure](#datamodel.costandusage.requesterdetails.requesterdetailsobject.objectschemastructure) and [Object Example](#datamodel.costandusage.requesterdetails.requesterdetailsobject.objectexample) sections.

### Object Requirements

RequesterDetailsObject MUST adhere to the following requirements:

* RequesterDetailsObject MUST conform to the [RequesterDetailsObjectSchema](#schemas.costandusage.requesterdetailsobjectschema) JSON Schema.
* RequesterDetailsObject MUST NOT include properties that are not applicable to the *requester* associated with the *charge*.
* RequesterDetailsObject.Name MUST represent a readable display name for the *principal* identified by PrincipalId.
* RequesterDetailsObject.Email MUST represent an email address associated with the *principal* identified by PrincipalId.
* RequesterDetailsObject.Type MUST represent the kind of *principal* identified by PrincipalId.
* RequesterDetailsObject.Type MUST be a consistent, readable display value.
* RequesterDetailsObject SHOULD include Type when the *service provider* distinguishes kinds of *principals*.
* RequesterDetailsObject.Credential MUST represent the *credential* identified by CredentialId.
* RequesterDetailsObject.Credential.Id MUST match CredentialId.
* RequesterDetailsObject.Credential.Type MUST represent the kind of *credential* identified by CredentialId.
* RequesterDetailsObject.Credential.Type MUST be a consistent, readable display value.
* RequesterDetailsObject.Credential.Name MUST represent a readable display name for the *credential* identified by CredentialId.
* RequesterDetailsObject SHOULD represent a level of the *requester* that is neither the *principal* nor the *credential* as a custom property whose value is an object.
* RequesterDetailsObject custom properties representing a level of the *requester* SHOULD include the Id, Type, and Name entries defined for RequesterDetailsObject.Credential.

### Object Schema Structure

RequesterDetails contains a structured JSON object describing the *principal* identified by PrincipalId and the *credential* identified by CredentialId.

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

<div class="h7-nonindex">Additional Levels</div>

The `Credential` object is the shape a level of the *requester* takes: `Id` for the identifier the *service provider* publishes for that level, `Type` for the kind of entity the level represents, and `Name` for a readable display name. A *service provider* that represents a *requester* at further levels (e.g., a tenant, a delegating identity, an intermediate role) describes each one as a custom property holding an object of that same shape.

This specification defines the *principal* and the *credential* because they are the two levels that appear across *service providers*. It does not enumerate the levels between them, which vary by authorization model. Reusing one shape for every level means a level named by a data generator and a level named by a later version of this specification are read the same way.

<div class="h7-nonindex">Property Placement</div>

Attributes describing the *principal* identified by PrincipalId belong at the top level of the object. Attributes describing the *credential* identified by CredentialId belong in the `Credential` object. A top-level property whose value is an object describes a level of the *requester* rather than an attribute of the *principal*. Placing the descriptive attributes of the *principal* at the top level allows analyses that group or filter on those attributes to read them directly.

`Credential.Id` repeats the value carried in CredentialId. A *service provider* that publishes the *credential* identifier alongside its descriptive attributes has a FOCUS-defined key available for it rather than a custom property. Analyses that group or filter on the *credential* read CredentialId, which is available without parsing the object.

Where a *service provider* publishes no identifier for the *credential* presented, CredentialId is null and the `Credential` property is omitted. The attributes describing the *principal* remain at the top level.

### Object Example

Here is a basic example of the object format.

* For more detailed examples, please see this column's entry in the JSON Object Examples appendix entry [here](#appendix.examples:jsonobject.examples:requesterdetails).
* For the JSON schema, please see [Requester Details Object Schema](#schemas.costandusage.requesterdetailsobjectschema).

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

RequesterDetailsObject

### Object Display Name

Requester Details Object

## Column ID

RequesterDetails

## Display Name

Requester Details

## Description

A set of properties describing the *requester* on whose behalf a request that produced a *charge* was made.

## Content Constraints

| Constraint | Value |
| :--- | :--- |
| Dataset | [Cost and Usage](#datamodel.costandusage) |
| Column type | Dimension |
| Feature level | Conditional |
| Allows nulls | True |
| Data type | JSON |
| Value format | [JSON Object Format](#attributes.jsonobjectformat) |
| Object | [RequesterDetailsObject](#datamodel.costandusage.requesterdetails.requesterdetailsobject) |

## Version Introduced

1.5
