# FOCUS Metadata Schema Column Definition
The FOCUS metadata schema column definition provides a list of the columns present in the FOCUS dataset along with metadata about the columsn. The intent of the schema metadata is to aid pracitioners to understand the structure of the FOCUS data, without the need to parse the included dataset. 


## Logical Section: Schema 
### Subsection: Schema Column Definition

## Schema Definition Metadata

 * ### column_name
   * use: provides the date the schema was created
   * type: STRING
 * ### data_type
   * use: data type of the column as provided and must be provided for all columns in the FOCUS dataset
   * type: STRING
 * ### max_length
   * use: provides a maximum character length for columns whose data type where character length is relevant. This is typically provided for String type columns
   * type: Integer
* ### precision
  * use: provide the maximum number of digits for the values in the column. This is typically provided for numeric columns
  * type: Integer 
* ### scale
   * use: provide the maximum number of digits after the decimal point. This is typically provided for numeric columns
   * type: Integer
* ### encoding
   * use: provides the encoding of the column. This is typically provided for string columns
   * type: STRING



## Example Schema Definition Metadata

### API Schema 

#### Endpoint: <api_root>/FOCUS/metadata/schema/{id}/columns
#### Example Request:

    Method: GET 
    Endpoint : <api_root>/FOCUS/metadata/schema/{id}/columns
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

