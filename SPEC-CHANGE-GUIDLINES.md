# FOCUS Specification Change Guidelines

The FOCUS specification is designed to be updated over time to support new use cases and to adapt to changes in the industry. Communication, specificity, and impact are considered as changes are made. While data using the FOCUS specification facilitates a wide range of analysis, the specification and the change process are scoped to the <official use cases> and to the schema described in the FOCUS specification and not to all possible analysis of the data. While example queries may be provided specific queries are not considered expressly supported content. 


## Versions

The FOCUS specification is released periodically. For each release a version number is assigned. Version numbers at this time are not strictly representative of compatibility. The version number is used to identify the release and to provide a reference point for changes. 

## Version Changelog
A changelog is provided specifying helpful information to consumers of focus data. The changelog for each version identifies the following:
- The version number
- Impact Classification
- Change Type Classification 
- Designation of deprecation of a feature or column
- Designation of the addition of a new feature or column
- Description of the change
- Examples of the change if needed

    

## Change Process

TODO: A series of guidelines of how changes are proposed, reviewed, and accepted.

### Addition of a New Feature or Column

    When a new feature or column is introduced to the FOCUS specification, depending on the circumstances of the change, the support of the column may be initially optional. This is to allow for the adoption of a new feature or columne by prodivers that support it, without restricting other adopters from using newer versions of the specification. 
- The feature or item addition is proposed and specification is modified. 
- Change log includes an indication that the new feature/column has been added.
    - example: "Example  Column 1 has been added in version 2.0"


### Removal of a Feature or Column
    
    When a feature or column is removed from the FOCUS specification, the following steps are taken:
- The feature or item removal is proposed, which, in addition to the proposed specification change, includes a deprecation period expressed in terms of Focus versions
  - example: "Example  Column 1 will be deprecated in version 2.1 and removed in version 2.4"
  


## Change Type Classification

Changes to the FOCUS specification are classified into one of the following types:

### Addition:
The addition of a new feature or column to the FOCUS specification.

### Deprecation:
A feature or column from the FOCUS specification is moving to deprecated status discouraging use and indicating that will the same will be removed in a future version 

### Removal:
The removal of a feature or column from the FOCUS specification.

### Improvement:
Modification to improve or refine a feature or column in the FOCUS specification, that was not considered broken. 

### Bug Fix:
Modification to correct an error in the FOCUS specification, that was considered broken.

### Editorial:
Modification to correct a spelling, grammar, or formatting error in the FOCUS specification, that does not impact the intended logic of the specification contents. 


## Change Impact Classification

The FOCUS specification is designed to be updated overtime to increase it use and to adapt to changes in the industry over time.  In order to provide insight into the impact of the change, changes are classified into one of the following categories Change Impact categories. :


 ### Compatible Change:

Any change in the spec that does not require modification by the consumer to continue using the spec for published use cases. 

Examples: 
  - Adding a new column for a new use case or 
  - Adding a new category for an existing that does not require splitting or re-categorization.

### Migration Compatible Change:

Any change that still supports the Published Supported Features, but may require modification to query or ingestion by consumers of a FOCUS dataset.

Examples: 
   - An existing categorization column is changes to split a category into two different categories
   - An existing column that contains a numerical value is has its units changed, requireing a modification to queries using the column. The ability to use the column is preserved but a new query must be written

### Incompatible Change: 
Any change to the spec that ends the support of a Published Use Case. The removal of a Use Case or a column without an alternative source for the data supplied by the column. Incompatible Changes, require prior notification and  

Examples:
   - Removing a column




