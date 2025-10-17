# Examples: Metadata

The following sections contain examples of metadata provided by a hypothetical FOCUS data provider called ACME to supply the required reference between the [*FOCUS datasets*](#glossary:FOCUS-dataset) and the schema metadata.  Provider implementations will vary on how the metadata is disseminated; however, the provider's chosen metadata delivery approach should be able to support the structure represented in this example.

In this example, the provider supports delivery of FOCUS data via file export to a data storage system. It uses JSON as the format for providing the metadata. The provider delivers data every 12 hours into a path structure described below:

| Type of data        | Path              |
|:--------------------|:------------------|
| Export location     | `/FOCUS`          |
| Metadata location   | `/FOCUS/metadata` |
| Cost data location  | `/FOCUS/data`     |

Here are some metadata examples for various scenarios:
