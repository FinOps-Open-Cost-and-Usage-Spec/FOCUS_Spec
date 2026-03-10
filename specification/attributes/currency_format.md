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

CurrencyFormat MUST adhere to the following requirements:

* FOCUS column representing national currency MUST adhere to the following requirements:
  * FOCUS column representing national currency MUST conform to ISO 4217:2015 standard.
  * FOCUS column representing national currency MUST use the three-letter alphabetic code defined in ISO 4217:2015 (e.g., USD, EUR).
* FOCUS column representing virtual currency MUST conform to [StringHandling](#attributes.stringhandling) requirements (e.g., Credits, Tokens).
* Custom column representing national currency MUST adhere to the following requirements:
  * Custom column representing national currency SHOULD conform to ISO 4217:2015 standard.
  * Custom column representing national currency SHOULD use the three-letter alphabetic code defined in ISO 4217:2015 (e.g., USD, EUR).
* Custom column representing virtual currency SHOULD conform to StringHandling requirements.

## Introduced (version)

0.5
