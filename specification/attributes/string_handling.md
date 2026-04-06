# String Handling

Columns that capture string values conforming to specified requirements foster data integrity, interoperability, and consistency, improve data analysis and reporting, and support reliable data-driven decision-making.

## Requirements

Column conforming to StringHandling attribute MUST adhere to the following requirements:

* [*FOCUS dataset column*](#glossary:FOCUS-dataset-column) MUST preserve the original casing of string values.
* *FOCUS dataset column* MUST preserve the original spacing of string values.
* *FOCUS dataset column* MUST preserve other relevant consistency factors as specified by the data generator or end-user.
* *FOCUS dataset column* MUST remain consistent across all [*billing periods*](#glossary:billing-period) when the *FOCUS dataset column* contains immutable string values (e.g., resource identifier, region identifier).
* When column contains mutable string values (e.g., resource name, region name), *FOCUS dataset column* MUST adhere to the following requirements:
  * *FOCUS dataset column* MUST reflect the altered value in all records pertaining to a period after the change.
  * *FOCUS dataset column* MUST reflect the string value as it existed prior to the change in all records pertaining to a period prior to the change when the record does not represent a correction to a previously closed billing period.
  * *FOCUS dataset column* MAY reflect the altered value in records pertaining to a period prior to the change when the record represents a correction to a previously closed billing period.
* When *FOCUS dataset column* contains not-nullable string values, it MUST adhere to the following requirements:
  * *FOCUS dataset column* SHOULD NOT contain empty strings.
  * *FOCUS dataset column* SHOULD NOT contain strings consisting solely of whitespace characters.

## Attribute ID

StringHandling

## Attribute Name

String Handling

## Description

Requirements for string-capturing columns appearing in a [*FOCUS dataset*](#glossary:FOCUS-dataset).

## Introduced (version)

1.0
