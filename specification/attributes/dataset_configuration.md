# Dataset Configuration

Dataset Configuration allows FinOps practitioners to tailor the structure and content of a [*FOCUS dataset*](#glossary:FOCUS-dataset). Datasets provided by data generators are often massive, and their ingestion can lead to excessive storage costs and slow processing times. By removing large, static, or irrelevant columns, FinOps practitioners can optimize the dataset for better performance and lower storage costs.

Common scenarios where dataset configuration is valuable include:

* **Managing Scale**: Trim large exports to reduce time and cost of data preparation
* **Reducing Noise**: Tailor datasets for specific workflows (e.g., cost allocation, commitment analysis)
* **Lowering Barriers**: Strip away technical complexity for spreadsheet users
* **Limiting Deliveries**: Request or export only the period and records needed, in request-based (pull) or scheduled (push) delivery
* **Enabling Comparison**: Remove custom (`x_`) columns for standardized cross-provider reporting

## Period Configuration

Period configuration limits a delivery to a period of time and, optionally, to the records that changed during it. It applies to datasets that define a last-updated column. It uses three options:

* Start: Beginning of the period (inclusive). Defaults to the start of the current [*billing period*](#glossary:billing-period). Also serves as the changed-since point in time.
* End: End of the period (exclusive). Defaults to the time of the request.
* IncludeAllRows: Whether to include records that were active at Start but did not change during the period. Defaults to true, so practitioners receive every row they may need and opt out of unchanged rows to reduce data size.

Period configuration applies to request-based (pull) delivery, where each request carries the options, and to scheduled (push) delivery such as exports, where the options are set once. A pull has no knowledge of earlier deliveries, so IncludeAllRows defaults to true. The first push delivery includes all rows. Each later push delivery defaults to IncludeAllRows set to false and a Start equal to the capture time of the previous delivery.

## Requirements

Dataset conforming to DatasetConfiguration attribute MUST adhere to the following requirements:

* *FOCUS dataset* MUST be configurable to include only a user-defined selection of columns.
* *FOCUS dataset* MUST adhere to all column-level specifications defined in the FOCUS schema, regardless of the user's chosen configuration (e.g., column selection).
* *FOCUS dataset* SHOULD be configurable with Start, End, and IncludeAllRows options when the dataset defines a last-updated column.
* *FOCUS dataset* MUST adhere to the following requirements when Start, End, or IncludeAllRows is configured:
  * *FOCUS dataset* MUST include a separate record for every change last updated on or after Start and before End.
  * *FOCUS dataset* MUST NOT include records last updated before Start or on or after End, except as required by IncludeAllRows.
  * *FOCUS dataset* MUST include records active at Start that did not change during the period when IncludeAllRows is true.
  * *FOCUS dataset* MUST NOT include records active at Start that did not change during the period when IncludeAllRows is false.
  * *FOCUS dataset* MUST treat IncludeAllRows as true when it is not configured, except for scheduled deliveries after the first.
* *FOCUS dataset* MAY offer a default column set.
* *FOCUS dataset* default column set MUST include all applicable [*FOCUS columns*](#glossary:FOCUS-column) when a default column set is offered.

## Example

A practitioner configures their FOCUS [Cost and Usage](#datamodel.costandusage) dataset to include only these columns:

* BillingAccountId
* ServiceName
* BilledCost
* EffectiveCost
* Tags

Even though columns like `CommitmentDiscountId` and `ResourceId` are excluded, the included cost columns (`BilledCost`, `EffectiveCost`) still reflect commitment discounts correctly. The dataset remains conformant to the FOCUS specification because each included column follows all requirements for that column, including requirements that reference columns not in the dataset.

## Attribute ID

DatasetConfiguration

## Attribute Name

Dataset Configuration

## Description

Defines configuration options for controlling the structure and content of a FOCUS dataset.

## Version Introduced

1.4
