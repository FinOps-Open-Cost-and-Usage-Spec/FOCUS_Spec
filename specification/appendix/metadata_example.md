# Metadata Examples

The following is an example metadata JSON structure provided by a hypothetical FOCUS data provider. This example illustrates an example of how a provider can supply the required reference between the FOCUS data and the schema metadata.  Provider implementations will vary on how the metadata is stored and retrieved, however the providers chosen metadata delivery approach should be able to support the structure represented in this example. 

## Scenario
In this example, the provider supports delivery of FOCUS data via file export to a data storage system. The provider delivers data every 12 hours. 

#### Example Data Structure

- export root location: `/FOCUS`
- metadata location: `/FOCUS/metadata`
- focus data location: `/FOCUS/data`

## Data Generator Metadata

#### Supplied Metadata

Location: /FOCUS/metadata/data_generator.json

Content: 
```
{
    "DataGenerator": "ACME"
}
```

## Schema Metadata

### Scenario

ACME has only provided one schema for their provided FOCUS data. ACME provides a directory of schemas and each schema is a single file. Currently, there is only one file in this directory. 

#### Supplied Metadata

Location: `/FOCUS/metadata/schemas/schema-1234-abcde-12345-abcde-12345.json`

Content: 
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
## Schema Metadata to FOCUS Data Reference

### Scenario

For each FOCUS data export, ACME includes a metadata reference to the schema object. Because multiple files are provided, ACME has elected to include a metadata file that includes the focus schema reference that applies to the data export files. 

#### Supplied Metadata

Location: `/FOCUS/data/export1-metadata.json`

Content: 
```
{
  "SchemaId":"1234-abcde-12345-abcde-12345",  
  "data_location": 
  [
    {
      "filepath": "/FOCUS/data/export1/export1-part1.csv",
      "total_bytes": 9010387,
      "total_rows": 4450
    },
    {
      "filepath": "/FOCUS/data/export1/export1-part2.csv",
      "total_bytes": 9010387,
      "total_rows": 4450
    },
    {
      "filepath": "/FOCUS/data/export1/export1-part3.csv",
      "total_bytes": 9010387,
      "total_rows": 4450
    },
    {
      "filepath": "/FOCUS/data/export1/export1-part4.csv",
      "total_bytes": 9010387,
      "total_rows": 4450
    }
  ]
}
```

## Changes to FOCUS Data Columns

### Scenario

ACME has decided add additional columns to their FOCUS data export. The new columns are x_awesome_column1 and x_awesome_column2.

### New schema metadata object

The provider creates a new schema object to represent the new schema, this schema object has a unique SchemaId.

#### Supplied Metadata

Location: `/FOCUS/metadata/schemas/schema-23456-abcde-23456-abcde-23456.json`

Content:
```
 {
  "SchemaId": "23456-abcde-23456-abcde-23456",
  "FocusVersion": "1.0",
  "name": "New Columns",
  "CreationDate": "2024-02-02T12:01:03.083z",
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

### New schema metadata object is referenced in export metadata

The provider includes a reference to the applicable schema object for exports that use the new schema. 

#### Supplied Metadata

Location: `/FOCUS/data/export2-metadata.json`

Content:
```
{
  "SchemaId":"23456-abcde-23456-abcde-23456",  
  "data_location": 
  [
    {
      "filepath": "/FOCUS/data/export2/export2-part1.csv",
      "total_bytes": 9010387,
      "total_rows": 4450
    },
    {
      "filepath": "/FOCUS/data/export2/export2-part2.csv",
      "total_bytes": 9010387,
      "total_rows": 4450
    },
    {
      "filepath": "/FOCUS/data/export2/export2-part3.csv",
      "total_bytes": 9010387,
      "total_rows": 4450
    },
    {
      "filepath": "/FOCUS/data/export2/export2-part4.csv",
      "total_bytes": 9010387,
      "total_rows": 4450
    }
  ]
}
```
