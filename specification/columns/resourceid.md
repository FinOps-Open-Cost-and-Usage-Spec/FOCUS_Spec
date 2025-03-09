# Resource ID

A Resource ID is an identifier assigned to a [*resource*](#glossary:resource) by the service provider. The Resource ID is commonly used for cost reporting, analysis, and allocation scenarios.

The ResourceId column adheres to the following requirements:

* The ResourceId column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports billing based on provisioned resources.
* This column MUST be of type String.
* The ResourceId value MAY be a nullable column as some cost data [*rows*](#glossary:row) may not be associated with a *resource*.
* ResourceId MUST appear in the cost data if an identifier is assigned to a *resource* by the service provider.
* ResourceId SHOULD be a fully-qualified identifier that ensures global uniqueness within the service provider.

## Column ID

ResourceId

## Display Name

Resource ID

## Description

Identifier assigned to a *resource* by the service provider.

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
