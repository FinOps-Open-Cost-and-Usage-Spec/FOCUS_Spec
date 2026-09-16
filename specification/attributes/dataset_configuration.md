# Dataset Configuration

Dataset Configuration allows FinOps practitioners to tailor the structure, content, and scoped detail of a [*FOCUS dataset*](#glossary:FOCUS-dataset). Datasets provided by data generators are often massive, and their ingestion can lead to excessive storage costs and slow processing times. By selecting only the columns and detail needed for a given workflow, FinOps practitioners can optimize the dataset for better performance and lower storage costs.

Common scenarios where dataset configuration is valuable include:

* **Managing Scale**: Trim large exports to reduce time and cost of data preparation
* **Reducing Noise**: Tailor datasets for specific workflows (e.g., cost allocation, commitment analysis)
* **Managing Detail**: Include optional detail for areas of a dataset where detailed attribution is needed (e.g., per-user or per-feature costs for a shared service)
* **Lowering Barriers**: Strip away technical complexity for spreadsheet users
* **Enabling Comparison**: Remove custom (`x_`) columns for standardized cross-provider reporting

## Requirements

Dataset conforming to DatasetConfiguration attribute MUST adhere to the following requirements:

* *FOCUS dataset* MUST be configurable to include only a user-defined selection of columns.
* *FOCUS dataset* MUST adhere to all column-level specifications defined in the FOCUS schema, regardless of the selected configuration (e.g., column selection or detail variant selection).
* When a [*detail scope*](#glossary:detail-scope) is offered, *FOCUS dataset* MUST adhere to the following requirements:
  * *FOCUS dataset* MUST be configurable to select each [*detail variant*](#glossary:detail-variant) offered for a *detail scope*.
  * *FOCUS dataset* MUST include only one *detail variant* for each *detail scope*.
  * *FOCUS dataset* MUST preserve the sum of each [*FOCUS dataset column*](#glossary:FOCUS-dataset-column) representing a summable [*metric*](#glossary:metric) for the records in a *detail scope* across all offered *detail variants*.
  * *FOCUS dataset* MUST include the columns documented for a selected *detail variant*, regardless of the user-defined selection of columns.
  * *FOCUS dataset* MUST be configurable to select one [*detail representation*](#glossary:detail-representation) when more than one *detail representation* is offered for a selected *detail variant*.
  * *FOCUS dataset* detail scope documentation MUST adhere to the following requirements:
    * *FOCUS dataset* detail scope documentation MUST include the values of [*FOCUS columns*](#glossary:FOCUS-column) representing [*dimensions*](#glossary:dimension) that identify the records in each *detail scope*.
    * *FOCUS dataset* detail scope documentation MUST include each *detail variant* offered for each *detail scope*.
    * *FOCUS dataset* detail scope documentation MUST include the columns populated for each offered *detail variant*.
    * *FOCUS dataset* detail scope documentation MUST include whether each offered *detail variant* uses [DataGeneratorCalculatedSplitCostAllocationHandling](#attributes.datagenerator-calculatedsplitcostallocationhandling).
    * *FOCUS dataset* detail scope documentation MUST include each *detail representation* offered for each *detail variant*.
    * *FOCUS dataset* detail scope documentation MUST include the relationship between records delivered at each *detail representation* and other records representing the same underlying data in [*dataset artifacts*](#glossary:dataset-artifact) or [*companion artifacts*](#glossary:companion-artifact) (e.g., records that replace or supplement other records).
    * *FOCUS dataset* detail scope documentation MUST include the columns that relate records in a *companion artifact* to the related records in the *dataset artifact* when a *companion artifact* is offered.
    * *FOCUS dataset* detail scope documentation MUST be accessible to practitioners.
* *FOCUS dataset* SHOULD represent records with identical values in all delivered *FOCUS dataset columns*, other than *FOCUS dataset columns* representing summable *metrics*, as a single record.
* *FOCUS dataset* SHOULD preserve the aggregate value of each *FOCUS dataset column* representing a summable *metric* when records are represented as a single record.
* *FOCUS dataset* MAY offer a default column set.
* *FOCUS dataset* default column set MUST include all applicable FOCUS columns when a default column set is offered.

## Example

A practitioner configures their FOCUS Cost and Usage dataset to include only these columns:

* BillingAccountId
* ServiceName
* BilledCost
* EffectiveCost
* Tags

Even though columns like `CommitmentDiscountId` and `ResourceId` are excluded, the included cost columns (`BilledCost`, `EffectiveCost`) still reflect commitment discounts correctly. The dataset remains conformant to the FOCUS specification because each included column follows all requirements for that column, including requirements that reference columns not in the dataset.

A data generator offers a detail scope for records where Service Name is "Example AI Service". The detail scope documentation identifies three detail variants for that scope: the default variant, which does not populate per-user detail; a "user" detail variant, which populates the custom column `x_UserId`; and a "feature" detail variant, which populates the custom column `x_FeatureName`.

Neither the "user" nor the "feature" detail variant is more detailed than the other, since each populates a column the other does not. The records in the detail scope sum to the same totals for each summable metric under either selection.

A practitioner selects the "user" detail variant and the expanded detail representation. In the delivered dataset artifact, each record in the detail scope is replaced by one record per user, and the summable metrics of those records sum to the values of the record they replace. The mechanism used to make these selections is not defined by FOCUS.

## Attribute ID

DatasetConfiguration

## Attribute Name

Dataset Configuration

## Description

Defines configuration options for controlling the structure, content, and scoped detail of a FOCUS dataset.

## Version Introduced

1.4
