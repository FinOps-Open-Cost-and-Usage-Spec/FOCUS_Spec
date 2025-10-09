# FOCUS Specification Change Guidelines

The FOCUS specification is designed to be updated over time to support new use cases and adapt to industry changes. Communication, specificity, and impact are considered as changes are made. While data using the FOCUS specification facilitates a wide range of analysis, the specification and the change process are scoped to the <official use cases> and the schema described in the FOCUS specification and not to all possible data analyses. While example queries may be provided, specific queries are not considered expressly supported content. 

## Versions

The FOCUS specification is released periodically. For each release a version number is assigned. Version numbers at this time are not strictly representative of compatibility. The version number is used to identify the release and to provide a reference point for changes. 

### Supported Release Cadence
For planning and conformance purposes, FOCUS may identify certain MINOR releases as officially‑supported for broad adoption and conformance evaluation. Deprecation retention requirements reference these officially‑supported releases. The set of officially‑supported releases is recorded in the release notes and/or conformance program documentation.

## Version Changelog

A changelog is provided specifying helpful information to consumers of the FOCUS specification. The changelog for each version identifies the following:

* The version number
* Impact Classification
* Change Type Classification 
* Deprecation designation of a feature or column to include the version where deprecation occured
   * Any exception rationale if removal precedes the retention period
* Designation of the addition of a new feature or column
* Description of the change
* Examples of the change, if needed

## Change Process

### Addition of a New Feature or Column

When a new feature or column is introduced to the FOCUS specification, depending on the circumstances of the change, its support may be initially optional. This allows providers that support it to adopt the new feature or column without restricting other adopters from using newer versions of the specification. 

* Within the Content Constraints section, Feature Level indicates whether the column is Mandatory (i.e., required), Conditional (i.e., required under certain circumstances), or Recommended (i.e., not required).
   *  Example: Feature level is specified: "Recommended"    
* Changelog indicates that the new feature/column has been added.
    * Example: "Column 1 has been added in version 2.0."

### Renaming a Column or Metadata 
    
The FOCUS specification requires the renaming of a column or metadata to be declared in the specification.

* The column or metdata specification is to include a section that indicates the previous name and the version in which it was changed
* Example: "Example1 column was renamed Example2 in FOCUS version 2.1"

### Deprecation and Removal of a Feature or Column
    
The FOCUS specification requires that removal actions are preceded with a deprecation notice.

* The feature or item removal is proposed, which must designate the column or metadata as deprecated.
  * If the removal version is not yet determined, the changelog MUST state, "This column will be removed at a future FOCUS version."
  * If the removal version has already been determined, the changelog MUST state, "This column will be removed in version 2.1."
* Prior to removal, the FOCUS specification MUST be updated to include the version that will remove the deprecated column/metadata.

#### Deprecation Retention Period

Once a capability or column is designated as deprecated in a published version of the FOCUS specification:

* It MUST remain in the specification for a minimum of one release before removal (e.g., deprecated in v1.3, removed in v1.4).
* Exceptions (e.g., legal, security, or privacy requirements) MAY justify immediate removal with documented rationale in the changelog.

When a feature or column is deprecated, it MUST be classified as:
* Migration Compatible if the same supported feature is fully supported by another feature or column in the specification.
* Incompatible if deprecation signals planned loss of support for a supported feature.

The deprecation notice in the changelog MUST include this classification. If circumstances change during the retention period, the updated classification MUST be documented in the removal version's changelog.

#### Expected Behavior for Removed Capabilities

Data generators are expected to remove capabilities at the same time that the FOCUS specification does. If a data generator chooses to retain a capability (e.g., column) after it has been removed from the FOCUS specification, they must explain the rationale in their FOCUS documentation (e.g., conformance gap report). 

## Change Type Classification

Changes to the FOCUS specification are classified into one of the following types:

### Addition

The addition of a new feature or column to the FOCUS specification.

### Deprecation

A feature or column from the FOCUS specification is moving to deprecated status, discouraging use and indicating that the same will be removed in a future version.

### Removal

A feature or column removed from the specification after completing deprecation requirements or with documented exception rationale. The changelog specifies the removal version, deprecation timeline, and compatibility classification.

### Improvement

Modification to improve or refine a feature or column in the FOCUS specification that was not considered broken. 

### Bug Fix

Modification to correct an error in the FOCUS specification, that was considered broken.

### Editorial

Modification to correct a spelling, grammar, or formatting error in the FOCUS specification that does not impact the intended logic of the specification contents. 

## Change Impact Classification

The FOCUS specification is designed to be updated overtime to increase use and to adapt to changes in the industry over time.  In order to provide insight into the impact of the change, changes are classified into one of the following categories Change Impact categories:

 ### Compatible Change

Any change in the specification that does not require modification by the consumer to continue using the specification for published use cases. 

Examples: 
  * Adding a new column for a new supported feature 
  * Adding a new category for an existing column that does not require splitting or re-categorization.

### Migration Compatible Change

Any change that still supports the Published Supported Features, but may require modification to query or ingestion by consumers of a FOCUS dataset.

Examples: 
   * An existing categorization column is changed to split a category into two different categories
   * An existing column that contains a numerical value is has its units changed, requiring a modification to queries using the column. The ability to use the column is preserved but a new query must be written

### Incompatible Change

The removal of a supported feature or column without an alternative feature or column that fully supports the same use case. Removals MUST observe the Deprecation Retention Period requirements prior to removal.

Examples:
   - Removing a column without introducing a replacement column
