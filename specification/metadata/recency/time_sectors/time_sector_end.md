# Time Sector End

The Time Sector End is the datetime of the end of the time sector. The EndTime MUST be later than the StartTime.

TimeSectorEnd adheres to the following requirements:

* TimeSectorEnd MUST be present in the [TimeSectors](#timesectors) subsection of the [Recency](#recency) metadata section.
* TimeSectorEnd MUST be of type Date/Time.
* TimeSectorEnd MUST NOT be null.
* TimeSectorEnd MUST conform to [DateTimeFormat](#date/timeformat).
* TimeSectorEnd must be exclusive of the end time of the subsequent time sector.
* TimeSectorEnd MUST be later than TimeSectorStart.

## Metadata ID

TimeSectorEnd

## Metadata Name

Time Sector End

## Content constraints

| Constraint    | Value                                |
|:--------------|:-------------------------------------|
| Feature level | Mandatory                            |
| Allows nulls  | False                                |
| Data type     | Date/Time                            |
| Value format  | [Date/Time Format](#date/timeformat) |

## Introduced (version)

1.3
