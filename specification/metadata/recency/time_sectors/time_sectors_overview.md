# Time Sectors

The FOCUS recency metadata's Time Sectors provide a list of time periods and metadata about them. Time Sectors are used when the associated [*FOCUS dataset*](#glossary:FOCUS-dataset) is defined as a time series dataset (i.e., its dataset artifacts represent data distributed over time). Each time sector represents a single time period and the completeness of that time period as it pertains to the dataset artifact. Time sectors do not represent start and end dates of the dataset artifact but rather periods of time relative to the datasets Charge Period Start and Charge Period End. Length of time sectors can be determined by the Data Generator, though it is suggested to align time sector periods to the reports time granularity (Hourly cost reports = hourly time sectors).

## Requirements

TimeSectors adheres to the following requirements:

* TimeSectors MUST be present in an object within the [Recency](#recency) collection when the the associated *FOCUS dataset* is defined as a time series dataset.
* TimeSectors MUST be structured as a collection of objects.
* TimeSectors MUST NOT be null.
* TimeSectors collection MUST contain at least one object.
* TimeSectors collection MUST NOT contain null objects.
* TimeSectors collection object MUST be updated, if already present, or added to the collection whenever the data generator updates or provides new dataset artifacts.

## Metadata ID

TimeSectors

## Metadata Name

Time Sectors

## Introduced (version)

1.3
