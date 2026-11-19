# Recency

The recency metadata object and its contents provide information about how up-to-date FOCUS datasets are and when they have been updated.

## Requirements

[Recency](#meta) adheres to the following requirements:

* [Recency](#meta) MAY be present in the [Metadata](#metadata).
* [Recency](#meta) MUST be structured as a collection of objects.
* [Recency](#meta) MUST NOT be null.
* [Recency](#meta) collection MUST NOT contain null objects.
* [Recency](#meta) collection MAY contain one and only one object for every [DatasetInstance](#meta) object.
* [Recency](#meta) collection object MUST be associated with one and only one [DatasetInstance](#meta) object.
* [Recency](#meta) collection object MUST be retrievable without inspection of the contents of [dataset instance artifacts](#term).
* [Recency](#meta) collection object SHOULD be updated when the data generator updates the corresponding [dataset instance artifact](#term).

## Metadata ID

Recency

## Metadata Name

Recency

## Examples

Example scenarios include but are not limited to:

* [Updating Recency metadata for a time series dataset](#appendix.examples:metadata.recencymetadataupdatetimeseries)
* [Updating Recency metadata for a non time series dataset](#appendix.examples:metadata.recencymetadataupdatenontimeseries)

For an example of the FOCUS recency metadata, please refer to: [Recency Metadata Example](#supportedfeatures.recencymetadata).

## Version Introduced

1.3
