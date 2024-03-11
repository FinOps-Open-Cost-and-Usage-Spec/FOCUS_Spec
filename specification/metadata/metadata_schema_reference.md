# Reference in FOCUS Data
The provider itself must provide a reference to the schema utilized in the FOCUS dataset. This reference can be a schema_id or a schema_endpoint. This reference ensures that the practioners is able to programatically deteremine the schema used by that FOCUS data entity. 

## Available Meta Data
* ### schema_id
    * Use: unique identifier for the schema
    * Type: STRING


## Methods of Delivery

### Database
The provider must supply a table that identifies the schema used for the corresponding FOCUS dataset table

#### Table Name: focus_schema_reference
#### Example Query:

    select * from focus_schema_reference where schema_id = '1234';

#### Returned Data

| schema_id | focus_table           | 
|----------|-----------------------|
| 1234     | FOCUS_data_2024-01-01 |
| 1234     | FOCUS_data_2024-04-01 |
| 2345     | FOCUS_data_2024-08-01 |


### API
When the provider returns the FOCUS data they include in the response a reference to the schema utilized in the FOCUS dataset. This reference can be a schema_id or a schema_endpoint.

#### Example Request:

    GET <api_root>/FOCUS/data/<more_specific_api>
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