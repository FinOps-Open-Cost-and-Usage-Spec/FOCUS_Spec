# FOCUS Metadata Schema
The FOCUS metadata schema provides a list of the columns present in the FOCUS dataset provided.   


## Logical Section: Schema

## Available Meta Data
 * ### schema_id
   * Use: unique identifier for the schema
   * Type: STRING
 * ### index
   * use: provides the index number for the column to specify the order of the columns, 0 based
   * type: INTEGER
 * ### column_name
   * use: provides the date the schema was created
   * type: STRING
 * ### data_type (provided by API delivery mechanism only)
   * use: provides the endpoint for the schema, including the id
   * type: STRING
   * content_restrictions: <format for specifying datatype needed here>



## Methods of Delivery

### Database 
Although database delivery methods typically include schema information, the FOCUS metadata specification requires a table be provided to supply a schema definition for the FOCUS data. By doing this FOCUS schema metadata can support data where schema is modified by the provider as changes are made and can also support providers that supply FOCUS datasets that are versioned. 


#### Table Name: focus_schema
#### Example Query:

    select * from focus_schemas where schema_id = '1234';

#### Returned Data

| schema_id | ordinal | column_name                    | data_type |
|----------------|---------|--------------------------------|-----------|
| 1234           | 1       | "Name of included FOCUS column" | STRING    |
| 1234           | 2       | "Name of included FOCUS column" | LONG      |
| 1234           | 3       | "Name of included FOCUS column" | DATETIME  |


### API

#### Endpoint: <api_root>/FOCUS/metadata/schema/{id}
#### Example Request:

    GET <api_root>/FOCUS/metadata/schema/{id}
####

#### Response 
```
{
	"schema_id": "1234",
	"columns": [
                 {
                     index: 0,
                     column_name: "<Name of included FOCUS column>",
                     datatype: "STRING"
                 },
                 {
                     index: 1,
                     column_name: "<Name of included FOCUS column>",
                     datatype: "LONG"
                 },
                 {
                     index: 2,
                     column_name: "OurCompaniesSpecialColumn",
                     datatype: "DATETIME"
                 },
         ]
}`
```

