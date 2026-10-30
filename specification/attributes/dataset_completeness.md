# Dataset Completeness

FinOps practitioners need data beyond what [FOCUS columns](#term) define to facilitate a variety of FinOps activities. When this data is only available in [native datasets](#term), practitioners cannot rely on [FOCUS datasets](#term) as a primary data source, making FOCUS an added overhead rather than a data generator-agnostic alternative that supports essential FinOps activities.

The [Dataset Completeness](#attr) attribute requires [*data generators*](#metadata.datagenerator) to include [custom columns](#term) in a [FOCUS dataset](#term) for all [native dataset](#term) columns except those explicitly listed as exclusions with justification in publicly-available documentation. This allows practitioners to adopt [FOCUS datasets](#term) without losing analytical capabilities.

## Requirements

Dataset conforming to [DatasetCompleteness](#attr) attribute MUST adhere to the following requirements:

* [FOCUS dataset](#term) MUST adhere to the following [custom column](#term) presence requirements:
  * [FOCUS dataset](#term) MUST include [custom columns](#term) (e.g., `x_ChargeSubType`) needed to support [invoice reconciliation](#term) when the [invoice issuer](#term) supports payable invoices, and when [FOCUS columns](#term) are not sufficient.
  * [FOCUS dataset](#term) MUST include [custom columns](#term) corresponding to [native dataset](#term) columns, except those explicitly listed as exclusions with justification in publicly-available documentation, provided those excluded columns are unrelated to [invoice reconciliation](#term).
  * [FOCUS dataset](#term) MUST have all included [custom columns](#term) documented in publicly-available documentation, including description, purpose, and relationship to [native dataset](#term) columns.
  * [FOCUS dataset](#term) SHOULD include [custom columns](#term) that enable correlation between [FOCUS dataset](#term) records and [native dataset](#term) records (e.g., native [charge](#term) identifiers), even when they meet the criteria for exclusion.
  * [FOCUS dataset](#term) SHOULD exclude [custom columns](#term) that duplicate information already captured in [FOCUS columns](#term), except during a transitional period as defined in publicly-available documentation, to enable migration without breaking changes.
* [FOCUS dataset](#term) MUST retain the fidelity of corresponding [native dataset](#term) values within [custom columns](#term) without lossy transformations (e.g., rounding or truncation).
* [FOCUS dataset](#term) MUST NOT alter the aggregated values of summable [metrics](#term) (e.g., costs and quantities) due to the inclusion of [custom columns](#term).
* [FOCUS dataset](#term) SHOULD sort all [FOCUS columns](#term) alphabetically first, then all [custom columns](#term) alphabetically second.

## Implementation Context

A service provider's native cost dataset includes a column `internal_project_id` used for organizational hierarchy attribution. Since no [FOCUS column](#term) captures this data, the corresponding [FOCUS dataset](#term) includes it as a [custom column](#term) (`x_InternalProjectId`), enabling practitioners to perform the same project-level cost allocation without falling back to the [native dataset](#term).

The native dataset also includes a native billing event reference (`billing_event_id`) that does not directly support analysis but allows practitioners to trace [FOCUS dataset](#term) records back to native records. The [FOCUS dataset](#term) includes this as `x_BillingEventId` to enable correlation between the two datasets.

Even when a single native record results in multiple FOCUS records (e.g., separating discounted and non-discounted portions of a charge in a [Cost and Usage](#ds) [dataset artifact](#term)), [custom columns](#term) like `x_InternalProjectId` and `x_BillingEventId` are preserved in all resulting records and cost metrics like `BilledCost` are split accurately, maintaining data integrity.

[Custom columns](#term) that duplicate newly introduced [FOCUS columns](#term) may be preserved during a documented transitional period to enable migration without breaking changes.

This attribute ensures [custom columns](#term) are fully represented in the [FOCUS dataset](#term) schema. Data generators may require FOCUS consumers to explicitly select these columns when generating a [dataset artifact](#term) (see [Dataset Configuration](#attr)).

## Attribute ID

DatasetCompleteness

## Attribute Name

Dataset Completeness

## Description

Defines requirements for a [FOCUS dataset](#term) to include [custom columns](#term) for [native dataset](#term) columns not represented in [FOCUS columns](#term).

## Version Introduced

1.4
