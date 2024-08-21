# Schema Metadata

## Scenario

ACME has only provided one schema for their provided FOCUS data. ACME provides a directory of schemas and each schema is a single file. Acme's provides a file representing the schema for the data they provide.

### Supplied Metadata

#### Location of the schema object:

```
/FOCUS/metadata/schemas/schema-1234-abcde-12345-abcde-12345.json
```

#### Content of the schema object: 

```
{
  "SchemaId": "1234-abcde-12345-abcde-12345",
  "FocusVersion": "1.0",
  "name": "my original schema",
  "CreationDate": "2024-01-01T12:01:03.083z",
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
          }
      ]
} 
```
