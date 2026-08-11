# Currency Format

Columns that contain currency information in cost data following a consistent format reduce friction for FinOps practitioners who consume the data for analysis, reporting, and other use cases.

A currency may be one of the following currency types:

* [*National currency*](#glossary:national-currency) (e.g., USD, EUR).
* [*Consumption currency*](#glossary:consumption-currency) (e.g., platform credits, normalized billing units).

## Requirements

Column conforming to CurrencyFormat attribute MUST adhere to the following requirements:

* [*FOCUS dataset column*](#glossary:FOCUS-dataset-column) MUST conform to [ISO 4217:2015](https://www.iso.org/standard/64758.html) standard, except when the value is presented in a *consumption currency*.
* *FOCUS dataset column* MUST use the three-letter alphabetic code defined in ISO 4217:2015 (e.g., USD, EUR), except when the value is presented in a *consumption currency*.
* *FOCUS dataset column* MUST conform to [StringHandling](#attributes.stringhandling) requirements when the value is presented in a *consumption currency*.
* *FOCUS dataset column* MUST NOT use a three-letter alphabetic code defined in ISO 4217:2015 when the value is presented in a *consumption currency*.

## Implementation Context

A *consumption currency* is the [*virtual currency*](#glossary:virtual-currency) subtype a [*service provider*](#glossary:service-provider) issues to price consumption within its own platform. Other forms of *virtual currency*, such as a cryptocurrency, have no code defined in ISO 4217:2015 and no allowed value under this attribute.

Columns that carry a national currency by their own definition are unaffected by the *consumption currency* exception. BillingCurrency, for example, separately constrains its values to *national currency* in each dataset that includes it.

## Attribute ID

CurrencyFormat

## Attribute Name

Currency Format

## Description

Formatting for currency columns appearing in a [*FOCUS dataset*](#glossary:FOCUS-dataset).

## Version Introduced

0.5
