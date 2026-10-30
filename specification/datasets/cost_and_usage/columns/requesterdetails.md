# Requester Details

[Requester Details](#col) represents properties describing the [requester](#term) associated with a [charge](#term). A [requester](#term) is commonly represented at more than one level: the [principal](#term) to which access to a [resource](#term) or [service](#term) is granted, and the [credential](#term) that authenticated that [principal](#term) on the request that produced the [charge](#term). [Requester Details](#col) carries these as a collection of key-value entries, where the `Principal` entry describes the [principal](#term) identified by [Principal ID](#col) and the `Credential` entry describes the [credential](#term) identified by [Credential ID](#col).

Where [Principal ID](#col) and [Credential ID](#col) provide opaque identifiers suited to grouping and joining, [Requester Details](#col) carries the descriptive attributes published alongside those identifiers, such as a display name, an email address, and the kind of [principal](#term) or [credential](#term) the identifier represents. A request may be authenticated with an API key acting under a named user, or with a session established for a service account; in each case the named user or service account is the [principal](#term), and the API key or session is the [credential](#term).

[Requester Details](#col) helps practitioners attribute cost to a recognizable [requester](#term) while preserving [Principal ID](#col) and [Credential ID](#col) as stable, opaque keys, and provides a defined location for identity attributes that would otherwise appear as custom columns.

## Requirements

### Column Requirements

[RequesterDetails](#col) MUST adhere to the following requirements:

* [RequesterDetails](#col) MUST be of type JSON Array (serialized as a String where necessary).
* [RequesterDetails](#col) MUST conform to [StringHandling](#attr) requirements.
* [RequesterDetails](#col) MUST conform to [JsonObjectFormat](#attr) requirements.
* [RequesterDetails](#col) MUST adhere to the following nullability requirements:
  * [RequesterDetails](#col) MUST NOT be null when [PrincipalId](#col) is not null or [CredentialId](#col) is not null.
  * [RequesterDetails](#col) MAY be null when [PrincipalId](#col) is null and [CredentialId](#col) is null.
* [RequesterDetails](#col) MUST conform to [RequesterDetailsObject](#obj) requirements when [RequesterDetails](#col) is not null.

## Requester Details Object

[Requester Details](#col) consists of a JSON array of entries, where each entry is an object carrying a `key` property naming what the entry describes and a `value` property carrying its attributes. The `Principal` entry describes the [principal](#term) identified by [PrincipalId](#col), and the `Credential` entry describes the [credential](#term) identified by [CredentialId](#col).

The following section details the normative requirements for the [RequesterDetailsObject](#obj) and its nested properties. For a logical overview of the expected content, see the [Schema Structure](#datamodel.costandusage.requesterdetails.requesterdetailsobject.objectschemastructure) and [Object Example](#datamodel.costandusage.requesterdetails.requesterdetailsobject.objectexample) sections.

### Object Requirements

[RequesterDetailsObject](#obj) MUST adhere to the following requirements:

* [RequesterDetailsObject](#obj) MUST conform to the [RequesterDetailsObjectSchema](#schema) JSON Schema.
* [RequesterDetailsObject](#obj) MUST NOT include entries that are not applicable to the [requester](#term) associated with the [charge](#term).
* [RequesterDetailsObject](#obj) MUST NOT include an entry whose Entry.key is "Principal" when [PrincipalId](#col) is null.
* [RequesterDetailsObject](#obj) MUST NOT include an entry whose Entry.key is "Credential" when [CredentialId](#col) is null.
* [RequesterDetailsObject](#obj) entries MUST adhere to the following requirements:
  * Entry.key in [RequesterDetailsObject](#obj) MUST be unique within [RequesterDetailsObject](#obj).
  * Entry.value in [RequesterDetailsObject](#obj) MUST carry the descriptive attributes of the [requester](#term) level named by Entry.key.
  * Entry.value.Type MUST represent the kind of entity described by the entry.
  * Entry.value.Name MUST represent a readable display name for the entity described by the entry.
  * Entry.value.Email MUST represent an email address associated with the entity described by the entry.
  * Custom entry in [RequesterDetailsObject](#obj) MUST represent a level of the [requester](#term) that is neither the [principal](#term) nor the [credential](#term).

### Object Schema Structure

[RequesterDetails](#col) contains an array of key-value entries describing the [principal](#term) identified by [PrincipalId](#col) and the [credential](#term) identified by [CredentialId](#col).

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

The `value` of each entry is an object. FOCUS supports the properties below for describing the entity; a [*data generator*](#metadata.datagenerator) uses them as necessary and may include additional custom properties.

| Property | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `Type` | String | False | The kind of entity the entry describes (e.g., "User", "Service Account", "API Key", "Session"). |
| `Name` | String | False | Readable display name for the entity the entry describes. |
| `Email` | String | False | Email address associated with the entity the entry describes. |

### Object Implementation Guidance

<div class="h7-nonindex">Custom Keys and Properties</div>

To facilitate querying data across [principals](#term) and across [service providers](#term), a data generator may include one or more custom entries, or custom properties within the `value` of a FOCUS-defined entry. The "x_" prefix followed by PascalCase format (e.g., `x_MyCustomKey`) makes custom keys easy to identify and prevents collisions with FOCUS-defined keys.

<div class="h7-nonindex">Additional Levels</div>

Every entry value uses the same set of properties, so the [principal](#term), the [credential](#term), and any additional level share one shape. Each further level at which a [requester](#term) is represented (e.g., a delegating identity, a client application) is carried as a custom entry whose value uses those same properties. A client application (e.g., a command-line agent, an IDE extension, a hosted agent runtime) is a level of this kind when the [service provider](#term) defines it in its identity and access management model and identifies which one made each request, so [charges](#term) from one [principal](#term) through several client applications carry a different entry for each. Where the [service provider](#term) does not define client applications but records which one a [credential](#term) was issued to, that record is an attribute of the [credential](#term) and is carried as a custom property within the `Credential` entry.

This specification defines the [principal](#term) and the [credential](#term) because they are the two levels that appear across [service providers](#term). It does not enumerate the levels between them, which vary by authorization model. Reusing one shape for every level means a level named by a data generator and a level named by a later version of this specification are read the same way.

<div class="h7-nonindex">Entry Placement</div>

Attributes describing the [principal](#term) identified by [PrincipalId](#col) belong in the `value` of the `Principal` entry. Attributes describing the [credential](#term) identified by [CredentialId](#col) belong in the `value` of the `Credential` entry. An entry appears only when its attributes are published, and the `Principal` and `Credential` entries appear only when [PrincipalId](#col) or [CredentialId](#col), respectively, is not null. A [charge](#term) whose [PrincipalId](#col) is not null and whose [CredentialId](#col) is null therefore carries no `Credential` entry and can carry a `Principal` entry, and a [principal](#term) or [credential](#term) with no published identifier has no entry.

[RequesterDetails](#col) is not null when [PrincipalId](#col) or [CredentialId](#col) is not null, including where the data generator publishes no display name or email address for the identified entity. The identity and access management model that defines an entity also defines what kind of entity it is, so `Type` is always available, and the `value` of an entry for that entity can hold `Type` alone (e.g., `{"Type": "Service Account"}`).

### Object Example

Here is an example of the object format.

* For more detailed examples, please see this column's entry in the JSON Object Examples appendix entry [here](#appendix.examples:jsonobject.examples:requesterdetails).
* For the JSON schema, please see [Requester Details Object Schema](#schema).

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

A set of properties describing the [requester](#term) associated with a [charge](#term).

## Content Constraints

| Constraint | Value |
| :--- | :--- |
| Dataset | [Cost and Usage](#ds)                     |
| Operating model conditions | [Includes Requester Attribution](#omc)                                                   |
| Column type | Dimension |
| Feature level | Conditional |
| Allows nulls | True |
| Data type | JSON |
| Value format | [JSON Object Format](#attr)                        |
| Object | [RequesterDetailsObject](#obj)                                                            |

## Version Introduced

1.5
