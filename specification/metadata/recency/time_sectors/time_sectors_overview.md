# Time Sectors

The FOCUS recency metadata's [Time Sectors](#meta) provide a list of time periods and metadata about them. [Time Sectors](#meta) are used when the associated [FOCUS dataset](#term) is defined as a time series dataset (i.e., its dataset artifacts represent data distributed over time). Each time sector represents a single time period and the completeness of that time period as it pertains to the dataset artifact. Time sectors do not represent start and end dates of the dataset artifact but rather periods of time relative to the datasets [Charge Period Start](#col) and [Charge Period End](#col). Length of time sectors can be determined by the Data Generator, though it is suggested to align time sector periods to the reports time granularity (Hourly cost reports = hourly time sectors).

## Requirements

[TimeSectors](#meta) adheres to the following requirements:

* [TimeSectors](#meta) MUST be present in an object within the [Recency](#meta) collection when the associated [FOCUS dataset](#term) is defined as a time series dataset.
* [TimeSectors](#meta) MUST be structured as a collection of objects.
* [TimeSectors](#meta) MUST NOT be null.
* [TimeSectors](#meta) collection MUST contain at least one object.
* [TimeSectors](#meta) collection MUST NOT contain null objects.
* [TimeSectors](#meta) collection object MUST be updated, when already present, or added to the collection whenever the data generator updates or provides new dataset artifacts.

## Metadata ID

TimeSectors

## Metadata Name

Time Sectors

## Version Introduced

1.3
