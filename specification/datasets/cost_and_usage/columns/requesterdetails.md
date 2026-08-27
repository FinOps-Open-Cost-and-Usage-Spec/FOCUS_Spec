# Requester Details

Requester Details represents a set of properties describing the [*requester*](#glossary:requester) on whose behalf a request that produced a [*charge*](#glossary:charge) was made. A *requester* is commonly represented at more than one level: the [*principal*](#glossary:principal) to which access to a [*resource*](#glossary:resource) or [*service*](#glossary:service) is granted, and the [*credential*](#glossary:credential) that *principal* presented on the request. Requester Details carries these as a collection of key-value entries, where the `Principal` entry describes the *principal* identified by [Principal ID](#datamodel.costandusage.principalid) and the `Credential` entry describes the *credential* identified by [Credential ID](#datamodel.costandusage.credentialid).

Where Principal ID and Credential ID provide opaque identifiers suited to grouping and joining, Requester Details carries the descriptive attributes published alongside those identifiers, such as a display name, an email address, and the kind of *principal* or *credential* the identifier represents. A request may be authenticated with an API key acting under a named user, or with a workload identity acting under a service account; in each case the named user or service account is the *principal*, and the API key or workload identity is the *credential*.

Requester Details helps practitioners attribute cost to a recognizable *requester* while preserving Principal ID and Credential ID as stable, opaque keys, and provides a defined location for identity attributes that would otherwise appear as custom columns.

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

Requester Details consists of an array of entries, where each entry is an object carrying a `key` property naming what the entry describes and a `value` property carrying its attributes. The `Principal` entry describes the *principal* identified by PrincipalId, and the `Credential` entry describes the *credential* identified by CredentialId.

The following section details the normative requirements for the RequesterDetailsObject and its nested properties. For a logical overview of the expected content, see the [Schema Structure](#datamodel.costandusage.requesterdetails.requesterdetailsobject.objectschemastructure) and [Object Example](#datamodel.costandusage.requesterdetails.requesterdetailsobject.objectexample) sections.

### Object Requirements

RequesterDetailsObject MUST adhere to the following requirements:

* RequesterDetailsObject MUST conform to the [RequesterDetailsObjectSchema](#schemas.costandusage.requesterdetailsobjectschema) JSON Schema.
* RequesterDetailsObject MUST be an array of entries.
* RequesterDetailsObject MUST include at least one entry.
* RequesterDetailsObject MUST NOT include entries that are not applicable to the *requester* associated with the *charge*.

RequesterDetailsObject entries MUST adhere to the following requirements:

* Entry in RequesterDetailsObject MUST include a `key` property.
* Entry in RequesterDetailsObject MUST include a `value` property.
* Entry.key in RequesterDetailsObject MUST be "Principal", "Credential", or a custom key.
* Entry.key in RequesterDetailsObject MUST be unique within RequesterDetailsObject.
* Entry.value in RequesterDetailsObject MUST be an object carrying the descriptive attributes of the *requester* level named by Entry.key.
* Entry.value.Type MUST represent the kind of entity described by the entry.
* Entry.value.Name MUST represent a readable display name for the entity described by the entry.
* Entry.value.Email MUST represent an email address associated with the entity described by the entry.
* Custom entry in RequesterDetailsObject MUST represent a level of the *requester* that is neither the *principal* nor the *credential*.

### Object Schema Structure

RequesterDetails contains an array of key-value entries describing the *principal* identified by PrincipalId and the *credential* identified by CredentialId.

<div class="h7-nonindex">Entry Properties</div>

Each entry in the array contains the following properties:

| Property | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `key` | String | True | Names what the entry describes. One of the FOCUS-defined keys below, or a custom key. |
| `value` | Object | True | The attributes applicable to `key`. |

<div class="h7-nonindex">FOCUS-Defined Keys</div>

| Key | Required | Description |
| :--- | :--- | :--- |
| `Principal` | False | The *principal* identified by Principal ID. |
| `Credential` | False | The *credential* identified by Credential ID. |

<div class="h7-nonindex">Value Properties</div>

The `value` of each entry is an object. FOCUS supports the properties below for describing the entity; a data generator uses them as necessary and may include additional custom properties.

| Property | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `Type` | String | False | The kind of entity the entry describes (e.g., "User", "Service Account", "API Key", "Session"). |
| `Name` | String | False | Readable display name for the entity the entry describes. |
| `Email` | String | False | Email address associated with the entity the entry describes. |

### Object Implementation Guidance

<div class="h7-nonindex">Custom Keys and Properties</div>

To facilitate querying data across *principals* and across [*service providers*](#glossary:service-provider), a data generator may include one or more custom entries, or custom properties within the `value` of a FOCUS-defined entry. Custom entry keys and custom property names MUST be prefixed with "x_" followed by PascalCase format (e.g., `x_MyCustomKey`) to make them easy to identify as well as prevent collisions with FOCUS-defined keys.

<div class="h7-nonindex">Additional Levels</div>

Every entry value uses the same set of properties, so the *principal*, the *credential*, and any additional level share one shape. A *requester* represented at further levels (e.g., a tenant, a delegating identity, an intermediate role) carries each one as a custom entry whose value uses those same properties.

This specification defines the *principal* and the *credential* because they are the two levels that appear across *service providers*. It does not enumerate the levels between them, which vary by authorization model. Reusing one shape for every level means a level named by a data generator and a level named by a later version of this specification are read the same way.

<div class="h7-nonindex">Entry Placement</div>

Attributes describing the *principal* identified by PrincipalId belong in the `value` of the `Principal` entry. Attributes describing the *credential* identified by CredentialId belong in the `value` of the `Credential` entry. An entry is present only when attributes for it are published, so a *charge* with a *principal* and no identified *credential* carries a `Principal` entry alone.

### Object Example

Here is an example of the object format.

* For more detailed examples, please see this column's entry in the JSON Object Examples appendix entry [here](#appendix.examples:jsonobject.examples:requesterdetails).
* For the JSON schema, please see [Requester Details Object Schema](#schemas.costandusage.requesterdetailsobjectschema).

```json
[
  {
    "key" : "Principal",
    "value" : {
      "Name" : "Alex Rivera",
      "Email" : "alex.rivera@example.com",
      "Type" : "User"
    }
  },
  {
    "key" : "Credential",
    "value" : {
      "Type" : "API Key",
      "Name" : "prod-ingest-key"
    }
  }
]
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
