# Schema Metadata to FOCUS Data Reference

## Scenario

Acme makes a change to the schema of their data exports. For each FOCUS data export, ACME includes a metadata reference to the schema object.  Because multiple files are provided, Acme has elected to include a metadata file that includes the focus schema reference that applies to the data export files. They therefore include the new schema id in their export metadata file. 

### Supplied Metadata

#### Location of the existing schema metadata reference file: 

```
/FOCUS/data/export1-metadata.json
```

#### Content for the existing export metadata object: 
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


#### Location for the new export metadata object:
```
`/FOCUS/data/export2-metadata.json`
```
#### Content for the new export metadata object:
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

