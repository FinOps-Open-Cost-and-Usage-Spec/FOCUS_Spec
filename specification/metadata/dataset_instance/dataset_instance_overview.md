# Dataset Instance

The Dataset Instance metadata object provided by a Data Generator provides information about the dataset instance and its content. Dataset Instances are a Data Generator-delivered instance of a FOCUS Dataset. For example, a Data Generator may provide multiple datasets utilizing the FOCUS spec, including multiple instances of the FOCUS Cost and Usage dataset, each representing a different time granularity.

## Requirements

* Dataset Instance metadata MUST be provided for every dataset instance provided by the data generator.
* Dataset Instance metadata MUST provide a reference to the dataset instance of the dataset artifact.
* Dataset Instance metadata MUST be retrievable independently from the dataset artifact it describes.
* Dataset Instance metadata MAY be provided through the structure and/or schema of the delivery mechanism (e.g., database tables).
* Dataset Instance metadata SHOULD be updated when a data generator updates the corresponding dataset artifact.

## Dataset Instance Example

For an example of the FOCUS dataset instance metadata, please refer to: [Dataset Instance Metadata Example](#datasetinstancemedataexample).
