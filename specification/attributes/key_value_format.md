# Key-Value Format

This is the specified format for providing data in the form of key-value pairs, which are also known as name-value pairs, attribute-value pairs, and field-value pairs in other contexts. 

This format is often used in place of enumerating data which would be inherently sparse and/or without predetermined keys (attributes) into separate columns. To faciliate parsing, this format does not support nesting.

## Attribute ID

KeyValueFormat

## Attribute Name

Key-Value Format

## Description

Rules and formatting requirements for columns appearing in billing data which convey data as key-value pairs.

## Requirements

* Columns subject to Key-Value Format MUST be a serialized JSON string, consistent with the ECMA-404 definition of an object.
* Keys MUST be unique within an object.
* Values MAY be a number, string, `true`, `false`, or `null`.
  * Values MAY NOT be an object nor an array.

## Exceptions

None

## Introduced (version)

1.0
