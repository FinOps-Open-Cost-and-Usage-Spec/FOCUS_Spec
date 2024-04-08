# Metadata Example API

## Example Generator Metadata

In this example the billing data generator's FOCUS metadata API is queried for the provider metadata.

#### Endpoint: <api_root>/FOCUS/metadata/provider
#### Example Request:

    Method: GET 
    Endpoint : <api_root>/FOCUS/metadata/provider
####

#### Response
```
{
	"billing_generator": "awesome_corp",
	"provider_prefix": "awecorp
   
}`
```

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

## Example Schema Definition Metadata

In this example the billing data generator's FOCUS metadata API is queried for the schema_id = 1234. 

### API Schema 

#### Endpoint: <api_root>/FOCUS/metadata/schema/{id}/columns
#### Example Request:

    Method: GET 
    Endpoint : <api_root>/FOCUS/metadata/schema/1234/columns
####

#### Response 
```
{
	"schema_id": "1234",
	"FOCUS_version": "1.0",
    "name": "my original schema",
    "creation_date": "2024-01-01T12:01:03.083z"
	"column_definition": [
                 {
                     column_name: "BillingAccountId",
                     datatype: "STRING"
                     max_length: 64,
                     encoding: "UTF-8"
                 },
                 {
                     column_name: "BillingAccountName",
                     datatype: "STRING"
                     max_length: 64,
                     encoding: "UTF-8"
                 },
                 {
                     column_name: "ChargePeriodStart",
                     datatype: "DATETIME"
                 },
                 {
                     column_name: "ChargePeriodEnd",
                     datatype: "DATETIME"
                 },
                 {
                     column_name: "BilledCost",
                     datatype: "DECIMAL",
                     precision: 20,
                     scale: 10
                 },
                 {
                     column_name: "EffecitiveCost",
                     datatype: "DECIMAL",
                     precision: 20,
                     scale: 10
                 },
         ]
}`
```

## Example Schema Reference Metadata

In this example, when the provider returns the FOCUS data they include in the response a reference to the schema utilized in the FOCUS dataset. 

#### Example Request:
    Endpoint: <api_root>/FOCUS/data/2024010001
    Method: GET 
####

#### Response
```
{
	"schema_id": "1234",
	"data": [
             ...
         ]
}
```