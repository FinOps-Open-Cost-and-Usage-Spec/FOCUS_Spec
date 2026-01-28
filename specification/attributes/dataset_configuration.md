# Dataset Configuration

FinOps practitioners often need to configure the data in a [*FOCUS dataset*](#glossary:FOCUS-dataset) to optimize cost, storage, and performance. FOCUS datasets can include many columns, some of which may be static for a given provider, very large, or simply not needed for specific scenarios. Dataset Configuration defines options that allow practitioners to control the structure and content of the data included in the dataset.

## Attribute ID

DatasetConfiguration

## Attribute Name

Dataset Configuration

## Description

Defines configuration options for controlling the structure and content of a FOCUS dataset.

## Requirements

* FOCUS datasets MUST allow selecting which columns to include.
  * FOCUS datasets MUST produce conformant column values regardless of which columns are included.
  * FOCUS datasets SHOULD sum metric columns by default when the selected dimension columns result in rows with identical values.
* FOCUS datasets SHOULD allow opting in or out of row aggregation (summing metrics).
  * FOCUS datasets MUST sum metric column values when rows are aggregated.
  * FOCUS datasets SHOULD use case-insensitive matching when aggregating rows.
* FOCUS datasets MUST allow selecting the time granularity based on [ChargePeriodStart](#chargeperiodstart), when available.
  * FOCUS datasets MUST allow selecting daily granularity.
  * FOCUS datasets MUST allow selecting hourly granularity when the dataset includes costs priced at an hourly or lower grain.
  * FOCUS datasets SHOULD allow selecting monthly granularity.
  * FOCUS datasets MUST sum metric columns based on selected dimension columns with identical values when time granularity is changed.
* FOCUS datasets SHOULD allow selecting the FOCUS version.
  * FOCUS datasets MUST NOT add or remove columns when a specific FOCUS version is selected.
* FOCUS datasets SHOULD allow filtering rows by column values.
  * FOCUS datasets MUST use case-insensitive matching when filtering rows.
* FOCUS datasets MUST include metadata describing the selected configuration options.

## Exceptions

None

## Introduced (version)

1.4
