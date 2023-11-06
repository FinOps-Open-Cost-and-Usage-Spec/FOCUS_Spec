# Currency Code Format

Columns that contain currency information in cost data following a consistent format reduces friction for FinOps practitioners that consume the data for analysis, reporting, and other use cases.

All currency related columns defined in the FOCUS schema MUST follow the currency formatting requirements listed below. Custom currency-related columns SHOULD also follow the currency formatting requirements.

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
