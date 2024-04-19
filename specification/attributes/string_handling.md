# String Handling

Columns that capture string values conforming to specified requirements foster data integrity, interoperability, and consistency, improve data analysis and reporting, and support more reliable data-driven decision-making.

All columns capturing a string value, defined in the [FOCUS](#glossary:finops-cost-and-usage-specification) specification, MUST follow the requirements listed below. Custom string value capturing columns SHOULD adopt the same requirements over time.

## Attribute ID

StringHandling

## Attribute Name

String Handling

## Description

Requirements for string-capturing columns appearing in billing data.

## Requirements

* String values MUST maintain the original casing, spacing, and other relevant consistency factors as specified by providers and end-users.
* Changes to mutable string values (e.g., resource names) MUST be accurately reflected in charges incurred after the string value change and MUST NOT alter records incurred before the change, preserving data integrity and auditability for past billing periods.
* Immutable string values that refer to the same entity (e.g., resource identifiers, region identifiers, etc.) MUST remain consistent and unchanged across all billing periods.
* Empty strings and strings consisting solely of spaces are not regarded as valid values for not-nullable string columns.

## Exceptions

None

## Introduced (version)

1.0
