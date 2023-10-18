# Numeric Format

Columns that provide numeric values conforming to specified rules and formatting requirements ensure clarity, accuracy, and ease of interpretation for humans and systems.

This format requires that single numeric values be represented using an integer or decimal format without additional characters or qualifiers.  The following lists provide examples of values that meet the requirements and those that do not.

* Values Meeting Numeric Requirements:
  * -100.2
  * -3
  * 4
  * 1.234
  
* Values NOT Meeting Numeric Requirements
  * 1 1/2 - contains fractional notation
  * [3,5,8] - contains an array
  * [4:5] - contains a range
  * 5i + 4 - contains a complex number
  * sqrt(2) - contains a mathematical symbol or operation
  * 2.3^3 - contains an exponent
  * 32 GiB - contains a unit of measure
  * $32 - contains a currency symbol
  * 3,432,342 - contains a comma
  * +333 - contains a positive sign

The FOCUS specification does not require a specific level of precision for numeric values.  The level of precision required for a given column is determined by the provider as a part of a data definition published by the provider.  The following table outlines the options for specifying the level of precision for a given column in a data definition document.

* Integer number formats correspond to standard data types defined by ISO/IEC 9899:2018

* Decimal formats correspond to ISO/IEC/IEEE 60559:2011 and IEEE 754-2008 definitions.

| Precision      | Qualifier            | Definition          | Range / Significant Digits          |
| :--------------| :------------------- | :------------------ | :-------------------- |
| Integer        | Short                | 16-bit signed short int ISO/IEC 9899:2018 | -32,767 to +32,767 |
| Integer        | Long                 | 32-bit signed long int ISO/IEC 9899:2018 | -2,147,483,647 to +2,147,483,647 |
| Integer        | Extended             | 64-bit signed two's complement integer *or higher* | -(2^63 - 1) to (2^63 - 1) |
| Decimal         | Single               | 32-bit binary format IEEE 754-2008 floating-point (decimal32) | 9 |
| Decimal          | Double               | 64-bit binary format IEEE 754-2008 floating-point (decimal64) | 16 |
| Decimal          | Extended      | 128-bit binary format IEEE 754-2008 floating-point (decimal128) or higher | 36+ |

## Attribute ID

NumericFormat

## Attribute name

Numeric Format

## Description

Rules and formatting requirements for numeric columns appearing in billing data.

## Requirements

All columns capturing a numeric value, defined in the FOCUS specification, MUST be a real number represented as an integer or a decimal value, meeting the following requirements:

* Columns with a Numeric format MUST contain a single numeric value.
* Numeric values MUST be expressed as integer or decimal values. Fractional notation MUST NOT be used.
* Numeric values MUST NOT be expressed with mathematical symbols, operators, or exponent values.
* Numeric values MUST NOT contain qualifiers or additional characters (e.g., currency symbols, units of measure, etc.).
* Numeric values MUST NOT contain commas or punctuation marks except for a single decimal point if required to express a decimal value.
* Numeric values MUST NOT include a character to represent a sign for a positive value. A negative sign (-) MUST indicate a negative value.
* Numeric values MUST NOT be used to represent binary values (e.g., 0 or 1).

Numeric data types are defined in each column specification.  The following table outlines valid values for the "Data type" constraint in a column definition.  One of the following three data types MUST be present in the "Data type" constraint for a column definition with a "Value format" of "Numeric value."

| Data Type       |                 |
| :-------------- | :-------------- |
| Numeric         | General Numeric Type  | Specifies any numeric value compliant with this attribute definition.  This type is used when the column definition does not specify a more specific numeric type. |
| Integer         | Integer               | Specifies a numeric value represented by a whole number or by zero. |
| Decimal         | Decimal               | Specifies a numeric value represented by a decimal number |

The Numeric Data type is specified in the column definition as the "Data type" constraint, as shown in the following example table.  All columns listing a numeric data type MUST list "Numeric value" as the value format.

|    Constraint   |      Value      |
|:----------------|:----------------|
| Column required | True            |
| Data type       | Decimal         |
| Allows nulls    | False           |
| Value format    | Numeric value   |

## Exceptions

None

## Introduced (version)

1.0
