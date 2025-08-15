ACME provides two FOCUS datasets: Cost and Usage and Contract. Each [Schema](#schema) 

# Schema Metadata

## Scenario

ACME provides two FOCUS datasets: Cost and Usage and Contract. Each [Schema](#schema). Each schema metadat object includes the Dataset metadat to indicate which Focus Dataset the Schema conforms with. 

## Supplied Metadata

Metadata can be provided at a location such as `/FOCUS/metadata/schemas/schema-1234-abcde-12345-abcde-12345.json`.

The schema for the data artifact conforming to the dataset FOCUS Cost and Usage 

```json
{
  "SchemaId": "1234-abcde-12345-abcde-12345",
  "FocusVersion": "1.0",
  "CreationDate": "2024-01-01T12:01:03.083z",
  "Dataset": "FOCUS Cost and Usage",
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
                "ColumnName": "EffectiveCost",
                "DataType": "DECIMAL",
                "NumericPrecision": 20,
                "NumberScale": 10
          },
          {
                "ColumnName": "Tags",
                "DataType": "JSON",
                "ProviderTagPrefixes": ["acme", "ac"]
          }
      ]
}
```

The schema for the data artifact conforming to the dataset FOCUS Contracts 

```json
{
  "SchemaId": "1234-abcde-12345-abcde-12345",
  "FocusVersion": "1.0",
  "CreationDate": "2024-01-01T12:01:03.083z",
  "Dataset": "FOCUS Contract",
  "ColumnDefinition": [
          {
                "ColumnName": "ContractId",
                "DataType": "STRING",
                "StringMaxLength": 64,
                "StringEncoding": "UTF-8"
          },
          {
              "ColumnName": "OverColumnName",
              "DataType": "STRING",
              "StringMaxLength": 64,
              "StringEncoding": "UTF-8"
          }
      ]
}
```
