# Dataset Configuration

Dataset Configuration allows FinOps practitioners to tailor the structure, content, and granularity of a [*FOCUS dataset*](#glossary:FOCUS-dataset). Datasets provided by data generators are often massive, and their ingestion can lead to excessive storage costs and slow processing times. By removing large, static, or irrelevant columns and selecting [*dataset instances*](#glossary:dataset-instance) with the level of detail needed for a given workflow, FinOps practitioners can optimize the dataset for better performance and lower storage costs.

Common scenarios where dataset configuration is valuable include:

* **Managing Scale**: Trim large exports to reduce time and cost of data preparation
* **Reducing Noise**: Tailor datasets for specific workflows (e.g., cost allocation, commitment analysis)
* **Managing Granularity**: Select dataset instances that expose the level of detail needed for a workflow (e.g., service-level, resource-level, actor-level)
* **Lowering Barriers**: Strip away technical complexity for spreadsheet users
* **Enabling Comparison**: Remove custom (`x_`) columns for standardized cross-provider reporting

Dataset instance granularities identify the levels of detail represented by records in a [*dataset instance*](#glossary:dataset-instance). Each granularity configuration defines one level of detail for records that match a documented applicability filter (e.g., ServiceName).

## Requirements

Dataset conforming to DatasetConfiguration attribute MUST adhere to the following requirements:

* *FOCUS dataset* MUST be configurable to include only a user-defined selection of columns.
* *FOCUS dataset* MUST be configurable to select a granularity configuration for each applicability filter when more than one granularity configuration is offered for that applicability filter.
* *FOCUS dataset* MUST adhere to all column-level specifications defined in the FOCUS schema, regardless of the selected or default configuration (e.g., column selection, granularity configuration).
* *FOCUS dataset* MUST have mutually exclusive applicability filters for granularity configurations within a delivered dataset instance.
* *FOCUS dataset* granularity configuration documentation MUST adhere to the following requirements when a delivered dataset instance uses one or more granularity configurations:
  * *FOCUS dataset* granularity configuration documentation MUST identify the columns that define the granularity configuration.
  * *FOCUS dataset* granularity configuration documentation MUST identify the applicability filter for the granularity configuration (e.g., ServiceName).
  * *FOCUS dataset* granularity configuration documentation SHOULD identify the representation of more granular detail for the granularity configuration (e.g., expanded records, embedded JSON objects, referenced detail datasets).
  * *FOCUS dataset* granularity configuration documentation MUST describe whether a delivered dataset instance replaces or supplements other delivered dataset instances that represent the same underlying usage or charges.
  * *FOCUS dataset* granularity configuration documentation MUST describe how summable metrics are represented across delivered dataset instances when one delivered dataset instance supplements another delivered dataset instance that represents the same underlying usage or charges.
  * *FOCUS dataset* granularity configuration documentation SHOULD describe how non-summable metrics (e.g., ListUnitPrice, ContractedUnitPrice) are represented across delivered dataset instances that represent the same underlying usage or charges.
  * *FOCUS dataset* granularity configuration documentation SHOULD identify granularity configurations that include privacy-sensitive identifiers (e.g., actor-level identifiers).
* *FOCUS dataset* MAY offer a default granularity configuration for an applicability filter.
* *FOCUS dataset* granularity configuration MUST be the least granular granularity configuration offered for the same applicability filter (e.g., the granularity configuration with the fewest granularity-defining columns) when the granularity configuration is offered as a default.
* *FOCUS dataset* MAY offer a default column set.
* *FOCUS dataset* default column set MUST include all applicable [*FOCUS columns*](#glossary:FOCUS-column) when a default column set is offered.

## Example

A practitioner configures their FOCUS Cost and Usage dataset to include only these columns:

* BillingAccountId
* ServiceName
* BilledCost
* EffectiveCost
* Tags

Even though columns like `CommitmentDiscountId` and `ResourceId` are excluded, the included cost columns (`BilledCost`, `EffectiveCost`) still reflect commitment discounts correctly. The dataset remains conformant to the FOCUS specification because each included column follows all requirements for that column, including requirements that reference columns not in the dataset.

Another practitioner configures their FOCUS Cost and Usage dataset to receive a dataset instance with different granularity configurations for different sets of records. The dataset instance includes records for AI services configured with `PrincipalId` and `ConsumerId`, records for another service configured with `PrincipalId`, and records for other services configured without actor-level columns. The data generator documents the applicability filter for each granularity configuration and describes how cost metrics are represented when a separate delivered dataset instance represents the same underlying usage or charges.

## Attribute ID

DatasetConfiguration

## Attribute Name

Dataset Configuration

## Description

Defines configuration options for controlling the structure, content, and granularity of a FOCUS dataset.

## Version Introduced

1.4
