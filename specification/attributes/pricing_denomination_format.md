# Pricing Denomination Format

Columns that contain information about proprietary units of measure in cost data, following a consistent format reduce friction for FinOps practitioners who consume the data for analysis, reporting, and other use cases.

All columns capturing a proprietary unit value defined in the FOCUS specification MUST follow the requirements listed below.

## Attribute ID

PricingDenominationFormat

## Attribute Name

Pricing Denomination Format

## Description

Formatting for proprietary unit of measure columns appearing in a [*FOCUS dataset*](#glossary:FOCUS-dataset).

## Requirements

* Pricing Denomination columns MUST conform to [Currency Code Format](#currencycodeformat) requirements when [ChargeCategory](#chargecategory) = "Purchase".
* Pricing Denomination columns MUST conform to [String Handling](#stringhandling) requirements in all other cases.

## Exceptions

None

## Introduced (version)

1.2
