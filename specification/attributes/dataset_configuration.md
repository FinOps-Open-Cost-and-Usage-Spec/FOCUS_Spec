# Dataset Configuration

FinOps practitioners often need to configure the data in a [*FOCUS dataset*](#glossary:FOCUS-dataset) to optimize cost, storage, and performance. FOCUS datasets can include many columns, some of which may be static for a given provider, very large, or simply not needed for specific scenarios. Dataset Configuration defines options that allow practitioners to control the structure and content of the data included in the dataset.

## Attribute ID

DatasetConfiguration

## Attribute Name

Dataset Configuration

## Description

Defines configuration options for controlling the structure and content of a FOCUS dataset.

## Requirements

* A *FOCUS dataset* MUST allow selecting which columns to include.
  * A *FOCUS dataset* MUST produce conformant column values regardless of which columns are included.
  * A *FOCUS dataset* SHOULD sum metric columns by default when the selected dimension columns result in rows with identical values.
* A *FOCUS dataset* SHOULD allow opting in or out of row aggregation (summing metrics).
  * A *FOCUS dataset* MUST sum metric column values when rows are aggregated.
  * A *FOCUS dataset* SHOULD use case-insensitive matching when aggregating rows.
* A *FOCUS dataset* MUST allow selecting the time granularity based on [ChargePeriodStart](#chargeperiodstart), when available.
  * A *FOCUS dataset* MUST allow selecting daily granularity.
  * A *FOCUS dataset* MUST allow selecting hourly granularity when the dataset includes costs priced at an hourly or lower grain.
  * A *FOCUS dataset* SHOULD allow selecting monthly granularity.
  * A *FOCUS dataset* MUST sum metric columns based on selected dimension columns with identical values when time granularity is changed.
* A *FOCUS dataset* SHOULD allow selecting the FOCUS version.
  * A *FOCUS dataset* MUST NOT add or remove columns when a specific FOCUS version is selected.
* A *FOCUS dataset* SHOULD allow filtering rows by column values.
  * A *FOCUS dataset* MUST use case-insensitive matching when filtering rows.
* A *FOCUS dataset* MUST include metadata describing the selected configuration options.

## Exceptions

None

## Introduced (version)

1.4
