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
* When *FOCUS dataset* populates specific columns for records matching criteria, *FOCUS dataset* MUST adhere to the following requirements:
  * *FOCUS dataset* MUST be configurable to select one set of columns for records matching the same criteria when more than one set is offered.
  * *FOCUS dataset* MUST include the columns in a selected set, regardless of the user-defined selection of columns.
  * *FOCUS dataset* MUST be configurable to select how a selected set is delivered when more than one delivery option is documented.
  * Criteria documentation MUST adhere to the following requirements:
    * Criteria documentation MUST include the values of [*FOCUS columns*](#glossary:FOCUS-column) representing [*dimensions*](#glossary:dimension) that identify the matching records (e.g., Service Name is "Example AI Service").
    * Criteria documentation MUST include each set of columns offered for the same criteria.
    * Criteria documentation MUST include the columns in each set.
    * Criteria documentation MUST include whether each set uses [DataGeneratorCalculatedSplitCostAllocationHandling](#attributes.datagenerator-calculatedsplitcostallocationhandling).
    * Criteria documentation MUST include each delivery option offered for each set.
    * Criteria documentation MUST include the relationship between records delivered under each delivery option and other records representing the same underlying data in [*dataset artifacts*](#glossary:dataset-artifact) or [*companion artifacts*](#glossary:companion-artifact) (e.g., records that replace or supplement other records).
    * Criteria documentation MUST include the columns that relate records in a companion artifact to the related records in the dataset artifact when a companion artifact is offered.
    * Criteria documentation MUST be accessible to practitioners.
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

A data generator populates specific columns for records where Service Name is "Example AI Service". The criteria documentation identifies two sets for those records: a default set that does not populate per-user detail, and a set that populates the custom column `x_UserId`.

A practitioner selects the `x_UserId` set and chooses to have those columns delivered by replacing the corresponding records. In the delivered dataset artifact, each matching record is replaced by one record per user, and the summable metrics of those records sum to the values of the record they replace. The mechanism used to make these selections is not defined by FOCUS.

## Attribute ID

DatasetConfiguration

## Attribute Name

Dataset Configuration

## Description

Defines configuration options for controlling the structure and content of a FOCUS dataset, including which columns are populated.

## Version Introduced

1.4
