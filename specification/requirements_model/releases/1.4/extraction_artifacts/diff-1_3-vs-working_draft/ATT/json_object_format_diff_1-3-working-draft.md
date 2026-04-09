## Diff

@@ -1,13 +1,13 @@
## Requirements

* JsonObjectFormat columns MUST contain a serialized JSON string, consistent with the ECMA 404 definition of an object.
* Objects used within JsonObjectFormat {+MUST+} adhere to the following[-additional-] requirements:
  * Object keys MUST be unique within an object.
  * Object values MUST be one of the following types: number, string, `true`, `false`, array, object, or `null`.
* Arrays used within JsonObjectFormat {+MUST+} adhere to the following[-additional-] requirements:
  * Array elements MUST all use the same, consistent type.
  * Array elements MUST NOT be repeated.
  * Array elements MUST NOT be null.
* JsonObjectFormat columns MUST conform to all requirements of the corresponding column definition, which may specify or restrict the shape or contents of the Object.
* Data Generator-defined custom columns whose contents contain a JSON object MUST have their object schema documented by the data generator.
* JsonObjectFormat objects SHOULD NOT exceed 3 levels of nesting.
