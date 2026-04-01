# JSON Object Format

JSON Objects extend the [Key-Value Format](#attributes.key-valueformat) to add support for complex data types like arrays and nested key-value pairs. This format is used when the Key-Value Format is insufficient to represent the complexity, such as when multiple sets of key-value pairs apply to the same charge record. JSON Objects are also referred to as maps, trees, or hashtables.

* [*FOCUS dataset column*](#glossary:FOCUS-dataset-column) MUST contain a serialized JSON string, consistent with the [ECMA 404](https://www.ecma-international.org/wp-content/uploads/ECMA-404_2nd_edition_december_2017.pdf) definition of an object.
* *FOCUS dataset column* MUST conform to all requirements of the corresponding column definition, which may specify or restrict the shape or contents of the object.
* Object in *FOCUS dataset column* SHOULD NOT exceed 3 levels of nesting.
* Key in Object in *FOCUS dataset column* MUST be unique.
* Key value in Object in *FOCUS dataset column* MUST be of type number, string, boolean (`true` or `false`), array, object, or `null`.
* Object in array in *FOCUS dataset column* MUST adhere to the following requirements:
  * Object in array in *FOCUS dataset column* MUST be of a consistent type.
  * Object in array in *FOCUS dataset column* MUST NOT be repeated.
  * Object in array in *FOCUS dataset column* MUST NOT be null.

## Attribute ID

JsonObjectFormat

## Attribute Name

JSON Object Format

## Description

Rules and formatting requirements for columns appearing in a [*FOCUS dataset*](#glossary:FOCUS-dataset) that convey data as complex, hierarchical objects.

## Requirements

Column conforming to JsonObjectFormat attribute MUST adhere to the following requirements:

## Introduced (version)

1.3
