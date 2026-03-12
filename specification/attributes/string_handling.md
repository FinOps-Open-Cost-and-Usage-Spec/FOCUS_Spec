# String Handling

Columns that capture string values conforming to specified requirements foster data integrity, interoperability, and consistency, improve data analysis and reporting, and support reliable data-driven decision-making.

## Attribute ID

StringHandling

## Attribute Name

String Handling

## Description

Requirements for string-capturing columns appearing in a [*FOCUS dataset*](#glossary:FOCUS-dataset).

## Requirements

Column conforming to StringHandling attribute MUST adhere to the following requirements:

* When FOCUS column contains string values, FOCUS column MUST adhere to the following requirements:
  * FOCUS column MUST preserve the original casing of string values.
  * FOCUS column MUST preserve the original spacing of string values.
  * FOCUS column MUST preserve other relevant consistency factors as specified by the data generator or end-user.
  * FOCUS column MUST remain consistent across all [*billing periods*](#glossary:billing-period) when the FOCUS column contains immutable string values (e.g., resource identifier, region identifier).
  * When column contains mutable string values, FOCUS column MUST adhere to the following requirements:
    * FOCUS column (e.g., resource name, region name) MUST reflect the altered value in all records pertaining to a period after the change.
    * FOCUS column MUST reflect the string value as it existed prior to the change in all records pertaining to a period prior to the change when the record does not represent a correction to a previously closed billing period.
    * FOCUS column MAY reflect the altered value in records pertaining to a period prior to the change when the record represents a correction to a previously closed billing period.
  * When column contains not-nullable string values, FOCUS column MUST adhere to the following requirements:
    * FOCUS column SHOULD NOT contain empty strings.
    * FOCUS column SHOULD NOT contain strings consisting solely of whitespace characters.
* When custom column contains string values, FOCUS column MUST adhere to the following requirements:
  * Custom column SHOULD preserve the original casing of string values.
  * Custom column SHOULD preserve the original spacing of string values.
  * Custom column SHOULD preserve other relevant consistency factors as specified by the data generator or end-user.
  * Custom column SHOULD remain consistent across all *billing periods* when the custom column contains immutable string values.
  * When column contains mutable string values, custom column MUST adhere to the following requirements:
    * Custom column SHOULD reflect the altered value in all records pertaining to a period after the change.
    * Custom column SHOULD reflect the string value as it existed prior to the change in all records pertaining to a period prior to the change when the record does not represent a correction to a previously closed billing period.
    * Custom column MAY reflect the altered value in records pertaining to a period prior to the change when the record represents a correction to a previously closed billing period.
  * When column contains not-nullable string values, custom column MUST adhere to the following requirements:
    * Custom column SHOULD NOT contain empty strings.
    * Custom column SHOULD NOT contain strings consisting solely of whitespace characters.

## Introduced (version)

1.0
