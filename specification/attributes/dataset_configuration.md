# Dataset Configuration

Dataset Configuration allows FinOps practitioners to tailor the structure and content of a [*FOCUS dataset*](#glossary:FOCUS-dataset), including when specific columns are populated. Datasets provided by data generators are often massive, and their ingestion can lead to excessive storage costs and slow processing times. By selecting only what is needed, FinOps practitioners can optimize the dataset for better performance and lower storage costs.

Common scenarios where dataset configuration is valuable include:

* **Managing Scale**: Trim large exports to reduce time and cost of data preparation
* **Reducing Noise**: Tailor datasets for specific workflows (e.g., cost allocation, commitment analysis)
* **Managing Detail**: Populate specific columns only for records that need them (e.g., per-user or per-feature costs for a shared service)
* **Lowering Barriers**: Strip away technical complexity for spreadsheet users
* **Enabling Comparison**: Remove custom (`x_`) columns for standardized cross-provider reporting

## Requirements

Dataset conforming to DatasetConfiguration attribute MUST adhere to the following requirements:

* *FOCUS dataset* MUST be configurable to include only a user-defined selection of columns.
* *FOCUS dataset* MUST adhere to all column-level specifications defined in the FOCUS schema, regardless of the selected configuration.
* When *FOCUS dataset* populates specific columns for records matching user-defined criteria, *FOCUS dataset* MUST adhere to the following requirements:
  * Column population documentation MUST adhere to the following requirements:
    * Column population documentation MUST include the columns that can be populated.
    * Column population documentation MUST include whether populated columns use [DataGeneratorCalculatedSplitCostAllocationHandling](#attributes.datagenerator-calculatedsplitcostallocationhandling).
    * Column population documentation MUST be accessible to practitioners.
  * User-defined criteria MUST adhere to the following requirements:
    * User-defined criteria MUST include one or more conditions and the columns to populate for matching records.
    * User-defined criteria MUST include a [*FOCUS column*](#glossary:FOCUS-column) and one or more matching values for each condition.
    * User-defined criteria MAY support additional comparison operators (e.g., wildcard, less than, greater than or equal to).
* *FOCUS dataset* SHOULD represent records with identical values in all delivered [*FOCUS dataset columns*](#glossary:FOCUS-dataset-column), other than *FOCUS dataset columns* representing summable [*metrics*](#glossary:metric), as a single record.
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

A data generator's column population documentation states that the custom column `x_UserId` can be populated for records where Service Name is "Example AI Service". A practitioner defines criteria matching that Service Name value and requests `x_UserId` as a populated column. The delivered records for matching Service Name values include populated `x_UserId` values; other records are unaffected. The mechanism used to define and submit criteria is not defined by FOCUS.

## Attribute ID

DatasetConfiguration

## Attribute Name

Dataset Configuration

## Description

Defines configuration options for controlling the structure and content of a FOCUS dataset, including which columns are populated.

## Version Introduced

1.4
