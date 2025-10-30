# Time Sector Start

The Time Sector Start is the datetime of the start of the time sector.

The TimeSectorStart property adheres to the following requirements:

* TimeSectorStart MUST be present in the [TimeSectors](#timesectors) subsection of the [Recency](#recency) metadata section.
* TimeSectorStart MUST be of type Date/Time.
* TimeSectorStart MUST NOT contain null values.
* TimeSectorStart MUST conform to [DateTimeFormat](#date/timeformat).

## Metadata ID

TimeSectorStart

## Metadata Name

Time Sector Start

## Content constraints

| Constraint    | Value                                |
|:--------------|:-------------------------------------|
| Feature level | Mandatory                            |
| Allows nulls  | False                                |
| Data type     | Date/Time                            |
| Value format  | [Date/Time Format](#date/timeformat) |

## Introduced (version)

1.3
