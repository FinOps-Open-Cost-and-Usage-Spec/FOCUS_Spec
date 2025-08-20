# Last Updated

Date time the when the dataset or time sector was last updated. For datasets that are not over time datasets, last Updated is the last time the data within the dataset was updated. For time sector datasets, last Updated is the last time the data within the time sector was updated.

The LastUpdated MUST be present in the metadata. This MUST be of type Date/Time and MUST NOT contain null values. LastUpdated MUST conform to [DateTimeFormat](#date/timeformat).

## Metadata ID

LastUpdated

## Metadata Name

Last Updated

## Content constraints

| Constraint    | Value                                     |
|:--------------|:------------------------------------------|
| Feature level | Mandatory                                 |
| Allows nulls  | False                                     |
| Data type       | Date/Time                            |
| Value format    | [Date/Time Format](#date/timeformat) |

## Introduced (version)

1.3
