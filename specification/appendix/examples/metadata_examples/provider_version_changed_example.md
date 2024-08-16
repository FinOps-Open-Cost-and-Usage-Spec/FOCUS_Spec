## Focus Version Changed by Provider Using Provider Version

### Scenario

ACME uses provider version. They have made a change to their approach to create Focus data that does not adopt a new Focus Version, nor make a change the included columns but does impact values in the data. This is to illustrate that Provider Version changes are independent of column changes, however provider version changes may include column changes.

The provider creates a new schema object to represent the new schema. The provider includes both the new Focus Version and Provider Version in the schema object.
### Supplied Metadata

#### Location of the new schema object:

```
/FOCUS/metadata/schemas/schema-56789-abcde-56789-abcde-56789.json
```

#### Content of the new schema object:

```
 {
  "SchemaId": "56789-abcde-56789-abcde-56789",
  "FocusVersion": "1.1",
  "ProviderVersion": "2.4",
  "name": "New Columns",
  "CreationDate": "2024-05-02T12:01:03.083z",
  "ColumnDefinition": [
    {
      "ColumnName": "BillingAccountId",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8"
          },
          {
                "ColumnName": "BillingAccountName",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8"
          },
          {
               "ColumnName": "ChargePeriodStart",
               "DataType": "DATETIME"
          },
          {
                "ColumnName": "ChargePeriodEnd",
                "DataType": "DATETIME"
          },
          {
                "ColumnName": "BilledCost",
                "DataType": "DECIMAL",
                "NumericPrecision": 20,
                "NumberScale": 10
          },
          {
                "ColumnName": "EffecitiveCost",
                "DataType": "DECIMAL",
                "NumericPrecision": 20,
                "NumberScale": 10
          },
          {
                "ColumnName": "Tags",
                "DataType": "JSON",
                "ProviderTagPrefixes": ["awecorp", "ac"]
          },
          {
                "ColumnName": "x_awesome_column1",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8"
          },
          {
                "ColumnName": "x_awesome_column2",
                "DataType": "DATETIME"
          },
      ]
}
```
For an example of how Acme ensures the schema metadata reference requirement is met see: [Schema Metadata to FOCUS Data Reference](../schema_metadata_reference_example.md)


