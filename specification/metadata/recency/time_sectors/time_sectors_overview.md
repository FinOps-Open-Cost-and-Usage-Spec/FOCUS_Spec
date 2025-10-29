# Time Sectors

The FOCUS recency metadata's Time Sectors provide a list of time periods and metadata about them. Time Sectors are used when the associated FOCUS dataset is defined as a time series dataset (i.e., its dataset artifacts represent data distributed over time). Each time sector represents a single time period and the completeness of that time period as it pertains to the dataset artifact. Time sectors do not represent start and end dates of the dataset artifact but rather periods of time relative to the datasets Charge Period Start and Charge Period End. Length of time sectors can be determined by the Data Generator, though it is suggested to align time sector periods to the reports time granularity (Hourly cost reports = hourly time sectors).

<div class='h4-nonindex'>Requirements<div>

* Time Sectors MUST be present in Recency when the the associated FOCUS dataset is defined as a time series dataset.
* Time Sectors MUST be structured as a collection of objects.
* Time Sectors MUST NOT be null.
* Time Sectors collection MUST contain at least one object.
* Time Sectors object MUST NOT be null.
* Time Sectors objects MUST be updated, if already present, or added to the collection whenever Data Generator updates or provides new dataset artifacts.
