# Dataset Completeness

FinOps practitioners need data beyond what [*FOCUS columns*](#glossary:FOCUS-column) define to facilitate a variety of FinOps activities, like organizational hierarchy attribution, commitment discount tracking, invoice reconciliation, or optimizations. When this data is only available in [*native datasets*](#glossary:native-dataset), practitioners cannot rely on [*FOCUS datasets*](#glossary:FOCUS-dataset) as a primary data source, making FOCUS an added overhead rather than a data generator-agnostic alternative that supports essential FinOps activities.

The Dataset Completeness attribute ensures data generators include [*custom columns*](#glossary:custom-column) in a *FOCUS dataset* to cover *native dataset* columns that materially support analysis or reporting and are not already captured by [*FOCUS columns*](#glossary:FOCUS-column). This bridges the gap between FOCUS standardization and data generator capabilities, allowing practitioners to adopt *FOCUS datasets* without losing analytical capabilities.

## Attribute ID

DatasetCompleteness

## Attribute Name

Dataset Completeness

## Description

Defines requirements for a *FOCUS dataset* to include custom columns for *native dataset* columns not represented in FOCUS columns.

## Requirements

* *FOCUS dataset* MUST include [*custom columns*](#glossary:custom-column) corresponding to *native dataset* columns that materially support analysis or reporting scenarios and do not duplicate information already captured in FOCUS columns.
* *FOCUS dataset* MUST NOT alter the aggregated values of summable [*metrics*](#glossary:metric) (e.g., costs and quantities) when records are split or aggregated or when custom columns are added.
* *FOCUS dataset* SHOULD include custom columns that enable correlation between *FOCUS dataset* records and *native dataset* records (e.g., native [*charge*](#glossary:charge) identifiers).
* *FOCUS dataset* SHOULD NOT include custom columns that duplicate information already captured in FOCUS columns.
* *FOCUS dataset* MAY omit *native dataset* columns that do not support any analysis or reporting scenarios.
* *FOCUS dataset* MAY preserve custom columns even after one or more equivalent FOCUS columns are introduced, to enable migration without breaking changes.
* Custom columns SHOULD accurately represent the corresponding values from the *native dataset*.

## Example

A service provider's native cost dataset includes a column `internal_project_id` used for organizational hierarchy attribution. Since no *FOCUS column* captures this data, the corresponding *FOCUS dataset* includes it as a *custom column* (`x_InternalProjectId`), enabling practitioners to perform the same project-level cost allocation without falling back to the *native dataset*.

The native dataset also includes a native billing event reference (`billing_event_id`) that does not directly support analysis but allows practitioners to trace *FOCUS dataset* records back to native records. The *FOCUS dataset* includes this as `x_BillingEventId` to enable correlation between the two datasets.

Even when Discount Handling splits a single native charge into two FOCUS rows (e.g., separating a commitment discount), *custom columns* like `x_InternalProjectId` and `x_BillingEventId` are preserved on both rows and cost metrics like `BilledCost` are split accurately, maintaining data integrity.

## Exceptions

None

## Introduced (version)

1.4
