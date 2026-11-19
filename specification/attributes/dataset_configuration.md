# Dataset Configuration

Dataset Configuration allows FinOps practitioners to tailor the structure and content of a [*FOCUS dataset*](#glossary:FOCUS-dataset). Datasets provided by data generators are often massive, and their ingestion can lead to excessive storage costs and slow processing times. By removing large, static, or irrelevant columns and limiting rows to the period and changes needed, FinOps practitioners can optimize the dataset for better performance and lower storage costs.

Common scenarios where dataset configuration is valuable include:

* **Managing Scale**: Trim large exports to reduce time and cost of data preparation
* **Reducing Noise**: Tailor datasets for specific workflows (e.g., cost allocation, commitment analysis)
* **Lowering Barriers**: Strip away technical complexity for spreadsheet users
* **Limiting Rows**: Request or export only the period and changed rows needed, in request-based (pull) or scheduled (push) delivery
* **Enabling Comparison**: Remove custom (`x_`) columns for standardized cross-provider reporting

## Configuration Options

A *FOCUS dataset* is configured through the following options. Each applies to request-based (pull) delivery, where each request carries the options, and to scheduled (push) delivery such as exports, where the options are set once.

| Option | Description | Default |
| --- | --- | --- |
| Columns | Columns to include. | Default column set, when offered |
| Start | Beginning (inclusive) of the period to deliver. Rows are included when their period, as declared by the dataset, overlaps the period from Start to End. | Start of the current [*billing period*](#glossary:billing-period) |
| End | End (exclusive) of the period to deliver. | Time of the request |
| UpdatedSince | Only rows last updated on or after this time. Use it to receive only changes since an earlier delivery. | None (all rows in the period) |

Not setting UpdatedSince delivers every row in the period, so practitioners receive every row they may need. Setting it reduces data size. Defaults differ by delivery:

* Pull: UpdatedSince is not set, because a request has no knowledge of earlier deliveries.
* First push delivery: UpdatedSince is not set.
* Later push deliveries: UpdatedSince is the capture time of the previous delivery.

When UpdatedSince is set and Start or End is not, the period is unbounded on that side, so changes are not missed (e.g., a price announced now for a future date).

## Requirements

Dataset conforming to DatasetConfiguration attribute MUST adhere to the following requirements:

* *FOCUS dataset* MUST be configurable to include only a user-defined selection of columns.
* *FOCUS dataset* MUST adhere to all column-level specifications defined in the FOCUS schema, regardless of the user's chosen configuration (e.g., column selection).
* *FOCUS dataset* MUST adhere to the following requirements when the dataset declares a period:
  * *FOCUS dataset* MUST be configurable with a Start option.
  * *FOCUS dataset* MUST be configurable with an End option.
  * *FOCUS dataset* MUST include only rows with a period that overlaps the period from Start to End.
  * *FOCUS dataset* MUST use the start of the current *billing period* as Start when neither Start nor UpdatedSince is configured.
  * *FOCUS dataset* MUST use the time of the request as End when neither End nor UpdatedSince is configured.
* *FOCUS dataset* MUST adhere to the following requirements when the dataset declares a last-updated column and a row key:
  * *FOCUS dataset* SHOULD be configurable with an UpdatedSince option.
  * *FOCUS dataset* MUST include every row last updated on or after UpdatedSince when UpdatedSince is configured.
  * *FOCUS dataset* MUST NOT include rows last updated before UpdatedSince when UpdatedSince is configured.
  * *FOCUS dataset* MUST include a separate row for every change when UpdatedSince is configured.
  * *FOCUS dataset* MUST use the capture time of the previous delivery as UpdatedSince for each scheduled delivery after the first, when UpdatedSince is not configured.
  * *FOCUS dataset* MUST be delivered without UpdatedSince when a previously delivered row's key values change.
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
