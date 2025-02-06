# Object Format

Columns that provide complex, hierarchical information can be used in place of separate columns to support more dynamic structures that may change across rows, but where the simpler [*Key-Value Format*](#key-valueformat) may not be sufficient. Objects extend key-value pairs to add support for complex data types like arrays and nested key-value pairs. Objects are also referred to as maps, trees, or hashtables.

All complex object columns defined in the FOCUS specification MUST follow the object formatting requirements listed below.

## Attribute ID

ObjectFormat

## Attribute Name

Object Format

## Description

Rules and formatting requirements for columns appearing in a [*FOCUS dataset*](#glossary:FOCUS-dataset) that convey data as complex, hierarchical objects.

## Requirements

* Object Format columns MUST contain a serialized JSON string, consistent with the [ECMA 404](https://www.ecma-international.org/wp-content/uploads/ECMA-404_2nd_edition_december_2017.pdf) definition of an object.
* Object keys MUST be unique within an object.
* Object values MUST be one of the following types: number, string, `true`, `false`, array, object, or `null`.
* Object array elements MUST be one of the following types: number, string, or object.
* Object array elements MUST all use the same, consistent type.
* Object array elements MUST NOT be repeated.
* Object array elements MUST NOT be null.
* Objects are RECOMMENDED to not exceed 3 levels of nesting.

## Exceptions

None

## Introduced (version)

1.0-preview
