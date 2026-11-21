# Dataset Configuration

Dataset Configuration allows FinOps practitioners to tailor the structure and content of a [*FOCUS dataset*](#glossary:FOCUS-dataset). Datasets provided by data generators are often massive, and their ingestion can lead to excessive storage costs and slow processing times. By removing large, static, or irrelevant columns and limiting rows to the period and changes needed, FinOps practitioners can optimize the dataset for better performance and lower storage costs.

Common scenarios where dataset configuration is valuable include:

* **Managing Scale**: Trim large exports to reduce time and cost of data preparation
* **Reducing Noise**: Tailor datasets for specific workflows (e.g., cost allocation, commitment analysis)
* **Lowering Barriers**: Strip away technical complexity for spreadsheet users
* **Limiting Rows**: Request or export only the period and changed rows needed, in [*request-based delivery*](#glossary:request-based-delivery) or [*scheduled delivery*](#glossary:scheduled-delivery)
* **Enabling Comparison**: Remove custom (`x_`) columns for standardized cross-provider reporting

## Configuration Options

A *FOCUS dataset* is configured through the following options. Each applies to *request-based delivery*, where each request carries the options, and to *scheduled delivery* such as exports, where the options are set once.

| Option | Description | Default |
| --- | --- | --- |
| Columns | Columns to include. | Default column set, when offered |
| PeriodStart | Beginning (inclusive) of the period to deliver. Rows whose period ends on or before PeriodStart are excluded. | Start of the current [*billing period*](#glossary:billing-period) |
| PeriodEnd | End (exclusive) of the period to deliver. Rows whose period starts on or after PeriodEnd are excluded. | None |
| UpdatedSince | Only rows last updated after this time are delivered. Use to receive only changes since an earlier delivery. | None (all rows in the period) |

Not setting UpdatedSince delivers every row in the period, so practitioners receive every row they may need. Setting it reduces data size. Defaults differ by delivery:

* *Request-based delivery*: UpdatedSince is not set.
* First *scheduled delivery*: UpdatedSince is not set.
* Later *scheduled deliveries*: UpdatedSince is the latest last-updated value in the previous delivery.

## Requirements

Dataset conforming to DatasetConfiguration attribute MUST adhere to the following requirements:

* *FOCUS dataset* MUST be configurable to include only a user-defined selection of columns.
* *FOCUS dataset* MAY offer a default column set.
* *FOCUS dataset* default column set MUST include all applicable [*FOCUS columns*](#glossary:FOCUS-column) when a default column set is offered.
* *FOCUS dataset* MUST adhere to all column-level specifications defined in the FOCUS schema, regardless of the user's chosen configuration (e.g., column selection).
* *FOCUS dataset* MUST adhere to the following requirements when the dataset declares period columns:
  * *FOCUS dataset* MUST be configurable with a PeriodStart option.
  * *FOCUS dataset* MUST be configurable with a PeriodEnd option.
  * *FOCUS dataset* MUST use the start of the current *billing period* as PeriodStart when PeriodStart is not configured.
  * *FOCUS dataset* MUST NOT include rows with a period that ends on or before PeriodStart.
  * *FOCUS dataset* MUST NOT include rows with a period that starts on or after PeriodEnd.
  * *FOCUS dataset* MUST include rows with a period that has no start and ends after PeriodStart.
* *FOCUS dataset* MUST adhere to the following requirements when the dataset declares a [*row key*](#glossary:row-key):
  * *FOCUS dataset* MUST NOT have rows that represent different entities with the same *row key* values.
  * *FOCUS dataset* MUST have a unique *row key* value for each row when the dataset does not declare a last-updated column.
  * *FOCUS dataset* MUST have the same *row key* values across rows that represent versions of the same entity when the dataset declares a last-updated column.
  * *FOCUS dataset* MUST NOT have multiple rows with the same *row key* and last-updated column values within a single dataset artifact when the dataset declares a last-updated column.
* *FOCUS dataset* MUST adhere to the following requirements when the dataset declares a last-updated column and a *row key*:
  * *FOCUS dataset* MUST be configurable with an UpdatedSince option.
  * *FOCUS dataset* MUST use the latest last-updated column value of the previous delivery as UpdatedSince for each scheduled delivery after the first.
* *FOCUS dataset* MUST adhere to the following requirements when UpdatedSince is not set:
  * *FOCUS dataset* MUST include all rows not excluded by PeriodStart or PeriodEnd.
  * *FOCUS dataset* MUST include only the row with the latest last-updated column value for each *row key* when the dataset declares a last-updated column and a *row key*.
  * *FOCUS dataset* MUST include rows with a period that starts before PeriodStart and has no end or ends after PeriodStart.
* *FOCUS dataset* MUST adhere to the following requirements when UpdatedSince is set:
  * *FOCUS dataset* MUST include every row last updated after UpdatedSince.
  * *FOCUS dataset* MUST NOT include rows last updated on or before UpdatedSince.
  * *FOCUS dataset* MUST NOT include rows included in the previous delivery.

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
