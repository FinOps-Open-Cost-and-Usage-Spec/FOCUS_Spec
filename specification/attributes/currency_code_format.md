# Currency Code Format

Columns that contain currency information in cost data following a consistent format reduces friction for FinOps practitioners that consume the data for analysis, reporting, and other use cases.

All columns capturing a currency value, defined in the FOCUS specification, MUST follow the requirements listed below. Provider-generated, currency-related columns SHOULD adopt the same format requirements over time.

## Attribute ID

CurrencyCodeFormat

## Attribute name

Currency Code Format

## Description

Formatting for currency columns appearing in billing data.

## Requirements

* Currency related columns MUST be represented as a three-letter alphabetic code as dictated in the governing document [ISO 4217:2015](https://www.iso.org/standard/64758.html).

## Exceptions

None

## Introduced (version)

0.5
