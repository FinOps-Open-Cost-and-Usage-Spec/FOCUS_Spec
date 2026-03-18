# Dataset Completeness

FinOps practitioners need data beyond what [*FOCUS columns*](#glossary:FOCUS-column) define to facilitate a variety of FinOps activities. When this data is only available in [*native datasets*](#glossary:native-dataset), practitioners cannot rely on [*FOCUS datasets*](#glossary:FOCUS-dataset) as a primary data source, making FOCUS an added overhead rather than a data generator-agnostic alternative that supports essential FinOps activities.

The Dataset Completeness attribute requires [*data generators*](#glossary:data-generator) to include [*custom columns*](#glossary:custom-column) in a *FOCUS dataset* for all *native dataset* columns except those explicitly documented as exclusions with justification. This allows practitioners to adopt *FOCUS datasets* without losing analytical capabilities.

## Attribute ID

DatasetCompleteness

## Attribute Name

Dataset Completeness

## Description

Defines requirements for a *FOCUS dataset* to include custom columns for *native dataset* columns not represented in FOCUS columns.

## Implementation Context

A service provider's native cost dataset includes a column `internal_project_id` used for organizational hierarchy attribution. Since no *FOCUS column* captures this data, the corresponding *FOCUS dataset* includes it as a *custom column* (`x_InternalProjectId`), enabling practitioners to perform the same project-level cost allocation without falling back to the *native dataset*.

The native dataset also includes a native billing event reference (`billing_event_id`) that does not directly support analysis but allows practitioners to trace *FOCUS dataset* records back to native records. The *FOCUS dataset* includes this as `x_BillingEventId` to enable correlation between the two datasets.

Even when Discount Handling splits a single native charge into two FOCUS rows (e.g., separating a commitment discount), *custom columns* like `x_InternalProjectId` and `x_BillingEventId` are preserved on both rows and cost metrics like `BilledCost` are split accurately, maintaining data integrity.

Custom columns that duplicate newly introduced FOCUS columns may be temporarily preserved to enable migration without breaking changes.

## Requirements

*FOCUS dataset* MUST adhere to the following requirements:

* *FOCUS dataset* MUST include [*custom columns*](#glossary:custom-column) for all *native dataset* columns except those explicitly documented as exclusions with justification (e.g., deprecated fields).
  * *FOCUS dataset* SHOULD NOT exclude custom columns that enable correlation between *FOCUS dataset* records and *native dataset* records (e.g., native [*charge*](#glossary:charge) identifiers), even when documented as an exclusion.
  * *FOCUS dataset* SHOULD exclude custom columns that duplicate information already captured in FOCUS columns, except for a limited time when equivalent FOCUS columns are newly introduced, to enable migration without breaking changes.
* *FOCUS dataset* MUST NOT alter the aggregated values of summable [*metrics*](#glossary:metric) (e.g., costs and quantities) when custom columns are introduced.
* *FOCUS dataset* MUST ensure custom columns accurately represent the corresponding values from the *native dataset*.
* *FOCUS dataset* SHOULD sort all *FOCUS columns* alphabetically first, then all *custom columns* alphabetically second.

## Exceptions

None

## Introduced (version)

1.4
