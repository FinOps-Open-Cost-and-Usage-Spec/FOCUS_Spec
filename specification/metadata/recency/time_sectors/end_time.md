# End Time

The end time of the time sector. The EndTime MUST be later than the StartTime.

The EndTime MUST be present in the metadata. This MUST be of type Date/Time and MUST NOT contain null values. The EndTime must be exclusive of the start time of the subsequent time sector. The EndTime MUST be later than the StartTime. EndTime MUST conform to [DateTimeFormat](#date/timeformat).

## Metadata ID

StartTime

## Metadata Name

Start Time

## Content constraints

| Constraint    | Value                                     |
|:--------------|:------------------------------------------|
| Feature level | Mandatory                                 |
| Allows nulls  | False                                     |
| Data type       | Date/Time                            |
| Value format    | [Date/Time Format](#date/timeformat) |

## Introduced (version)

1.3
