# Key-Value Format

This is the specified format for providing data in the form of key-value pairs. In addition, this can support keyword data which has a key but not value. This format is used for data such as tags, labels, and resource metadata. 

## Attribute ID

KeyValueFormat

## Attribute Name

Key-Value Format

## Description

Rules and formatting requirements for columns appearing in billing data which convey key-value pairs and/or keyword attributes.

## Requirements

* Data MUST be provided as a string in a format consistent with ECMA-404, as a single Object
    * When applied to the key-value pair, string refers to the key and value refers to the value
* Keys MUST be unique within an object
    * In the case of key collisions, multiple sets of key value pairs may be provided by prefixing tag keys to disambiguate sources
* Keys SHOULD be case insensitive
* Values SHOULD be case sensitive
* Source data containing only a keyword instead of a key-value pair SHOULD be expressed as a key-value pair with keyword being treated as the key and TRUE being the value
* Source data containing a key with a null value MAY be expressed as a key-value pair with key being the key and an empty string being the value 

## Exceptions

None

## Introduced (version)

1.0
