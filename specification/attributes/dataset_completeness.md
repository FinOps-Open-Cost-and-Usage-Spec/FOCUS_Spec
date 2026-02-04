# Dataset Completeness

FinOps practitioners need [*FOCUS datasets*](#glossary:FOCUS-dataset) to include the same information available in [*native datasets*](#glossary:native-dataset). When *FOCUS datasets* lack columns needed for critical scenarios, like organizational hierarchy attribution, commitment discount tracking, invoice reconciliation, or provider-specific optimizations, practitioners cannot rely on *FOCUS datasets* as a primary data source. Missing columns force practitioners to use proprietary *native datasets*, making FOCUS an added overhead rather than a provider-agnostic alternative that supports essential FinOps activities.

This attribute ensures [*data generators*](#glossary:data-generator) provide complete coverage by including custom columns (prefixed with `x_`) for *native dataset* columns not represented in FOCUS columns. Custom columns bridge the gap between FOCUS standardization and provider-specific capabilities, allowing practitioners to adopt *FOCUS datasets* without losing analytical capabilities.

## Attribute ID

DatasetCompleteness

## Attribute Name

Dataset Completeness

## Description

Defines requirements for a *FOCUS dataset* to include custom columns for *native dataset* columns not represented in FOCUS columns.

## Requirements

* *FOCUS dataset* MUST include custom column corresponding to *native dataset* that supports analysis or reporting scenarios and does not duplicate information already captured in FOCUS columns.
* *FOCUS dataset* SHOULD include custom columns that enable correlation between *FOCUS dataset* records and *native dataset* records (e.g., native [*charge*](#glossary:charge) identifiers).
* *FOCUS dataset* SHOULD NOT include custom column that duplicates information already captured in FOCUS columns.
* *FOCUS dataset* MAY omit column that does not support any analysis or reporting scenarios.
* *FOCUS dataset* MAY preserve custom column even after one or more equivalent FOCUS columns are introduced, to enable migration without breaking changes.
* Custom column MUST be handled consistently to preserve data integrity when rows are split or aggregated to conform to other FOCUS requirements.
* Custom column MUST be documented, including its description, purpose, and relationship to native column(s).
* Custom column MUST NOT introduce values that would violate the integrity of FOCUS [*dimensions*](#glossary:dimension) and [*metrics*](#glossary:metric), particularly summable values such as costs and quantities.
* Custom column SHOULD preserve the same fidelity as their equivalent(s) in the native dataset.

## Exceptions

None

## Introduced (version)

1.4
