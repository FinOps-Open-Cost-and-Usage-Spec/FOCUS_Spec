# String Handling

Columns that capture String values conforming to specified requirements foster data integrity, interoperability, and consistency, improve data analysis and reporting, and support more reliable data-driven decision-making.

All columns capturing a String value, defined in the [FOCUS](#glossary:finops-cost-and-usage-specification) specification, MUST follow the requirements listed below. Custom String value capturing columns SHOULD adopt the same requirements over time.

## Attribute ID

StringHandling

## Attribute Name

String Handling

## Description

Requirements for String-capturing columns appearing in billing data.

## Requirements

* String values MUST maintain the original casing, spacing, and other relevant consistency factors as specified by providers and end-users.
* Changes to mutable string values (e.g., resource names) MUST be accurately reflected in charges related to subsequent costs incurred after the string value change and MUST NOT alter the original values in historical records, preserving data integrity and auditability for past billing periods.
* Immutable string values that refer to the same entity (e.g., resource identifiers) MUST remain consistent and unchanged across all billing periods.

## Exceptions

None

## Introduced (version)

1.0
