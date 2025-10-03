# Time Sector End

The Time Sector End is the datetime of the end of the time sector. The EndTime MUST be later than the StartTime.

The Time Sector End MUST be present in the metadata. This MUST be of type Date/Time and MUST NOT contain null values. The Time Sector End must be exclusive of the end time of the subsequent time sector. The Time Sector End MUST be later than the StartTime. EndTime MUST conform to [DateTimeFormat](#date/timeformat).

## Metadata ID

TimeSectorEnd

## Metadata Name

Time Sector End

## Content constraints

| Constraint    | Value                                     |
|:--------------|:------------------------------------------|
| Feature level | Mandatory                                 |
| Allows nulls  | False                                     |
| Data type       | Date/Time                            |
| Value format    | [Date/Time Format](#date/timeformat) |

## Introduced (version)

1.3
