# Date/Time Format

Columns that provide date and time information conforming to specified rules and formatting requirements ensure clarity, accuracy, and ease of interpretation for both humans and systems.

## Attribute ID

DateTimeFormat

## Attribute Name

Date/Time Format

## Description

Rules and formatting requirements for date/time-related columns appearing in a [*FOCUS dataset*](#glossary:FOCUS-dataset).

## Requirements

Column conforming to DateTimeFormat attribute MUST adhere to the following requirements:

* When FOCUS column contains date/time values, FOCUS column MUST adhere to the following requirements:
  * FOCUS column MUST be expressed in UTC (Coordinated Universal Time) to avoid ambiguity and ensure consistency across different time zones.
  * FOCUS column MUST conform to the ISO 8601 standard, which provides a globally recognized format for representing dates and times.
  * When column represents a specific moment in time, FOCUS column MUST adhere to the following requirements:
    * FOCUS column MUST use the extended ISO 8601 format with UTC offset ('YYYY-MM-DDTHH:mm:ssZ').
    * FOCUS column MUST include both the date and time components, separated with the letter 'T'.
    * FOCUS column MUST use two-digit hours (HH), minutes (mm), and seconds (ss).
    * FOCUS column MUST end with the ISO 8601 UTC designator 'Z'.
* When custom column contains date/time values, custom column MUST adhere to the following requirements:
  * Custom column SHOULD be expressed in UTC (Coordinated Universal Time).
  * Custom column SHOULD conform to the ISO 8601 standard.
  * When column represents a specific moment in time, custom column MUST adhere to the following requirements:
    * Custom column SHOULD use the extended ISO 8601 format with UTC offset ('YYYY-MM-DDTHH:mm:ssZ').
    * Custom column SHOULD include both the date and time components, separated with the letter 'T'.
    * Custom column SHOULD use two-digit hours (HH), minutes (mm), and seconds (ss).
    * Custom column SHOULD end with the ISO 8601 UTC designator 'Z'.

## Introduced (version)

0.5
