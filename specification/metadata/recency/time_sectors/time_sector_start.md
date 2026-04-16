# Time Sector Start

The Time Sector Start is the datetime of the start of the time sector.

TimeSectorStart adheres to the following requirements:

* TimeSectorStart MUST be present in the [TimeSectors](#metadata.recency.timesectors) subsection of the [Recency](#metadata.recency) metadata section.
* TimeSectorStart MUST be of type Date/Time.
* TimeSectorStart MUST NOT be null.
* TimeSectorStart MUST conform to [DateTimeFormat](#attributes.date/timeformat).

## Metadata ID

TimeSectorStart

## Metadata Name

Time Sector Start

## Content Constraints

| Constraint    | Value                                |
|:--------------|:-------------------------------------|
| Feature level | Mandatory                            |
| Allows nulls  | False                                |
| Data type     | Date/Time                            |
| Value format  | [Date/Time Format](#attributes.date/timeformat) |

## Introduced (version)

1.3
