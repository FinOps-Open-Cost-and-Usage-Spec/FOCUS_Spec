# Currency Format

Columns that contain currency information in cost data following a consistent format reduce friction for FinOps practitioners who consume the data for analysis, reporting, and other use cases.

A currency may be one of the following currency types:

* [National currency](#term) (e.g., USD, EUR).
* [Consumption currency](#term) (e.g., platform credits, normalized billing units).

## Requirements

Column conforming to [CurrencyFormat](#attr) attribute MUST adhere to the following requirements:

* When the value represents a [national currency](#term), [FOCUS dataset column](#term) MUST adhere to the following requirements:
  * [FOCUS dataset column](#term) MUST conform to [ISO 4217:2015](https://www.iso.org/standard/64758.html) standard.
  * [FOCUS dataset column](#term) MUST use the three-letter alphabetic code defined in ISO 4217:2015 (e.g., USD, EUR).
* [FOCUS dataset column](#term) MUST NOT use a code defined in ISO 4217:2015 when the value does not represent a [national currency](#term).

## Implementation Context

A [consumption currency](#term) is one subtype of [virtual currency](#term). Which currency types a column allows, and whether other subtypes such as a cryptocurrency are excluded, is set by that column's own requirements, not by this attribute.

Whether a value represents a [national currency](#term) follows from the column's own definition or from the column's documentation, not from the format of the value. A single column can carry both currency types (e.g., a [national currency](#term) on purchase rows and a [consumption currency](#term) on usage rows).

Columns that carry a [national currency](#term) by their own definition take their currency type from that definition. Billing Currency, for example, separately constrains its values to [national currency](#term) in each dataset that includes it.

## Attribute ID

CurrencyFormat

## Attribute Name

Currency Format

## Description

Formatting for currency columns appearing in a [FOCUS dataset](#term).

## Version Introduced

0.5
