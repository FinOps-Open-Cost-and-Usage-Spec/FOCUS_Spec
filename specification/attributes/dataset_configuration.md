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
* A *FOCUS dataset* MUST include [Metadata](#metadata) describing the column selection applied to the dataset.

## Exceptions

None

## Introduced (version)

1.4
