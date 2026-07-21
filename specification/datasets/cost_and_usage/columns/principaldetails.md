# Principal Details

Principal Details represents a set of properties describing the [*principal*](#glossary:principal) identified by [Principal ID](#datasets.costandusage.principalid). Where Principal ID provides a single opaque identifier suited to grouping and joining, Principal Details carries the descriptive attributes a [*service provider*](#glossary:service-provider) publishes alongside that identifier, such as a display name, an email address, and the kind of *principal* the identifier represents.

A *service provider* commonly exposes more than one identity element for a single request. A request may be authenticated with an API key acting under a named user, or with a workload identity acting under a service account. Principal Details describes the *principal* named in Principal ID through its top-level properties, and records any intermediate identities through which the request passed in a nested array. Keeping the descriptive attributes at the top level means the most common analyses (e.g., grouping [*charges*](#glossary:charge) by principal name or email) read directly from those properties rather than traversing nested structures.

Principal Details helps practitioners attribute cost to a recognizable actor while preserving Principal ID as a stable, opaque key, and gives *service providers* a defined location for identity attributes that would otherwise appear as custom columns.

> **Note:** Principal Details may carry properties that are classified as Personal Data or Personally Identifiable Information (PII) under privacy frameworks such as GDPR or CCPA, including values that are pseudonymized. Which of these properties a dataset carries is a matter for the data generator and the data consumer to settle between them. Organizations need to separately ensure that the ingestion, storage, and processing of datasets containing this column comply with their internal data privacy, security, and retention policies.

## Requirements

### Column Requirements

PrincipalDetails MUST adhere to the following requirements:

* PrincipalDetails MUST be of type JSON Object (serialized as a String where necessary).
* PrincipalDetails MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* PrincipalDetails MUST conform to [JsonObjectFormat](#attributes.jsonobjectformat) requirements.
* PrincipalDetails MUST adhere to the following nullability requirements:
  * PrincipalDetails MUST be null when [PrincipalId](#datasets.costandusage.principalid) is null.
  * PrincipalDetails MAY be null when PrincipalId is not null.
* PrincipalDetails MUST conform to [PrincipalDetailsObject](#datasets.costandusage.principaldetails.principaldetailsobject) requirements when PrincipalDetails is not null.

## Principal Details Object

Principal Details consists of a valid JSON object whose top-level properties describe the *principal* identified by PrincipalId. An optional `Intermediates` array records additional identities through which the request passed before reaching that *principal*.

The following section details the normative requirements for the PrincipalDetailsObject and its nested properties. For a logical overview of the expected content, see the [Schema Structure](#datasets.costandusage.principaldetails.principaldetailsobject.objectschemastructure) and [Object Example](#datasets.costandusage.principaldetails.principaldetailsobject.objectexample) sections.

### Object Requirements

PrincipalDetailsObject MUST adhere to the following requirements:

* PrincipalDetailsObject MUST conform to the [PrincipalDetailsObjectSchema](#schemas.costandusage.principaldetailsobjectschema) JSON Schema.
* PrincipalDetailsObject MUST include at least one property.
* PrincipalDetailsObject MUST NOT include properties that are not applicable to the corresponding PrincipalId.
* PrincipalDetailsObject MAY include properties that contain personally identifiable information (PII).
* PrincipalDetailsObject.PrincipalName MUST represent a readable display name for the *principal* identified by PrincipalId.
* PrincipalDetailsObject.PrincipalEmail MUST represent an email address associated with the *principal* identified by PrincipalId.
* PrincipalDetailsObject.PrincipalType MUST represent the kind of *principal* identified by PrincipalId.
* PrincipalDetailsObject.PrincipalType MUST be a consistent, readable display value.
* PrincipalDetailsObject SHOULD include PrincipalType when the *service provider* distinguishes kinds of *principals*.
* PrincipalDetailsObject.Intermediates[\*] MUST represent an identity through which the request passed before reaching the *principal* identified by PrincipalId.
* PrincipalDetailsObject.Intermediates[\*] MUST NOT represent the *principal* identified by PrincipalId.
* PrincipalDetailsObject.Intermediates[\*].PrincipalId MUST conform to PrincipalId requirements.
* PrincipalDetailsObject.Intermediates MUST be ordered from the identity nearest the *service provider* boundary to the identity nearest the *principal* identified by PrincipalId.

### Object Schema Structure

PrincipalDetails contains a structured JSON object describing the *principal* identified by PrincipalId.

<div class="h7-nonindex">Top-Level Properties</div>

| Property | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `PrincipalName` | String | False | Readable display name for the *principal* identified by Principal ID. |
| `PrincipalEmail` | String | False | Email address associated with the *principal* identified by Principal ID. |
| `PrincipalType` | String | False | The kind of *principal* identified by Principal ID (e.g., "User", "Service Account", "Application"). |
| `Intermediates` | Array | False | Identities through which the request passed before reaching the *principal* identified by Principal ID. |

<div class="h7-nonindex">Intermediates Object</div>

The `Intermediates` array contains one or more objects, each of which contains the following entries:

| Key | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `PrincipalType` | String | True | The kind of intermediate identity (e.g., "API Key", "Session", "Delegated Role"). |
| `PrincipalId` | String | False | Identifier of the intermediate identity. |
| `PrincipalName` | String | False | Readable display name for the intermediate identity. |

### Object Implementation Guidance

<div class="h7-nonindex">Custom Properties</div>

To facilitate querying data across *principals* and across *service providers*, a data generator may include one or more custom properties. These may be placed at the top level of the object (alongside `PrincipalName`) or nested within the individual `Intermediates` objects. Custom keys must be prefixed with "x_" followed by PascalCase format (e.g., `x_MyCustomKey`) to make them easy to identify as well as prevent collisions with FOCUS-defined keys.

<div class="h7-nonindex">Property Placement</div>

Attributes describing the *principal* identified by PrincipalId belong at the top level of the object. Attributes describing an identity the request passed through on the way to that *principal* belong in an `Intermediates` entry. Placing the descriptive attributes of the *principal* at the top level allows analyses that group or filter on those attributes to read them directly, without flattening the `Intermediates` array.

### Object Example

Here is a basic example of the object format.

* For more detailed examples, please see this column's entry in the JSON Object Examples appendix entry [here](#appendix.examples:jsonobject.examples:principaldetails).
* For the JSON schema, please see [Principal Details Object Schema](#schemas.costandusage.principaldetailsobjectschema).

```json
{
  "PrincipalName" : "Alex Rivera",
  "PrincipalEmail" : "alex.rivera@example.com",
  "PrincipalType" : "User",
  "Intermediates" : [ {
    "PrincipalType" : "API Key",
    "PrincipalId" : "key_01HQZX3M8N",
    "PrincipalName" : "prod-ingest-key"
  } ]
}
```

### Object ID

PrincipalDetailsObject

### Object Display Name

Principal Details Object

## Column ID

PrincipalDetails

## Display Name

Principal Details

## Description

A set of properties describing the *principal* identified by Principal ID.

## Content Constraints

| Constraint | Value |
| :--- | :--- |
| Dataset | [Cost and Usage](#datasets.costandusage) |
| Column type | Dimension |
| Feature level | Conditional |
| Allows nulls | True |
| Data type | JSON |
| Value format | [JSON Object Format](#attributes.jsonobjectformat) |
| Object | [PrincipalDetailsObject](#datasets.costandusage.principaldetails.principaldetailsobject) |

## Version Introduced

1.5
