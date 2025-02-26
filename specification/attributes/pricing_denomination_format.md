# Pricing Denomination Format

Columns that contain some combination of currencies (e.g. USD, EUR) and non-currency consumable units of measure (e.g. credits, tokens) in cost data, following a consistent format reduce friction for FinOps practitioners who consume the data for analysis, reporting, and other use cases.

All columns capturing currency and/or non-currency values defined in the FOCUS specification MUST follow the requirements listed below.

## Attribute ID

PricingDenominationFormat

## Attribute Name

Pricing Denomination Format

## Description

Formatting for a combination of currency and non-currency columns appearing in a [*FOCUS dataset*](#glossary:FOCUS-dataset).

## Requirements

* Pricing Denomination columns MUST conform to [String Handling](#stringhandling) requirements when [ChargeCategory] is not "Purchase" and the provider presents prices in a non-currency consumable unit of measure (e.g. credits, tokens).
* Pricing Denomination columns MUST conform to [Currency Code Format](#currencycodeformat) requirements in all other cases.

## Exceptions

None

## Introduced (version)

1.2
