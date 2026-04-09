## Diff

## Requirements

* JsonObjectFormat columns MUST contain a serialized JSON string, consistent with the ECMA 404 definition of an object.
* Objects used within JsonObjectFormat {+MUST+} adhere to the following[-additional-] requirements:
  * Object keys MUST be unique within an object.
  * Object values MUST be one of the following types: number, string, `true`, `false`, array, object, or `null`.
* Arrays used within JsonObjectFormat {+MUST+} adhere to the following[-additional-] requirements:
  * Array elements MUST all use the same, consistent type.
  * Array elements MUST NOT be repeated.
  * Array elements MUST NOT be null.
