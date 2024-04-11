# String Format

Columns that capture String values conforming to specified requirements foster data integrity, interoperability, and consistency, improve data analysis and reporting, and support more reliable data-driven decision-making.

All columns capturing a String value, defined in the [FOCUS](#glossary:finops-cost-and-usage-specification) specification, MUST follow the requirements listed below. Custom String value capturing columns SHOULD adopt the same requirements over time.

## Attribute ID

StringFormat

## Attribute Name

String Format

## Description

Requirements for String-capturing columns appearing in billing data.

## Requirements

* String values appearing in the billing data MUST maintain the original casing, spacing, and other pertinent consistency factors.
* String values referring to the same entity SHOULD be consistent within a provider's context.
* The provider SHOULD ensure that both provider-defined and user-input String values do not contain multiple consecutive spaces or leading/trailing spaces.
* String-formatted columns MUST also adhere to [Null Handling](#nullhandling) requirements.

## Exceptions

None

## Introduced (version)

1.0
