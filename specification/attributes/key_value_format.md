# Key-Value Format

Columns that provide Key-Value information are often used in place of separate columns for enumerating data which would be inherently sparse and/or without predetermined keys. This consolidates related information and provides more consistency in the schema. Key-value pairs are also referred to as name-value pairs, attribute-value pairs, or field-value pairs.

## Attribute ID

KeyValueFormat

## Attribute Name

Key-Value Format

## Description

Rules and formatting requirements for columns appearing in a [*FOCUS dataset*](#glossary:FOCUS-dataset) that convey data as key-value pairs.

## Requirements

Column conforming to KeyValueFormat attribute MUST adhere to the following requirements:

* *FOCUS dataset* column MUST be a serialized JSON string, consistent with the [ECMA 404](https://www.ecma-international.org/wp-content/uploads/ECMA-404_2nd_edition_december_2017.pdf) definition of an object.
* Keys in *FOCUS dataset* column MUST be unique within the object.
* Key values in *FOCUS dataset* column MUST be of type number, string, boolean (`true` or `false`), or `null`.
* Key values in *FOCUS dataset* column MUST NOT be objects or arrays.

## Introduced (version)

1.0-preview
