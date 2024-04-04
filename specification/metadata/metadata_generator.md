# FOCUS Metadata Generator
The FOCUS metadata provider logical section provides metadata about the provider of the FOCUS data. 

## Logical Section: Schema Generator

## Schema Definition Metadata

* ### billing_generator
    * use: Human readable name of the entity that is generating the billing data 
    * type: STRING
* ### provider_prefix
    * use: Shortened name of the provider supplied to be used as the prefix for tags and may be used to modify the name of custom columns.
    * type: STRING




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

