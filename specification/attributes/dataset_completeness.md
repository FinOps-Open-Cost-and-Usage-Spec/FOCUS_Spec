# Dataset Completeness

FinOps practitioners need [*FOCUS datasets*](#glossary:FOCUS-dataset) to include the same information available in [*native datasets*](#glossary:native-dataset). When *FOCUS datasets* lack columns needed for critical scenarios, like organizational hierarchy attribution, commitment discount tracking, or provider-specific optimizations, practitioners cannot adopt FOCUS. Missing columns force practitioners to use proprietary *native datasets*, making FOCUS an added overhead rather than an open, provider-agnostic alternative.

This attribute ensures [*data generators*](#glossary:data-generator) provide complete coverage by including custom columns (prefixed with `x_`) for *native dataset* columns not represented in FOCUS columns. Custom columns bridge the gap between FOCUS standardization and provider-specific capabilities, allowing practitioners to adopt *FOCUS datasets* without losing analytical capabilities.

## Attribute ID

DatasetCompleteness

## Attribute Name

Dataset Completeness

## Description

Defines requirements for a *FOCUS dataset* to include custom columns for *native dataset* columns not represented in FOCUS columns.

## Requirements

* A *FOCUS dataset* MUST include custom columns for *native dataset* columns not represented in FOCUS columns.
  * A *FOCUS dataset* MAY exclude *native dataset* columns that do not support any analysis or reporting scenarios.
  * A *FOCUS dataset* SHOULD NOT include custom columns that duplicate information already captured in FOCUS columns.
  * A *FOCUS dataset* SHOULD maintain the same data fidelity for custom columns as their *native dataset* equivalents.
  * A *FOCUS dataset* MAY preserve non-FOCUS versions of custom columns even after FOCUS equivalents are introduced to enable migration without breaking changes.
* A *FOCUS dataset* SHOULD include custom columns that enable correlation between *FOCUS datasets* and *native datasets* (e.g., native [*charge*](#glossary:charge) identifiers).
* A *FOCUS dataset* SHOULD provide documentation describing custom columns, their purpose, and relationship to native columns.
* A *FOCUS dataset* MUST handle custom column values consistently to preserve data integrity when rows are split or aggregated to conform to other FOCUS requirements.
  * Custom columns MUST NOT introduce values that would violate the integrity of FOCUS-defined [*dimensions*](#glossary:dimension) and [*metrics*](#glossary:metric), particularly summable values such as costs and quantities.

## Exceptions

None

## Introduced (version)

1.4
