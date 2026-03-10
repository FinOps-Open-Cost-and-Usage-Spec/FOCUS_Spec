# String Handling

Columns that capture string values conforming to specified requirements foster data integrity, interoperability, and consistency, improve data analysis and reporting, and support reliable data-driven decision-making.

## Attribute ID

StringHandling

## Attribute Name

String Handling

## Description

Requirements for string-capturing columns appearing in a [*FOCUS dataset*](#glossary:FOCUS-dataset).

## Requirements

StringHandling MUST adhere to the following requirements:

* FOCUS column containing string values MUST adhere to the following requirements:
  * FOCUS column containing string values MUST preserve the original casing of string values.
  * FOCUS column containing string values MUST preserve the original spacing of string values.
  * FOCUS column containing string values MUST preserve other relevant consistency factors as specified by the data generator or end-user.
  * FOCUS column containing immutable string values (e.g., resource identifiers, region identifiers) MUST remain consistent across all [*billing periods*](#glossary:billing-period).
  * FOCUS column representing mutable string values MUST reflect the altered value in all records pertaining to a period after the change.
  * FOCUS column representing mutable string values MUST reflect the string value as it existed prior to the change in all records pertaining to a period prior to the change when the record does not represent a correction to a previously closed billing period.
  * FOCUS column representing mutable string values MAY reflect the altered value in records pertaining to a period prior to the change when the record represents a correction to a previously closed billing period.
  * FOCUS column containing not-nullable string values SHOULD NOT contain empty strings.
  * FOCUS column containing not-nullable string values SHOULD NOT contain strings consisting solely of whitespace characters.
* Custom column containing string values MUST adhere to the following requirements:
  * Custom column containing string values SHOULD preserve the original casing of string values.
  * Custom column containing string values SHOULD preserve the original spacing of string values.
  * Custom column containing string values SHOULD preserve other relevant consistency factors as specified by the data generator or end-user.
  * Custom column containing immutable string values SHOULD remain consistent across all *billing periods*.
  * Custom column representing mutable string values SHOULD reflect the altered value in all records pertaining to a period after the change.
  * Custom column representing mutable string values SHOULD reflect the string value as it existed prior to the change in all records pertaining to a period prior to the change when the record does not represent a correction to a previously closed billing period.
  * Custom column representing mutable string values MAY reflect the altered value in records pertaining to a period prior to the change when the record represents a correction to a previously closed billing period.
  * Custom column containing not-nullable string values SHOULD NOT contain empty strings.
  * Custom column containing not-nullable string values SHOULD NOT contain strings consisting solely of whitespace characters.

## Introduced (version)

1.0
