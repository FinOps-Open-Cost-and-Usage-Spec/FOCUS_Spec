# Dataset Metadata Example

## Scenario

ACME provides two FOCUS datasets: Cost and Usage and Contract. Each [Schema](#schema) metadata object includes the [Dataset](#dataset) metadata to indicate which FOCUS Dataset the Schema conforms to.

## Supplied Metadata

Metadata can be provided at a location such as `/FOCUS/metadata/schemas/schema-1234-abcde-12345-abcde-12345.json`.

The schema for the data artifact conforming to the dataset FOCUS Cost and Usage.

```json
{
  "SchemaId": "1234-abcde-12345-abcde-12345",
  "FocusVersion": "1.0",
  "CreationDate": "2024-01-01T12:01:03.083z",
  "DatasetInstanceId": "178151-dbad145e-178151-dbad145e-178151",
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

The schema for the data artifact conforming to the dataset FOCUS Contracts.

```json
{
  "SchemaId": "1234-abcde-12345-abcde-12345",
  "FocusVersion": "1.0",
  "CreationDate": "2024-01-01T12:01:03.083z",
  "DatasetInstanceId": "178151-dbad145e-178151-dbad145e-246811",
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

