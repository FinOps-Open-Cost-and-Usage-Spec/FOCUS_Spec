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
* Deprecation designation of a feature or column to include the version where deprecation occurred
   * Any exception rationale if removal precedes the retention period
* Designation of the addition of a new dataset, to include whether it is a preview, and its promotion, extension, or removal in a later version
  * The reason, when a new dataset is published without preview status
* Designation of the addition of a new feature or column
* Description of the change
* Examples of the change, if needed

## Change Process

### Addition of a New Feature or Column

When a new feature or column is introduced to the FOCUS specification, depending on the circumstances of the change, its support may be initially optional. This allows data generators that support it to adopt the new feature or column without restricting other adopters from using newer versions of the specification. 

* Within the Content Constraints section, Feature Level indicates whether the column is Mandatory (i.e., required), Conditional (i.e., required under certain circumstances), Recommended (i.e., not required, but encouraged), or Optional (i.e., not required).
   *  Example: Feature level is specified: "Recommended"    
* Changelog indicates that the new feature/column has been added.
    * Example: "Column 1 has been added in version 2.0."

### Renaming a Column or Metadata 
    
The FOCUS specification requires the renaming of a column or metadata to be declared in the specification.

* The column or metadata specification is to include a section that indicates the previous name and the version in which it was changed
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

Data generators are expected to remove capabilities at the same time that the FOCUS specification does. If a data generator chooses to retain a capability (e.g., column) after it has been removed from the FOCUS specification, they must explain the rationale in their FOCUS documentation (e.g., conformance gap report). See the [Requirements Model Guidelines](writing-requirements-model-guidelines.md) for additional information. 

### Entity Removal Process

To ensure complete and error-free removal of deprecated entities from the FOCUS specification, follow this checklist:

