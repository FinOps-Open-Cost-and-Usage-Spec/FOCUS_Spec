# Dataset Configuration

Dataset Configuration allows FinOps practitioners to tailor the structure and content of a [*FOCUS dataset*](#glossary:FOCUS-dataset). Datasets provided by data generators are often massive, and their ingestion can lead to excessive storage costs and slow processing times. By removing large, static, or irrelevant columns, FinOps practitioners can optimize the dataset for better performance and lower storage costs.

Common scenarios where dataset configuration is valuable include:

* **Managing Scale**: Trim large exports to reduce time and cost of data preparation
* **Reducing Noise**: Tailor datasets for specific workflows (e.g., cost allocation, commitment analysis)
* **Lowering Barriers**: Strip away technical complexity for spreadsheet users
* **Limiting Deliveries**: Request or export only records that changed since a point in time, in request-based (pull) or scheduled (push) delivery
* **Enabling Comparison**: Remove custom (`x_`) columns for standardized cross-provider reporting

## Changed-Since Configuration

A changed-since point in time limits a delivery to records created or modified since that point, as indicated by the dataset's last-updated column. It applies to request-based (pull) delivery, where each request carries the point in time, and to scheduled (push) delivery such as exports, where the point in time is set once for the first delivery and then advances to the capture time of the previous delivery.

## Requirements

Dataset conforming to DatasetConfiguration attribute MUST adhere to the following requirements:

* *FOCUS dataset* MUST be configurable to include only a user-defined selection of columns.
* *FOCUS dataset* MUST adhere to all column-level specifications defined in the FOCUS schema, regardless of the user's chosen configuration (e.g., column selection).
* *FOCUS dataset* SHOULD be configurable to include only records created or modified since a user-defined point in time (e.g., the time of the previous delivery) when the dataset defines a last-updated column.
* *FOCUS dataset* MUST adhere to the following requirements when a changed-since point in time is configured:
  * *FOCUS dataset* MUST include every record last updated on or after the changed-since point in time.
  * *FOCUS dataset* MUST NOT include records last updated before the changed-since point in time.
  * *FOCUS dataset* changed-since point in time MUST be the capture time of the previous delivery for each scheduled delivery after the first.
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
