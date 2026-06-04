# Dataset Instance

The Dataset Instance metadata object provides information about the [*dataset instance*](#glossary:dataset-instance) and its content. Dataset Instance is a data generator-delivered instance of a FOCUS Dataset. For example, a Data Generator may provide multiple datasets utilizing the FOCUS specification, including multiple instances of the FOCUS Cost and Usage dataset, each representing a different time granularity.

## Requirements

DatasetInstance adheres to the following requirements:

* DatasetInstance MUST be present in the [Metadata](#metadata).
* DatasetInstance MUST be structured as a collection of objects.
* DatasetInstance MUST NOT be null.
* DatasetInstance collection MUST contain at least one object for every [*FOCUS dataset*](#glossary:FOCUS-dataset) supported by the data generator.
* DatasetInstance collection object MUST NOT be null.
* DatasetInstance collection object MUST be associated with one and only one *FOCUS dataset*.

## Metadata ID

DatasetInstance

## Metadata Name

Dataset Instance

## Examples

For an example of the FOCUS dataset instance metadata, please refer to: [Dataset Instance Metadata Example](#datasetinstancemetadata).

## Introduced (version)

1.3
