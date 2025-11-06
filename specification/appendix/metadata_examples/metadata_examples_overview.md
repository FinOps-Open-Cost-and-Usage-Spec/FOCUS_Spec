# Examples: Metadata

The following sections contain examples of metadata provided by a hypothetical FOCUS data generator called ACME to supply the required reference between the [*FOCUS dataset artifacts*](#glossary:dataset-instance-artifact) and the [Metadata](#metadata).  Data Generator implementations will vary on how the metadata is disseminated; however, the data generator's chosen metadata delivery approach should be able to support the structure represented in this example.

In this example, the data generator supports delivery of FOCUS data via file export to a data storage system. It uses JSON as the format for providing the metadata. The data generator delivers data every 12 hours into a path structure described below:

| Type of data        | Path              |
|:--------------------|:------------------|
| Export location     | `/FOCUS`          |
| Metadata location   | `/FOCUS/metadata` |
| Cost data location  | `/FOCUS/data`     |

Here are some metadata examples for various scenarios:
