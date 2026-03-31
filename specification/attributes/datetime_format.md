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

* *FOCUS dataset* column MUST be expressed in UTC (Coordinated Universal Time) to avoid ambiguity and ensure consistency across different time zones.
* *FOCUS dataset* column MUST conform to the ISO 8601 standard, which provides a globally recognized format for representing dates and times (see [ISO 8601-1:2019](https://www.iso.org/standard/70907.html) governing document for details).
* When column represents a specific moment in time, *FOCUS dataset* column MUST adhere to the following requirements:
  * *FOCUS dataset* column MUST use the extended ISO 8601 format with UTC offset (`YYYY-MM-DDTHH:mm:ssZ`).
  * *FOCUS dataset* column MUST include both the date and time components, separated with the letter `T`.
  * *FOCUS dataset* column MUST use two-digit hours (`HH`), minutes (`mm`), and seconds (`ss`).
  * *FOCUS dataset* column MUST end with the ISO 8601 UTC designator `Z`.

## Introduced (version)

0.5
