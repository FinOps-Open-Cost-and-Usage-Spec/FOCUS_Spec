# Object Format

## Examples

- Valid key-value format demonstrating all valid values (object structures may differ, but should use these types):

  ```json
  {
    "KeyString": "Value1",
    "KeyNumber": 42,
    "KeyBool":   true,
    "KeyBool2":  false,
    "KeyEmpty":  "",
    "KeyNull":   null,
    "KeyStrArr": ["Value1", "Value2"],
    "KeyNumArr": [3, 42, 86, 999],
    "KeyObjArr": [{ "Key": "Value1" }, { "Key": "Value2" }]
    "KeyObject": {
        "KeyString": "Value1",
        "KeyNumber": 42,
        "KeyBool":   true,
        "KeyBool2":  false,
        "KeyEmpty":  "",
        "KeyNull":   null,
        "KeyStrArr": ["Value1", "Value2"],
        "KeyNumArr": [3, 42, 86, 999],
        "KeyObjArr": [{ "Key": "Value1" }, { "Key": "Value2" }]
    }
  }
  ```

- Disambiguating keys using a prefix: `{"parent/key1":"Value1", "child/key1":"Value2"}`

## Discussion

- Object format should extend Key-Value format with added support for arrays and nested objects.
- Object format should not deviate from the base Key-value format rules.
- Object format should be used sparingly and only when absolutely needed for scenarios that are not common for non-technical users given complex querying logic.
- Object values should prefer nested objects with named keys rather than arrays due to complex lookup logic required to aggregate specific array elements across many rows (e.g., selecting a single number out of an array that has a mix of different types of data points).

## References

- [ECMA 404](https://www.ecma-international.org/wp-content/uploads/ECMA-404_2nd_edition_december_2017.pdf)
