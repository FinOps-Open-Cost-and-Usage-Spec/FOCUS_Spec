# Dataset Instance

The Dataset Instance metadata object provides information about the [dataset instance](#term) and its content. Dataset Instance is a data generator-delivered instance of a FOCUS Dataset. For example, a [Data Generator](#meta) may provide multiple datasets utilizing the FOCUS specification, including multiple instances of the FOCUS [Cost and Usage](#ds) dataset, each representing a different time granularity.

## Requirements

[DatasetInstance](#meta) adheres to the following requirements:

* [DatasetInstance](#meta) MUST be present in the [Metadata](#metadata).
* [DatasetInstance](#meta) MUST be structured as a collection of objects.
* [DatasetInstance](#meta) MUST NOT be null.
* [DatasetInstance](#meta) collection MUST contain at least one object for every [FOCUS dataset](#term) supported by the data generator.
* [DatasetInstance](#meta) collection object MUST NOT be null.
* [DatasetInstance](#meta) collection object MUST be associated with one and only one [FOCUS dataset](#term).

## Metadata ID

DatasetInstance

## Metadata Name

Dataset Instance

## Examples

For an example of the FOCUS dataset instance metadata, please refer to: [Dataset Instance Metadata Example](#supportedfeatures.datasetinstancemetadata).

## Version Introduced

1.3
