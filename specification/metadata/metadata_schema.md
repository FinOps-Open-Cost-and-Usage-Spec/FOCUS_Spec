# FOCUS Metadata Schema 
Each FOCUS dataset must have a metadata about the schema associated with it. The schema metadata provides information about the structure of the data provided. In the event that the provider modifies the columns provided in the FOCUS dataset, metadata about the schema must be provided, including column definitions.  

## Logical Section: Schema


## Available Meta Data:
 * ### schema_id
   * Use: unique identifier for the schema
   * Type: STRING
 * ### FOCUS_version
   * Use: the declared version of the FOCUS data within the schema
   * Type: STRING
 * ### name
   * use: human-readable name for the schema 
   * type: STRING
 * ### creation_date
   * use: date the schema was created
   * type: DATETIME

## Sub-Sections
### Schema Column Definition
  
  * See: [Schema Column Definition](metadata_schema_column_definition.md)
### Schema Reference
  * See: [Schema Reference](metadata_schema_reference.md)
   
## Example Schema Metadata

In this example, the billing data includes two different structures of data. An older schema for data previously provided, and a newer schema for more recent data. Both schemas metata is provided. 

### API

#### Endpoint: <api_root>/FOCUS/metadata/schemas 
#### Example Request:
    endpoint: <api_root>/FOCUS/metadata/schemas 
    method: GET 
####

#### Response 
```
{
	[
		{
			"schema_id": "1234",
			"FOCUS_version": "1.0",
			"name": "my original schema",
			"creation_date": "2024-01-01T12:01:03.083z"
			"schema_column_endpoint": <api_root>/FOCUS/metadata/schemas/1234/columns
		},
		{
			"schema_id": "2345",
			"FOCUS_version": "1.1",
			"name": "my new schema",
			"creation_date": "2024-07-01T12:00:04.001z"
			"schema_column_endpoint": <api_root>/FOCUS/metadata/schemas/2345/columns
		}
	]
}
```




