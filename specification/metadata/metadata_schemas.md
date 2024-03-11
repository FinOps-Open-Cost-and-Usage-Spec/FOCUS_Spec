# FOCUS Metadata Schema List
The FOCUS metadata schema list provides a list of the metadata schemas that are utilized by the provided FOCUS data. This list acts as a reference that can be refered to by the FOCUS data to identify the schema utilized in the FOCUS dataset/s. 

## Logical Section: Schema

## Available Meta Data
 * ### schema_id
   * Use: unique identifier for the schema
   * Type: string
 * ### name
   * use: provides a human-readable name for the schema 
   * type: string
 * ### creation_date
   * use: provides the date the schema was created
   * type: datetime
 * ### schema_endpoint (provided by API delivery mechanism only)
   * use: provides the endpoint for the schema, including the id
   * type: datetime

   
## Methods of Delivery

### Database 
#### Table Name: focus_schema_verisons 
#### Example Query:

    select * from focus_schema_verisons;

#### Returned Data

| schema_id | name             | creation_date   |
|-----------|------------------|-----------------|
| 1         | my original schema | 2024-01-01T12:01:03.083z |
| 2         | my original schema | 2024-07-01T12:00:04.001z |


### API

#### Endpoint: <api_root>/FOCUS/metadata/schemas 
#### Example Request:

    GET <api_root>/FOCUS/metadata/schemas
####

#### Response 
```
{
	[
		{
			"schema_id": "1234",
			"name": "my original schema",
			"creation_date": "2024-01-01T12:01:03.083z"
			"schema_endpoint": <needs possibly a better name> my_awesome_focus_api/metadata/schemas/1234
		},
		{
			"schema_id": "2345",
			"name": "my new schema",
			"creation_date": "2024-07-01T12:00:04.001z"
			"schema_endpoint": <needs possibly a better name> my_awesome_focus_api/metadata/schemas/2345
		}
	]
}
```