1. **Confirm Deprecation Status**: Verify the entity has been deprecated for at least one release cycle and meets retention period requirements. A [preview](#preview-process) dataset is exempt and MAY be removed without a deprecation notice or retention period.

2. **Identify All Files Related to the Entity**:
   * Remove definition files from specification paths (for example: `specification/datasets/*/columns/`, or other relevant subfolders)
   * Remove any applicable supporting content files from `supporting_content/`
   * Remove the entity from any tables or listings that include it (for example: dataset tables in `specification/datasets/*/dataset.md`)
  
3. **Update References**:
   * Remove any associated normative requirements (for example: “MUST” entries in dataset or requirement documentation)
   * Search for and update or remove all links to and mentions of the removed entity
   * Update migration guidance documents to reflect removal
   * Review and update any examples or tables referencing the removed entity

4. **Update Version Information**:
   * Update changelog to document the removal
   * Update version migration guidance to indicate entities have been removed

5. **Validate Removal**:
   * Ensure no broken links remain in the specification
   * Verify build processes complete successfully
   * Check that all references have been addressed

6. **Communicate Changes**:
   * Update release notes with removal details
   * Notify stakeholders of the removal

## Preview Process

Preview is a status for a FOCUS dataset published in a version of FOCUS so implementers can build it and report what they find. A dataset with this status is called a preview. See [Preview](../../specification/overview.md#preview) in the specification for the definition.

Each preview has a tracking issue with a scope list, which names the requirements and supporting entities outside the dataset that are part of the preview (see [Designating a Preview](#designating-a-preview)). Stable content is any content not marked as preview.

A supporting entity is an entity defined outside a preview dataset's own section that the dataset depends on and that exists only for the preview (e.g., an operating model condition, or an object schema such as the SKU Price Eligibility Object Schema that the SKU Price dataset uses). A requirement is not a supporting entity.

**Proposed (FR #2782, question 1):**

* **Proposed:** The definition of supporting entity above, with its test: an entity outside the dataset that exists only for the preview.
* **Why:** The SKU Price Preview notes and the scope list rule for requirements already use this test, and all three supporting entities on the [SKU Price scope list](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2768) meet it. Under the test, stable content (e.g., a column in another dataset, a glossary term, or an operating model condition that stable requirements also use, such as Includes Regions) cannot be a supporting entity, so a scope list cannot let stable content change without a deprecation notice.
* **Open:** Confirm the test.
* **Open:** Whether supporting entity also needs a glossary entry, since the specification's overview and General Availability glossary entry use the term.
* **Open:** What happens when stable content later starts to use a supporting entity, which then no longer meets the test. One answer: before that stable content is published, the entity leaves the scope list, its Preview markings are removed, and it follows the normal change management process. What its Version Introduced section then shows follows question 11.
* **Elsewhere:** Whether content in a stable dataset, such as a column, can be a preview stays open on FR #960.

### Designating a Preview

A FOCUS dataset preview MUST adhere to the following requirements:

* A new FOCUS dataset SHOULD be published as a preview in the first version that includes it.
* A new FOCUS dataset published without preview status MUST have the reason recorded in the version changelog.
* A preview MUST apply only to an entire FOCUS dataset, including all of its columns.
* A preview MUST NOT include requirements or supporting entities outside that dataset unless the scope list in the preview's tracking issue names them.
* A preview MUST NOT be a FOCUS dataset that an earlier version published without preview status.
* A preview MUST have a tracking issue for its progress toward leaving preview status.
* A preview MUST include normative requirements written the same way as any other requirements (e.g., a `MUST` is not relaxed to `SHOULD` because the dataset is a preview).
* A preview MAY be omitted without affecting conformance to the FOCUS specification.
* A preview MAY change in the next version without a deprecation notice.
* The Specification MUST follow the normal change management process for all entities when not marked as preview.

**Proposed (FR #2782, question 13):**

* **Proposed:** A dataset enters preview through the same pull request gates as any other content in its release.
* **Why:** Section 5.3 of the [FOCUS Operating Procedures](https://github.com/FinOps-Open-Cost-and-Usage-Spec/foundation/blob/main/operating_procedures.md) has a preview follow the same lifecycle and IPR process as the release it ships in.
* **Open:** The latest point in a release cycle at which FOCUS Members can still designate a dataset a preview. For comparison, FOCUS Members chose a preview for SKU Price on October 22, 2026, during the 1.5 Final Consistency Review (October 8 to 29).

**TODO (FR #2782, question 8):** Decide whether and how a validator checks preview content on request while conformance checks leave it out. Follows FR #2811, which takes the conformance-exclusion part of this question.

A preview tracking issue MUST adhere to the following requirements:

* A preview tracking issue MUST list any questions to learn from generating or using the dataset, and who raised each one.
* A preview tracking issue MUST include the scope list, naming each requirement excluded from conformance, including any outside the dataset that exist only for the preview.
* A preview tracking issue MUST NOT name on the scope list a requirement outside the dataset unless that requirement exists only for the preview.
* A preview tracking issue MUST name in the scope list each supporting entity outside the dataset that the preview includes (e.g., an operating model condition).
* A preview tracking issue SHOULD list at least one early implementer, who is any person or organization, inside or outside the working group, that will generate or use the dataset to answer open questions.
* A preview tracking issue MUST state the date of the next status decision.
* A preview tracking issue MUST record that a request for comments went to existing data generators, and who responded.
* A preview tracking issue MUST name a single person who keeps it up to date.

**Proposed (FR #2782, question 4):**

* **Proposed:** The second and third requirements above. The scope list names each requirement outside the dataset that exists only for the preview, wherever it is defined, and names no other requirement outside the dataset. A requirement that applies to stable content stays evaluated for conformance.
* **Why:** The [SKU Price scope list](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2768) names two such requirements: the Data Model requirement, which is outside any dataset, and the Cost and Usage requirement that ChargeCategory match SkuPrice.ChargeCategory. The merged text said "in other datasets", which does not cover the Data Model requirement.
* **Open:** A requirement that combines stable checks with a check that exists only for the preview. In the specification, the Charge Category match is its own bullet, but the 1.5 requirements model groups every Charge Category bullet under one requirement, so excluding that grouped requirement would also stop stable checks.
* **Open:** How the requirements model and validators treat that dependency. Follows FR #2811.

**TODO (FR #2782, question 5):** Decide each of the following. Follows FR #2811.

* Where the specification states, as a normative requirement, that preview content is not evaluated for conformance.
* Which source fixes the scope list for each version: the tracking issue, the dataset's Preview note, or the requirements model.
* Whether naming a supporting entity on the scope list excludes that entity's own requirements from conformance (e.g., the two requirements in each of Includes Purchases and Includes Quantity Tier Pricing), or whether the scope list names those requirements too.

**Proposed (FR #2782, question 16):**

* **Proposed:** The last requirement above: each tracking issue names a single person who keeps it up to date.
* **Proposed:** Tracking issues follow the section layout of the [SKU Price tracking issue](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2768): a detailed description, the pull requests, the open questions, the scope list, and the definition of done. The definition of done carries the other tracking issue requirements above as checklist items (e.g., the early implementer, the date of the next status decision, and the request for comments).
* **Open:** Who sends the request for comments to data generators, when, and in what form.
* **Open:** How practitioners and data generators outside the working group commit to trying a preview.

### Marking a Preview

* Add a `> **Preview:**` note at the top of the dataset's page, its examples, and its supported features, summarizing the scope list and linking to the tracking issue.
* Add "(preview)" after the dataset's name in listings (e.g., the data model dataset table).
* Add a note to each section outside the dataset that has requirements on the scope list or defines a supporting entity on it (e.g., the Charge Category column in Cost and Usage), naming them and stating that, while the dataset is in preview, those requirements are excluded from conformance and those supporting entities may change without a deprecation notice.
* Record the preview and every later change to it in the version changelog, with migration notes.
* Add "(preview)" after the name of each preview dataset in the version's release notes, including a preview extended from an earlier version, and state there that only the datasets named as previews are previews.
* Set the status of each requirement on the scope list to Preview in the requirements model.
* Set each Version Introduced section in the dataset, including its columns, to `Preview: <version>` (e.g., `Preview: 1.5`).
* Set the Version Introduced section of each supporting entity on the scope list to `Preview: <version>`, unless the tracking issue explicitly notes an exception for that entity.

**TODO (FR #2782, question 10):** Decide each of the following. Follows FR #2811.

* How a delivered dataset's metadata marks preview content.
* How a data generator states that it provides a preview.
* How published schema files mark preview content.

**Proposed (FR #2782, question 11):**

* **Proposed:** Move the choice of what Version Introduced shows after promotion to FR #2816, which covers Version Introduced for all content.
* **Why:** Task Force discussion so far leaned toward the promotion version alone, so implementers can see which version promoted the dataset. Until FR #2816 decides, the Promote step below updates each Version Introduced section to `Preview: <version> · GA: <version>`.
* **Open here:** What the Version Introduced section shows on the supported features that depend on a preview while the dataset is a preview.

**Proposed (FR #2782, question 17):**

* **Proposed:** The release notes step above, which also covers a preview extended from an earlier version.
* **Proposed:** The website and announcements follow the same practice: they name each preview dataset as a preview wherever they list what a version includes, so readers do not take a whole release as a preview.
* **Open:** Confirm with whoever owns the release announcement and the website.

### Exiting Preview

At each later version, FOCUS Members choose one outcome and record it with its evidence in the tracking issue:

* **Promote:** Remove the preview designation once the open questions are addressed. The dataset's requirements become Active in the requirements model, and the "(preview)" label and Preview notes are removed. Each Version Introduced section is updated to include the general availability (GA) version (e.g., `Preview: 1.5 · GA: 1.6`).
* **Extend:** Keep the preview for one more version, with a plan for the next evidence.
* **Remove:** Remove the dataset without a deprecation notice or retention period. This is the default when there is no new evidence since the last decision.

**TODO (FR #2782, question 14):** Decide each of the following.

* What evidence is enough to promote a preview.
* What counts as no new evidence for the removal default, including for datasets that no data generator produces yet.

**Proposed (FR #2782, question 15):**

* **Proposed:** A preview stays for at least one published version, so the first status decision comes in the version after the one that introduced it.
* **Proposed:** Each decision follows that version's release gates.
* **Why:** The removal default above already limits how long a preview without new evidence can last. Because release cycles overlap, the time between a preview's publication and its first decision depends on which gate the decision is tied to.
* **Open:** Which release gate each decision is tied to.
* **Open:** Whether a preview that keeps producing new evidence also has a maximum number of versions.

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
   * Removing a column without introducing a replacement column
