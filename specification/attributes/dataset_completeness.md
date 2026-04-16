# Dataset Completeness

FinOps practitioners need data beyond what [*FOCUS columns*](#glossary:FOCUS-column) define to facilitate a variety of FinOps activities. When this data is only available in [*native datasets*](#glossary:native-dataset), practitioners cannot rely on [*FOCUS datasets*](#glossary:FOCUS-dataset) as a primary data source, making FOCUS an added overhead rather than a data generator-agnostic alternative that supports essential FinOps activities.

The Dataset Completeness attribute requires [*data generators*](#metadata.datagenerator) to include [*custom columns*](#glossary:custom-column) in a *FOCUS dataset* for all *native dataset* columns except those explicitly listed as exclusions with justification in publicly-available documentation. This allows practitioners to adopt *FOCUS datasets* without losing analytical capabilities.

## Requirements

Dataset conforming to DatasetCompleteness attribute MUST adhere to the following requirements:

* *FOCUS dataset* MUST adhere to the following *custom column* presence requirements:
  * *FOCUS dataset* MUST include *custom columns* (e.g., `x_ChargeSubType`) needed to support [*invoice reconciliation*](#glossary:invoice-reconciliation) when the [*invoice issuer*](#glossary:invoice issuer) supports payable invoices, and when *FOCUS columns* are not sufficient.
  * *FOCUS dataset* MUST include *custom columns* corresponding to [*native dataset*](#glossary:native-dataset) columns, except those explicitly listed as exclusions with justification in publicly-available documentation, provided those excluded columns are unrelated to *invoice reconciliation*.
  * *FOCUS dataset* MUST have all included *custom columns* documented in publicly-available documentation, including description, purpose, and relationship to *native dataset* columns.
  * *FOCUS dataset* SHOULD include *custom columns* that enable correlation between *FOCUS dataset* records and *native dataset* records (e.g., native [*charge*](#glossary:charge) identifiers), even if they meet the criteria for exclusion.
  * *FOCUS dataset* SHOULD exclude *custom columns* that duplicate information already captured in *FOCUS columns*, except during a transitional period as defined in publicly-available documentation, to enable migration without breaking changes.
* *FOCUS dataset* MUST retain the fidelity of corresponding *native dataset* values within *custom columns* without lossy transformations (e.g., rounding or truncation).
* *FOCUS dataset* MUST NOT alter the aggregated values of summable [*metrics*](#glossary:metric) (e.g., costs and quantities) due to the inclusion of *custom columns*.
* *FOCUS dataset* SHOULD sort all *FOCUS columns* alphabetically first, then all *custom columns* alphabetically second.

## Implementation Context

A service provider's native cost dataset includes a column `internal_project_id` used for organizational hierarchy attribution. Since no *FOCUS column* captures this data, the corresponding *FOCUS dataset* includes it as a *custom column* (`x_InternalProjectId`), enabling practitioners to perform the same project-level cost allocation without falling back to the *native dataset*.

The native dataset also includes a native billing event reference (`billing_event_id`) that does not directly support analysis but allows practitioners to trace *FOCUS dataset* records back to native records. The *FOCUS dataset* includes this as `x_BillingEventId` to enable correlation between the two datasets.

Even when [Discount Handling](#attributes.discounthandling) splits a single native charge into two FOCUS rows (e.g., separating a commitment discount), *custom columns* like `x_InternalProjectId` and `x_BillingEventId` are preserved on both rows and cost metrics like `BilledCost` are split accurately, maintaining data integrity.

*Custom columns* that duplicate newly introduced *FOCUS columns* may be preserved during a documented transitional period to enable migration without breaking changes.

This attribute ensures *custom columns* are fully represented in the *FOCUS dataset* schema. Data generators may require FOCUS consumers to explicitly select these columns when generating a [*dataset artifact*](#glossary:dataset-artifact) (see [Dataset Configuration](#attributes.datasetconfiguration)).

## Attribute ID

DatasetCompleteness

## Attribute Name

Dataset Completeness

## Description

Defines requirements for a *FOCUS dataset* to include *custom columns* for *native dataset* columns not represented in *FOCUS columns*.

## Introduced (version)

1.4
