# Schema ID

The Schema ID provides the reference item to associate which Schema was used for the generation of a [*FOCUS dataset*](#glossary:FOCUS-dataset).

SchemaId adheres to the following requirements:

* SchemaId MUST be present in an object within the [Schema](#schema) collection.
* SchemaId MUST be of type String.
* SchemaID MUST NOT be null.
* SchemaId SHOULD be a Globally Unique Identifier (GUID).

## Metadata ID

SchemaId

## Metadata Name

Schema ID

## Content constraints

| Constraint    | Value              |
|:--------------|:-------------------|
| Feature level | Mandatory          |
| Allows nulls  | False              |
| Data type     | String             |
| Value format  | GUID (recommended) |

## Introduced (version)

1.0
