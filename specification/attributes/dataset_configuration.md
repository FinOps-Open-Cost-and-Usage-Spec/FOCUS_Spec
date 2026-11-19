# Dataset Configuration

Dataset Configuration allows FinOps practitioners to tailor the structure and content of a [*FOCUS dataset*](#glossary:FOCUS-dataset). Datasets provided by data generators are often massive, and their ingestion can lead to excessive storage costs and slow processing times. By removing large, static, or irrelevant columns and limiting rows to the period and changes needed, FinOps practitioners can optimize the dataset for better performance and lower storage costs.

Common scenarios where dataset configuration is valuable include:

* **Managing Scale**: Trim large exports to reduce time and cost of data preparation
* **Reducing Noise**: Tailor datasets for specific workflows (e.g., cost allocation, commitment analysis)
* **Lowering Barriers**: Strip away technical complexity for spreadsheet users
* **Limiting Rows**: Request or export only the period and changed rows needed, in request-based (pull) or scheduled (push) delivery
* **Enabling Comparison**: Remove custom (`x_`) columns for standardized cross-provider reporting

## Configuration Options

A *FOCUS dataset* is configured through the following options. Each option applies to every delivery mechanism: request-based (pull) delivery, where each request carries the options, and scheduled (push) delivery such as exports, where the options are set once.

| Option | Description | Default |
| --- | --- | --- |
| Columns | Columns to include. | Default column set, when offered |
| Start | Beginning (inclusive) of the period to deliver. Applies to the period column the dataset declares. Also the changed-since point in time: rows last updated on or after Start are changes. | Start of the current [*billing period*](#glossary:billing-period) |
| End | End (exclusive) of the period to deliver. Applies to the same period column as Start. | Time of the request |
| IncludeAllRows | Whether to include rows that were active at Start but did not change during the period. Set to false to receive only changed rows. | true |

IncludeAllRows defaults to true so practitioners receive every row they may need and opt out of unchanged rows to reduce data size.

Defaults differ by delivery:

* Pull: IncludeAllRows is true, because a request has no knowledge of earlier deliveries.
* First push delivery: IncludeAllRows is true.
* Later push deliveries: IncludeAllRows is false and Start is the capture time of the previous delivery.

## Requirements

Dataset conforming to DatasetConfiguration attribute MUST adhere to the following requirements:

* *FOCUS dataset* MUST be configurable to include only a user-defined selection of columns.
* *FOCUS dataset* MUST adhere to all column-level specifications defined in the FOCUS schema, regardless of the user's chosen configuration (e.g., column selection).
* *FOCUS dataset* SHOULD be configurable with Start and End options when the dataset declares a period column.
* *FOCUS dataset* MUST adhere to the following requirements when Start or End is configured:
  * *FOCUS dataset* MUST include a separate row for every change with a period column value on or after Start and before End.
  * *FOCUS dataset* MUST NOT include rows with a period column value before Start or on or after End, except as required by IncludeAllRows.
  * *FOCUS dataset* Start MUST be the capture time of the previous delivery for each scheduled delivery after the first, when Start is not configured.
* *FOCUS dataset* SHOULD be configurable with an IncludeAllRows option when the dataset declares a period column.
* *FOCUS dataset* MUST adhere to the following requirements when IncludeAllRows is configured or defaulted:
  * *FOCUS dataset* MUST include rows active at Start that did not change during the period when IncludeAllRows is true.
  * *FOCUS dataset* MUST NOT include rows active at Start that did not change during the period when IncludeAllRows is false.
  * *FOCUS dataset* IncludeAllRows MUST be true when not configured, except for scheduled deliveries after the first.
  * *FOCUS dataset* MUST be delivered with IncludeAllRows set to true when a previously delivered row's identifying values change.
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
