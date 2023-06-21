# Datetime Requirements

Billing data columns that provide date and time information (datetime related columns) conforming to specified rules and formatting requirements ensure clarity, accuracy and ease of interpretation for both humans and systems.

All datetime related columns, defined in the FOCUS specification, MUST be represented in UTC and follow the ISO 8601 aligned formatting requirements listed below. Provider generated datetime related columns SHOULD adopt the same format requirements over time.

## Attribute ID

DatetimeRequirements

## Attribute name

Datetime Requirements

## Description

Rules and formatting requirements for datetime related columns appearing in billing data.

## Requirements

* Datetime values MUST be in UTC (Coordinated Universal Time) to avoid ambiguity and ensure consistency across different time zones.
* Datetime values format MUST be aligned with ISO 8601 standard, which provides a globally recognized format for representing dates and times (see [ISO 8601-1:2019] governing document for details).
* Values providing information about a specific moment in time MUST be represented in the extended ISO 8601 format with time zone offset ('YYYY-MM-DDTHH:mm:ssZ') and conform to the following guidelines:
  * Include the date and time components, separated with the letter 'T'
  * Use two-digit hours (HH), minutes (mm), and seconds (ss).
  * End with the 'Z' indicator to denote UTC (Coordinated Universal Time)

## Exceptions

None

## Introduced (version)

0.5
