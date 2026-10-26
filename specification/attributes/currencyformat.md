# Currency Format

Columns that contain currency information in cost data following a consistent format reduce friction for FinOps practitioners who consume the data for analysis, reporting, and other use cases.

A currency may be one of the following currency types:

* [*National currency*](#glossary:national-currency) (e.g., USD, EUR).
* [*Consumption currency*](#glossary:consumption-currency) (e.g., platform credits, normalized billing units).

## Requirements

Column conforming to CurrencyFormat attribute MUST adhere to the following requirements:

* When the value represents a *national currency*, [*FOCUS dataset column*](#glossary:FOCUS-dataset-column) MUST adhere to the following requirements:
  * *FOCUS dataset column* MUST conform to [ISO 4217:2015](https://www.iso.org/standard/64758.html) standard.
  * *FOCUS dataset column* MUST use the three-letter alphabetic code defined in ISO 4217:2015 (e.g., USD, EUR).
* *FOCUS dataset column* MUST NOT use a code defined in ISO 4217:2015 when the value does not represent a *national currency*.

## Implementation Context

A *consumption currency* is one subtype of [*virtual currency*](#glossary:virtual-currency). Which currency types a column allows, and whether other subtypes such as a cryptocurrency are excluded, is set by that column's own requirements, not by this attribute.

Whether a value represents a *national currency* follows from the column's own definition or from the column's documentation, not from the format of the value. A single column can carry both currency types (e.g., a *national currency* on purchase rows and a *consumption currency* on usage rows).

Columns that carry a *national currency* by their own definition take their currency type from that definition. Billing Currency, for example, separately constrains its values to *national currency* in each dataset that includes it.

## Attribute ID

CurrencyFormat

## Attribute Name

Currency Format

## Description

Formatting for currency columns appearing in a [*FOCUS dataset*](#glossary:FOCUS-dataset).

## Version Introduced

0.5
