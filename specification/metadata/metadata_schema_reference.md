# Reference in FOCUS Data
The provider must provide a reference to the schema utilized in the FOCUS dataset. Because methods of delivery vary, the reference to the schema utilized may be built in, such as a database, where schema is an included component of the tables. Others such as a file, may not be built in and therefore need to provide an ID to the schema used.  

## Logical Section: Schema
### Subsection: Schema Reference

## Available Meta Data:
* ### schema_id
    * Use: unique identifier for the schema
    * Type: STRING


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