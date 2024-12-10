# Resource ID

A Resource ID is an identifier assigned to a [*resource*](#glossary:resource) by the provider. The Resource ID is commonly used for cost reporting, analysis, and allocation scenarios.

---
The ResourceId column adheres to the following requirements:

* ResourceId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports billing based on provisioned resources.
* If present, the column MUST conform to the following additional requirements:
  * ResourceId MUST be of type String.
  * ResourceId MUST conform to [String Handling](#stringhandling) requirements.
  * ResourceId MUST be null when a charge  is not related to a *resource*.
  * ResourceId MUST NOT be null when a charge is related to a *resource*.
  * ResourceId MUST ensure global uniqueness within the provider.
  * ResourceId SHOULD be a fully-qualified identifier.

---
The ResourceId column adheres to the following requirements:

* The ResourceId column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports billing based on provisioned resources.
* This column MUST be of type String.
* The ResourceId value MAY be a nullable column as some cost data [*rows*](#glossary:row) may not be associated with a *resource*.
* ResourceId MUST appear in the cost data if an identifier is assigned to a *resource* by the provider.
* ResourceId SHOULD be a fully-qualified identifier that ensures global uniqueness within the provider.

## Column ID

ResourceId

## Display Name

Resource ID

## Description

Identifier assigned to a *resource* by the provider.

## Content Constraints

| Constraint      | Value           |
|:----------------|:----------------|
| Column type     | Dimension       |
| Feature level   | Conditional     |
| Allows nulls    | True            |
| Data type       | String          |
| Value format    | \<not specified> |

## Introduced (version)

0.5
