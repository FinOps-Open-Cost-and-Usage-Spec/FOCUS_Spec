# Dataset Configuration

FinOps practitioners often need to configure the data in a [*FOCUS dataset*](#glossary:FOCUS-dataset) to optimize cost, storage, and performance. FOCUS datasets can include many columns, some of which may be static for a given provider, very large, or simply not needed for specific scenarios. Dataset Configuration defines options that allow practitioners to control the structure and content of the data included in the dataset.

Common scenarios where dataset configuration is valuable include:

* Reducing dataset size for cost optimization when working with large exports
* Creating focused datasets for specific workflows (cost allocation, commitment analysis)
* Simplifying data for non-technical users with spreadsheet tools
* Excluding custom (x_) columns for standardized cross-provider reporting

## Attribute ID

DatasetConfiguration

## Attribute Name

Dataset Configuration

## Description

Defines configuration options for controlling the structure and content of a FOCUS dataset.

## Requirements

* A *FOCUS dataset* MUST allow selecting which columns to include.
  * A *FOCUS dataset* MUST produce conformant column values regardless of which columns are included.
* A *FOCUS dataset* SHOULD include [Metadata](#metadata) describing the column selection applied to the dataset.

## Example

A practitioner configures their dataset to include only these columns:

* BillingAccountId
* ServiceName
* BilledCost
* EffectiveCost
* Tags

Even though columns like `CommitmentDiscountId` and `ResourceId` are excluded, the included cost columns (`BilledCost`, `EffectiveCost`) still reflect commitment discounts correctly. The dataset remains conformant because each included column follows all FOCUS requirements for that column, including requirements that reference columns not in the dataset.

## Exceptions

None

## Introduced (version)

1.4
