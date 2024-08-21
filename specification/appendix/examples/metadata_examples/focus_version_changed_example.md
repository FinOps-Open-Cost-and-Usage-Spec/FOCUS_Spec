# Provider has an error in their schema metadata.

## Scenario

Acme's previous exports used Focus Version 1.0. They are now going to adopt Focus Version 1.1.  It is required that they create a new schema metadata object when using a new focus version regardless of schema changes. In this example the FOCUS new version adoption doesn't include columns changes. This is to illustrate that Focus Version changes are independent of column changes, however this scenario is unlikely.

### Supplied Metadata

#### Location of the new schema object:

```
/FOCUS/metadata/schemas/schema-45678-abcde-45678-abcde-45678.json
```

#### Content of the schema object: 

```
 {
  "SchemaId": "45678-abcde-45678-abcde-45678",
  "FocusVersion": "1.1",
  "name": "Focus Version 1.1 Schema",
  "CreationDate": "2024-04-02T12:01:03.083z",
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
