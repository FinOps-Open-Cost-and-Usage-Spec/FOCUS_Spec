# Key-Value Format

## Examples

- Valid key-value format string: `{"key1":"Value1", "key2":"80", "key3":"Value3"}`
- Disambiguating keys using a prefix: `{"parent/key1":"Value1", "child/key1":"Value2"}`
- Usage of a keyword: `{"label1":TRUE}`
  - An example of a source of keyword usage is a system like Jira where labels are applied to a story/epic are present rather than also having a value associated to them
- Key-value pair with a NULL value: `{"key1":""}`

## References:

- [ECMA 404](https://www.ecma-international.org/wp-content/uploads/ECMA-404_2nd_edition_december_2017.pdf)
