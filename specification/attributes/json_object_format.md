# JSON Object Format

JSON Objects extend the [Key-Value Format](#keyvalueformat) to add support for complex data types like arrays and nested key-value pairs. This format is used when the Key-Value Format is insufficient to represent the complexity, such as when multiple sets of key-value pairs apply to the same charge record. JSON Objects are also referred to as maps, trees, or hashtables.

All complex JSON Object columns defined in the FOCUS specification MUST follow the object formatting requirements listed below.

## Attribute ID

JsonObjectFormat

## Attribute Name

JSON Object Format

## Description

Rules and formatting requirements for columns appearing in a [*FOCUS dataset*](#glossary:FOCUS-dataset) that convey data as complex, hierarchical objects.

## Requirements

* JsonObjectFormat columns MUST contain a serialized JSON string, consistent with the [ECMA 404](https://www.ecma-international.org/wp-content/uploads/ECMA-404_2nd_edition_december_2017.pdf) definition of an object.
* Objects used within JsonObjectFormat adhere to the following additional requirements:
  * Object keys MUST be unique within an object.
  * Object values MUST be one of the following types: number, string, `true`, `false`, array, object, or `null`.
* Arrays used within JsonObjectFormat adhere to the following additional requirements:
  * Array elements MUST all use the same, consistent type.
  * Array elements MUST NOT be repeated.
  * Array elements MUST NOT be null.
* JsonObjectFormat columns MUST conform to all requirements of the corresponding column definition, which may specify or restrict the shape or contents of the Object.
* Data Generator-defined [custom columns](#column_handling:custom-column) whose contents contain a JSON object MUST have their object schema documented by the data generator.
* JsonObjectFormat objects SHOULD NOT exceed 3 levels of nesting.

## Exceptions

None

## Introduced (version)

1.3
