# FOCUS Metadata Version
The FOCUS metadata version is independent of the FOCUS specification version. The metadata version declares the version of the metadata structure and not the providers modified schema. When new logical sections are added or requirements for those sections are modified metadata version will be incremented. By retrieving the focus metadata version the practioner is able to understand what metadata will be present and how to use it. 

## Available Meta Data
 ###FOCUS_metadata_version: Specifies the version of the metadata structure. 
    
## Methods of Delivery

### Database 
#### Table Name: focus_schema_verisons 
#### Example Query:

    select * from focus_schema_verisons;

#### Returned Data

| focus_metadata_version |
|------------------------|
| 1                      |


### API

#### Endpoint: <api_root>/FOCUS/metadata/version 
#### Example Request:

    GET <api_root>/FOCUS/metadata/version
####

#### Response 
```
{"focus_metadata_version": "1.1"}
```




