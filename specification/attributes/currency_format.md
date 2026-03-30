# Currency Format

Columns that contain currency information in cost data following a consistent format reduce friction for FinOps practitioners who consume the data for analysis, reporting, and other use cases.

A currency may be one of the following currency types:

* National currency (e.g., USD, EUR).
* Virtual currency (e.g., tokens, credits).

## Attribute ID

CurrencyFormat

## Attribute Name

Currency Format

## Description

Formatting for currency columns appearing in a [*FOCUS dataset*](#glossary:FOCUS-dataset).

## Requirements

Column conforming to CurrencyFormat attribute MUST adhere to the following requirements:

* When [*FOCUS column*](#glossary:FOCUS-column) represents national currency, *FOCUS column* MUST adhere to the following requirements:
  * *FOCUS column* MUST conform to [ISO 4217:2015](https://www.iso.org/standard/64758.html) standard.
  * *FOCUS column* MUST use the three-letter alphabetic code defined in ISO 4217:2015 (e.g., USD, EUR).
* When [*custom column*](#glossary:custom-column) represents national currency, *custom column* MUST adhere to the following requirements:
  * *Custom column* SHOULD conform to ISO 4217:2015 standard.
  * *Custom column* SHOULD use the three-letter alphabetic code defined in ISO 4217:2015 (e.g., USD, EUR).

## Introduced (version)

0.5
