# Time Sector End

The [Time Sector End](#meta) is the datetime of the end of the time sector. The [Time Sector End](#meta) MUST be later than the [Time Sector Start](#meta).

[TimeSectorEnd](#meta) adheres to the following requirements:

* [TimeSectorEnd](#meta) MUST be present in the [TimeSectors](#meta) subsection of the [Recency](#meta) metadata section.
* [TimeSectorEnd](#meta) MUST be of type Date/Time.
* [TimeSectorEnd](#meta) MUST NOT be null.
* [TimeSectorEnd](#meta) MUST conform to [DateTimeFormat](#attr).
* [TimeSectorEnd](#meta) must be exclusive of the end time of the subsequent time sector.
* [TimeSectorEnd](#meta) MUST be later than [TimeSectorStart](#meta).

## Metadata ID

TimeSectorEnd

## Metadata Name

Time Sector End

## Content Constraints

| Constraint    | Value                                |
|:--------------|:-------------------------------------|
| Feature level | Mandatory                            |
| Allows nulls  | False                                |
| Data type     | Date/Time                            |
| Value format  | [Date/Time Format](#attr)                       |

## Version Introduced

1.3
