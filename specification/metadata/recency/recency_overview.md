# Recency

The recency metadata object and its contents provide information about how up-to-date FOCUS datasets are and when they have been updated.

## Requirements

Recency adheres to the following requirements:

* Recency MAY be present in the [Metadata](#metadata).
* Recency MUST be structured as a collection of objects.
* Recency MUST NOT be null.
* Recency collection MUST NOT contain null objects.
* Recency collection MAY contain one and only one object for every [DatasetInstance](#datasetinstance) object.
* Recency collection object MUST be associated with one and only one DatasetInstance object.
* Recency collection object MUST be retrievable without inspection of the contents of [*dataset instance artifacts*](#glossary:dataset-instance-artifact).
* Recency collection object SHOULD be updated when the data generator updates the corresponding *dataset instance artifact*.

## Metadata ID

Recency

## Metadata Name

Recency

## Examples

Example scenarios include but are not limited to:

* [Updating Recency metadata for a time series dataset](#recencymetadataupdatetimeseries)
* [Updating Recency metadata for a non time series dataset](#recencymetadataupdatenontimeseries)

For an example of the FOCUS recency metadata, please refer to: [Recency Metadata Example](#recencymetadata).

## Introduced (version)

1.3
