# Introduction

The FOCUS specification's metadata specification provides a common, provider-neutral metadata repository. This metadata provides practitioners information on the schema of FOCUS data, the location of the FOCUS data, and recency of the FOCUS data (this is a forward looking statement for now)




## Logical Sections

### FOCUS Metadata Version
 This section provides the version of the metadata structure. This is independent of the FOCUS specification version. The metadata version declares the version of the metadata structure and not the providers modified schema. When new logical sections are added or requirements for those sections are modified metadata version will be incremented.

See:[Metadata Version](metadata_version.md)

### Schemas
This section provides metadata about the schemas of the FOCUS data. The schemas section provides a list of the schemas used and a definition of those schemas. A schema represents the logical structure of the data, including what columns are included, and what data types are used for each column.
See:[Metdata Schema](metadata_schemas.md)

### FUTURE Sections
- Manifest: declares the location of data
- recency: delcares how up to date the FOCUS data is


## Methods of Delivery

Because methods of delivery of FOCUS differ by provider, the metadata specification provides guidance on how metadata is to be provided for each method of delivery. The supported methods of delivery are:


### Database
Provider supplies FOCUS data via a database that the provider itself maintains. Schema metadata is available via database queries. 

Logical sections of the metadata specifications are provided under the following breakdown:
#### Database Schema Location
Schema name is to "FOCUS_metadata"

#### Database Schema Location
Logical sections are designated by tables prefix. For example the table that specifies the list of schemas would be called schema_schemas.

### API
Provider supplies FOCUS data via a rest API. Schema metadata is available via API calls. In this case specific endpoints and their responding data are documented.




