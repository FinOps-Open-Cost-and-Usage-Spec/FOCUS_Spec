# Currency Format

Columns that contain currency information in cost data following a consistent format reduce friction for FinOps practitioners who consume the data for analysis, reporting, and other use cases.

A currency may be one of the following currency types:

* National currency (e.g. USD, EUR).
* Virtual currency (e.g. tokens, credits).

All columns capturing a currency value, defined in the FOCUS specification, MUST follow the requirements listed below. Custom currency-related columns SHOULD also follow the same formatting requirements.

## Attribute ID

CurrencyFormat

## Attribute Name

Currency Format

## Description

Formatting for currency columns appearing in a [*FOCUS dataset*](#glossary:FOCUS-dataset).

## Requirements

* Currency-related columns MUST conform to [StringHandling](#stringhandling) requirements when the value is presented in virtual currency (e.g. credits, tokens).
* Currency-related columns MUST be represented as a three-letter alphabetic code as dictated in the governing document [ISO 4217:2015](https://www.iso.org/standard/64758.html) when the value is presented in national currency (e.g. USD, EUR).

## Exceptions

None

## Introduced (version)

0.5
