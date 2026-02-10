# Date/Time Format

Columns that provide date and time information conforming to specified rules and formatting requirements ensure clarity, accuracy, and ease of interpretation for both humans and systems.

## Attribute ID

DateTimeFormat

## Attribute Name

Date/Time Format

## Description

Rules and formatting requirements for date/time-related columns appearing in a [*FOCUS dataset*](#glossary:FOCUS-dataset).

## Requirements (FOCUS 1.4)

DateTimeFormat MUST adhere to the following requirements:

* FOCUS column containing date/time values MUST adhere to the following requirements:
  * FOCUS column containing date/time values MUST be expressed in UTC (Coordinated Universal Time) to avoid ambiguity and ensure consistency across different time zones.
  * FOCUS column containing date/time values MUST conform to the ISO 8601 standard, which provides a globally recognized format for representing dates and times.
  * FOCUS column containing date/time values and representing a specific moment in time MUST use the extended ISO 8601 format with UTC offset ('YYYY-MM-DDTHH:mm:ssZ').
  * FOCUS column containing date/time values and representing a specific moment in time MUST include both the date and time components, separated with the letter 'T'.
  * FOCUS column containing date/time values and representing a specific moment in time MUST use two-digit hours (HH), minutes (mm), and seconds (ss).
  * FOCUS column containing date/time values and representing a specific moment in time MUST end with the ISO 8601 UTC designator 'Z'.
* Custom column containing date/time values MUST adhere to the following requirements:
  * Custom column containing date/time values SHOULD be expressed in UTC (Coordinated Universal Time).
  * Custom column containing date/time values SHOULD conform to the ISO 8601 standard.
  * Custom column containing date/time values and representing a specific moment in time SHOULD use the extended ISO 8601 format with UTC offset ('YYYY-MM-DDTHH:mm:ssZ').
  * Custom column containing date/time values and representing a specific moment in time SHOULD include both the date and time components, separated with the letter 'T'.
  * Custom column containing date/time values and representing a specific moment in time SHOULD use two-digit hours (HH), minutes (mm), and seconds (ss).
  * Custom column containing date/time values and representing a specific moment in time SHOULD end with the ISO 8601 UTC designator 'Z'.

## Requirements

* Date/time values MUST be in UTC (Coordinated Universal Time) to avoid ambiguity and ensure consistency across different time zones.
* Date/time values format MUST be aligned with ISO 8601 standard, which provides a globally recognized format for representing dates and times (see [ISO 8601-1:2019](https://www.iso.org/standard/70907.html) governing document for details).
* Values providing information about a specific moment in time MUST be represented in the extended ISO 8601 format with UTC offset ('YYYY-MM-DDTHH:mm:ssZ') and conform to the following guidelines:
  * Include the date and time components, separated with the letter 'T'
  * Use two-digit hours (HH), minutes (mm), and seconds (ss).
  * End with the 'Z' indicator to denote UTC (Coordinated Universal Time)

## Exceptions

None

## Introduced (version)

0.5
