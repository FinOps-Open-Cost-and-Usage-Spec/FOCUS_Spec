# Dataset Configuration

Dataset Configuration allows FinOps practitioners to tailor the structure, content, and service-specific detail of a [*FOCUS dataset*](#glossary:FOCUS-dataset). Datasets provided by data generators are often massive, and their ingestion can lead to excessive storage costs and slow processing times. By selecting only the columns and detail needed for a given workflow, FinOps practitioners can optimize the dataset for better performance and lower storage costs.

Common scenarios where dataset configuration is valuable include:

* **Managing Scale**: Trim large exports to reduce time and cost of data preparation
* **Reducing Noise**: Tailor datasets for specific workflows (e.g., cost allocation, commitment analysis)
* **Managing Detail**: Include optional detail for cost areas where detailed attribution is needed (e.g., per-user or per-feature costs for a shared service)
* **Lowering Barriers**: Strip away technical complexity for spreadsheet users
* **Enabling Comparison**: Remove custom (`x_`) columns for standardized cross-provider reporting

## Requirements

FOCUS dataset conforming to DatasetConfiguration attribute MUST adhere to the following requirements:

* *FOCUS dataset* MUST be configurable to include only a user-defined selection of columns.
* *FOCUS dataset* MUST adhere to all column-level specifications defined in the FOCUS schema, regardless of the selected configuration (e.g., column selection or detail level).
* *FOCUS dataset* MUST be configurable to select one detail level for a detail scope when the same data coverage can be delivered at more than one detail level.
* *FOCUS dataset* MUST be configurable to select one delivery method for all detail scopes or for each detail scope when a selected detail level can be delivered through more than one delivery method.
* *FOCUS dataset* MUST include the columns documented for a selected detail level.
* *FOCUS dataset* detail-scope documentation MUST include FOCUS dimension criteria that identify the data coverage of each offered detail scope.
* *FOCUS dataset* detail-scope documentation MUST include all offered detail levels for each offered detail scope.
* *FOCUS dataset* detail-scope documentation MUST include the columns populated for each offered detail level.
* *FOCUS dataset* detail-scope documentation MUST include the available delivery methods for each offered detail level.
* *FOCUS dataset* detail-scope documentation MUST include the relationship of each delivery method to other delivered [*dataset artifacts*](#glossary:dataset-artifact) that represent the same underlying usage or charges.
* *FOCUS dataset* detail-scope documentation MUST include the columns used to relate a detail dataset artifact to the corresponding less-detailed dataset artifact when the detail is delivered in a separate dataset artifact.
* *FOCUS dataset* SHOULD represent records with identical values in all delivered dimension columns and non-summable metric columns as a single record.
* *FOCUS dataset* SHOULD preserve the aggregate value of each summable metric when records are represented as a single record.
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

A provider offers a user-attribution detail scope. The detail-scope documentation identifies its data coverage as records where ServiceName is `"Example AI Service"`. The documentation identifies a `"user"` detail level and the custom `x_UserId` column that is populated for that detail level.

A practitioner selects the `"user"` detail level for that scope and selects the replacement delivery method. The delivered dataset includes `x_UserId` and replaces a record in the documented data coverage with the detailed records it represents. The configuration mechanism used to select the detail level and delivery method is provider-defined.

## Attribute ID

DatasetConfiguration

## Attribute Name

Dataset Configuration

## Description

Defines configuration options for controlling the structure, content, and service-specific detail of a FOCUS dataset.

## Version Introduced

1.4 (column selection); 1.5 (service-specific detail configuration)
