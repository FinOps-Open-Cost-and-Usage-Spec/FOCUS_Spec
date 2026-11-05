# Schema ID

The [Schema ID](#meta) provides the reference item to associate which Schema was used for the generation of a [FOCUS dataset](#term).

[SchemaId](#meta) adheres to the following requirements:

* [SchemaId](#meta) MUST be present in an object within the [Schema](#meta) collection.
* [SchemaId](#meta) MUST be of type String.
* SchemaID MUST NOT be null.
* [SchemaId](#meta) SHOULD be a Globally Unique Identifier (GUID).

## Metadata ID

SchemaId

## Metadata Name

Schema ID

## Content Constraints

| Constraint    | Value              |
|:--------------|:-------------------|
| Feature level | Mandatory          |
| Allows nulls  | False              |
| Data type     | String             |
| Value format  | GUID (recommended) |

## Version Introduced

1.0
